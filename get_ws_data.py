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
        # converts to json string to dictionary.
        response = json.loads(response)

        # if current_data exists, appends the new response.
        # Else, groups the data with timestamp as key.
        # A new key is created for each minute.
        t = datetime.now()
        s = t.strftime('%Y-%m-%d %H:%M')
        current_data = ws_data.get(s, False)
        if current_data:
            current_data.append(response)
        else:
            ws_data[s] = [response]

        # update the file with latest data.
        with open('data.json', 'w') as f:
            json.dump(ws_data, f, indent = 4)

def run():
    asyncio.run(getData())

if __name__ == "__main__":
    # creates 100 threads to get 100 response in 100ms.
    while True:
        threads = []
        for i in range(100):
            thread = threading.Thread(target=run)
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        sleep(0.1)