# Project 2

Web Programming with Python and JavaScript

Short Description: To build Online Messaging Application using below languages and lib
--------------------------------------------------------------------------------------------
	- HTML5, Bootstrap CSS and Custom SASS file
	- Java Scripting(ES6)
	- Scripting Templates (Handlebars)
	- Websocket (client-Side: socket.io, ServerSerde:flask_socketio) 
	- Flask

Implementation:
---------------
	- Create a single page application using scripting template, javascript, socketio and ajax technology.
	- Browser Local storage for remembering display and channel name.
	- Store Channels and Messages on Server side to available for other users

Personal Touch:
--------------
	- Sending and receiving file through messaging.

Python Module:
--------------
	- application.py: Main python web application program to handles the channels and messaging request and response. Also using global dictionary to store channels and message.
	
	- messaging.py : Classes for Channel and Message

templates folder:
----------------
	- onlinemessaging.html : GUI (single page)

static folder:
--------------
	- Contains CSS, JS
 

Known Issue:
-------
	This application has below issue.
		- After joining the channel, user manually refresh the page to start messaging.

     
