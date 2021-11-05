import asyncio
import logging

logging.basicConfig(filename='server.log',
                    filemode='w',
                    format='%(asctime)s [%(levelname)s] - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.DEBUG)


async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    logging.info(f"Received {message!r} from {addr!r}")
    logging.info(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()

    logging.info("Close the connection")
    writer.close()


async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    logging.debug(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    logging.critical("Server has been interrupted!")
    exit()
