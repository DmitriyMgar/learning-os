import pytest
from kata.lesson_01_async_basics import hello

@pytest.mark.asyncio
async def test_hello():
    assert await hello("bob") == "hello, bob"
