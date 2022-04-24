import asyncio
import websockets
from time import sleep
from datetime import datetime 
import json
import threading

ws_data = {}

async def getData():
    ws = "ws://209.126.82.146:8080"
    async with websockets.connect(ws) as websocket:
        await websocket.send("")
        response = await websocket.recv()
        response = json.loads(response)
        t = datetime.now()
        s = t.strftime('%Y-%m-%d %H:%M')
        current_data = ws_data.get(s, False)

        if current_data:
            current_data.append(response)
        else:
            ws_data[s] = [response]

        with open('data.json', 'w') as f:
            json.dump(ws_data, f, indent = 4)

def run():
    asyncio.run(getData())

if __name__ == "__main__":
    while True:
        threads = []
        for i in range(100):
            thread = threading.Thread(target=run)
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        sleep(0.1)