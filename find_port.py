import websockets
import json
import threading
import asyncio
open_ports = []
max_port_range = 65535

async def connect_to_ws(ws,port):
    print(port)
    try:
        ws = ws + ":" + str(port)
        async with websockets.connect(ws) as websocket:
            await websocket.send("")
            response = await websocket.recv()
            if response:
                open_ports.append(port)
    except:
        pass

def port_scan(min, max):
    for i in range(min,max+1):
        asyncio.run(connect_to_ws("ws://209.126.82.146", i))

if __name__ == "__main__":

    threads = []
    thread_loop_range = 100
    for i in range(thread_loop_range):
        max_range = round(max_port_range/thread_loop_range) * i
        min_range = max_range - round(max_port_range/thread_loop_range)
        thread = threading.Thread(target=port_scan,args=(min_range,max_range))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

    print(open_ports)
