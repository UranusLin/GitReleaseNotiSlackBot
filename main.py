import asyncio

import service

if __name__ == '__main__':
    asyncio.run(service.get_release_and_send_msg())
