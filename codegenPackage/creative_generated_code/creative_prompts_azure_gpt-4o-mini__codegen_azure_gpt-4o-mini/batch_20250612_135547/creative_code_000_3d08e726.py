"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-tokens.live
Prompt: Generate a code snippet for a token claim process using a smart contract.
Generated: DETERMINISTIC_3d08e726b2a1a192
Batch ID: 20250612_135547
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

// Import necessary libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Define the TokenClaim contract
contract TokenClaim is Ownable {
    // Declare state variables
    mapping(address => uint256) private claims; // Mapping to track claims for each address
    IERC20 public token; // ERC20 token to be claimed

    // Event to log claimed tokens
    event TokensClaimed(address claimant, uint256 amount);

    // Constructor to initialize the token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        token = IERC20(_tokenAddress); // Set the ERC20 token address
    }

    // Function to set claim amount for an address (only owner can call)
    function setClaimAmount(address claimant, uint256 amount) external onlyOwner {
        require(claimant != address(0), "Claimant address cannot be zero");
        claims[claimant] = amount; // Set the claim amount
    }

    // Function for users to claim their tokens
    function claimTokens() external {
        uint256 amount = claims[msg.sender]; // Retrieve claim amount for the sender
        require(amount > 0, "No tokens to claim"); // Ensure there is an amount to claim

        claims[msg.sender] = 0; // Reset claim amount to prevent re-entrancy
        require(token.transfer(msg.sender, amount), "Token transfer failed"); // Transfer tokens

        emit TokensClaimed(msg.sender, amount); // Emit claim event
    }

    // Function to withdraw unclaimed tokens (only owner can call)
    function withdrawUnclaimedTokens() external onlyOwner {
        uint256 balance = token.balanceOf(address(this)); // Get contract's token balance
        require(balance > 0, "No tokens to withdraw"); // Ensure there are tokens to withdraw

        require(token.transfer(owner(), balance), "Withdrawal failed"); // Transfer tokens to owner
    }

    // Function to check the claim amount for an address
    function getClaimAmount(address claimant) external view returns (uint256) {
        return claims[claimant]; // Return the claim amount
    }
}
```
