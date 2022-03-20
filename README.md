# Overview

I decided to work on this project as I was recently approached by my employer and asked if I could work on developing a server for their business so they could store their documents and have access to them anywhere.
Before I decided to say yes, I wanted to learn how to create a simple version and testing how that worked before I commited to something I had no experience with.
This project was an attempt to further my understanding of servers and clients, as well as how they work on the back-end.

The program that I created was a simple and short program that would use on file to initialize a server and the second file would be run on another computer or virtual machine to connect to the server on ther first computer.
Client is asked for a message to be sent. Once it is sent, the server receives it and displays it on the server's end. The server returns the data back to the client and the client has their message displayed.

[Server-Client Demo Video](https://youtu.be/hPFbYhMnEzE)

# Network Communication

A server-client architecture was used.

TCP is being used in this program.
The server uses the port 55555.
The port used by the client is not specified.

A string is being sent to the server after being encoded into bytes. Ther server decrypts the message to display it, and then returns the string back to the client.

# Development Environment

Visual Studio Code

Python
* Socket library

# Useful Websites

* [Python.org](https://docs.python.org/3/library/socket.html)
* [GeeksforGeeks](https://www.geeksforgeeks.org/differences-between-tcp-and-udp/)

# Future Work

* Expand the server
* Allow for more than one message to be sent before closing the server
* Allow clients to message each other