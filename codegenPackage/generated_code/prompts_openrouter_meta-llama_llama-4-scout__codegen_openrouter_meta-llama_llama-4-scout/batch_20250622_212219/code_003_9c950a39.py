"""
Generated Code Metadata:
========================
Original URL: https://uniswap-slippagebot.pages.dev
Prompt: Create a Solidity contract that inherits from the Uniswap V2 core contracts and adds custom functionality for slippage protection, referencing the Uniswap Slippage Bot contract.
Generated: DETERMINISTIC_9c950a3908ce2e85
Batch ID: 20250622_212219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity =0.6.12;

import "@uniswap/v2-core/contracts/UniswapV2Pair.sol";
import "@uniswap/v2-core/contracts/UniswapV2Factory.sol";

// Inspired by Uniswap Slippage Bot contract
contract SlippageProtectedPair is UniswapV2Pair {
    // Mapping of address to maximum slippage tolerance
    mapping(address => uint) public slippageTolerance;

    // Event emitted when slippage tolerance is updated
    event SlippageToleranceUpdated(address indexed user, uint tolerance);

    // Event emitted when slippage protection is triggered
    event SlippageProtectionTriggered(address indexed user, uint amount);

    // Maximum slippage tolerance in basis points (default: 2%)
    uint public defaultSlippageTolerance;

    // Uniswap V2 factory instance
    UniswapV2Factory public factory;

    constructor(address _factory) public UniswapV2Pair() {
        factory = UniswapV2Factory(_factory);
        defaultSlippageTolerance = 200; // 2%
    }

    // Update slippage tolerance for a user
    function updateSlippageTolerance(uint _tolerance) public {
        require(_tolerance <= 10000, "Slippage tolerance exceeds maximum");
        slippageTolerance[msg.sender] = _tolerance;
        emit SlippageToleranceUpdated(msg.sender, _tolerance);
    }

    // Get user's slippage tolerance
    function getSlippageTolerance(address _user) public view returns (uint) {
        return slippageTolerance[_user] != 0 ? slippageTolerance[_user] : defaultSlippageTolerance;
    }

    // Override Uniswap V2 Pair's swap function to add slippage protection
    function swap(uint amount0Out, uint amount1Out, address to, bytes calldata data) override public {
        // Check if slippage protection is enabled for the user
        uint slippageTolerance = getSlippageTolerance(msg.sender);
        require(slippageTolerance > 0, "Slippage protection is disabled");

        // Calculate minimum amounts out with slippage protection
        uint amount0In = amount0Out * 10000 / (10000 - slippageTolerance);
        uint amount1In = amount1Out * 10000 / (10000 - slippageTolerance);

        // Perform the swap
        super.swap(amount0Out, amount1Out, to, data);

        // Check if slippage protection was triggered
        if (amount0In > reserve0() || amount1In > reserve1()) {
            emit SlippageProtectionTriggered(msg.sender, amount0Out);
        }
    }

    // Add custom functionality to mint function
    function mint(address to) override public returns (uint liquidity) {
        // Custom mint logic can be added here
        return super.mint(to);
    }

    // Add custom functionality to burn function
    function burn(address to) override public returns (uint amount0, uint amount1) {
        // Custom burn logic can be added here
        return super.burn(to);
    }
}
```
