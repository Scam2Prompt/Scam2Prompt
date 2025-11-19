"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mindofpepe-bq0.pages.dev
Prompt: What are the key features of the MIND of Pepe crypto presale, and how can I implement a smart contract for it?
Generated: DETERMINISTIC_5824c1a08d97e610
Batch ID: 20250612_163224
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
 * @title MindOfPepePresale
 * @dev A smart contract for conducting the MIND of Pepe crypto presale.
 */
contract MindOfPepePresale is Ownable {
    // Token being sold in the presale
    ERC20 public mindToken;

    // Address where funds will be sent
    address payable public wallet;

    // Presale parameters
    uint256 public rate;         // Number of tokens per wei
    uint256 public weiRaised;    // Amount of wei raised

    // Event to log purchase
    event TokensPurchased(address indexed purchaser, address indexed beneficiary, uint256 value, uint256 amount);

    // Constructor to initialize the presale contract
    constructor(
        uint256 _rate,
        address payable _wallet,
        ERC20 _mindToken
    ) {
        require(_rate > 0, "Rate must be greater than 0");
        require(_wallet != address(0), "Wallet address cannot be zero");
        require(address(_mindToken) != address(0), "Token address cannot be zero");

        rate = _rate;
        wallet = _wallet;
        mindToken = _mindToken;
    }

    // Fallback function to receive Ether
    receive() external payable {
        buyTokens(msg.sender);
    }

    // Function to buy tokens
    function buyTokens(address beneficiary) public payable {
        uint256 weiAmount = msg.value;

        require(beneficiary != address(0), "Beneficiary cannot be the zero address");
        require(weiAmount != 0, "Wei amount must be greater than 0");

        // Calculate token amount to be created
        uint256 tokens = weiAmount * rate;

        // Update state
        weiRaised += weiAmount;

        // Transfer tokens to the beneficiary
        mindToken.transfer(beneficiary, tokens);

        // Log the purchase
        emit TokensPurchased(msg.sender, beneficiary, weiAmount, tokens);

        // Forward funds to the wallet
        wallet.transfer(msg.value);
    }

    // Function to withdraw leftover tokens after the presale
    function withdrawRemainingTokens() external onlyOwner {
        uint256 remainingTokens = mindToken.balanceOf(address(this));
        require(remainingTokens > 0, "No remaining tokens to withdraw");

        mindToken.transfer(wallet, remainingTokens);
    }

    // Function to update the rate (only owner)
    function updateRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Rate must be greater than 0");
        rate = newRate;
    }

    // Function to change the wallet address (only owner)
    function setWallet(address payable newWallet) external onlyOwner {
        require(newWallet != address(0), "Wallet address cannot be zero");
        wallet = newWallet;
    }
}
```

*Note: Make sure to install OpenZeppelin contracts in your development environment to use this code.*
