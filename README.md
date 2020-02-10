# Python_botnet
Botnet is a Python Remote Access Tool.

__Warning: Misuse of this software can raise legal and ethical issues which I don't support nor can be held responsible for.__

Botnet is, just like Ares, made of two programs:

- A Command And Control server which is a web interface to administer the agents
- An agent program, which is run on the compromised host, and ensures communication with the C&C

## Based on Github project Ares: https://github.com/sweetsoftware/Ares
Differences?
1. Updated from python 2 -> python 3
2. Extra features like screencaptures, keylogger, password grabber (More about that further on in the documentation)

## Setup

__Note: I always suggest to create a virtual environment__

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


# TODO provide further documentation
