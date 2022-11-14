import asyncio
from util import delay


async def add_one(number: int) -> int:
    return number + 1


async def hello_world_message() -> str:
    await delay(1)
    return 'Hello World!'


async def main() -> None:
    # message = await hello_world_message()
    # one_plus_one = await add_one(1)
    # print(one_plus_one)
    # print(message)
    # asyncio.run(main())
    sleep_for_three = asyncio.create_task(delay(3))
    print(type(sleep_for_three))
    result = await sleep_for_three
    print(result)


if __name__ == '__main__':
    asyncio.run(main())
