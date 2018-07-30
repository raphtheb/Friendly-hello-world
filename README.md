# Friendly-hello-world
Hello world-ing for fun and profits

# Requirements
* [Docker](https://docs.docker.com/docker-for-mac/) installed and running. Only tested on 18.03.1
* Ability to pull docker images ( curl + Internet access?)

# Usage

To build the requisite docker images, run:

`./hwaas build`

To start the service, run:

`./hwaas`

For more information and options, run:

`./hwaas help`

To start X servers and Y clients, run:
`./hwaas X Y`

To stop all running instances, run:

`./hwaas stop`


# Known issues

* No healthcheck implemented for client/server.
* No memory/ CPU limitations per client/server. Benchmarking and limiting those would help.
* No easy way to extract performance metrics (except polling redis manually).
* The startup script is a wonky Bash script i wrote in ~ 5 minutes. It could be a real CLI tool.
* No tests!!!
* Realistically, you'd want your images built on a safe, central system instead of locally generated.
* Optimize redis. This merely runs default values.
* It would be great to communicate back to a given client if a request has failed and to have retry logic.
* Some logic to see if docker-compose is already running. If you try to start it when already stopped, all sorts of wonkiness ensues.
* A k8s implementation would absolutely be better than this.
* Biggest caveat of all, large swathes of this code have been taken from public repositories online. I'm not sure how good of a test it really is. I'm not going to link to them out of respect, but they're trivial to find.

