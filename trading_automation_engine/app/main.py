
import asyncio
import os
from app.market import market_feed
from app.engine import TradingEngine
from app.health import health_status

async def main():
    engine = TradingEngine()
    await asyncio.gather(
        market_feed(engine),
        engine.run(),
        health_status(engine)
    )

if __name__ == "__main__":
    asyncio.run(main())
