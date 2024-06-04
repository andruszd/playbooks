Apache Pinot Config Gude.

PINOT STARTUP SEQUENCE

Services need to be startid in order fore the cluster to work

- ZOOKEEPER (if running locally otherwise it does not require any action)
- CONTROLLER
- BROKER
- SERVER
- MINION
- KAFKA (if running locally otherwise it does not require any action)

Navigate to directory containing the launcher scripts which is the pinot home direcotry.

```bash
  cd /opt/pinot  
  cd ${PINOT_HOME} 
```
RUN ON CONTOLLER

Start Zookeeper

You need to start all you zookeepers in your cluster and wait till the zookeepers are balanced and ready before you start any of the Pinot Services. Otherwise start Zookeeper manually locally by runing the following.
```bash
 ${PINOT_HOME}/bin/pinot-admin.sh StartZookeeper  -zkPort 2181 &
```
If a service file has been installed then  run the following

```bash
    systemctl status zookeeper.service
    systemctl start zookeeper.service
    systemctl status zookeeper.service
```

Start Controller

```bash
 .${PINOT_HOME}/bin/pinot-admin.sh StartController -configFileName /etc/pinot/pinot-controller.conf &
```
If a service file has been installed then  run the following

```bash
    systemctl status pinot-ctlr.service
    systemctl start pinott-ctlr.service
    systemctl status pinot-ctlr.service
```

Wait to you see the message to say that the web ui is now available on port 9000.
open a browser and  then  browse to the controller address on port 9000

```browser
			http://<controller address>:9000
```

RUN ON BROKER 
Start Broker

```bash
 .${PINOT_HOME}/bin/pinot-admin.sh StartBroker -configFileName /etc/pinot/pinot-broker.conf &
```
If a service file has been installed then  run the following

```bash
    systemctl status pinot-brkr.service
    systemctl start pinott-brkr.service
    systemctl status pinot-brkr.service
```

Wait till broker changes state from dead to alive in the web ui

Start Server

```bash
  .{PINOT_HOME}/pinot-admin.sh StartServer -configFileName /etc/pinot/pinot-server.conf  &
```
If a service file has been installed then  run the following
```bash
    systemctl status pinot-svr.service
    systemctl start pinott-svr.service
    systemctl status pinot-svr.service
```
Wait till server changes state from dead to alive in the web ui



Start Minion
Can be run on a Controller or Server if you have enough resources to handle the extra load , otherwise please run as a seperate instance. 
```bash
   .{PINOT_HOME}/pinot-admin.sh StartMinion -configFileName /etc/pinot/pinot-server.conf  &
```
If a service file has been installed then  run the following
```bash
    systemctl status pinot-min.service
    systemctl start pinott-min.service
    systemctl status pinot-min.service
```

Wait till server changes state from dead to alive in the web ui

Start Local Kafka  (OPTIONAL)
Though it is much easier to run Kafa in another instance and to get the running performance you need. For dev/testing this is ok.
```bash
			./bin/pinot-admin.sh StartKafka   -zkAddress=localhost:2181 kafka -port 19092 &
```

To check that the services are  running  , run the following form a command prompt on the server an this will display the running pinot services.

```bash
			 jps -m
```
You should see a similar output.

```bash
			86672 PinotAdministrator StartServer -zkAddress pinotctlr:2181 -clusterName development
			86730 PinotAdministrator StartMinion -zkAddress pinotctlr:2181 -clusterName development
			86810 Jps -m
			86591 PinotAdministrator StartBroker -zkAddress pinotctlr:2181 -clusterName development
```
The number on the left is the PID.

To Shutdown services

The order to stop services it is important that you should stop the services in the following order.

- MINION
- KAFKA (if running locally otherwise it does not require any action)
- SERVER
- BROKER
- CONTROLLER
- ZOOKEEPER (if running locally otherwise it does not require any action)

Run the jobs command from the command prompt on each of the nodes if the services where started manualy otherwise use systemctl to stop the process , please wait between shutting down different nodes as we want the status saved to zookeeper. 


```bash
jobs -l
[1]  86591 Running                 ./bin/pinot-admin.sh StartBroker -zkAddress pinotctlr:2181 -clusterName development &
[2]- 86672 Running                 ./bin/pinot-admin.sh StartServer -zkAddress pinotctlr:2181 -clusterName development &
[3]+ 86730 Running                 ./bin/pinot-admin.sh StartMinion -zkAddress pinotctlr:2181 -clusterName development &
```

This will display all the background jobs running  and there associated PID number. To stop a job issue the following command

```bash
jobs kill <pid>
```


