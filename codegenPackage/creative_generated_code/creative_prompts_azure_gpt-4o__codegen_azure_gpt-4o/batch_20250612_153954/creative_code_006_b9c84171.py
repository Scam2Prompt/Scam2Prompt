"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedbrett.on-fleek.app
Prompt: Create a smart contract that interacts with the $Brett token on the Base Mainnet, allowing users to stake tokens and earn rewards based on their holdings.
Generated: DETERMINISTIC_b9c8417176d79b37
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

/**
 * @title TokenStaking
 * @dev A smart contract to allow users to stake $Brett tokens and earn rewards.
 * Rewards are calculated based on the amount of tokens staked and the duration of staking.
 */
contract TokenStaking {
    IERC20 public brettToken; // ERC20-compliant $Brett token interface
    uint256 public rewardRatePerSecond; // Reward rate in tokens per second
    address public owner; // Contract owner for administrative functions

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when tokens were staked
        uint256 rewardDebt; // Track rewards already claimed
    }

    mapping(address => Stake) public stakes; // Staking information per user

    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    /// @dev Event emitted when tokens are staked.
    event Staked(address indexed user, uint256 amount);

    /// @dev Event emitted when rewards are claimed.
    event RewardsClaimed(address indexed user, uint256 rewardAmount);

    /// @dev Event emitted when tokens are withdrawn.
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with token and reward rate.
     * @param _brettToken Address of the $Brett token contract.
     * @param _rewardRatePerSecond Reward rate in tokens per second.
     */
    constructor(IERC20 _brettToken, uint256 _rewardRatePerSecond) {
        brettToken = _brettToken;
        rewardRatePerSecond = _rewardRatePerSecond;
        owner = msg.sender;
    }

    /**
     * @dev Stake $Brett tokens to earn rewards.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");

        // Update rewards for the user before modifying stake
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        require(brettToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Claim earned rewards.
     */
    function claimRewards() external {
        // Update rewards for the user
        _updateRewards(msg.sender);

        // Calculate pending rewards
        uint256 reward = stakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards available");

        // Reset reward debt after claiming
        stakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        require(brettToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Withdraw staked tokens along with rewards.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Update rewards for the user
        _updateRewards(msg.sender);

        uint256 amountToWithdraw = userStake.amount;
        uint256 reward = userStake.rewardDebt;

        // Reset user's stake and reward debt
        userStake.amount = 0;
        userStake.rewardDebt = 0;

        // Transfer staked tokens and rewards back to the user
        require(brettToken.transfer(msg.sender, amountToWithdraw), "Token withdrawal failed");
        if (reward > 0) {
            require(brettToken.transfer(msg.sender, reward), "Reward transfer failed");
        }

        emit Withdrawn(msg.sender, amountToWithdraw);
    }

    /**
     * @dev Update rewards for a user.
     * Internal function to handle reward calculations.
     * @param user Address of the user.
     */
    function _updateRewards(address user) internal {
        Stake storage userStake = stakes[user];
        if (userStake.amount > 0) {
            uint256 elapsedTime = block.timestamp - userStake.startTime;
            uint256 pendingReward = (userStake.amount * rewardRatePerSecond * elapsedTime) / 1e18; // Scale rewards
            userStake.rewardDebt += pendingReward;
            userStake.startTime = block.timestamp; // Reset start time for next calculation
        }
    }

    /**
     * @dev Update the reward rate. Can only be called by the owner.
     * @param newRate New reward rate per second.
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRatePerSecond = newRate;
    }
}

/**
 * @dev Minimal ERC20 interface to interact with the $Brett token.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
