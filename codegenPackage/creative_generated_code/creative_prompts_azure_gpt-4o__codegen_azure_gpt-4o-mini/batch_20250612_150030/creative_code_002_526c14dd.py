"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wepestreetpepe-new.pages.dev
Prompt: Generate code to simulate a cryptocurrency presale transaction for tokens like "Wall Street Pepe Token" (WEPE), ensuring compliance with Ethereum-based smart contracts.
Generated: DETERMINISTIC_526c14dd95ebb30c
Batch ID: 20250612_150030
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

// Importing OpenZeppelin's ERC20 token implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title WallStreetPepeTokenPresale
 * @dev A smart contract to simulate a presale transaction for Wall Street Pepe Token (WEPE).
 */
contract WallStreetPepeTokenPresale is Ownable {
    // The token being sold
    ERC20 public token;

    // Presale parameters
    uint256 public presaleRate; // Rate in wei per token
    uint256 public presaleEndTime; // End time for presale
    uint256 public tokensSold; // Total tokens sold during presale

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);

    /**
     * @dev Constructor to set the token, rate, and duration.
     * @param _token Address of the ERC20 token contract
     * @param _presaleRate Rate in wei per token
     * @param _presaleDuration Duration of the presale in seconds
     */
    constructor(ERC20 _token, uint256 _presaleRate, uint256 _presaleDuration) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_presaleRate > 0, "Presale rate must be greater than zero");
        require(_presaleDuration > 0, "Presale duration must be greater than zero");

        token = _token;
        presaleRate = _presaleRate;
        presaleEndTime = block.timestamp + _presaleDuration;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * @param amount The number of tokens to purchase
     */
    function buyTokens(uint256 amount) external payable {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value == amount * presaleRate, "Incorrect Ether sent");

        // Calculate total tokens to be sold
        tokensSold += amount;

        // Transfer tokens from the contract to the buyer
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        // Emit event for the purchase
        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw Ether collected from presale.
     * Only owner can call this function.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        // Transfer the Ether to the owner's address
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers to the contract
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
