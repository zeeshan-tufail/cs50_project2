import os

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from messaging import Channel, Message 

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

CHANNELS = []
#Also can use below set for unique name 
#ch = set()
#ch.add(channel)  

@app.route("/")
def index():
    #return "Project 2: TODO"
    return render_template("onlinemessaging.html")

@app.route("/channel_list", methods=["GET"])
def channel_list():
    return jsonify({"success":True, "channels":CHANNELS})

@app.route("/add_channel", methods=["POST"])
def add_channel():
    channelName = request.form.get("channelName")
    channelDesc = request.form.get("channelDesc")
           
    if channelName is not None:       
        #Array not empty           
        if CHANNELS:                                      
            for channel in CHANNELS:
                if channel["channel_name"] == channelName:
                    return jsonify({"success":False, "channels":CHANNELS, "Error":"Channel Name already exists."})
        
        channelObj = Channel(channel_name=channelName, channel_description=channelDesc, capacity=100)
        #message2 = Message(message="message3", created_by="shani", channel_name=channelName)  
        #message3 = Message(message="message3", created_by="shani", channel_name=channelName) 
        #channelObj.msgQueue.append(message2.serialize())        
        #channelObj.msgQueue.append(message3.serialize())
        #print(channelObj.serialize())
        #print(json.dumps(channelObj.serialize()))
        CHANNELS.append(channelObj.serialize()) 
        
                  
    print(CHANNELS)            
    return jsonify({"success":True, "channels":CHANNELS})

@app.route("/join", methods=["POST"])
def join():
    #username = request.form.get("username")
    channelname = request.form.get("channelName")    
    print(channelname)
    #channel = filter(lambda item:channelname in item, CHANNELS)
    for channel in CHANNELS:
        if channel["channel_name"] == channelname:
            channel["total_user"] +=1

    return jsonify({"success":True})
    
    
@app.route("/channel_messages", methods=["POST"])   
def channel_messages():
    channelname = request.form.get("channelName")    
    print(channelname)
    messages=[]
    for channel in CHANNELS:
        if channel["channel_name"] == channelname:
            channel["total_user"] +=1
            messages = channel["msgQueue"]

    return jsonify({"success":True, "messages":messages})

@socketio.on("send message")
def vote(data):    
    message = data["message"]    
    channelName = data["channelName"]
    sentBy = data["sentBy"]
    file=""
    fileName=data["fileName"]
    print(fileName)
    if fileName:
        try:
            file = data["file"]
            print(file)
        except KeyError:
            print("No attachement.")
    '''
    
    myblob = data["myblob"]
    print(type(file))    
    print(myblob)
    
    f = open('F:/BaseCurrency.txt', 'wb')
    f.write(file)
    f.close()
    '''
    msg = Message(message=message, created_by=sentBy, channel_name=channelName)
    for channel in CHANNELS:
        if channel["channel_name"] == channelName:
            msgQueue = channel["msgQueue"]
            print(len(msgQueue))
            if channel["capacity"] == len(msgQueue):
                msgQueue.pop(0)
            msgQueue.append(msg.serialize())

    emit(channelName, {"msg":msg.serialize(), "file":file, "fileName":fileName}, broadcast=True) #{"selection":selection, "myblob":myblob}        

if __name__ == "__main__":
    app.run()