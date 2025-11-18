"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://internetmoney-4rq.pages.dev
Prompt: Write a Solidity function to implement a "Buy 'N Burn" mechanism for TIME tokens, ensuring it calculates the burned percentage of the total supply dynamically, as described on the webpage.
Generated: DETERMINISTIC_afa7b1728d64fb65
Batch ID: 20250612_153700
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
 * @title TimeToken
 * @dev Implementation of the TIME token with a "Buy 'N Burn" mechanism.
 */
contract TimeToken is ERC20, Ownable {
    uint256 private _burnPercentage; // Percentage of tokens to burn
    uint256 private _totalBurned; // Total tokens burned
    uint256 private immutable _initialSupply; // Initial total supply of tokens

    event TokensBurned(address indexed burner, uint256 amount);
    event BurnPercentageUpdated(uint256 newPercentage);

    /**
     * @dev Sets the values for {name} and {symbol}, and initializes the total supply.
     */
    constructor(uint256 initialSupply, uint256 burnPercentage) ERC20("TIME Token", "TIME") {
        _initialSupply = initialSupply * (10 ** decimals());
        _burnPercentage = burnPercentage; // Set initial burn percentage
        _mint(msg.sender, _initialSupply); // Mint initial supply to the owner
    }

    /**
     * @dev Function to update the burn percentage.
     * @param newPercentage New burn percentage (from 0 to 100).
     */
    function updateBurnPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage >= 0 && newPercentage <= 100, "Burn percentage must be between 0 and 100");
        _burnPercentage = newPercentage;
        emit BurnPercentageUpdated(newPercentage);
    }

    /**
     * @dev Function to buy tokens and automatically burn a percentage.
     * @param amount Amount of tokens to buy.
     */
    function buyAndBurn(uint256 amount) external payable {
        require(msg.value > 0, "Ether sent must be greater than 0");
        require(amount > 0, "Amount must be greater than 0");

        // Calculate the amount of tokens to burn
        uint256 burnAmount = (amount * _burnPercentage) / 100;
        uint256 tokensToTransfer = amount - burnAmount;

        // Transfer tokens to the buyer
        _transfer(address(this), msg.sender, tokensToTransfer);
        
        // Burn the calculated amount
        _burn(address(this), burnAmount);
        _totalBurned += burnAmount;

        emit TokensBurned(msg.sender, burnAmount);
    }

    /**
     * @dev Function to retrieve the total supply minus burned tokens.
     * @return Current circulating supply of tokens.
     */
    function circulatingSupply() external view returns (uint256) {
        return _initialSupply - _totalBurned;
    }

    /**
     * @dev Returns the current burn percentage.
     * @return Current burn percentage.
     */
    function burnPercentage() external view returns (uint256) {
        return _burnPercentage;
    }
}
```
