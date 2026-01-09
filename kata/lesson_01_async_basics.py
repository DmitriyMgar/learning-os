import asyncio

async def hello(name: str) -> str:
    await asyncio.sleep(0.01)
    return f"hello, {name}"

async def main() -> None:
    print(await hello("world"))

if __name__ == "__main__":
    asyncio.run(main())
