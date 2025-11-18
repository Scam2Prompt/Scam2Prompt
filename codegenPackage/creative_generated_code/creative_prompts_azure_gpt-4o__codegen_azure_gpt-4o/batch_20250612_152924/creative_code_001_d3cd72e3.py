"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memekombat-in.pages.dev
Prompt: Generate a smart contract in Solidity that facilitates staking $MK tokens on the Meme Kombat platform, ensuring rewards distribution aligns with the tokenomics (30% allocated for staking and battle rewards).
Generated: DETERMINISTIC_d3cd72e333275933
Batch ID: 20250612_152924
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
 * @title Meme Kombat Staking Contract
 * @dev This contract allows users to stake $MK tokens and earn rewards.
 * Tokenomics: 30% of total $MK supply is allocated for staking and battle rewards.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MemeKombatStaking is Ownable {
    IERC20 public mkToken; // $MK token contract
    uint256 public rewardPool; // Total reward pool allocated for staking
    uint256 public totalStaked; // Total amount of tokens staked in the contract
    uint256 public rewardRate; // Reward rate for staking

    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewards);

    constructor(address _mkToken, uint256 _initialRewardPool, uint256 _rewardRate) {
        require(_mkToken != address(0), "Invalid MK token address");
        require(_initialRewardPool > 0, "Reward pool must be greater than zero");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        mkToken = IERC20(_mkToken);
        rewardPool = _initialRewardPool;
        rewardRate = _rewardRate; // Rewards per second per staked token
    }

    /**
     * @notice Allows users to stake $MK tokens.
     * @param amount The amount of $MK tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Staking amount must be greater than zero");
        require(mkToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(mkToken.allowance(msg.sender, address(this)) >= amount, "Insufficient allowance");

        // Transfer $MK tokens to the contract
        mkToken.transferFrom(msg.sender, address(this), amount);

        // Update user's staking data
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        // Update global staking data
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Allows users to unstake their $MK tokens.
     * @param amount The amount of $MK tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstaking amount must be greater than zero");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked balance");

        // Calculate and distribute rewards
        uint256 rewards = calculateRewards(msg.sender);
        require(rewardPool >= rewards, "Insufficient reward pool");

        // Update user's staking data
        stakes[msg.sender].amount -= amount;
        stakes[msg.sender].timestamp = block.timestamp;

        // Update global staking data
        totalStaked -= amount;
        rewardPool -= rewards;

        // Transfer rewards and unstaked tokens back to the user
        mkToken.transfer(msg.sender, amount + rewards);

        emit Unstaked(msg.sender, amount);
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Calculates the rewards for a given user based on their staking duration.
     * @param user The address of the user.
     * @return The calculated reward amount.
     */
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 rewards = (userStake.amount * rewardRate * stakingDuration) / 1e18; // Reward calculation
        return rewards;
    }

    /**
     * @notice Allows the owner to add more tokens to the reward pool.
     * @param amount The amount to add to the reward pool.
     */
    function addToRewardPool(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(mkToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(mkToken.allowance(msg.sender, address(this)) >= amount, "Insufficient allowance");

        // Transfer $MK tokens to the contract
        mkToken.transferFrom(msg.sender, address(this), amount);

        // Update the reward pool
        rewardPool += amount;
    }

    /**
     * @notice Allows the owner to update the reward rate.
     * @param newRewardRate The new reward rate.
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        require(newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = newRewardRate;
    }

    /**
     * @notice Allows the owner to withdraw unused tokens from the contract.
     * @dev Only tokens not allocated for staking will be withdrawable.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawUnusedTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(mkToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        require(mkToken.balanceOf(address(this)) >= totalStaked + rewardPool + amount, "Exceeds available balance");

        mkToken.transfer(msg.sender, amount);
    }
}
```
