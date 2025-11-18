"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dasdasdaadsd.pages.dev
Prompt: Create a Solidity smart contract to implement an airdrop mechanism for BEFE tokens, distributing them to eligible wallet addresses based on predefined criteria.
Generated: DETERMINISTIC_3f1360c21bb4eeb1
Batch ID: 20250612_151906
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Airdrop contract for BEFE tokens
contract BEFEAirdrop is Ownable {
    // Token to be distributed
    IERC20 public token;

    // Event to log airdrop distribution
    event AirdropDistributed(address indexed recipient, uint256 amount);

    // Mapping to track airdrop eligibility
    mapping(address => bool) public eligibleRecipients;

    // Constructor to set the token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    // Function to set eligible recipients
    function setEligibleRecipients(address[] calldata recipients) external onlyOwner {
        for (uint256 i = 0; i < recipients.length; i++) {
            eligibleRecipients[recipients[i]] = true;
        }
    }

    // Function to airdrop tokens to eligible recipients
    function airdropTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");

        // Loop through eligible recipients and distribute tokens
        for (uint256 i = 0; i < eligibleRecipients.length; i++) {
            address recipient = eligibleRecipients[i];
            // Check if the recipient is eligible
            if (eligibleRecipients[recipient]) {
                // Transfer tokens to the recipient
                require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");
                token.transfer(recipient, amount);
                emit AirdropDistributed(recipient, amount);
            }
        }
    }

    // Function to withdraw remaining tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        token.transfer(msg.sender, amount);
    }

    // Function to check if an address is eligible for airdrop
    function isEligible(address recipient) external view returns (bool) {
        return eligibleRecipients[recipient];
    }
}
```
