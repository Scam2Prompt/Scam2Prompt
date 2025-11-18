"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-reward.web.app
Prompt: Create a Solidity contract that supports staking rewards for multiple meme coins, with a mechanism to incentivize holding a specific token like $STARS.
Generated: DETERMINISTIC_8c1ebe0345dbfefc
Batch ID: 20250612_154133
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
 * @title MultiMemeCoinStaking
 * @dev A staking contract that supports staking multiple meme coins and incentivizes holding a specific token ($STARS).
 * Users can stake supported tokens to earn rewards, with additional bonuses for $STARS holders.
 */
contract MultiMemeCoinStaking {
    // Struct to store staker information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        mapping(address => uint256) tokenStakes; // Amount staked per token
    }

    // Supported tokens for staking
    mapping(address => bool) public supportedTokens;

    // Mapping of staker address to their staking details
    mapping(address => Staker) public stakers;

    // Reward token (for simplicity, assuming it's an ERC20 token)
    address public rewardToken;

    // Incentive token ($STARS)
    address public starsToken;

    // Reward rate per token per second
    uint256 public rewardRate;

    // Additional bonus multiplier for $STARS holders
    uint256 public starsBonusMultiplier;

    // Time-related variables
    uint256 public lastRewardTime;

    // Owner of the contract
    address public owner;

    // Events for logging
    event TokensStaked(address indexed user, address indexed token, uint256 amount);
    event TokensUnstaked(address indexed user, address indexed token, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewardAmount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor to initialize contract parameters
    constructor(
        address _rewardToken,
        address _starsToken,
        uint256 _rewardRate,
        uint256 _starsBonusMultiplier
    ) {
        owner = msg.sender;
        rewardToken = _rewardToken;
        starsToken = _starsToken;
        rewardRate = _rewardRate;
        starsBonusMultiplier = _starsBonusMultiplier;
        lastRewardTime = block.timestamp;
    }

    // Function to add supported tokens
    function addSupportedToken(address token) external onlyOwner {
        supportedTokens[token] = true;
    }

    // Function to remove supported tokens
    function removeSupportedToken(address token) external onlyOwner {
        supportedTokens[token] = false;
    }

    // Function to update reward rate
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    // Function to stake tokens
    function stake(address token, uint256 amount) external {
        require(supportedTokens[token], "Token is not supported for staking");
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens from the user to the contract
        require(ERC20(token).transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        Staker storage staker = stakers[msg.sender];

        // Update user's staking details
        staker.tokenStakes[token] += amount;
        staker.amountStaked += amount;

        emit TokensStaked(msg.sender, token, amount);
    }

    // Function to unstake tokens
    function unstake(address token, uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.tokenStakes[token] >= amount, "Insufficient staked amount");

        // Update user's staking details
        staker.tokenStakes[token] -= amount;
        staker.amountStaked -= amount;

        // Transfer tokens back to the user
        require(ERC20(token).transfer(msg.sender, amount), "Token transfer failed");

        emit TokensUnstaked(msg.sender, token, amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 baseReward = staker.amountStaked * rewardRate * (block.timestamp - lastRewardTime);

        // Check if the user holds the incentive token ($STARS)
        uint256 starsBalance = ERC20(starsToken).balanceOf(user);
        if (starsBalance > 0) {
            baseReward = baseReward * starsBonusMultiplier / 100;
        }

        return baseReward;
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];

        uint256 rewardAmount = calculateRewards(msg.sender);

        // Update reward debt and last reward time
        staker.rewardDebt += rewardAmount;
        lastRewardTime = block.timestamp;

        // Transfer rewards to the user
        require(ERC20(rewardToken).transfer(msg.sender, rewardAmount), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    // Function to withdraw contract rewards (owner only)
    function withdrawRewards(uint256 amount) external onlyOwner {
        require(ERC20(rewardToken).transfer(msg.sender, amount), "Reward withdrawal failed");
    }
}

// Interface for ERC20 token
interface ERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
