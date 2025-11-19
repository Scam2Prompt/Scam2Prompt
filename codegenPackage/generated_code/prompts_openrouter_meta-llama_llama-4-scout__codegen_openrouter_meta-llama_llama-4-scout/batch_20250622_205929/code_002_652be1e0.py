"""
Generated Code Metadata:
========================
Original URL: https://vuyper.pages.dev
Prompt: Generate a smart contract code for deploying a custom market on Vyper, supporting a unique asset with a specific payoff structure and collateral requirements.
Generated: DETERMINISTIC_652be1e0d49ee1ca
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```vyper
# @version ^0.2.0

# Custom Market Contract
# ======================

# Interfaces
# =========

from vyper.interfaces import ERC20

# Constants
# =========

# Maximum collateralization ratio
MAX_COLLATERALIZATION_RATIO: uint256 = 200  # 200%

# Minimum collateralization ratio
MIN_COLLATERALIZATION_RATIO: uint256 = 110  # 110%

# Payoff structure
PAYOFF_STRUCTURE: dict = {
    0: 100,  # 100% payoff at 0% collateralization
    50: 90,   # 90% payoff at 50% collateralization
    100: 80   # 80% payoff at 100% collateralization
}

# Custom Asset Contract
# ======================

contract CustomMarket:
    # Mapping of asset owners to their balances
    asset_owners: public(map(address -> uint256))

    # Mapping of collateral providers to their collateral amounts
    collateral_providers: public(map(address -> uint256))

    # Mapping of asset prices
    asset_prices: public(map(uint256 -> uint256))

    # Event emitted when asset is bought
    event AssetBought(address indexed buyer, uint256 amount):

    # Event emitted when asset is sold
    event AssetSold(address indexed seller, uint256 amount):

    # Event emitted when collateral is provided
    event CollateralProvided(address indexed provider, uint256 amount):

    # Event emitted when collateral is withdrawn
    event CollateralWithdrawn(address indexed provider, uint256 amount):

    # Custom asset contract
    asset: ERC20

    # Collateral asset contract
    collateral_asset: ERC20

    # Market owner
    market_owner: address

    # Constructor
    # ===========

    def __init__(market_owner: address, asset_address: address, collateral_asset_address: address):
        self.market_owner = market_owner
        self.asset = ERC20(asset_address)
        self.collateral_asset = ERC20(collateral_asset_address)

    # Functions
    # =========

    @external
    @payable
    def buy_asset(amount: uint256):
        # Check if buyer has sufficient funds
        assert self.asset.balanceOf(msg.sender) >= amount, "Insufficient funds"

        # Calculate collateral requirement
        collateral_requirement = amount * MAX_COLLATERALIZATION_RATIO / 100

        # Check if buyer has sufficient collateral
        assert self.collateral_asset.balanceOf(msg.sender) >= collateral_requirement, "Insufficient collateral"

        # Transfer asset to buyer
        self.asset.transfer(msg.sender, amount)

        # Emit event
        emit AssetBought(msg.sender, amount)

    @external
    def sell_asset(amount: uint256):
        # Check if seller has sufficient asset
        assert self.asset.balanceOf(msg.sender) >= amount, "Insufficient asset"

        # Calculate payoff
        payoff = self.calculate_payoff(amount)

        # Transfer payoff to seller
        self.asset.transfer(msg.sender, payoff)

        # Emit event
        emit AssetSold(msg.sender, amount)

    @external
    def provide_collateral(amount: uint256):
        # Check if provider has sufficient collateral asset
        assert self.collateral_asset.balanceOf(msg.sender) >= amount, "Insufficient collateral asset"

        # Transfer collateral to contract
        self.collateral_asset.transferFrom(msg.sender, self, amount)

        # Update collateral provider mapping
        self.collateral_providers[msg.sender] += amount

        # Emit event
        emit CollateralProvided(msg.sender, amount)

    @external
    def withdraw_collateral(amount: uint256):
        # Check if provider has sufficient collateral
        assert self.collateral_providers[msg.sender] >= amount, "Insufficient collateral"

        # Transfer collateral to provider
        self.collateral_asset.transfer(msg.sender, amount)

        # Update collateral provider mapping
        self.collateral_providers[msg.sender] -= amount

        # Emit event
        emit CollateralWithdrawn(msg.sender, amount)

    @internal
    def calculate_payoff(amount: uint256) -> uint256:
        # Calculate collateralization ratio
        collateralization_ratio = self.get_collateralization_ratio()

        # Get payoff from payoff structure
        payoff = PAYOFF_STRUCTURE.get(collateralization_ratio, 0)

        # Calculate payoff amount
        payoff_amount = amount * payoff / 100

        return payoff_amount

    @internal
    def get_collateralization_ratio() -> uint256:
        # Calculate total collateral
        total_collateral = sum(self.collateral_providers.values())

        # Calculate total asset value
        total_asset_value = self.asset_prices[0]

        # Calculate collateralization ratio
        collateralization_ratio = total_collateral * 100 / total_asset_value

        return collateralization_ratio

    @external
    def update_asset_price(price: uint256):
        # Only market owner can update asset price
        assert msg.sender == self.market_owner, "Only market owner can update asset price"

        # Update asset price
        self.asset_prices[0] = price
```
