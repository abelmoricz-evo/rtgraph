import json
from random import randint
from asyncio import sleep
from asgiref.sync import sync_to_async

from .models import User
from .models import Sensor
from .models import Record

from . import counter

from channels.generic.websocket import AsyncWebsocketConsumer

class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        NewUser = await User.create('marcellus wallace', 'wood', 'shotty McShotgun')
        await NewUser.save_to_db()
        ForceSensor = await Sensor.create('force-load', 'lbs', 50, NewUser)
        await ForceSensor.save_to_db()

        for i in range(100):
            data = counter.update()
            NewRecord = await Record.create(i*200, data, NewUser.tool_selected, ForceSensor)
            NewRecord.pk = None
            await NewRecord.save_to_db()
            await self.send(json.dumps({'value': data}))
            await sleep(.2)
    
    async def disconnect(self):
        pass