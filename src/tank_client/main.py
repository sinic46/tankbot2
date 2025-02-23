import asyncio
import websockets



class tank_server:
    
    def __init__(self):
        pass

    async def handler(self, websocket):
        try:
            async for message in websocket:
                print(f"Received message: {message}")
                if message == "forward":
                    tank_actions.forward()
                    await websocket.send("Moving forward")
                else:
                    print("Invalid command")
                    await websocket.send("Invalid command")
        except websockets.ConnectionClosed as e:
            print(f"Connection closed: {e}")

    async def main(self):
        server = await websockets.serve(self.handler, "localhost", 8765)
        await server.wait_closed()

    def start(self):
        asyncio.get_event_loop().run_until_complete(self.main())

if __name__ == "__main__":

    tank = tank_server()
    print("Starting tank server")
    tank.start() 