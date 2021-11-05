import asyncio
import time
import random
import json


async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888, loop=loop)
    print('Send: %r' % message)
    writer.write(message.encode())
    data = await reader.read(100)
    print('Received: %r' % data.decode())
    print('Close the socket')
    writer.close()


def message_generator():
    price = round(random.uniform(10, 100), 2)
    clock = round(time.time(), 1)
    return price, clock


while True:
    try:
        temp_msg = message_generator()
        message = json.dumps({'price': temp_msg[0], 'time': temp_msg[1]})
        loop = asyncio.get_event_loop()
        loop.run_until_complete(tcp_echo_client(message, loop))
        time.sleep(0.1)
    except KeyboardInterrupt:
        loop.close()