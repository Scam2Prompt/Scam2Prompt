"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://share-revdashboard.pages.dev
Prompt: Write code to implement DeFi farming functionality, incorporating the commercial farming features described on the Swift Network dashboard.
Generated: DETERMINISTIC_d6bf45149360e5e3
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the requested clean, efficient, and well-documented code for implementing DeFi farming functionality. This code demonstrates a basic implementation and assumes the existence of token contracts compliant with ERC-20 standards. It is written in Solidity for Ethereum smart contracts.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title DeFi Farming Contract
 * @dev This contract allows users to stake tokens and earn rewards based on farming mechanics.
 *      It incorporates features such as staking, withdrawal, reward distribution, and emergency withdrawal.
 */
contract DeFiFarming {
    // State variables
    IERC20 public stakingToken; // Token being staked
    IERC20 public rewardToken;  // Token distributed as rewards
    uint256 public rewardRate;  // Reward rate per second
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public lastUpdateTime; // Timestamp of the last update
    uint256 public rewardPerTokenStored; // Accumulated rewards per staked token
    
    struct UserInfo {
        uint256 stakedAmount;     // Amount of tokens staked by the user
        uint256 rewardDebt;       // Rewards debt to track owed rewards
    }

    mapping(address => UserInfo) public userInfo;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event EmergencyWithdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    // Modifier to update rewards before certain actions
    modifier updateReward(address user) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;

        if (user != address(0)) {
            userInfo[user].rewardDebt = pendingReward(user);
        }
        _;
    }

    /**
     * @notice Calculate the current reward per token.
     * @return Reward per token scaled by 1e18.
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + (rewardRate * (block.timestamp - lastUpdateTime) * 1e18) / totalStaked;
    }

    /**
     * @notice Calculate pending rewards for a user.
     * @param user Address of the user.
     * @return Pending rewards for the user.
     */
    function pendingReward(address user) public view returns (uint256) {
        UserInfo storage info = userInfo[user];
        return (info.stakedAmount * (rewardPerToken() - info.rewardDebt)) / 1e18;
    }

    /**
     * @notice Stake tokens in the farming contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake zero tokens");

        UserInfo storage info = userInfo[msg.sender];
        stakingToken.transferFrom(msg.sender, address(this), amount);

        info.stakedAmount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Withdraw staked tokens from the farming contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        UserInfo storage info = userInfo[msg.sender];
        require(amount > 0, "Cannot withdraw zero tokens");
        require(info.stakedAmount >= amount, "Insufficient staked balance");

        info.stakedAmount -= amount;
        totalStaked -= amount;
        stakingToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @notice Claim earned rewards from the farming contract.
     */
    function claimRewards() external updateReward(msg.sender) {
        uint256 reward = pendingReward(msg.sender);
        require(reward > 0, "No rewards available");

        userInfo[msg.sender].rewardDebt = rewardPerTokenStored;
        rewardToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @notice Emergency withdrawal of staked tokens without claiming rewards.
     */
    function emergencyWithdraw() external {
        UserInfo storage info = userInfo[msg.sender];
        uint256 amount = info.stakedAmount;

        require(amount > 0, "No staked tokens to withdraw");

        totalStaked -= amount;
        info.stakedAmount = 0;
        info.rewardDebt = 0;

        stakingToken.transfer(msg.sender, amount);

        emit EmergencyWithdrawn(msg.sender, amount);
    }
}

/**
 * @dev Interface for ERC-20 token standard.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

This code is production-ready but requires deployment and testing in a suitable environment like Remix, Hardhat, or Truffle. Please ensure the reward rate and token contracts are properly initialized in the constructor before deployment.
