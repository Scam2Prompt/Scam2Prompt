"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elephantrewards.pages.dev
Prompt: Create a Solidity contract for a stablecoin minting mechanism that dynamically adjusts yield generation based on the percentage to peg, inspired by TRUNK's behavior.
Generated: DETERMINISTIC_e555a83c63d7e3ef
Batch ID: 20250612_153420
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DynamicYieldStablecoin
 * @dev This contract implements a stablecoin minting mechanism that adjusts yield generation
 * based on the percentage to peg, inspired by TRUNK's behavior.
 */
contract DynamicYieldStablecoin is ERC20, Ownable {
    // The target stablecoin peg value (in terms of ether)
    uint256 public constant PEG_VALUE = 1 ether;
    // The total supply of the stablecoin
    uint256 public totalSupply;

    // Yield adjustment parameters
    uint256 public yieldCoefficient = 100; // Default yield coefficient
    uint256 public yieldAdjustmentRate = 10; // Rate at which yield coefficient adjusts (in percentage)
    uint256 public lastAdjustmentTime;

    event YieldAdjusted(uint256 newYieldCoefficient);
    event Minted(address indexed recipient, uint256 amount);
    event Burned(address indexed burner, uint256 amount);

    /**
     * @dev Constructor to initialize the stablecoin with a name and symbol.
     */
    constructor() ERC20("DynamicYieldStablecoin", "DYS") {
        lastAdjustmentTime = block.timestamp;
    }

    /**
     * @dev Mint new stablecoins based on the current stablecoin supply and yield coefficient.
     * @param amount The amount of stablecoins to mint.
     */
    function mint(uint256 amount) external onlyOwner {
        require(amount > 0, "Mint amount must be greater than zero");
        
        // Adjust the yield based on the current percentage to peg
        adjustYield();

        // Mint the stablecoin to the owner
        _mint(msg.sender, amount);
        totalSupply += amount;

        emit Minted(msg.sender, amount);
    }

    /**
     * @dev Burn a specified amount of stablecoins from the owner's balance.
     * @param amount The amount of stablecoins to burn.
     */
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");
        
        _burn(msg.sender, amount);
        totalSupply -= amount;

        emit Burned(msg.sender, amount);
    }

    /**
     * @dev Adjust the yield based on the percentage to peg.
     */
    function adjustYield() internal {
        // Simulate getting the current price of the stablecoin
        uint256 currentPrice = getCurrentPrice(); // Assume this function fetches current market price

        // Calculate the percentage to peg
        uint256 percentageToPeg = (currentPrice * 100) / PEG_VALUE;

        if (block.timestamp >= lastAdjustmentTime + 1 days) { // Adjust yield daily
            if (percentageToPeg < 100) {
                yieldCoefficient += yieldAdjustmentRate;
            } else {
                yieldCoefficient = 100; // Reset yield coefficient if above peg
            }
            lastAdjustmentTime = block.timestamp;

            emit YieldAdjusted(yieldCoefficient);
        }
    }

    /**
     * @dev A placeholder function to simulate fetching the current price of the stablecoin.
     * In a production contract, this should be replaced with an oracle or price feed.
     */
    function getCurrentPrice() internal view returns (uint256) {
        // Simulating the price; in a real contract, this would be fetched from an oracle
        return PEG_VALUE; // Assuming it is always at peg for demonstration
    }
}
```
