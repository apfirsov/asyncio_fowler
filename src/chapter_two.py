import asyncio


async def delay(delay_seconds: int) -> int:
    print(f'start sleeping {delay_seconds} sec.')
    await asyncio.sleep(delay_seconds)
    print(f'sleeping {delay_seconds} sec. done')
    return delay_seconds


if __name__ == '__main__':
    pass
