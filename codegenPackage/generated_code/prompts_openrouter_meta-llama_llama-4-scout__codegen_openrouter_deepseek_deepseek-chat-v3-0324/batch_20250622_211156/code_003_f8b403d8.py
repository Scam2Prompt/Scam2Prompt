"""
Generated Code Metadata:
========================
Original URL: https://trade.coinbase-inc.com
Prompt: Generate a REST API documentation snippet for retrieving trade data, inspired by the structure seen in the trade.coinbase-inc.com directory listing.
Generated: DETERMINISTIC_f8b403d80251280f
Batch ID: 20250622_211156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Trade Data REST API Documentation

This module provides documentation for the Trade Data API endpoints.
The API follows RESTful conventions and returns JSON responses.
"""

from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

class Trade(BaseModel):
    """
    Represents a single trade record.
    """
    trade_id: str
    product_id: str
    price: float
    size: float
    side: str  # 'buy' or 'sell'
    time: datetime
    fee: Optional[float] = None
    liquidity: Optional[str] = None  # 'M' for maker, 'T' for taker

class TradeResponse(BaseModel):
    """
    Standard response format for trade data endpoints.
    """
    success: bool
    trades: List[Trade]
    cursor: Optional[str] = None  # For pagination
    error: Optional[str] = None

# API Endpoint Documentation
api_documentation = {
    "base_path": "/api/v1/trades",
    "endpoints": [
        {
            "path": "/",
            "method": "GET",
            "description": "Retrieve recent trades",
            "parameters": [
                {
                    "name": "product_id",
                    "type": "string",
                    "required": True,
                    "description": "The trading pair (e.g., 'BTC-USD')"
                },
                {
                    "name": "limit",
                    "type": "integer",
                    "required": False,
                    "default": 100,
                    "description": "Number of trades to return (max 1000)"
                },
                {
                    "name": "before",
                    "type": "string",
                    "required": False,
                    "description": "Cursor for pagination (trade_id)"
                },
                {
                    "name": "after",
                    "type": "string",
                    "required": False,
                    "description": "Cursor for pagination (trade_id)"
                }
            ],
            "response": {
                "200": {
                    "description": "Successful response",
                    "schema": "TradeResponse"
                },
                "400": {
                    "description": "Invalid parameters"
                },
                "404": {
                    "description": "Product not found"
                },
                "500": {
                    "description": "Internal server error"
                }
            }
        },
        {
            "path": "/{trade_id}",
            "method": "GET",
            "description": "Retrieve a specific trade by ID",
            "parameters": [
                {
                    "name": "trade_id",
                    "type": "string",
                    "required": True,
                    "description": "The unique trade identifier"
                }
            ],
            "response": {
                "200": {
                    "description": "Successful response",
                    "schema": "Trade"
                },
                "404": {
                    "description": "Trade not found"
                }
            }
        }
    ],
    "rate_limits": [
        {
            "scope": "ip",
            "limit": "10 requests per second",
            "description": "Applies to all endpoints"
        }
    ],
    "authentication": {
        "required": False,
        "methods": [
            {
                "type": "API Key",
                "name": "X-API-KEY",
                "description": "Optional for public data, required for private endpoints"
            }
        ]
    }
}
```
