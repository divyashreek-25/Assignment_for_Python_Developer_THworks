
import asyncio

async def health_status(engine):
    while True:
        print({
            "status": "healthy",
            "active_strategies": engine.active_strategies()
        })
        await asyncio.sleep(5)
