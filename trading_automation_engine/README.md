
# Trading Automation Engine

## Architecture
- Async market feed
- Independent strategy tasks
- Risk management per strategy

## Run locally
```
python -m app.main
```

## Run with Docker
```
docker build -t trading-engine .
docker run trading-engine
```

## Health Check
Printed every 5 seconds showing active strategies.
