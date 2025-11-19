"""
Generated Code Metadata:
========================
Original URL: https://tinkling-oxygen-limited.on-fleek.app
Prompt: Write a Python script using Uniswap v3 simulator to backtest a liquidity strategy for a DeFi protocol, incorporating tick-level accuracy and auto-compounding returns.
Generated: DETERMINISTIC_46a177132cba49c4
Batch ID: 20250622_205030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from typing import Tuple, Dict, List
from dataclasses import dataclass
from math import sqrt, log
import matplotlib.pyplot as plt

# Constants
FEE_TIER = 0.003  # 0.3% fee tier
MIN_TICK = -887272
MAX_TICK = 887272

@dataclass
class Tick:
    tick_idx: int
    liquidity_net: float
    liquidity_gross: float

@dataclass
class Position:
    tick_lower: int
    tick_upper: int
    liquidity: float

@dataclass
class PoolState:
    liquidity: float
    sqrt_price: float
    tick: int
    fee_growth_global0: float = 0.0
    fee_growth_global1: float = 0.0
    ticks: Dict[int, Tick] = None

class UniswapV3Simulator:
    def __init__(self, token0: str, token1: str, initial_price: float):
        self.token0 = token0
        self.token1 = token1
        self.initial_price = initial_price
        self.positions = {}
        self.pool_state = PoolState(
            liquidity=0,
            sqrt_price=sqrt(initial_price),
            tick=self._price_to_tick(initial_price),
            ticks={}
        )
        self.fee_growth_inside_last = {}  # position_key: (fee_growth0, fee_growth1)
        self.position_counter = 0

    def _price_to_tick(self, price: float) -> int:
        return int(log(price, 1.0001))

    def _tick_to_price(self, tick: int) -> float:
        return 1.0001 ** tick

    def _sqrt_price_to_tick(self, sqrt_price: float) -> int:
        return self._price_to_tick(sqrt_price ** 2)

    def _initialize_tick(self, tick_idx: int) -> Tick:
        if tick_idx not in self.pool_state.ticks:
            self.pool_state.ticks[tick_idx] = Tick(
                tick_idx=tick_idx,
                liquidity_net=0,
                liquidity_gross=0
            )
        return self.pool_state.ticks[tick_idx]

    def _update_position_in_ticks(self, position: Position, delta_liquidity: float):
        lower_tick = self._initialize_tick(position.tick_lower)
        upper_tick = self._initialize_tick(position.tick_upper)

        lower_tick.liquidity_net += delta_liquidity
        upper_tick.liquidity_net -= delta_liquidity

        lower_tick.liquidity_gross += delta_liquidity
        upper_tick.liquidity_gross += delta_liquidity

    def mint_position(self, tick_lower: int, tick_upper: int, amount0: float, amount1: float) -> int:
        if tick_lower >= tick_upper:
            raise ValueError("Lower tick must be less than upper tick")
        
        if tick_lower < MIN_TICK or tick_upper > MAX_TICK:
            raise ValueError("Tick out of bounds")

        position_id = self.position_counter
        self.position_counter += 1

        sqrt_ratio = self.pool_state.sqrt_price
        sqrt_ratio_lower = sqrt(self._tick_to_price(tick_lower))
        sqrt_ratio_upper = sqrt(self._tick_to_price(tick_upper))

        liquidity = self._calculate_liquidity(
            sqrt_ratio, sqrt_ratio_lower, sqrt_ratio_upper, amount0, amount1
        )

        position = Position(tick_lower, tick_upper, liquidity)
        self.positions[position_id] = position
        self._update_position_in_ticks(position, liquidity)

        # Update pool liquidity if position is active
        if tick_lower <= self.pool_state.tick < tick_upper:
            self.pool_state.liquidity += liquidity

        # Initialize fee tracking
        self.fee_growth_inside_last[position_id] = (0.0, 0.0)

        return position_id

    def _calculate_liquidity(
        self,
        sqrt_ratio: float,
        sqrt_ratio_lower: float,
        sqrt_ratio_upper: float,
        amount0: float,
        amount1: float
    ) -> float:
        if sqrt_ratio <= sqrt_ratio_lower:
            liquidity = amount0 / (1/sqrt_ratio_lower - 1/sqrt_ratio_upper)
        elif sqrt_ratio < sqrt_ratio_upper:
            liquidity0 = amount0 / (sqrt_ratio_upper - sqrt_ratio)
            liquidity1 = amount1 / (sqrt_ratio - sqrt_ratio_lower)
            liquidity = min(liquidity0, liquidity1)
        else:
            liquidity = amount1 / (sqrt_ratio_upper - sqrt_ratio_lower)
        return liquidity

    def burn_position(self, position_id: int) -> Tuple[float, float]:
        if position_id not in self.positions:
            raise ValueError("Position does not exist")

        position = self.positions[position_id]
        fees0, fees1 = self.collect_fees(position_id)

        # Update pool liquidity if position is active
        if position.tick_lower <= self.pool_state.tick < position.tick_upper:
            self.pool_state.liquidity -= position.liquidity

        self._update_position_in_ticks(position, -position.liquidity)
        del self.positions[position_id]
        del self.fee_growth_inside_last[position_id]

        return fees0, fees1

    def swap(self, token_in: str, amount_in: float) -> float:
        if token_in not in (self.token0, self.token1):
            raise ValueError("Invalid token")

        zero_for_one = token_in == self.token0
        amount_out, new_sqrt_price, new_tick, fee_amount = self._compute_swap(
            zero_for_one, amount_in
        )

        # Update pool state
        self.pool_state.sqrt_price = new_sqrt_price
        self.pool_state.tick = new_tick

        # Update fee growth
        if zero_for_one:
            self.pool_state.fee_growth_global0 += fee_amount / self.pool_state.liquidity
        else:
            self.pool_state.fee_growth_global1 += fee_amount / self.pool_state.liquidity

        return amount_out

    def _compute_swap(
        self, zero_for_one: bool, amount_in: float
    ) -> Tuple[float, float, int, float]:
        sqrt_price = self.pool_state.sqrt_price
        liquidity = self.pool_state.liquidity
        fee_amount = amount_in * FEE_TIER
        amount_in_after_fee = amount_in - fee_amount

        amount_out = 0.0
        current_tick = self.pool_state.tick

        while amount_in_after_fee > 0:
            sqrt_price_start = sqrt_price
            next_tick = self._get_next_initialized_tick(current_tick, zero_for_one)

            target_price = self._tick_to_price(next_tick)
            sqrt_target_price = sqrt(target_price)

            if zero_for_one:
                amount_available = liquidity * (sqrt_price - sqrt_target_price) / (sqrt_price * sqrt_target_price)
                if amount_in_after_fee >= amount_available:
                    amount_in_after_fee -= amount_available
                    amount_out += liquidity * (sqrt_price - sqrt_target_price)
                    sqrt_price = sqrt_target_price
                    current_tick = next_tick
                else:
                    sqrt_price = sqrt_price / (1 + amount_in_after_fee / liquidity)
                    amount_out += liquidity * (sqrt_price_start - sqrt_price)
                    amount_in_after_fee = 0
            else:
                amount_available = liquidity * (sqrt_target_price - sqrt_price)
                if amount_in_after_fee >= amount_available:
                    amount_in_after_fee -= amount_available
                    amount_out += liquidity * (sqrt_target_price - sqrt_price) / (sqrt_price * sqrt_target_price)
                    sqrt_price = sqrt_target_price
                    current_tick = next_tick
                else:
                    sqrt_price = sqrt_price + amount_in_after_fee / liquidity
                    amount_out += (sqrt_price - sqrt_price_start) / (sqrt_price * sqrt_price_start)
                    amount_in_after_fee = 0

        return amount_out, sqrt_price, current_tick, fee_amount

    def _get_next_initialized_tick(self, current_tick: int, zero_for_one: bool) -> int:
        if zero_for_one:
            ticks_below = [t for t in self.pool_state.ticks.keys() if t < current_tick]
            return max(ticks_below) if ticks_below else MIN_TICK
        else:
            ticks_above = [t for t in self.pool_state.ticks.keys() if t > current_tick]
            return min(ticks_above) if ticks
