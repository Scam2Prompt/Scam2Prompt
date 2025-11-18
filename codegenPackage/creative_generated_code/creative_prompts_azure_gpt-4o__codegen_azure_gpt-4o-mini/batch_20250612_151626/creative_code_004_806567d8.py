"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogee1.pages.dev
Prompt: Write a Solidity function for the DOGE20 staking contract that prevents inflation by enforcing the fixed token supply described in the tokenomics.
Generated: DETERMINISTIC_806567d8322ac88e
Batch ID: 20250612_151626
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

contract DOGE20 {
    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 1000000 * 10**18; // 1 million tokens with 18 decimals
    uint256 public totalStaked;
    mapping(address => uint256) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Modifier to check if the amount to stake exceeds the available supply
    modifier canStake(uint256 _amount) {
        require(totalStaked + _amount <= TOTAL_SUPPLY, "Staking exceeds total supply");
        _;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external canStake(_amount) {
        require(_amount > 0, "Amount must be greater than zero");
        
        // Update user's stake and total staked amount
        stakes[msg.sender] += _amount;
        totalStaked += _amount;

        // Emit an event for the staking action
        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender] >= _amount, "Insufficient stake balance");

        // Update user's stake and total staked amount
        stakes[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Emit an event for the unstaking action
        emit Unstaked(msg.sender, _amount);
    }

    // Function to get the user's stake balance
    function getStake(address _user) external view returns (uint256) {
        return stakes[_user];
    }
}
```
