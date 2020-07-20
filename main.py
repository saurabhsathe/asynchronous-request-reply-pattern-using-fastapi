# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 12:38:28 2020

@author: Saurabh Sathe
"""
import random
import string
import asyncio
from fastapi import FastAPI,Response
#from datetime import datetime as time

from fastapi import BackgroundTasks
import time
app = FastAPI()
objdict=dict()

class Resource():
    
    def __init__(self,id):
        self.id=id
        self.status_code=202
    

async def api2():
    print("hellllloooooooo")
    await asyncio.sleep(40)
    print("hello after")
    
    
async def process(obj:Resource):
    await api2()
    obj.status_code=200
    return "yes"
    


def gen_id():
    ran = ''.join([random.choice(string.ascii_letters 
            + string.digits) for n in range(10)])
    return ran

@app.get('/')
async def gen_data(background_tasks: BackgroundTasks):
    global objdict
    print("here")
    genid=gen_id()
    print(genid)
    obj=Resource(genid)
    background_tasks.add_task(process,obj)
    objdict[genid]=obj
    print(objdict)
    print("object has been created")
    return Response(genid,status_code=200)
  
@app.get('/status/{objid}')
async def check_status(objid:str):
    print("in the status function")
    global objdict
    obj=objdict[objid]
    print(objdict)
    print(obj.status_code)
    if obj.status_code==200:
        return Response("Found",status_code=200)
    else:
        return Response("Found",status_code=404)
    