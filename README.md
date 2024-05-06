# Lan-Chat
# overview
This a simple Lan Chat between hosted by **server** and **multiple** clients.

# Technologies used
* ```pycharm```: Python Intrepreter to handle both ```server``` and ```client``` script.
* ```Socket API```: Handles the main concerns with server hosting and connecting multiple users

# Server
Mainyl start with importing some important libraries ```socket``` and ```threading```. As stated ```socket``` library handles server hosting functions:
* Creating server
* Sending messages
* Recieving messages

Begining with initiliziing ```socket``` object, afterwards, since we run from our terminal we expect three arguments, so we have to check we have three arguments ```target_file```, ```IP address```, ```port_number``` respectively.

Then we ```bind``` our server with the given ```IP address``` and ```Port```, make sure they are valid, if ran on ```same device``` we can use ```127.0.0.1``` and ```8000``` port number
if run on multiple devices on ```local wifi```, we can use ```IP address``` given to current device.

```server.listen()``` allows incoming connections, we can add ```MAX_NUMBER``` of intended clients

In the infinite loop:
```server.accept()``` it accepts new connection on form (```connection```, ```address```), then we send ```welcome message``` on that ```client device``` and recieves his/her ```username```. At the same time, we must handle recieving messages. So, we must run our ```Client_requests``` on different ```thread```.

In ```clientThread```, we expect recieving message from any client. and we validate message: 
- if it's ```not terminal``` message, we just print the recieved message and ```broadcast``` the message on all clients (that is to send that ```message``` to each ```client```)
- if it's ```not valid``` we just ```remove``` this client from our server.

# Client Script
We do the same first steps in our server, ```initializing socket server```, get ```IP address``` and ```port number```. Then,  we connect those parameters to our server. (They must be ```identical``` if run on same device)

Then we propmt our ```client``` to enter his/her ```username``` and send it to our server.

Now,  Two actions must be ```synchronized```:
- ```Receiving Messages``` from other clients
 ```Sending Messages``` to other client

It seems we must run both of them on different ```threads``` to enable ```synchronization```. We have two main ```functions``` ran on different ```threads``` at the same time:
- ```ResponseMessage```: which handles ```recieving``` messages from other clients. We validate our message and then print its contents.
- ```SendMessage```: whoch handles ```sending``` messages to other client. We can see we prepare our message by adding ```username``` along with message content allowing other clients to know who sent that message. If the message is not valid, we send a ```disconnection``` message to the server.

and That's it, very simple local chat to enable users talk to each other without the necessity of having ```internet```.

# screenshots 
## working on same device
![image](https://github.com/Ahmed-waled/Lan-Chat/assets/103792966/6ce10c88-f388-48f0-b89d-280f07607e57)

## Working on different devices
