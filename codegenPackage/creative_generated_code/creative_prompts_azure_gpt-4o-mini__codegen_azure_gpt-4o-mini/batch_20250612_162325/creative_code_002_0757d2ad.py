"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accept-gummyonsol-51d.pages.dev
Prompt: Generate a code snippet for a decentralized application (dApp) that allows users to claim their $Gummy tokens from the airdrop.
Generated: DETERMINISTIC_0757d2ad60905e38
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Airdrop contract for claiming $Gummy tokens
contract GummyAirdrop is Ownable {
    // The ERC20 token contract
    IERC20 public gummyToken;

    // Mapping to track claimed airdrop status
    mapping(address => bool) public hasClaimed;

    // Event to emit when tokens are claimed
    event TokensClaimed(address indexed user, uint256 amount);

    // Constructor to set the token address
    constructor(address _gummyToken) {
        require(_gummyToken != address(0), "Invalid token address");
        gummyToken = IERC20(_gummyToken);
    }

    // Function to claim airdrop tokens
    function claimTokens(uint256 amount) external {
        // Check if user has already claimed
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        // Validate requested amount
        require(amount > 0, "Claim amount must be greater than zero");
        
        // Check contract balance
        uint256 contractBalance = gummyToken.balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient contract balance");

        // Update claimed status
        hasClaimed[msg.sender] = true;

        // Transfer tokens to user
        bool success = gummyToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Emit event for successful claim
        emit TokensClaimed(msg.sender, amount);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        uint256 contractBalance = gummyToken.balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient contract balance");

        // Transfer tokens to owner
        bool success = gummyToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }
}
```
