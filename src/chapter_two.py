import asyncio
from util import delay


async def add_one(number: int) -> int:
    return number + 1


async def hello_world_message() -> str:
    await delay(1)
    return 'Hello World!'


async def hello_every_second():
    for i in range(15):
        await asyncio.sleep(1)
        print("While i wait, do something")


async def main() -> None:
    # message = await hello_world_message()
    # one_plus_one = await add_one(1)
    # print(one_plus_one)
    # print(message)
    # asyncio.run(main())

    # sleep_for_three = asyncio.create_task(delay(3))
    # print(type(sleep_for_three))
    # result = await sleep_for_three
    # print(result)

    # sleep_for_three = asyncio.create_task(delay(3))
    # sleep_again = asyncio.create_task(delay(3))
    # sleep_once_more = asyncio.create_task(delay(3))
    # await sleep_for_three
    # await sleep_again
    # await sleep_once_more

    first_delay = asyncio.create_task(delay(10))
    second_delay = asyncio.create_task(delay(10))
    await hello_every_second()
    await first_delay
    await second_delay

if __name__ == '__main__':
    asyncio.run(main())
