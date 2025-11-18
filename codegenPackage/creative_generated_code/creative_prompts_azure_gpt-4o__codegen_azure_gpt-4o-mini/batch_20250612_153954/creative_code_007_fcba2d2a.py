"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axgt-sushi.lat
Prompt: Write a smart contract to interact with SushiSwap's farming feature (Onsen), allowing users to stake tokens and claim rewards.
Generated: DETERMINISTIC_fcba2d2a52da98f5
Batch ID: 20250612_153954
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

// Interface for interacting with the SushiSwap MasterChef contract
interface IMasterChef {
    function deposit(uint256 pid, uint256 amount) external;
    function withdraw(uint256 pid, uint256 amount) external;
    function emergencyWithdraw(uint256 pid) external;
    function pendingSushi(uint256 pid, address user) external view returns (uint256);
}

// Interface for the ERC20 token standard
interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract SushiSwapStaking {
    // The address of the MasterChef contract
    IMasterChef public masterChef;

    // The address of the token to be staked
    IERC20 public stakingToken;

    // Pool ID in the MasterChef contract
    uint256 public poolId;

    // Mapping to track user balances
    mapping(address => uint256) public userBalances;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to set the MasterChef, staking token, and pool ID
    constructor(address _masterChef, address _stakingToken, uint256 _poolId) {
        masterChef = IMasterChef(_masterChef);
        stakingToken = IERC20(_stakingToken);
        poolId = _poolId;
    }

    // Function to stake tokens in the SushiSwap pool
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        
        // Transfer tokens from user to this contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // Approve MasterChef to spend the tokens
        stakingToken.approve(address(masterChef), amount);

        // Deposit tokens into MasterChef
        masterChef.deposit(poolId, amount);
        
        // Update user balance
        userBalances[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw tokens from the SushiSwap pool
    function withdraw(uint256 amount) external {
        require(amount > 0, "Cannot withdraw 0");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");

        // Withdraw tokens from MasterChef
        masterChef.withdraw(poolId, amount);

        // Update user balance
        userBalances[msg.sender] -= amount;

        // Transfer tokens back to user
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");
        
        emit Withdrawn(msg.sender, amount);
    }

    // Function to get pending rewards for a user
    function pendingRewards() external view returns (uint256) {
        return masterChef.pendingSushi(poolId, msg.sender);
    }

    // Emergency function to withdraw tokens without caring about rewards
    function emergencyWithdraw() external {
        uint256 balance = userBalances[msg.sender];
        require(balance > 0, "No tokens to withdraw");

        // Call emergency withdraw in MasterChef
        masterChef.emergencyWithdraw(poolId);
        
        // Reset user balance
        userBalances[msg.sender] = 0;

        // Transfer all tokens back to user
        require(stakingToken.transfer(msg.sender, balance), "Transfer failed");
    }
}
```
