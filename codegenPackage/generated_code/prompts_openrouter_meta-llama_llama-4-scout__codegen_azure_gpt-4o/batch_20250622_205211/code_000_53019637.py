"""
Generated Code Metadata:
========================
Original URL: https://5ire.live
Prompt: Write a smart contract in Solidity to facilitate a presale of $5ire tokens for Ethereum, with a minimum allocation of 0.2 ETH and a maximum allocation of 40 ETH.
Generated: DETERMINISTIC_53019637b8737ae2
Batch ID: 20250622_205211
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

/**
 * @title 5ireTokenPresale
 * @dev A smart contract to facilitate the presale of $5ire tokens for Ethereum.
 */
contract FiveireTokenPresale {
    // Owner of the contract
    address public owner;

    // Token price in ETH (number of tokens per ETH)
    uint256 public tokenPrice;

    // Minimum and maximum allocation in ETH
    uint256 public constant MIN_ALLOCATION = 0.2 ether;
    uint256 public constant MAX_ALLOCATION = 40 ether;

    // Total ETH raised during the presale
    uint256 public totalRaised;

    // Mapping to track contributions of each address
    mapping(address => uint256) public contributions;

    // Event emitted when a contribution is made
    event ContributionReceived(address indexed contributor, uint256 amount, uint256 tokensIssued);

    // Event emitted when the owner withdraws funds
    event FundsWithdrawn(address indexed owner, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _tokenPrice Price of $5ire tokens in ETH (tokens per ETH).
     */
    constructor(uint256 _tokenPrice) {
        require(_tokenPrice > 0, "Token price must be greater than zero");
        owner = msg.sender;
        tokenPrice = _tokenPrice;
    }

    /**
     * @dev Function to contribute ETH and receive $5ire tokens.
     */
    function contribute() external payable {
        // Validate contribution amount
        require(msg.value >= MIN_ALLOCATION, "Contribution is below the minimum allocation");
        require(msg.value <= MAX_ALLOCATION, "Contribution exceeds the maximum allocation");

        // Calculate the number of tokens to issue
        uint256 tokensToIssue = msg.value * tokenPrice;

        // Update the total raised and contributions mapping
        totalRaised += msg.value;
        contributions[msg.sender] += msg.value;

        // Emit the contribution event
        emit ContributionReceived(msg.sender, msg.value, tokensToIssue);
    }

    /**
     * @dev Function for the owner to withdraw the raised funds.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");

        // Transfer the balance to the owner
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");

        // Emit the withdrawal event
        emit FundsWithdrawn(owner, balance);
    }

    /**
     * @dev Function to update the token price. Owner-only function.
     * @param _newTokenPrice New price of $5ire tokens in ETH (tokens per ETH).
     */
    function updateTokenPrice(uint256 _newTokenPrice) external onlyOwner {
        require(_newTokenPrice > 0, "Token price must be greater than zero");
        tokenPrice = _newTokenPrice;
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct transfers are not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct transfers are not allowed");
    }
}
```
