import asyncio
import time
import random
import json


def message_generator():
    price = round(random.uniform(10, 100), 2)
    unix_time = round(time.time(), 1)
    return json.dumps({
        'price': price,
        'unix_time': unix_time
        })


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()


if __name__ == '__main__':
    while True:
        try:
            asyncio.run(tcp_echo_client(message_generator()))
            time.sleep(0.1)
        except KeyboardInterrupt:
            break

    exit()
