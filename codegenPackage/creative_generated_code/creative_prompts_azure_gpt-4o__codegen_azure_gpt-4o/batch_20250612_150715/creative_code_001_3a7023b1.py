"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-live.web.app
Prompt: Generate Solidity code for a smart contract that integrates Kangamoon's $KANG token and includes functionality for staking and earning in-game rewards.
Generated: DETERMINISTIC_3a7023b10682fe67
Batch ID: 20250612_150715
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
 * @title KangamoonStaking
 * @dev A smart contract for staking $KANG tokens and earning in-game rewards
 */
interface IKANGToken {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract KangamoonStaking {
    // State variables
    IKANGToken public kangToken; // Reference to the $KANG token contract
    address public owner; // Contract owner

    uint256 public rewardRate; // Reward rate per block for staking
    uint256 public totalStaked; // Total amount of tokens staked in the contract

    struct Stake {
        uint256 amount;
        uint256 rewardDebt; // Tracks reward debt to calculate claimable rewards
        uint256 lastUpdatedBlock;
    }

    mapping(address => Stake) public stakes; // Track staking information for each user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRewardRate);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract
     * @param _kangToken Address of the $KANG token contract
     * @param _rewardRate Reward rate per block
     */
    constructor(address _kangToken, uint256 _rewardRate) {
        require(_kangToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        kangToken = IKANGToken(_kangToken);
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Stake $KANG tokens to earn rewards
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Update user's rewards before modifying their stake
        updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        require(kangToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staking information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].lastUpdatedBlock = block.number;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake $KANG tokens and claim rewards
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens to unstake");

        // Update user's rewards before unstaking
        updateRewards(msg.sender);

        uint256 amountToUnstake = userStake.amount;

        // Reset user stake
        userStake.amount = 0;
        userStake.rewardDebt = 0;
        userStake.lastUpdatedBlock = block.number;
        totalStaked -= amountToUnstake;

        // Transfer staked tokens back to the user
        require(kangToken.transfer(msg.sender, amountToUnstake), "Token transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Claim earned rewards without unstaking
     */
    function claimRewards() external {
        updateRewards(msg.sender);

        Stake storage userStake = stakes[msg.sender];
        uint256 pendingReward = userStake.rewardDebt;
        require(pendingReward > 0, "No rewards to claim");

        userStake.rewardDebt = 0;
        require(kangToken.transfer(msg.sender, pendingReward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, pendingReward);
    }

    /**
     * @dev Update user's rewards based on staking duration
     * @param user Address of the user
     */
    function updateRewards(address user) internal {
        Stake storage userStake = stakes[user];
        if (userStake.amount > 0) {
            uint256 blocksStaked = block.number - userStake.lastUpdatedBlock;
            uint256 reward = (blocksStaked * rewardRate * userStake.amount) / 1e18;
            userStake.rewardDebt += reward;
            userStake.lastUpdatedBlock = block.number;
        }
    }

    /**
     * @dev Update the reward rate (owner-only function)
     * @param newRewardRate New reward rate per block
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        require(newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = newRewardRate;
        emit RewardRateUpdated(newRewardRate);
    }

    /**
     * @dev Emergency withdrawal of contract tokens (owner-only function)
     * @param amount Amount of tokens to withdraw
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(kangToken.transfer(owner, amount), "Token transfer failed");
    }
}
```
