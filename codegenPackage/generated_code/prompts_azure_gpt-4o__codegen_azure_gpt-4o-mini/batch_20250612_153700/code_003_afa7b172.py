"""
Generated Code Metadata:
========================
Original URL: https://internetmoney-4rq.pages.dev
Prompt: Write a Solidity function to implement a "Buy 'N Burn" mechanism for TIME tokens, ensuring it calculates the burned percentage of the total supply dynamically, as described on the webpage.
Generated: DETERMINISTIC_afa7b1728d64fb65
Batch ID: 20250612_153700
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TIME Token with Buy 'N Burn Mechanism
 * @dev This contract implements a token with a dynamic burn mechanism.
 */
contract TIME is ERC20, Ownable {
    // Percentage of tokens to burn on each buy transaction (in basis points)
    uint256 public burnPercentage;
    // Total supply of the token
    uint256 public totalSupply;

    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    /**
     * @dev Constructor to initialize the token with a name, symbol, and total supply.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of the token.
     * @param _burnPercentage The percentage of tokens to burn on each buy transaction.
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _burnPercentage) 
        ERC20(name, symbol) 
    {
        require(_burnPercentage <= 10000, "Burn percentage must be between 0 and 100%");
        burnPercentage = _burnPercentage;
        totalSupply = initialSupply * (10 ** decimals());
        _mint(msg.sender, totalSupply);
    }

    /**
     * @dev Function to buy tokens and burn a percentage of the total supply.
     * @param amount The amount of tokens to buy.
     */
    function buyTokens(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value > 0, "Ether value must be greater than zero");

        // Calculate the amount to burn
        uint256 burnAmount = (amount * burnPercentage) / 10000;

        // Ensure we do not burn more than the total supply
        require(burnAmount <= totalSupply, "Burn amount exceeds total supply");

        // Transfer tokens to the buyer
        _transfer(address(this), msg.sender, amount - burnAmount);

        // Burn the tokens
        _burn(address(this), burnAmount);
        emit TokensBurned(address(this), burnAmount);
    }

    /**
     * @dev Function to update the burn percentage.
     * @param newBurnPercentage The new burn percentage to set.
     */
    function updateBurnPercentage(uint256 newBurnPercentage) external onlyOwner {
        require(newBurnPercentage <= 10000, "Burn percentage must be between 0 and 100%");
        burnPercentage = newBurnPercentage;
    }

    /**
     * @dev Function to withdraw Ether from the contract.
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {}
}
```
