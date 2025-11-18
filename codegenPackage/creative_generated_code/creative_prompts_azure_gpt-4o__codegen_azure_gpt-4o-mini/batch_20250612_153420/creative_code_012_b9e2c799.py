"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-verse.pages.dev
Prompt: Generate a Solidity contract for an airdrop mechanism that distributes $HEHE tokens to 666 lucky users, as mentioned on the website.
Generated: DETERMINISTIC_b9e2c7998821ed7a
Batch ID: 20250612_153420
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

// Interface for the ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

// Airdrop contract
contract HEHEAirdrop {
    // The ERC20 token contract address
    IERC20 public token;

    // Total number of airdrop recipients allowed
    uint256 public constant MAX_RECIPIENTS = 666;

    // Mapping to track claimed statuses of recipients
    mapping(address => bool) public hasClaimed;

    // Counter for the number of recipients who have claimed their tokens
    uint256 public claimedCount;

    // Event emitted when tokens are successfully airdropped
    event AirdropClaimed(address indexed recipient, uint256 amount);

    // Constructor to set the token contract address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    // Function to claim airdrop tokens
    function claimAirdrop(uint256 amount) external {
        require(claimedCount < MAX_RECIPIENTS, "Airdrop limit reached");
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens to the caller
        hasClaimed[msg.sender] = true;
        claimedCount++;
        
        // Attempt the transfer, revert if it fails
        bool success = token.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Emit event for the successful airdrop
        emit AirdropClaimed(msg.sender, amount);
    }

    // Function to withdraw unclaimed tokens after the airdrop is completed
    function withdrawRemainingTokens() external {
        require(claimedCount >= MAX_RECIPIENTS, "Airdrop still ongoing");
        
        uint256 remainingBalance = token.balanceOf(address(this));
        require(remainingBalance > 0, "No remaining tokens to withdraw");

        // Transfer remaining tokens to the contract creator
        address owner = msg.sender; // Assuming the contract creator is the owner
        bool success = token.transfer(owner, remainingBalance);
        require(success, "Withdrawal failed");
    }

    // Function to check the number of claimed tokens
    function claimedCount() external view returns (uint256) {
        return claimedCount;
    }
}
```
