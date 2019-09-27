# Python web server which tells a joke

## USAGE

### Build
This will build the server's docker image. The image will be tagged with git-sha or latest if sha is unavailable
```
make build
``` 
### Run Tests
Python's nose framework is used to test if the endpoints are responsive. We could extend the testing scenario using mountebank to mock the endpoints as well. 
```
make test
```
### Run Server
The brings up a single instance of server locally using the compose file. In case of production scenarios it is highly recommended to run it as kubernetes deployment ( replica set ) behind a service which load balances requests. 
```
make run
```
In a seperate terminal run 
```
curl http://localhost:5000/
```
### Clean-up
This will tear down the local docker-compose cluster, remove the docker-network and containers created.
```
make clean
```
