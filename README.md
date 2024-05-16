# Designed and implemented a server-client sensor data monitoring system


Echo Client and Server with Logging
This repository contains two Python scripts:

echo-client.py: This script simulates a client that connects to a server and sends data periodically. The client sends a predefined message to the server and waits for a response. If the response matches a specific string, it sends a measurement data packet to the server.

server_logging_store_data.py: This script acts as a server that listens for incoming connections from clients. Upon connection, it sends a specific message to the client and waits to receive data. Once data is received, it logs the data along with a timestamp into separate text files for each client.

Usage
To use these scripts, follow the instructions below:

1.Clone the Repository: Clone this repository to your local machine using Git.

`git clone https://github.com/your-username/your-repository.git`

2.Navigate to the Repository: Change directory to the cloned repository.

`python server_logging_store_data.py`

3.Run the Server Script: Execute the server script to start the server.

`python server_logging_store_data.py`

4.Run the Client Script: Execute the client script to start the client.
`python echo-client.py`

Description
echo-client.py: This script initiates a TCP connection to a specified host and port. It sends a predefined message "GET STREAM DIGITAL" to the server and waits for a response. Upon receiving the response, if it matches the expected string, the client generates measurement data and sends it to the server. The client repeats this process in a loop with a delay of 1 second between each iteration.

server_logging_store_data.py: This script acts as a TCP server listening on a specified port. Upon receiving a connection from a client, it sends the message "GET STREAM DIGITAL" to the client and waits to receive data. Once data is received, it logs the data along with a timestamp into a separate text file named with the client's IP address and the current date and hour.

Dependencies
Python 3.x
Contributions
Contributions to this project are welcome. Feel free to submit pull requests or open issues for any improvements or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.
