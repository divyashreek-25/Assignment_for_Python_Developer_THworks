
import asyncio
from app.strategy import Strategy

class TradingEngine:
    def __init__(self):
        self.strategies = [
            Strategy("S1", "NIFTY", 20100, 20050, 50, 2000, 3000),
            Strategy("S2", "NIFTY", 20080, 20030, 25, 1500, 2500),
        ]
        self.ticks = asyncio.Queue()

    async def run(self):
        tasks = [asyncio.create_task(s.run(self.ticks)) for s in self.strategies]
        await asyncio.gather(*tasks, return_exceptions=True)

    def active_strategies(self):
        return sum(1 for s in self.strategies if s.state == "OPEN")
