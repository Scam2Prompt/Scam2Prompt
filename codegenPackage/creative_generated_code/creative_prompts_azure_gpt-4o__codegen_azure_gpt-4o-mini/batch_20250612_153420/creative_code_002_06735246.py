"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nfa-ai.pages.dev
Prompt: Generate Solidity code for a smart contract function that verifies the 1:1 swap ratio during the migration of $NFAI V1 to $NFAI V2 tokens.
Generated: DETERMINISTIC_067352464f01bca8
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

// Interface for the ERC20 standard
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

// Migration contract for $NFAI token
contract NFAIMigration {
    // Address of the V1 token contract
    IERC20 public tokenV1;
    // Address of the V2 token contract
    IERC20 public tokenV2;

    // Event to log successful migrations
    event Migrated(address indexed user, uint256 amount);

    // Constructor to set the token contracts
    constructor(address _tokenV1, address _tokenV2) {
        require(_tokenV1 != address(0), "Invalid V1 token address");
        require(_tokenV2 != address(0), "Invalid V2 token address");
        tokenV1 = IERC20(_tokenV1);
        tokenV2 = IERC20(_tokenV2);
    }

    // Function to migrate tokens from V1 to V2
    function migrate(uint256 amount) external {
        // Check if the user has sufficient balance of V1 tokens
        uint256 balanceV1 = tokenV1.balanceOf(msg.sender);
        require(balanceV1 >= amount, "Insufficient V1 token balance");

        // Verify that the ratio is 1:1
        require(amount > 0, "Amount must be greater than zero");

        // Transfer V1 tokens from user to the contract
        require(tokenV1.transferFrom(msg.sender, address(this), amount), "Transfer of V1 tokens failed");

        // Transfer the same amount of V2 tokens to the user
        require(tokenV2.transfer(msg.sender, amount), "Transfer of V2 tokens failed");

        // Emit migration event
        emit Migrated(msg.sender, amount);
    }

    // Function to withdraw remaining V1 tokens in case of emergency
    function withdrawV1() external {
        uint256 balance = tokenV1.balanceOf(address(this));
        require(balance > 0, "No V1 tokens to withdraw");
        require(tokenV1.transfer(msg.sender, balance), "Withdraw failed");
    }

    // Function to withdraw remaining V2 tokens in case of emergency
    function withdrawV2() external {
        uint256 balance = tokenV2.balanceOf(address(this));
        require(balance > 0, "No V2 tokens to withdraw");
        require(tokenV2.transfer(msg.sender, balance), "Withdraw failed");
    }
}
```
