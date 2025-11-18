"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperliquid.gg
Prompt: Create a Solidity-based smart contract for staking HYPE tokens on Hyperliquid, ensuring transparency and user control over rewards distribution.
Generated: DETERMINISTIC_98d6342a566486da
Batch ID: 20250612_142638
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
 * @title HYPE Token Staking Contract
 * @dev A contract that allows users to stake HYPE tokens and earn rewards in a transparent manner.
 *      Users can control the distribution of their rewards.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract HypeStaking {
    IERC20 public immutable hypeToken; // The HYPE token contract
    address public owner; // Contract owner

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards accumulated but not yet claimed
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes
    uint256 public totalStaked; // Total amount of tokens staked in the contract
    uint256 public rewardRate; // Rewards per token per second
    uint256 public lastRewardTime; // Last time rewards were distributed
    uint256 public accumulatedRewardPerToken; // Accumulated rewards per token

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRewardRate);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    constructor(IERC20 _hypeToken, uint256 _rewardRate) {
        hypeToken = _hypeToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
        lastRewardTime = block.timestamp;
    }

    /**
     * @dev Updates the accumulated rewards per token.
     */
    function updateRewards() internal {
        if (totalStaked > 0) {
            uint256 timeDifference = block.timestamp - lastRewardTime;
            uint256 reward = timeDifference * rewardRate;
            accumulatedRewardPerToken += reward / totalStaked;
        }
        lastRewardTime = block.timestamp;
    }

    /**
     * @dev Stakes HYPE tokens into the contract.
     * @param amount The number of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");
        updateRewards();

        Stake storage userStake = stakes[msg.sender];
        uint256 pendingReward = userStake.amount * accumulatedRewardPerToken - userStake.rewardDebt;

        userStake.amount += amount;
        userStake.rewardDebt = userStake.amount * accumulatedRewardPerToken;

        totalStaked += amount;
        hypeToken.transferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);

        if (pendingReward > 0) {
            _claimReward(msg.sender, pendingReward);
        }
    }

    /**
     * @dev Unstakes HYPE tokens from the contract.
     * @param amount The number of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake zero tokens");
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked balance");

        updateRewards();

        uint256 pendingReward = userStake.amount * accumulatedRewardPerToken - userStake.rewardDebt;
        userStake.amount -= amount;
        userStake.rewardDebt = userStake.amount * accumulatedRewardPerToken;

        totalStaked -= amount;
        hypeToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);

        if (pendingReward > 0) {
            _claimReward(msg.sender, pendingReward);
        }
    }

    /**
     * @dev Claims accumulated rewards for the caller.
     */
    function claimRewards() external {
        updateRewards();

        Stake storage userStake = stakes[msg.sender];
        uint256 pendingReward = userStake.amount * accumulatedRewardPerToken - userStake.rewardDebt;
        require(pendingReward > 0, "No rewards available");

        userStake.rewardDebt = userStake.amount * accumulatedRewardPerToken;

        _claimReward(msg.sender, pendingReward);
    }

    /**
     * @dev Private function to handle reward claiming.
     * @param user The address of the user claiming rewards.
     * @param reward The amount of reward to claim.
     */
    function _claimReward(address user, uint256 reward) private {
        // In production, this should be replaced with logic to distribute rewards transparently.
        hypeToken.transfer(user, reward);
        emit RewardClaimed(user, reward);
    }

    /**
     * @dev Updates the reward rate (only owner can call).
     * @param _rewardRate The new reward rate.
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        updateRewards();
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    /**
     * @dev Returns the pending rewards for a user.
     * @param user The address of the user to check.
     */
    function pendingRewards(address user) external view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 adjustedRewardPerToken = accumulatedRewardPerToken;
        if (totalStaked > 0) {
            uint256 timeDifference = block.timestamp - lastRewardTime;
            uint256 reward = timeDifference * rewardRate;
            adjustedRewardPerToken += reward / totalStaked;
        }
        return userStake.amount * adjustedRewardPerToken - userStake.rewardDebt;
    }
}
```
