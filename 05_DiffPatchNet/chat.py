import asyncio
import random
import cowsay
import shlex

clients = dict()
list_ids = dict()
free_cows = set(cowsay.list_cows())

async def chat(reader, writer):
    me = "{}:{}".format(*writer.get_extra_info('peername'))
    print(me, 'appeared')
    clients[me] = asyncio.Queue()
    send = asyncio.create_task(reader.readline())
    receive = asyncio.create_task(clients[me].get())
    while not reader.at_eof():
        done, pending = await asyncio.wait([send, receive], return_when=asyncio.FIRST_COMPLETED)
        for q in done:
            if q is send:
                send = asyncio.create_task(reader.readline())
                command = shlex.split(q.result().decode())
                match command:
                    case ['who']:
                        await clients[me].put(', '.join([name for name in clients.keys() if ':' not in name]))
                    case ['cows']:
                        await clients[me].put(', '.join(free_cows))
                    case ['login', cow_name]:
                        if cow_name in free_cows:
                            clients[cow_name] = clients.pop(me)
                            print(f'{me} is now a {cow_name}')
                            me = cow_name
                            free_cows.remove(cow_name)
                        else:
                            await clients[me].put('Name already in use')
                    case ['say', cow_name, msg]:
                        pass
                    case ['yield', msg]:
                        pass
                    case ['quit']:
                        pass
                    case _:
                        pass
            elif q is receive:
                receive = asyncio.create_task(clients[me].get())
                writer.write(f"{q.result()}\n".encode())
                await writer.drain()
    send.cancel()
    receive.cancel()
    print(me, "DONE")
    del clients[me]
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(chat, '0.0.0.0', 1337)
    async with server:
        await server.serve_forever()

asyncio.run(main())
