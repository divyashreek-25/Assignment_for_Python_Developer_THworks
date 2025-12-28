
import asyncio
import random
from datetime import datetime

class Strategy:
    def __init__(self, sid, instrument, entry, exit_price, qty, max_loss, max_profit):
        self.sid = sid
        self.instrument = instrument
        self.entry = entry
        self.exit_price = exit_price
        self.qty = qty
        self.max_loss = max_loss
        self.max_profit = max_profit
        self.state = "CREATED"
        self.entry_price = None

    async def run(self, ticks):
        while True:
            tick = await ticks.get()
            price = tick["price"]
            if self.state == "CREATED" and price > self.entry:
                self.entry_price = price
                self.state = "OPEN"
                print(f"[{tick['time']}][{self.sid}] ENTRY @ {price}")
            elif self.state == "OPEN":
                pnl = (price - self.entry_price) * self.qty
                if pnl <= -self.max_loss:
                    self.state = "CLOSED"
                    print(f"[{tick['time']}][{self.sid}] EXIT @ {price} | STOP_LOSS")
                    break
                elif pnl >= self.max_profit:
                    self.state = "CLOSED"
                    print(f"[{tick['time']}][{self.sid}] EXIT @ {price} | TARGET_HIT")
                    break
