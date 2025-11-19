"""
Generated Code Metadata:
========================
Original URL: https://pulsemex.com
Prompt: Design a simple smart contract on PulseChain to automate token distribution for a new DeFi project.
Generated: DETERMINISTIC_b373d89cf28bbdbd
Batch ID: 20250622_211952
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

// Importing the OpenZeppelin ERC20 contract for token functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for automated token distribution
contract TokenDistributor is Ownable {
    // Event to log the distribution of tokens
    event TokensDistributed(address indexed recipient, uint256 amount);

    // The token to be distributed
    IERC20 public token;

    // Mapping to track the distribution status of each address
    mapping(address => bool) public hasReceivedTokens;

    // Constructor to set the token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    // Function to distribute tokens to a list of addresses
    function distributeTokens(address[] calldata recipients, uint256 amount) external onlyOwner {
        require(recipients.length > 0, "No recipients provided");
        require(amount > 0, "Amount must be greater than zero");

        // Check if the contract has enough tokens to distribute
        uint256 totalAmount = amount * recipients.length;
        require(token.balanceOf(address(this)) >= totalAmount, "Insufficient token balance in contract");

        // Loop through each recipient and transfer tokens
        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            require(!hasReceivedTokens[recipient], "Recipient has already received tokens");
            require(recipient != address(0), "Invalid recipient address");

            // Transfer tokens to the recipient
            token.transfer(recipient, amount);
            hasReceivedTokens[recipient] = true; // Mark as received

            // Emit event for the distribution
            emit TokensDistributed(recipient, amount);
        }
    }

    // Function to withdraw any remaining tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient token balance in contract");

        // Transfer tokens to the owner
        token.transfer(owner(), amount);
    }

    // Function to check the contract's token balance
    function getContractTokenBalance() external view returns (uint256) {
        return token.balanceOf(address(this));
    }
}
```
