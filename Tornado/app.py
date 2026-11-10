import asyncio
from socketserver import TCPServer

def main():
    sockets = bind_sockets(8888)
    tornado.process.fork_processes(0)
    async def post_fork_main():
        server = TCPServer()
        server.add_sockets(sockets)
        await asyncio.Event().wait()
    asyncio.run(post_fork_main())

if __name__ == '__main__':
    asyncio.run(main())