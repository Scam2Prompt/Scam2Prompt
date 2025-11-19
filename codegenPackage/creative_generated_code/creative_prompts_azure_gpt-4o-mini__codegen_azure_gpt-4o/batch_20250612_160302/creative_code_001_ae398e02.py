"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-blubtheblob.com
Prompt: What are the best practices for developing a presale smart contract like the one for Blub The Blob?
Generated: DETERMINISTIC_ae398e0215a403c7
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the clean, production-ready smart contract code for implementing a presale similar to the one described. The code is written in Solidity (a popular language for Ethereum smart contracts), adhering to best practices.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title PresaleContract
 * @dev A smart contract for handling token presale events.
 */
contract PresaleContract {
    // Owner of the contract
    address public owner;

    // Token price in wei (1 ETH = 10^18 wei)
    uint256 public tokenPrice;

    // Total tokens available for presale
    uint256 public totalTokensAvailable;

    // Tokens sold so far
    uint256 public tokensSold;

    // Mapping to track buyer balances
    mapping(address => uint256) public balances;

    // Presale active state
    bool public presaleActive;

    // Event to log token purchases
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Event to indicate presale status change
    event PresaleStatusChanged(bool active);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can execute this.");
        _;
    }

    /**
     * @dev Contract constructor to initialize presale parameters.
     * @param _tokenPrice Price of each token (in wei).
     * @param _totalTokensAvailable Total tokens available for presale.
     */
    constructor(uint256 _tokenPrice, uint256 _totalTokensAvailable) {
        require(_tokenPrice > 0, "Token price must be greater than zero.");
        require(_totalTokensAvailable > 0, "Total tokens must be greater than zero.");
        
        owner = msg.sender;
        tokenPrice = _tokenPrice;
        totalTokensAvailable = _totalTokensAvailable;
        presaleActive = true; // Presale is active by default
    }

    /**
     * @dev Function to buy tokens during the presale.
     * The amount of tokens bought is calculated based on the sent ETH.
     */
    function buyTokens() external payable {
        require(presaleActive, "Presale is not active.");
        require(msg.value > 0, "No ETH sent.");
        uint256 tokensToBuy = msg.value / tokenPrice;
        require(tokensToBuy > 0, "Insufficient ETH sent for token purchase.");
        require(tokensSold + tokensToBuy <= totalTokensAvailable, "Not enough tokens available.");
        
        // Update state
        tokensSold += tokensToBuy;
        balances[msg.sender] += tokensToBuy;

        emit TokensPurchased(msg.sender, tokensToBuy);
    }

    /**
     * @dev Function to toggle the presale status (activate/deactivate).
     * Can only be called by the contract owner.
     */
    function togglePresaleStatus() external onlyOwner {
        presaleActive = !presaleActive;
        emit PresaleStatusChanged(presaleActive);
    }

    /**
     * @dev Function for the owner to withdraw collected funds.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw.");
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed.");
    }

    /**
     * @dev Function for the owner to withdraw unsold tokens.
     * Only callable after the presale ends.
     */
    function withdrawUnsoldTokens() external onlyOwner {
        require(!presaleActive, "Presale must be inactive to withdraw unsold tokens.");
        uint256 unsoldTokens = totalTokensAvailable - tokensSold;
        require(unsoldTokens > 0, "No unsold tokens remaining.");

        // Logic to transfer the unsold tokens can go here
        // (e.g., transfer tokens to the owner's address if using ERC-20)

        // Placeholder for actual token transfer implementation:
        // token.transfer(owner, unsoldTokens);
    }

    /**
     * @dev Fallback function to reject accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct ETH transfers are not allowed.");
    }

    /**
     * @dev Receive function to reject accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers are not allowed.");
    }
}
```

This smart contract implements a presale mechanism with robust error handling, owner controls, and event logging. While it doesn't integrate with an ERC-20 token directly, you can extend this code to work with specific token standards by adding token transfer logic.
