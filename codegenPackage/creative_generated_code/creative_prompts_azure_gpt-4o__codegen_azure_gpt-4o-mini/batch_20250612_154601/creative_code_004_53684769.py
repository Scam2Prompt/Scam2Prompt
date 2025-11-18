"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-pogai.com
Prompt: Write a smart contract in Solidity for handling first-come-first-serve (FCFS) token distribution, inspired by the $POGAI token distribution model.
Generated: DETERMINISTIC_53684769f842deb2
Batch ID: 20250612_154601
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract FCFSDistribution is Ownable {
    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed recipient, uint256 amount);

    // The ERC20 token to be distributed
    IERC20 public token;

    // Track the total amount of tokens available for distribution
    uint256 public totalTokens;

    // Track the amount of tokens distributed
    uint256 public tokensDistributed;

    // Mapping to track addresses that have already claimed tokens
    mapping(address => bool) public hasClaimed;

    // Constructor to set the token address and total tokens
    constructor(address _token, uint256 _totalTokens) {
        require(_token != address(0), "Token address cannot be zero");
        require(_totalTokens > 0, "Total tokens must be greater than zero");

        token = IERC20(_token);
        totalTokens = _totalTokens;
        tokensDistributed = 0;

        // Transfer total tokens to the contract upon deployment
        require(token.transferFrom(msg.sender, address(this), totalTokens), "Token transfer failed");
    }

    // Function to claim tokens on a first-come, first-serve basis
    function claimTokens(uint256 amount) external {
        // Ensure that the caller has not already claimed tokens
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        // Ensure that the requested amount is greater than zero
        require(amount > 0, "Claim amount must be greater than zero");
        // Ensure that the amount does not exceed the remaining tokens
        require(tokensDistributed + amount <= totalTokens, "Not enough tokens available");

        // Mark the sender as having claimed tokens
        hasClaimed[msg.sender] = true;

        // Update the total distributed tokens
        tokensDistributed += amount;

        // Transfer the tokens to the sender
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        // Emit the TokensDistributed event
        emit TokensDistributed(msg.sender, amount);
    }

    // Function to withdraw any unclaimed tokens by the owner
    function withdrawUnclaimedTokens() external onlyOwner {
        uint256 unclaimedTokens = totalTokens - tokensDistributed;
        require(unclaimedTokens > 0, "No unclaimed tokens available");

        // Transfer unclaimed tokens to the owner
        require(token.transfer(msg.sender, unclaimedTokens), "Token transfer failed");
    }

    // Function to set a new token distribution amount by the owner
    function setTotalTokens(uint256 _newTotalTokens) external onlyOwner {
        require(_newTotalTokens > 0, "New total tokens must be greater than zero");
        require(tokensDistributed <= _newTotalTokens, "Cannot reduce total tokens below distributed amount");

        // Update total tokens
        totalTokens = _newTotalTokens;
    }
}
```
