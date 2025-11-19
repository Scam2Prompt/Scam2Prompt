"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://market-jennercom.pages.dev
Prompt: Generate a smart contract in Solidity for a presale that caps at 1000 ETH and allows purchases of JENNER tokens at a rate of 99,500 tokens per 0.1 ETH.
Generated: DETERMINISTIC_7f7d9c430a46f266
Batch ID: 20250612_163200
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title JennerPresale
 * @dev A presale contract for JENNER tokens with a cap and specified rate.
 */
contract JennerPresale is Ownable {
    // The token being sold
    IERC20 public jennerToken;

    // Maximum amount of ETH that can be raised
    uint256 public constant CAP = 1000 ether;

    // Rate of token distribution: 99,500 tokens per 0.1 ETH
    uint256 public constant TOKEN_RATE = 995000; // tokens per 0.1 ETH

    // Total funds raised in the presale
    uint256 public totalRaised;

    // Track whether the presale is active
    bool public presaleActive;

    // Events for logging purchases and presale status changes
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 ethSpent);
    event PresaleStatusChanged(bool isActive);

    /**
     * @param _jennerToken Address of the JENNER token contract
     */
    constructor(address _jennerToken) {
        require(_jennerToken != address(0), "Invalid token address");
        jennerToken = IERC20(_jennerToken);
        presaleActive = false; // Presale starts inactive
    }

    /**
     * @notice Activate or deactivate the presale
     * @param _active New presale status
     */
    function setPresaleStatus(bool _active) external onlyOwner {
        presaleActive = _active;
        emit PresaleStatusChanged(_active);
    }

    /**
     * @notice Purchase JENNER tokens during the presale
     */
    function buyTokens() external payable {
        require(presaleActive, "Presale is not active");
        require(msg.value > 0, "Ether value must be greater than 0");
        require(totalRaised + msg.value <= CAP, "Cap reached");

        // Calculate number of tokens to purchase
        uint256 tokensToBuy = (msg.value * 10 * TOKEN_RATE) / 1 ether; // Calculate tokens based on the amount of ETH sent

        // Update total raised
        totalRaised += msg.value;

        // Transfer tokens to buyer
        require(jennerToken.balanceOf(address(this)) >= tokensToBuy, "Not enough tokens in the contract");
        require(jennerToken.transfer(msg.sender, tokensToBuy), "Token transfer failed");

        emit TokensPurchased(msg.sender, tokensToBuy, msg.value);
    }

    /**
     * @notice Withdraw funds raised to the owner's address
     */
    function withdrawFunds() external onlyOwner {
        require(totalRaised > 0, "No funds to withdraw");
        
        uint256 amount = address(this).balance;
        (bool success, ) = owner().call{value: amount}("");
        require(success, "Transfer failed");

        totalRaised = 0; // Reset total raised after withdrawal
    }

    /**
     * @notice Withdraw remaining tokens (if any) to the owner's address
     */
    function withdrawRemainingTokens() external onlyOwner {
        uint256 remainingTokens = jennerToken.balanceOf(address(this));
        require(remainingTokens > 0, "No tokens to withdraw");
        require(jennerToken.transfer(owner(), remainingTokens), "Token transfer failed");
    }

    /**
     * @dev Fallback function to accept ETH
     */
    receive() external payable {
        buyTokens(); // Allow sending ETH directly to buy tokens
    }
}
```
