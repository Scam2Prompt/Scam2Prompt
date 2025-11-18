"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ktest-296.pages.dev
Prompt: Write a smart contract in Solidity to implement a token presale mechanism with a cap of 5,000 ETH and an exchange rate of 1 ETH = 99,500 tokens.
Generated: DETERMINISTIC_9079c53a24f2f400
Batch ID: 20250612_152827
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
 * @title TokenPresale
 * @dev Implements a capped presale mechanism for an ERC20 token
 */
contract TokenPresale {
    // Address of the token contract
    address public tokenAddress;

    // Address to collect ETH contributions
    address public wallet;

    // Cap in ETH
    uint256 public cap = 5000 ether;

    // Exchange rate: 1 ETH = 99,500 tokens
    uint256 public constant exchangeRate = 99500;

    // Total amount of ETH raised
    uint256 public totalRaised;

    // Event to log contribution details
    event TokensPurchased(address indexed purchaser, uint256 value, uint256 amount);

    /**
     * @dev Constructor to initialize the contract
     * @param _tokenAddress Address of the token contract
     * @param _wallet Address to collect ETH contributions
     */
    constructor(address _tokenAddress, address _wallet) {
        require(_tokenAddress != address(0), "Token address cannot be the zero address");
        require(_wallet != address(0), "Wallet address cannot be the zero address");

        tokenAddress = _tokenAddress;
        wallet = _wallet;
    }

    /**
     * @dev Fallback function to accept ETH contributions
     */
    receive() external payable {
        purchaseTokens();
    }

    /**
     * @dev Function to purchase tokens during the presale
     */
    function purchaseTokens() public payable {
        uint256 weiAmount = msg.value;

        // Input validation
        require(weiAmount > 0, "Contribution amount must be greater than zero");
        require(totalRaised + weiAmount <= cap, "Contribution exceeds presale cap");

        // Calculate number of tokens based on exchange rate
        uint256 tokenAmount = weiAmount * exchangeRate;

        // Update total ETH raised
        totalRaised += weiAmount;

        // Transfer tokens to the contributor
        require(
            ERC20(tokenAddress).transfer(msg.sender, tokenAmount),
            "Token transfer failed"
        );

        // Forward the received ETH to the wallet
        (bool success, ) = wallet.call{value: weiAmount}("");
        require(success, "ETH transfer to wallet failed");

        // Emit event for logging
        emit TokensPurchased(msg.sender, weiAmount, tokenAmount);
    }

    /**
     * @dev Function to check remaining cap
     */
    function remainingCap() public view returns (uint256) {
        return cap - totalRaised;
    }
}

/**
 * @dev Interface for ERC20 token contract
 */
interface ERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
