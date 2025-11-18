"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fffrfh.pages.dev
Prompt: Write a smart contract in Solidity that allows users to stake stETH and earn MOR tokens as rewards, following the staking mechanism described on the Morpheus platform. Ensure the contract includes a 7-day lockup period for stETH deposits and pro-rata MOR emissions.
Generated: DETERMINISTIC_769b02747fc30435
Batch ID: 20250612_151329
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

// Interface for the ERC20 token (stETH)
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Interface for the MOR token
interface IMORToken {
    function mint(address recipient, uint256 amount) external;
}

// Staking contract for stETH and MOR token rewards
contract StakingContract {
    // Events for logging
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Unstaked(address indexed user, uint256 amount, uint256 timestamp);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constants
    uint256 public constant LOCKUP_PERIOD = 7 days;

    // Struct to hold user staking information
    struct UserInfo {
        uint256 amount; // Amount of stETH staked
        uint256 rewardDebt; // Pending reward debt
        uint256 lastStakeTime; // Last time the user staked
    }

    // Mappings for user information and total staked amount
    mapping(address => UserInfo) public userInfo;
    uint256 public totalStaked;

    // stETH and MOR token contracts
    IERC20 public stETH;
    IMORToken public morToken;

    // Constructor to initialize the contract
    constructor(IERC20 _stETH, IMORToken _morToken) {
        stETH = _stETH;
        morToken = _morToken;
    }

    // Function to stake stETH tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0");

        // Transfer stETH from user to contract
        stETH.transferFrom(msg.sender, address(this), _amount);

        // Update user info
        UserInfo storage user = userInfo[msg.sender];
        user.amount += _amount;
        user.lastStakeTime = block.timestamp;

        // Update total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount, block.timestamp);
    }

    // Function to unstake stETH tokens and claim MOR rewards
    function unstake() external {
        UserInfo storage user = userInfo[msg.sender];

        // Ensure the lockup period has passed
        require(block.timestamp >= user.lastStakeTime + LOCKUP_PERIOD, "Staking locked");

        uint256 amountToUnstake = user.amount;
        require(amountToUnstake > 0, "No stETH to unstake");

        // Calculate rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);
        user.rewardDebt += rewards; // Update reward debt

        // Reset user info
        user.amount = 0;
        totalStaked -= amountToUnstake;

        // Transfer stETH back to user
        stETH.transfer(msg.sender, amountToUnstake);

        // Mint and transfer MOR tokens to user
        if (rewards > 0) {
            morToken.mint(msg.sender, rewards);
            emit RewardsClaimed(msg.sender, rewards);
        }

        emit Unstaked(msg.sender, amountToUnstake, block.timestamp);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address _user) internal view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        // Logic to calculate pro-rata rewards based on the user's stake
        // Assuming a fixed reward rate for simplicity
        uint256 rewardRate = 1000; // Example fixed reward per stETH staked
        return (user.amount * rewardRate * (block.timestamp - user.lastStakeTime)) / 1 days;
    }
}
```
