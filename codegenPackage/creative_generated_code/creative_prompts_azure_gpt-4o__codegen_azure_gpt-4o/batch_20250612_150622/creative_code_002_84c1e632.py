"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kabosu-bsc.pages.dev
Prompt: Create a smart contract in Solidity that implements Kabosu token staking functionality, referencing the staking mechanism planned in Phase 2 of the roadmap.
Generated: DETERMINISTIC_84c1e632e81adf02
Batch ID: 20250612_150622
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
 * @title KabosuTokenStaking
 * @dev A smart contract for staking Kabosu tokens.
 * Users can stake their tokens and earn rewards based on the duration of staking.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract KabosuTokenStaking {
    // Kabosu token contract
    IERC20 public kabosuToken;

    // Structure to hold staking information
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 rewardRate; // Reward rate in percentage per year
    }

    // Mapping of staker address to staking details
    mapping(address => Stake) public stakes;

    // Event declarations for logging actions
    event Staked(address indexed user, uint256 amount, uint256 startTime);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardRateUpdated(uint256 newRewardRate);

    // Owner of the contract
    address public owner;

    // Default reward rate (e.g., 10%)
    uint256 public defaultRewardRate = 10;

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(address _kabosuToken) {
        require(_kabosuToken != address(0), "Invalid Kabosu token address");
        kabosuToken = IERC20(_kabosuToken);
        owner = msg.sender;
    }

    /**
     * @dev Stake Kabosu tokens to earn rewards.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(kabosuToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens to the contract
        require(kabosuToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Record staking details
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.startTime = block.timestamp;
        userStake.rewardRate = defaultRewardRate;

        emit Staked(msg.sender, amount, block.timestamp);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate staking duration in seconds
        uint256 stakingDuration = block.timestamp - userStake.startTime;

        // Calculate rewards (rewardRate is annual, so we divide by seconds in a year)
        uint256 reward = (userStake.amount * userStake.rewardRate * stakingDuration) / (100 * 365 days);

        // Transfer staked amount and reward to the user
        require(kabosuToken.transfer(msg.sender, userStake.amount + reward), "Token transfer failed");

        emit Unstaked(msg.sender, userStake.amount, reward);

        // Reset staking details
        userStake.amount = 0;
        userStake.startTime = 0;
        userStake.rewardRate = 0;
    }

    /**
     * @dev Update the default reward rate for staking (only owner).
     * @param newRewardRate New reward rate in percentage per year.
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        require(newRewardRate > 0, "Reward rate must be greater than zero");
        defaultRewardRate = newRewardRate;

        emit RewardRateUpdated(newRewardRate);
    }

    /**
     * @dev Emergency withdrawal of tokens by the owner.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(kabosuToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        require(kabosuToken.transfer(owner, amount), "Token transfer failed");
    }

    /**
     * @dev View staking details for a user.
     * @param user Address of the user.
     * @return amount Staked amount.
     * @return startTime Staking start time.
     * @return rewardRate Current reward rate applied to the staking.
     */
    function viewStake(address user) external view returns (uint256 amount, uint256 startTime, uint256 rewardRate) {
        Stake storage userStake = stakes[user];
        return (userStake.amount, userStake.startTime, userStake.rewardRate);
    }
}
```
