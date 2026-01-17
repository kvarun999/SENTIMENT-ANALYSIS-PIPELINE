import asyncio
import websockets
import json

# URL of your Backend WebSocket
WS_URL = "ws://localhost:8000/ws/sentiment"

async def test_connection():
    print(f"🔵 Attempting to connect to {WS_URL}...")
    
    try:
        async with websockets.connect(WS_URL) as websocket:
            print("🟢 CONNECTED! Waiting for messages...")
            print("   (If this script exits immediately, the Backend is closing the connection)")
            
            # Keep listening forever
            while True:
                try:
                    message = await websocket.recv()
                    print(f"📩 RECEIVED: {message}")
                except websockets.exceptions.ConnectionClosed:
                    print("🔴 Connection closed by server.")
                    break
    except Exception as e:
        print(f"❌ FAILED to connect: {e}")

if __name__ == "__main__":
    # You might need to install websockets first:
    # pip install websockets
    asyncio.run(test_connection())