"""
Generated Code Metadata:
========================
Original URL: https://btcbulltoken.pages.dev
Prompt: Write a Solidity smart contract function to handle token burns when Bitcoin reaches specific price milestones, such as $25,000 increments.
Generated: DETERMINISTIC_68bc47b9978481e6
Batch ID: 20250622_212151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";

/**
 * @title BitcoinPriceMilestoneToken
 * @author [Your Name]
 * @notice A token contract that burns tokens when Bitcoin reaches specific price milestones.
 */
contract BitcoinPriceMilestoneToken is ERC20, ERC20Burnable {
    // Mapping of price milestones to their respective token burn amounts
    mapping(uint256 => uint256) public milestones;

    // Current Bitcoin price
    uint256 public currentBitcoinPrice;

    // Oracle contract address for fetching Bitcoin price
    address public oracleContract;

    /**
     * @notice Event emitted when a token burn occurs due to a Bitcoin price milestone
     * @param milestone The price milestone reached
     * @param burnAmount The amount of tokens burned
     */
    event TokenBurned(uint256 milestone, uint256 burnAmount);

    /**
     * @notice Constructor for the BitcoinPriceMilestoneToken contract
     * @param name The name of the token
     * @param symbol The symbol of the token
     * @param oracleContract The address of the oracle contract for fetching Bitcoin price
     */
    constructor(string memory name, string memory symbol, address oracleContract) ERC20(name, symbol) {
        // Initialize oracle contract address
        this.oracleContract = oracleContract;

        // Initialize price milestones (in USD) and their respective token burn amounts
        milestones[25000] = 100; // Burn 100 tokens when Bitcoin reaches $25,000
        milestones[50000] = 200; // Burn 200 tokens when Bitcoin reaches $50,000
        milestones[75000] = 300; // Burn 300 tokens when Bitcoin reaches $75,000
    }

    /**
     * @notice Updates the current Bitcoin price
     * @param price The new Bitcoin price
     */
    function updateBitcoinPrice(uint256 price) public {
        // Only oracle contract can update the Bitcoin price
        require(msg.sender == oracleContract, "Only oracle contract can update Bitcoin price");

        currentBitcoinPrice = price;

        // Check if a price milestone is reached and burn tokens accordingly
        checkMilestones();
    }

    /**
     * @notice Checks if a price milestone is reached and burns tokens accordingly
     */
    function checkMilestones() internal {
        for (uint256 i = 0; i < 10000; i++) {
            uint256 milestone = 25000 + (i * 25000);
            if (currentBitcoinPrice >= milestone && milestones[milestone] > 0) {
                uint256 burnAmount = milestones[milestone];
                _burn(msg.sender, burnAmount);
                emit TokenBurned(milestone, burnAmount);
                // Remove milestone to prevent repeated burns
                milestones[milestone] = 0;
            }
        }
    }

    /**
     * @notice Burns tokens from the specified address
     * @param account The address to burn tokens from
     * @param amount The amount of tokens to burn
     */
    function burnFrom(address account, uint256 amount) public override {
        // Only burn tokens if the account has sufficient balance
        require(balanceOf(account) >= amount, "Insufficient balance");

        _burn(account, amount);
    }
}
```
