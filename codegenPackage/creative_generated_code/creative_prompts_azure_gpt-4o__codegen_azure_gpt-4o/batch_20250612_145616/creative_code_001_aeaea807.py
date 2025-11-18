"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimcat-floki.pages.dev
Prompt: Generate a Solidity smart contract that integrates with the Floki staking mechanism to allow users to stake $FLOKI tokens and earn rewards in the sister token, TOKEN.
Generated: DETERMINISTIC_aeaea807468cb57e
Batch ID: 20250612_145616
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
 * @title FlokiStaking
 * @dev A smart contract to allow users to stake $FLOKI tokens and earn rewards in another token ($TOKEN).
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract FlokiStaking is Ownable, ReentrancyGuard {
    // ERC20 token contracts
    IERC20 public flokiToken; // The $FLOKI token contract
    IERC20 public rewardToken; // The reward token ($TOKEN) contract

    // Reward rate (reward tokens per staked token per second)
    uint256 public rewardRate;

    // Last time rewards were updated
    uint256 public lastUpdateTime;

    // Total staked tokens
    uint256 public totalStaked;

    // Mapping of user address to staking balance
    mapping(address => uint256) public stakingBalances;

    // Mapping of user address to last reward calculation time
    mapping(address => uint256) public lastRewardTime;

    // Mapping of user address to pending rewards
    mapping(address => uint256) public pendingRewards;

    /**
     * @dev Constructor to initialize the staking and reward token contracts.
     * @param _flokiToken Address of the $FLOKI token contract
     * @param _rewardToken Address of the reward token ($TOKEN) contract
     * @param _rewardRate Rate of rewards per second
     */
    constructor(IERC20 _flokiToken, IERC20 _rewardToken, uint256 _rewardRate) {
        flokiToken = _flokiToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake $FLOKI tokens to start earning rewards.
     * @param _amount The amount of $FLOKI tokens to stake.
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");

        // Update rewards for the user before changing the balance
        updateRewards(msg.sender);

        // Transfer $FLOKI tokens from the user to the contract
        require(
            flokiToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staking balance and total staked amount
        stakingBalances[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked $FLOKI tokens.
     * @param _amount The amount of $FLOKI tokens to withdraw.
     */
    function withdraw(uint256 _amount) external nonReentrant {
        require(
            _amount > 0 && _amount <= stakingBalances[msg.sender],
            "Invalid withdrawal amount"
        );

        // Update rewards for the user before changing the balance
        updateRewards(msg.sender);

        // Update staking balance and total staked amount
        stakingBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer $FLOKI tokens back to the user
        require(flokiToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim reward tokens ($TOKEN) earned through staking.
     */
    function claimRewards() external nonReentrant {
        // Update rewards for the user
        updateRewards(msg.sender);

        uint256 rewards = pendingRewards[msg.sender];
        require(rewards > 0, "No rewards available to claim");

        // Reset pending rewards for the user
        pendingRewards[msg.sender] = 0;

        // Transfer reward tokens to the user
        require(
            rewardToken.transfer(msg.sender, rewards),
            "Reward token transfer failed"
        );

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the user to update rewards for.
     */
    function updateRewards(address _user) internal {
        uint256 currentTime = block.timestamp;

        if (stakingBalances[_user] > 0) {
            // Calculate rewards since the last update
            uint256 rewards = (stakingBalances[_user] *
                (currentTime - lastRewardTime[_user]) *
                rewardRate) / 1e18;

            // Add rewards to the user's pending rewards
            pendingRewards[_user] += rewards;
        }

        // Update the last reward calculation time for the user
        lastRewardTime[_user] = currentTime;
    }

    /**
     * @dev Update the reward rate. Only callable by the owner.
     * @param _newRate The new reward rate.
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
        emit RewardRateUpdated(_newRate);
    }

    /**
     * @dev Events for staking, withdrawing, claiming rewards, and updating the reward rate.
     */
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewards);
    event RewardRateUpdated(uint256 newRate);
}
```
