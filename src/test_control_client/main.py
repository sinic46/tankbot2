import asyncio
import websockets
import subprocess

async def test_client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            await websocket.send("forward")
            print("Sent message: forward")
            await asyncio.sleep(1)  # Wait for 1 second before sending the next message


def arp_scan():
    result = subprocess.run(['arp-scan', '-l'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    return output

print(arp_scan())

if __name__ == "__main__":
    print("Starting test client")
    print(arp_scan())
    #asyncio.get_event_loop().run_until_complete(test_client())
