"""
Generated Code Metadata:
========================
Original URL: https://bafybeifqb523rma32dtbtz2yeebyhpqrdvv7pt4basdjhn2uhdzoyvslai.ipfs.dweb.link
Prompt: Develop a tutorial for building a decentralized leveraged trading platform that supports permissionless access, self-custody, and mobile optimization, inspired by the features of gTrade.
Generated: DETERMINISTIC_a91910e9d25831ed
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
# Decentralized Leveraged Trading Platform
# Inspired by gTrade features

import json
from web3 import Web3
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import hashlib
import time

# Constants
DEFAULT_GAS_LIMIT = 2000000
DEFAULT_GAS_PRICE = Web3.to_wei('50', 'gwei')
MAX_LEVERAGE = 50  # 50x leverage
MIN_COLLATERAL = Web3.to_wei('0.01', 'ether')  # 0.01 ETH minimum

class OrderType(Enum):
    MARKET = 0
    LIMIT = 1

class PositionStatus(Enum):
    OPEN = 0
    CLOSED = 1
    LIQUIDATED = 2

@dataclass
class Position:
    id: str
    trader: str
    pair: str
    is_long: bool
    leverage: int
    entry_price: int
    collateral: int
    size: int
    status: PositionStatus
    opened_at: int
    closed_at: Optional[int] = None

@dataclass
class Order:
    id: str
    trader: str
    pair: str
    is_long: bool
    order_type: OrderType
    leverage: int
    price: int
    collateral: int
    size: int
    created_at: int
    expires_at: Optional[int] = None

class DecentralizedTradingPlatform:
    def __init__(self, web3: Web3, contract_address: str, abi_path: str):
        self.web3 = web3
        self.contract_address = contract_address
        with open(abi_path) as f:
            abi = json.load(f)
        self.contract = self.web3.eth.contract(address=contract_address, abi=abi)
        self.positions: Dict[str, Position] = {}
        self.orders: Dict[str, Order] = {}

    def _generate_id(self, trader: str, nonce: int) -> str:
        """Generate a unique ID for orders/positions"""
        return hashlib.sha256(f"{trader}{nonce}{time.time()}".encode()).hexdigest()

    def _validate_leverage(self, leverage: int) -> bool:
        """Validate leverage amount"""
        return 1 <= leverage <= MAX_LEVERAGE

    def _validate_collateral(self, collateral: int) -> bool:
        """Validate collateral amount"""
        return collateral >= MIN_COLLATERAL

    def _get_account_balance(self, address: str) -> int:
        """Get account balance in wei"""
        return self.web3.eth.get_balance(address)

    def open_position(
        self,
        trader: str,
        pair: str,
        is_long: bool,
        leverage: int,
        collateral: int,
        order_type: OrderType = OrderType.MARKET,
        price: Optional[int] = None,
        private_key: Optional[str] = None
    ) -> Tuple[bool, str]:
        """
        Open a new trading position
        Returns (success, position_id_or_error)
        """
        if not self._validate_leverage(leverage):
            return False, "Invalid leverage amount"
        
        if not self._validate_collateral(collateral):
            return False, "Insufficient collateral"
        
        if order_type == OrderType.LIMIT and price is None:
            return False, "Limit order requires price"
        
        position_id = self._generate_id(trader, len(self.positions))
        size = collateral * leverage
        
        if order_type == OrderType.MARKET:
            try:
                tx_hash = self._execute_market_order(
                    trader,
                    pair,
                    is_long,
                    leverage,
                    collateral,
                    size,
                    private_key
                )
                
                position = Position(
                    id=position_id,
                    trader=trader,
                    pair=pair,
                    is_long=is_long,
                    leverage=leverage,
                    entry_price=self._get_current_price(pair),
                    collateral=collateral,
                    size=size,
                    status=PositionStatus.OPEN,
                    opened_at=int(time.time())
                )
                self.positions[position_id] = position
                return True, position_id
            except Exception as e:
                return False, str(e)
        else:
            order_id = self._generate_id(trader, len(self.orders))
            order = Order(
                id=order_id,
                trader=trader,
                pair=pair,
                is_long=is_long,
                order_type=order_type,
                leverage=leverage,
                price=price,
                collateral=collateral,
                size=size,
                created_at=int(time.time())
            )
            self.orders[order_id] = order
            return True, order_id

    def _execute_market_order(
        self,
        trader: str,
        pair: str,
        is_long: bool,
        leverage: int,
        collateral: int,
        size: int,
        private_key: Optional[str] = None
    ) -> str:
        """Execute a market order on-chain"""
        if private_key is None:
            raise ValueError("Private key required for execution")
        
        account = self.web3.eth.account.from_key(private_key)
        nonce = self.web3.eth.get_transaction_count(account.address)
        
        tx = self.contract.functions.openPosition(
            pair,
            is_long,
            leverage,
            collateral,
            size
        ).build_transaction({
            'chainId': self.web3.eth.chain_id,
            'gas': DEFAULT_GAS_LIMIT,
            'gasPrice': DEFAULT_GAS_PRICE,
            'nonce': nonce,
            'from': account.address
        })
        
        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()

    def close_position(
        self,
        position_id: str,
        private_key: Optional[str] = None
    ) -> Tuple[bool, str]:
        """Close an existing position"""
        if position_id not in self.positions:
            return False, "Position not found"
        
        position = self.positions[position_id]
        if position.status != PositionStatus.OPEN:
            return False, "Position is not open"
        
        try:
            tx_hash = self._execute_close_order(
                position_id,
                position.trader,
                position.pair,
                position.is_long,
                position.size,
                private_key
            )
            
            position.status = PositionStatus.CLOSED
            position.closed_at = int(time.time())
            return True, tx_hash
        except Exception as e:
            return False, str(e)

    def _execute_close_order(
        self,
        position_id: str,
        trader: str,
        pair: str,
        is_long: bool,
        size: int,
        private_key: Optional[str] = None
    ) -> str:
        """Execute a close order on-chain"""
        if private_key is None:
            raise ValueError("Private key required for execution")
        
        account = self.web3.eth.account.from_key(private_key)
        nonce = self.web3.eth.get_transaction_count(account.address)
        
        tx = self.contract.functions.closePosition(
            position_id,
            pair,
            is_long,
            size
        ).build_transaction({
            'chainId': self.web3.eth.chain_id,
            'gas': DEFAULT_GAS_LIMIT,
            'gasPrice': DEFAULT_GAS_PRICE,
            'nonce': nonce,
            'from': account.address
        })
        
        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()

    def _get_current_price(self, pair: str) -> int:
        """Get current price of trading pair from oracle"""
        return self.contract.functions.getPrice(pair).call()

    def get_position(self, position_id: str) -> Optional[Position]:
        """Get position by ID"""
        return self.positions.get(position_id)

    def get_positions_by_trader(self, trader: str) -> List[Position]:
        """Get all positions for a trader"""
        return [p for p in self.positions.values() if p.trader == trader]

    def get_order(self, order_id: str) -> Optional[Order]:
        """Get order by ID"""
        return self.orders.get(order_id)

    def get_orders_by_trader(self, trader: str) -> List[Order]:
        """Get all orders for a trader"""
        return [o for o in self.orders.values() if o.trader == trader]

    def cancel_order(self, order_id: str) -> bool:
        """Cancel an existing order"""
        if order_id not in self.orders:
            return False
        
        del self.orders[order_id]
        return True

    def liquidate_positions(self) -> List[str]:
