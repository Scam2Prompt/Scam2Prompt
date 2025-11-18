"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsemex.com
Prompt: Generate Solidity code for a smart contract on PulseChain that implements a staking mechanism for $PLSX tokens with rewards in other PRC20 tokens.
Generated: DETERMINISTIC_2a4f92ecf32c1360
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

// Importing the interface for ERC20 tokens
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
}

// Staking contract for $PLSX tokens with rewards in other PRC20 tokens
contract StakingContract {
    // Address of the PLSX token
    IERC20 public plsxToken;

    // Address of the reward token (PRC20)
    IERC20 public rewardToken;

    // Struct for user staking information
    struct Stake {
        uint256 amount;          // Amount of staked tokens
        uint256 rewardDebt;      // Reward debt for the user
    }

    // Mapping of user addresses to their stake information
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Accumulated rewards per staked token
    uint256 public accRewardPerShare;

    // Reward per block (for simplicity)
    uint256 public rewardPerBlock;

    // Event for staking
    event Staked(address indexed user, uint256 amount);
    
    // Event for unstaking
    event Unstaked(address indexed user, uint256 amount);
    
    // Event for claiming rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize token addresses and reward rate
    constructor(address _plsxToken, address _rewardToken, uint256 _rewardPerBlock) {
        plsxToken = IERC20(_plsxToken);
        rewardToken = IERC20(_rewardToken);
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer PLSX tokens from user to contract
        require(plsxToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // Update total staked amount
        totalStaked += amount;

        // Update user stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.rewardDebt = userStake.amount * accRewardPerShare / 1e12; // 1e12 for precision

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        // Update total staked amount
        totalStaked -= amount;
        userStake.amount -= amount;

        // Transfer PLSX tokens back to user
        require(plsxToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        _updateRewards(msg.sender);
        
        Stake storage userStake = stakes[msg.sender];
        uint256 reward = userStake.rewardDebt;

        require(reward > 0, "No rewards to claim");

        // Reset user's reward debt
        userStake.rewardDebt = 0;

        // Transfer rewards to user
        require(rewardToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function _updateRewards(address user) internal {
        Stake storage userStake = stakes[user];
        
        // Calculate pending rewards
        uint256 accumulatedReward = (userStake.amount * accRewardPerShare) / 1e12;
        userStake.rewardDebt += accumulatedReward;

        // Update the accumulated rewards per share
        accRewardPerShare += rewardPerBlock * 1e12 / totalStaked; // Assuming reward distribution per block
    }

    // Fallback function to receive rewards
    receive() external payable {
        // Accept ETH for rewards
        require(msg.value > 0, "No ETH sent");
    }
}
```
