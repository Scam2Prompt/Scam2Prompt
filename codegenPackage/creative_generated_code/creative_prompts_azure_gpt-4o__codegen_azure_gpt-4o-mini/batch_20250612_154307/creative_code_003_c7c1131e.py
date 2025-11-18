"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-launch.web.app
Prompt: Develop a Solidity contract for the MemeVault ecosystem that enables staking of multiple meme coins, ensuring that $STARS holders receive higher rewards.
Generated: DETERMINISTIC_c7c1131e76274716
Batch ID: 20250612_154307
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

// Interface for the ERC20 token standard
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

// MemeVault contract for staking multiple meme coins
contract MemeVault {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastStakedTime;
    }

    // Mapping of stakers' addresses to their staking information
    mapping(address => Staker) public stakers;
    
    // Mapping of approved meme coins
    mapping(address => bool) public approvedTokens;

    // ERC20 token for $STARS rewards
    IERC20 public starsToken;

    // Reward rate per second for stakers
    uint256 public rewardRate;

    // Event for staking action
    event Staked(address indexed user, address indexed token, uint256 amount);
    // Event for withdrawing action
    event Withdrawn(address indexed user, address indexed token, uint256 amount);
    // Event for claiming rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the $STARS token address and reward rate
    constructor(IERC20 _starsToken, uint256 _rewardRate) {
        starsToken = _starsToken;
        rewardRate = _rewardRate;
    }

    // Modifier to check if a token is approved for staking
    modifier onlyApprovedToken(address token) {
        require(approvedTokens[token], "Token not approved for staking");
        _;
    }

    // Function to approve a token for staking
    function approveToken(address token) external {
        approvedTokens[token] = true;
    }

    // Function to stake a meme coin
    function stake(address token, uint256 amount) external onlyApprovedToken(token) {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer the token from the user to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.lastStakedTime = block.timestamp;

        emit Staked(msg.sender, token, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(address token, uint256 amount) external onlyApprovedToken(token) {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update staking information
        staker.amountStaked -= amount;

        // Transfer the token from the contract to the user
        IERC20(token).transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, token, amount);
    }

    // Function to claim rewards based on the staked amount and time
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculateRewards(msg.sender);

        require(reward > 0, "No rewards available");

        // Update the user's reward debt
        staker.rewardDebt += reward;

        // Transfer the $STARS rewards to the user
        starsToken.transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards based on staked amount and time
    function calculateRewards(address user) internal view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 stakingDuration = block.timestamp - staker.lastStakedTime;
        
        // Calculate rewards based on staking duration and a multiplier for $STARS holders
        uint256 rewardMultiplier = (IERC20(starsToken).balanceOf(user) > 0) ? 2 : 1;
        return (staker.amountStaked * rewardRate * stakingDuration * rewardMultiplier) / 1e18;
    }
}
```
