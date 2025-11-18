"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lookscoin.com
Prompt: Generate a Solidity contract that enables staking $LOOK tokens to form a branch and encode payment distribution for contributors.
Generated: DETERMINISTIC_867fbf5f9bf47fef
Batch ID: 20250612_153256
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

// Interface for the ERC20 token used for staking
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Contract for staking $LOOK tokens
contract LookStaking {
    // State variables
    IERC20 public lookToken; // The $LOOK token contract
    uint256 public totalStaked; // Total amount of tokens staked
    mapping(address => uint256) public stakedAmount; // Amount staked by each address
    mapping(address => uint256) public lastStakeTime; // Last stake time for each address

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    
    // Constructor to set the token address
    constructor(address _lookToken) {
        require(_lookToken != address(0), "Invalid token address");
        lookToken = IERC20(_lookToken);
    }

    // Function to stake $LOOK tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Must stake more than 0 tokens");
        
        // Transfer tokens from the user to this contract
        lookToken.transferFrom(msg.sender, address(this), amount);
        
        // Update state variables
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;
        lastStakeTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $LOOK tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Must unstake more than 0 tokens");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update state variables
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        lookToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to check staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmount[user];
    }

    // Function to get total staked amount
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```
