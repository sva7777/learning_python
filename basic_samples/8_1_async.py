import asyncio
import aiohttp
from time import time


def write_image(data):
    filename = "file-{}.jpeg".format(int(time() * 1000))
    with open(filename, "wb") as file:
        file.write(data)


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data)


async def main2():
    url = "https://loremflickr.com/320/240"

    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.ensure_future(fetch_content(url, session))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    t0 = time()
    loop.run_until_complete(main2())
    print(time() - t0)

    loop.close()
