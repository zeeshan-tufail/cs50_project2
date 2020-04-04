'''
Created on Apr 2, 2020

@author: Zeeshan
'''
import time, datetime
from queue import Queue

class Channel:
    def __init__(self, channel_name, channel_description, capacity):
        self.channel_name = channel_name
        self.channel_description = channel_description
        self.capacity = capacity
        self.create_date = time.asctime( time.localtime(time.time()) ) #(datetime.datetime.now()).strftime("%y-%m-%d %H:%M:%S") 
        self.total_user=0
        # Initializing a queue
        self.msgQueue = [] #Queue(maxsize=3)
     
    #def addMessage(self, Message):
    #    if len(self.msgQueue) == self.capacity:  #self.msgQueue.full()
    #        self.msgQueue.pop(0) #self.msgQueue.get_nowait()
            
        #self.msgQueue.put_nowait(Message)
        #self.msgQueue.append(Message)
    
    
    def serialize(self):
        return {"channel_name":self.channel_name,
             "channel_description":self.channel_description,
             "capacity":self.capacity,
             "create_date":self.create_date,
             "total_user":self.total_user,
             "msgQueue": self.msgQueue} 
    
      
    #def __str__(self):
    #    return f"{{channel_name:{self.channel_name}, channel_description:{self.channel_description}, capacity:{self.capacity}, create_date:{self.create_date}, total_user:{self.total_user}}}"    
          
    

class Message:
    def __init__(self,message, created_by, channel_name):
        self.message=message
        self.created_by=created_by
        self.channel_name = channel_name
        self.create_date = (datetime.datetime.now()).strftime("%y-%m-%d %H:%M:%S") #time.asctime( time.localtime(time.time()) )
        
       
    def serialize(self):
        return {"message":self.message,
             "created_by":self.created_by,
             "channel_name":self.channel_name,
             "create_date":self.create_date} 
    