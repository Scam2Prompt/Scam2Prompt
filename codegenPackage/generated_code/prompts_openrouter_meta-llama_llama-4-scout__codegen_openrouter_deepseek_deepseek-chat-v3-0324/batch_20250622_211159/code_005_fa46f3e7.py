"""
Generated Code Metadata:
========================
Original URL: https://supercore-7hg.pages.dev
Prompt: Create a GraphQL API to query swap pool data, including token prices, liquidity, and trading volumes, for the 9mm Swap platform.
Generated: DETERMINISTIC_fa46f3e7beacada9
Batch ID: 20250622_211159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import strawberry
from typing import List, Optional
from pydantic import BaseModel
import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Mock database models
class Token(BaseModel):
    id: str
    symbol: str
    name: str
    decimals: int

class Pool(BaseModel):
    id: str
    token0: Token
    token1: Token
    reserve0: float
    reserve1: float
    total_supply: float
    fee_tier: float
    created_at: datetime.datetime

class Swap(BaseModel):
    id: str
    pool_id: str
    amount0_in: float
    amount1_in: float
    amount0_out: float
    amount1_out: float
    timestamp: datetime.datetime

# Mock database
mock_pools = [
    Pool(
        id="1",
        token0=Token(id="0x1", symbol="ETH", name="Ethereum", decimals=18),
        token1=Token(id="0x2", symbol="USDT", name="Tether", decimals=6),
        reserve0=1000.0,
        reserve1=2000000.0,
        total_supply=1000000.0,
        fee_tier=0.003,
        created_at=datetime.datetime.now()
    ),
    Pool(
        id="2",
        token0=Token(id="0x3", symbol="BTC", name="Bitcoin", decimals=8),
        token1=Token(id="0x2", symbol="USDT", name="Tether", decimals=6),
        reserve0=50.0,
        reserve1=3000000.0,
        total_supply=1500000.0,
        fee_tier=0.003,
        created_at=datetime.datetime.now()
    )
]

mock_swaps = [
    Swap(
        id="1",
        pool_id="1",
        amount0_in=1.0,
        amount1_in=0.0,
        amount0_out=0.0,
        amount1_out=2000.0,
        timestamp=datetime.datetime.now()
    )
]

# GraphQL types
@strawberry.type
class TokenType:
    id: str
    symbol: str
    name: str
    decimals: int

@strawberry.type
class PoolType:
    id: str
    token0: TokenType
    token1: TokenType
    reserve0: float
    reserve1: float
    total_supply: float
    fee_tier: float
    created_at: str
    
    @strawberry.field
    def token0_price(self) -> float:
        try:
            return self.reserve1 / self.reserve0
        except ZeroDivisionError:
            return 0.0
    
    @strawberry.field
    def token1_price(self) -> float:
        try:
            return self.reserve0 / self.reserve1
        except ZeroDivisionError:
            return 0.0
    
    @strawberry.field
    def liquidity(self) -> float:
        return self.reserve0 * self.token0_price() + self.reserve1 * self.token1_price()

@strawberry.type
class SwapType:
    id: str
    pool_id: str
    amount0_in: float
    amount1_in: float
    amount0_out: float
    amount1_out: float
    timestamp: str

@strawberry.type
class VolumeStats:
    daily: float
    weekly: float
    monthly: float

@strawberry.type
class Query:
    @strawberry.field
    def pools(self, pool_id: Optional[str] = None) -> List[PoolType]:
        try:
            if pool_id:
                pool = next((p for p in mock_pools if p.id == pool_id), None)
                if not pool:
                    raise ValueError("Pool not found")
                return [PoolType(
                    id=pool.id,
                    token0=TokenType(**pool.token0.dict()),
                    token1=TokenType(**pool.token1.dict()),
                    reserve0=pool.reserve0,
                    reserve1=pool.reserve1,
                    total_supply=pool.total_supply,
                    fee_tier=pool.fee_tier,
                    created_at=pool.created_at.isoformat()
                )]
            return [
                PoolType(
                    id=pool.id,
                    token0=TokenType(**pool.token0.dict()),
                    token1=TokenType(**pool.token1.dict()),
                    reserve0=pool.reserve0,
                    reserve1=pool.reserve1,
                    total_supply=pool.total_supply,
                    fee_tier=pool.fee_tier,
                    created_at=pool.created_at.isoformat()
                ) for pool in mock_pools
            ]
        except Exception as e:
            logger.error(f"Error fetching pools: {str(e)}")
            raise
    
    @strawberry.field
    def swaps(self, pool_id: Optional[str] = None) -> List[SwapType]:
        try:
            swaps = mock_swaps
            if pool_id:
                swaps = [s for s in mock_swaps if s.pool_id == pool_id]
            return [
                SwapType(
                    id=swap.id,
                    pool_id=swap.pool_id,
                    amount0_in=swap.amount0_in,
                    amount1_in=swap.amount1_in,
                    amount0_out=swap.amount0_out,
                    amount1_out=swap.amount1_out,
                    timestamp=swap.timestamp.isoformat()
                ) for swap in swaps
            ]
        except Exception as e:
            logger.error(f"Error fetching swaps: {str(e)}")
            raise
    
    @strawberry.field
    def volume_stats(self, pool_id: str) -> VolumeStats:
        try:
            pool_swaps = [s for s in mock_swaps if s.pool_id == pool_id]
            now = datetime.datetime.now()
            
            daily = sum(s.amount0_in + s.amount1_in for s in pool_swaps 
                       if (now - s.timestamp) < datetime.timedelta(days=1))
            
            weekly = sum(s.amount0_in + s.amount1_in for s in pool_swaps 
                        if (now - s.timestamp) < datetime.timedelta(days=7))
            
            monthly = sum(s.amount0_in + s.amount1_in for s in pool_swaps 
                         if (now - s.timestamp) < datetime.timedelta(days=30))
            
            return VolumeStats(
                daily=daily,
                weekly=weekly,
                monthly=monthly
            )
        except Exception as e:
            logger.error(f"Error calculating volume stats: {str(e)}")
            raise

# Create schema
schema = strawberry.Schema(query=Query)

# Initialize FastAPI app
app = FastAPI(title="9mm Swap API", description="GraphQL API for 9mm Swap platform")

# Add GraphQL endpoint
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
```
