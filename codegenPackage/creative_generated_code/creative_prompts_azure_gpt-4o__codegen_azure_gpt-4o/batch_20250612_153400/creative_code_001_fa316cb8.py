"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-aerodrome.pages.dev
Prompt: Generate Solidity code for a smart contract that interacts with Aerodrome Finance's permissionless pools to deposit liquidity and claim AERO emissions rewards.
Generated: DETERMINISTIC_fa316cb831934857
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title AerodromeInteraction
 * @dev A smart contract to interact with Aerodrome Finance's permissionless pools.
 * It allows depositing liquidity into pools and claiming AERO emissions rewards.
 */
contract AerodromeInteraction {
    // Address of the Aerodrome pool being interacted with
    address public immutable poolAddress;

    // Address of the AERO token (reward token)
    address public immutable aeroToken;

    // Events for logging
    event LiquidityDeposited(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the pool and AERO token addresses
    constructor(address _poolAddress, address _aeroToken) {
        require(_poolAddress != address(0), "Pool address cannot be zero");
        require(_aeroToken != address(0), "AERO token address cannot be zero");

        poolAddress = _poolAddress;
        aeroToken = _aeroToken;
    }

    /**
     * @dev Deposits liquidity into the Aerodrome pool.
     * @param liquidityAmount The amount of liquidity to deposit (should be approved beforehand).
     */
    function depositLiquidity(uint256 liquidityAmount) external {
        require(liquidityAmount > 0, "Liquidity amount must be greater than zero");

        // Transfer liquidity tokens from the sender to the pool
        bool success = IERC20(poolAddress).transferFrom(
            msg.sender,
            address(this),
            liquidityAmount
        );
        require(success, "Liquidity transfer failed");

        // Deposit liquidity into the pool (assumes pool contract has a deposit method)
        IERC20(poolAddress).approve(poolAddress, liquidityAmount);
        IPool(poolAddress).deposit(liquidityAmount);

        emit LiquidityDeposited(msg.sender, liquidityAmount);
    }

    /**
     * @dev Claims AERO emissions rewards from the Aerodrome pool.
     */
    function claimRewards() external {
        // Claim AERO rewards (assumes pool contract has a claimRewards method)
        uint256 claimedAmount = IPool(poolAddress).claimRewards(msg.sender);

        require(claimedAmount > 0, "No rewards to claim");

        emit RewardsClaimed(msg.sender, claimedAmount);
    }

    /**
     * @dev Emergency function to withdraw all liquidity from the pool. Can only be called by the contract owner.
     */
    function emergencyWithdraw() external {
        uint256 totalLiquidity = IPool(poolAddress).getUserLiquidity(address(this));
        require(totalLiquidity > 0, "No liquidity to withdraw");

        IPool(poolAddress).withdraw(totalLiquidity);
    }
}

// Interfaces for interacting with the pool and ERC20 tokens

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
}

interface IPool {
    function deposit(uint256 amount) external;
    function claimRewards(address user) external returns (uint256);
    function withdraw(uint256 amount) external;
    function getUserLiquidity(address user) external view returns (uint256);
}
```
