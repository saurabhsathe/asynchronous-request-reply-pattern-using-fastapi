# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 20:16:48 2020

@author: Saurabh Sathe
"""


import random
import string
import asyncio
from flask import Flask


app=Flask(__name__)
objdict=dict()
class Resource():
    
    def __init__(self,id):
        self.id=id
        self.status_code=202
    
    
    async def process(self):
        print("hellllloooooooo")
        asyncio.sleep(10)
        print("hello after")
        status_code=200
        return 0

    



def gen_id():
    ran = ''.join([random.choice(string.ascii_letters 
            + string.digits) for n in range(10)])
    return ran

@app.route('/',methods=['GET','POST'])
async def gen_data():
    genid=gen_id()
    obj=Resource(genid)
    yield("your client id is:----->",genid)
    objdict[genid]=obj
    stat=await obj.process()
    print(stat)
    print(done)

@app.route('/<objid>',methods=['GET','POST'])
def get_status(objid):
    obj=objdict[objid]
    if obj.status_code==200:
        return "Done processing"


    

if __name__=='__main__':
    