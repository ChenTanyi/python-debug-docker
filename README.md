## Prerequisites

* [Docker](https://www.docker.com/)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Python Extension](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python)

## Build Docker Image

```cmd
docker build -t python-module .
```

## Run Docker Container

```cmd
docker run -d -p 3000:3000 --name python-test python-module
```

## Launch Debugger

Open `PythonModuleDebug` in VS Code. Set up `Breakpoint` and press `F5`.

## Known Bug

The process would add one by one everytime restarting the debugger.

See in: https://github.com/DonJayamanne/pythonVSCode/issues/1214