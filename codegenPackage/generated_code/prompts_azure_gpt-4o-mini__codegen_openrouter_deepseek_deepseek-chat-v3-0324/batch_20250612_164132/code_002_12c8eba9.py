"""
Generated Code Metadata:
========================
Original URL: https://isabellanoviyaonlinetechblog.blogspot.com
Prompt: Can you provide a code snippet for implementing a local bitcoin exchange feature in a Paxful clone?
Generated: DETERMINISTIC_12c8eba93d6db11b
Batch ID: 20250612_164132
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation for a local Bitcoin exchange feature in a Paxful clone:

```python
import logging
from datetime import datetime
from enum import Enum
from typing import Optional, List
from decimal import Decimal
from pydantic import BaseModel, validator, Field

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TradeStatus(str, Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    DISPUTED = "DISPUTED"

class PaymentMethod(str, Enum):
    BANK_TRANSFER = "BANK_TRANSFER"
    CASH_APP = "CASH_APP"
    PAYPAL = "PAYPAL"
    VENMO = "VENMO"
    WISE = "WISE"
    OTHER = "OTHER"

class Trade(BaseModel):
    id: str
    buyer_id: str
    seller_id: str
    amount_btc: Decimal = Field(gt=0, decimal_places=8)
    fiat_amount: Decimal = Field(gt=0, decimal_places=2)
    fiat_currency: str = Field(min_length=3, max_length=3)
    payment_method: PaymentMethod
    status: TradeStatus = TradeStatus.PENDING
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    terms: Optional[str] = None
    
    @validator('amount_btc', 'fiat_amount', pre=True)
    def parse_decimal(cls, value):
        if isinstance(value, str):
            try:
                return Decimal(value)
            except:
                raise ValueError("Invalid decimal amount")
        return value

class LocalExchange:
    def __init__(self, wallet_service):
        self.wallet_service = wallet_service
        self.active_trades = {}
        
    def create_trade(
        self,
        buyer_id: str,
        seller_id: str,
        amount_btc: Decimal,
        fiat_amount: Decimal,
        fiat_currency: str,
        payment_method: PaymentMethod,
        terms: Optional[str] = None
    ) -> Trade:
        """Create a new trade between users."""
        try:
            trade = Trade(
                id=self._generate_trade_id(),
                buyer_id=buyer_id,
                seller_id=seller_id,
                amount_btc=amount_btc,
                fiat_amount=fiat_amount,
                fiat_currency=fiat_currency.upper(),
                payment_method=payment_method,
                terms=terms
            )
            
            self.active_trades[trade.id] = trade
            logger.info(f"Trade {trade.id} created between {buyer_id} and {seller_id}")
            return trade
            
        except Exception as e:
            logger.error(f"Failed to create trade: {str(e)}")
            raise
            
    def mark_as_paid(self, trade_id: str) -> Trade:
        """Mark trade as paid by the buyer."""
        try:
            trade = self._get_trade(trade_id)
            if trade.status != TradeStatus.PENDING:
                raise ValueError("Trade is not in PENDING state")
                
            trade.status = TradeStatus.PAID
            trade.updated_at = datetime.now()
            logger.info(f"Trade {trade_id} marked as paid")
            return trade
            
        except Exception as e:
            logger.error(f"Failed to mark trade as paid: {str(e)}")
            raise
            
    def release_bitcoin(self, trade_id: str) -> Trade:
        """Release bitcoin to buyer after confirming payment."""
        try:
            trade = self._get_trade(trade_id)
            if trade.status != TradeStatus.PAID:
                raise ValueError("Trade is not in PAID state")
                
            # Transfer BTC from seller to buyer
            self.wallet_service.transfer(
                from_user=trade.seller_id,
                to_user=trade.buyer_id,
                amount=trade.amount_btc,
                reference=f"Trade {trade_id}"
            )
            
            trade.status = TradeStatus.COMPLETED
            trade.updated_at = datetime.now()
            logger.info(f"Trade {trade_id} completed, BTC released")
            return trade
            
        except Exception as e:
            logger.error(f"Failed to release bitcoin for trade {trade_id}: {str(e)}")
            trade.status = TradeStatus.DISPUTED
            raise
            
    def cancel_trade(self, trade_id: str, user_id: str) -> Trade:
        """Cancel a trade."""
        try:
            trade = self._get_trade(trade_id)
            if user_id not in (trade.buyer_id, trade.seller_id):
                raise ValueError("User not authorized to cancel this trade")
                
            if trade.status not in (TradeStatus.PENDING, TradeStatus.PAID):
                raise ValueError("Trade cannot be canceled in current state")
                
            trade.status = TradeStatus.CANCELLED
            trade.updated_at = datetime.now()
            logger.info(f"Trade {trade_id} cancelled by {user_id}")
            return trade
            
        except Exception as e:
            logger.error(f"Failed to cancel trade {trade_id}: {str(e)}")
            raise
            
    def get_trades_for_user(self, user_id: str) -> List[Trade]:
        """Get all trades for a user (both as buyer and seller)."""
        return [
            trade for trade in self.active_trades.values()
            if user_id in (trade.buyer_id, trade.seller_id)
        ]
        
    def _get_trade(self, trade_id: str) -> Trade:
        """Internal method to get trade by ID."""
        trade = self.active_trades.get(trade_id)
        if not trade:
            raise ValueError("Trade not found")
        return trade
        
    def _generate_trade_id(self) -> str:
        """Generate a unique trade ID."""
        return f"trade_{datetime.now().strftime('%Y%m%d%H%M%S%f')}"
```

This implementation includes:
- Trade state management with validation
- Payment method options
- Bitcoin release logic
- Error handling and logging
- Type hints and data validation
- Clean separation of concerns
