"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idegen-claims.pages.dev
Prompt: Write a Solidity function to manage staking and unstaking of $IDGN tokens, ensuring smooth trading as described in the tokenomics.
Generated: DETERMINISTIC_af5ff2906f4b46fa
Batch ID: 20250612_150426
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

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract IDGNStaking {
    // The ERC20 token that will be staked
    IERC20 public idgnToken;

    // Mapping to track the staked balances of users
    mapping(address => uint256) public stakedBalances;

    // Event to emit when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event to emit when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the token address
    constructor(IERC20 _idgnToken) {
        idgnToken = _idgnToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens from the user's wallet to the contract
        require(idgnToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staked balance
        stakedBalances[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balance before transfer to prevent reentrancy
        stakedBalances[msg.sender] -= amount;

        // Transfer tokens back to the user's wallet
        require(idgnToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to view staked balance of a user
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }
}
```
