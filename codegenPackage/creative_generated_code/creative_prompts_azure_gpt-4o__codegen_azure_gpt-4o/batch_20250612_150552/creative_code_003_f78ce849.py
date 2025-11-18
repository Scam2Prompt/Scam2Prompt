"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbootsdao-en.pages.dev
Prompt: Write a smart contract in Solidity that implements staking functionality for Moonboots DAO, allowing users to earn ecosystem rewards based on their $MBDAO token holdings.
Generated: DETERMINISTIC_f78ce849adecf356
Batch ID: 20250612_150552
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

/**
 * @title Moonboots DAO Staking Contract
 * @dev Implements staking functionality for $MBDAO token holders to earn rewards.
 */
contract MoonbootsStaking {
    // State variables
    address public owner; // Owner of the contract
    address public tokenAddress; // Address of the $MBDAO token contract
    uint256 public rewardRate; // Reward rate (tokens rewarded per second per staked token)

    struct Stake {
        uint256 amount; // Amount of tokens staked by the user
        uint256 rewardDebt; // Rewards already paid to the user
        uint256 lastUpdated; // Timestamp when staking data was last updated
    }

    mapping(address => Stake) public stakes; // User address to Stake mapping
    mapping(address => uint256) public pendingRewards; // Rewards pending to be claimed by users

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _tokenAddress Address of the $MBDAO token contract.
     * @param _rewardRate Reward rate per second per staked token.
     */
    constructor(address _tokenAddress, uint256 _rewardRate) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        owner = msg.sender;
        tokenAddress = _tokenAddress;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake $MBDAO tokens to earn rewards.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Transfer tokens from user to the contract
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), _amount);

        // Update user's staking data
        _updateRewards(msg.sender);
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].lastUpdated = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked balance");

        // Update user's staking data
        _updateRewards(msg.sender);
        stakes[msg.sender].amount -= _amount;

        // Transfer tokens back to the user
        IERC20(tokenAddress).transfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim pending rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        uint256 rewards = pendingRewards[msg.sender];
        require(rewards > 0, "No rewards to claim");

        // Reset pending rewards and transfer tokens to the user
        pendingRewards[msg.sender] = 0;
        IERC20(tokenAddress).transfer(msg.sender, rewards);

        emit RewardClaimed(msg.sender, rewards);
    }

    /**
     * @dev Update rewards for the user based on staked tokens and time elapsed.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        Stake storage userStake = stakes[_user];
        if (userStake.amount > 0) {
            uint256 timeElapsed = block.timestamp - userStake.lastUpdated;
            uint256 newRewards = (userStake.amount * rewardRate * timeElapsed) / 1e18;
            pendingRewards[_user] += newRewards;
            userStake.lastUpdated = block.timestamp;
        }
    }

    /**
     * @dev Set a new reward rate. Only callable by the contract owner.
     * @param _newRewardRate New reward rate per second per staked token.
     */
    function setRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Emergency withdrawal in case of critical issues. Only callable by the contract owner.
     * @param _amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        IERC20(tokenAddress).transfer(owner, _amount);
    }
}

/**
 * @dev Interface for interacting with ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
