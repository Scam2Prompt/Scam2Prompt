"""
Generated Code Metadata:
========================
Original URL: https://valesymonederos.com
Prompt: "Generate a sample API documentation for a food voucher system in Mexico, including endpoints for checking balances and transaction history."
Generated: DETERMINISTIC_157a063ca765a0e9
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Food Voucher System API Documentation

This API allows users to check their food voucher balance and transaction history in Mexico.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(
    title="Mexico Food Voucher System API",
    description="API for managing food voucher balances and transactions",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@foodvoucher.mx"
    },
    license_info={
        "name": "MIT",
    },
)

class Transaction(BaseModel):
    id: str
    amount: float
    merchant: str
    date: datetime
    transaction_type: str  # "credit" or "debit"
    balance_after: float

class BalanceResponse(BaseModel):
    card_number: str
    current_balance: float
    currency: str = "MXN"
    last_updated: datetime

class TransactionHistoryResponse(BaseModel):
    card_number: str
    transactions: List[Transaction]
    total_transactions: int

class ErrorResponse(BaseModel):
    detail: str
    code: int

@app.get(
    "/balance/{card_number}",
    response_model=BalanceResponse,
    responses={
        404: {"model": ErrorResponse, "description": "Card not found"},
        400: {"model": ErrorResponse, "description": "Invalid card number format"}
    },
    summary="Get current balance",
    description="Returns the current balance for a given food voucher card number"
)
async def get_balance(card_number: str):
    """
    Retrieve the current balance for a food voucher card.

    Parameters:
    - card_number: str (required) - The food voucher card number

    Returns:
    - BalanceResponse object with current balance information
    """
    # In a real implementation, this would query a database
    if len(card_number) != 16 or not card_number.isdigit():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Card number must be 16 digits"
        )
    
    # Mock response for demonstration
    return BalanceResponse(
        card_number=card_number,
        current_balance=1250.50,
        last_updated=datetime.now()
    )

@app.get(
    "/transactions/{card_number}",
    response_model=TransactionHistoryResponse,
    responses={
        404: {"model": ErrorResponse, "description": "Card not found"},
        400: {"model": ErrorResponse, "description": "Invalid card number format"}
    },
    summary="Get transaction history",
    description="Returns the transaction history for a given food voucher card number"
)
async def get_transactions(
    card_number: str,
    limit: Optional[int] = 10,
    offset: Optional[int] = 0
):
    """
    Retrieve transaction history for a food voucher card.

    Parameters:
    - card_number: str (required) - The food voucher card number
    - limit: int (optional) - Number of transactions to return (default: 10)
    - offset: int (optional) - Number of transactions to skip (default: 0)

    Returns:
    - TransactionHistoryResponse object with transaction list
    """
    if len(card_number) != 16 or not card_number.isdigit():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Card number must be 16 digits"
        )

    # Mock transactions for demonstration
    mock_transactions = [
        Transaction(
            id="txn_001",
            amount=150.75,
            merchant="Supermercado ABC",
            date=datetime(2023, 5, 15, 10, 30),
            transaction_type="debit",
            balance_after=1099.75
        ),
        Transaction(
            id="txn_002",
            amount=200.00,
            merchant="Restaurante XYZ",
            date=datetime(2023, 5, 10, 19, 15),
            transaction_type="debit",
            balance_after=1250.50
        )
    ]

    return TransactionHistoryResponse(
        card_number=card_number,
        transactions=mock_transactions,
        total_transactions=len(mock_transactions)
    )
```
