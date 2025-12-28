
import asyncio
import random
from datetime import datetime

async def market_feed(engine):
    price = 20100
    while True:
        price += random.randint(-10, 10)
        tick = {
            "instrument": "NIFTY",
            "price": price,
            "time": datetime.now().strftime("%H:%M:%S")
        }
        for _ in engine.strategies:
            await engine.ticks.put(tick)
        await asyncio.sleep(1)
