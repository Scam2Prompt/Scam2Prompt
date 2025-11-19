"""
Generated Code Metadata:
========================
Original URL: https://pepeunchained-sale.pages.dev
Prompt: Develop a Solidity contract that allows users to stake their $PEPU tokens and receive rewards on the Pepe Unchained blockchain.
Generated: DETERMINISTIC_74ee27877327910f
Batch ID: 20250612_164151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title PEPU Staking Contract
 * @dev Allows users to stake PEPU tokens and earn rewards
 */
contract PEPUStaking is Ownable, ReentrancyGuard {
    IERC20 public immutable stakingToken;
    IERC20 public immutable rewardsToken;

    // Staking parameters
    uint256 public constant REWARD_RATE = 10; // 10% annual reward rate
    uint256 public constant REWARD_INTERVAL = 365 days;
    uint256 public totalStaked;

    // User stakes and rewards tracking
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 lastClaimTime;
    }

    mapping(address => Stake) public stakes;
    mapping(address => uint256) public rewards;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor initializes the staking and rewards tokens
     * @param _stakingToken Address of the PEPU token to be staked
     * @param _rewardsToken Address of the reward token (can be same as staking token)
     */
    constructor(address _stakingToken, address _rewardsToken) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardsToken != address(0), "Invalid rewards token address");
        
        stakingToken = IERC20(_stakingToken);
        rewardsToken = IERC20(_rewardsToken);
    }

    /**
     * @dev Stake PEPU tokens to start earning rewards
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Update any existing stake and rewards
        _updateRewards(msg.sender);

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].startTime = block.timestamp;
        stakes[msg.sender].lastClaimTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and claim any pending rewards
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        // Update stake
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        _updateRewards(msg.sender);
        
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        rewards[msg.sender] = 0;
        rewardsToken.transfer(msg.sender, rewardAmount);

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Internal function to update user's rewards
     * @param user Address of the user to update rewards for
     */
    function _updateRewards(address user) internal {
        if (stakes[user].amount == 0) return;

        uint256 stakingDuration = block.timestamp - stakes[user].lastClaimTime;
        uint256 reward = (stakes[user].amount * REWARD_RATE * stakingDuration) / (REWARD_INTERVAL * 100);

        if (reward > 0) {
            rewards[user] += reward;
        }

        stakes[user].lastClaimTime = block.timestamp;
    }

    /**
     * @dev View function to check pending rewards for a user
     * @param user Address of the user to check rewards for
     * @return Pending rewards
     */
    function pendingRewards(address user) external view returns (uint256) {
        if (stakes[user].amount == 0) return rewards[user];

        uint256 stakingDuration = block.timestamp - stakes[user].lastClaimTime;
        uint256 reward = (stakes[user].amount * REWARD_RATE * stakingDuration) / (REWARD_INTERVAL * 100);

        return rewards[user] + reward;
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent by mistake
     * @param tokenAddress Address of the token to recover
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(stakingToken) && tokenAddress != address(rewardsToken), 
                "Cannot withdraw staking or rewards tokens");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
