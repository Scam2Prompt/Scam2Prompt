"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wiernerdog-ai.pages.dev
Prompt: Write a Solidity contract that mimics the staking mechanism of WienerAI, allowing users to stake tokens and earn rewards.
Generated: DETERMINISTIC_f56215a20f54fbad
Batch ID: 20250612_163659
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
 * @title StakingContract
 * @dev A simple staking contract for ERC20 tokens where users can stake and earn rewards.
 */
contract StakingContract {
    // ERC20 token interface
    IERC20 public stakingToken;

    // Reward rate per second for staked tokens
    uint256 public rewardRate = 100; // Example reward rate: 100 wei per token per second

    // Mapping of user addresses to their staked balances
    mapping(address => uint256) public stakedBalances;

    // Mapping of user addresses to their reward debt
    mapping(address => uint256) public rewardDebt;

    // Mapping of user addresses to their last claim time
    mapping(address => uint256) public lastClaimTime;

    // Total staked tokens
    uint256 public totalStaked;

    // Owner of the contract
    address public owner;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _stakingToken Address of the ERC20 token contract for staking.
     */
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
        owner = msg.sender;
    }

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Stake tokens to start earning rewards.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Calculate pending rewards before updating staked balance
        uint256 pendingReward = calculateReward(msg.sender);
        rewardDebt[msg.sender] += pendingReward;

        // Update staked balance and last claim time
        stakedBalances[msg.sender] += amount;
        lastClaimTime[msg.sender] = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and stop earning rewards.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedBalances[msg.sender] >= amount, "Insufficient balance to unstake");

        // Calculate pending rewards before updating staked balance
        uint256 pendingReward = calculateReward(msg.sender);
        rewardDebt[msg.sender] += pendingReward;

        // Update staked balance and last claim time
        stakedBalances[msg.sender] -= amount;
        lastClaimTime[msg.sender] = block.timestamp;

        totalStaked -= amount;

        require(stakingToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim earned rewards.
     */
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender) + rewardDebt[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewardDebt[msg.sender] = 0;
        lastClaimTime[msg.sender] = block.timestamp;

        // Reward distribution logic (for simplicity, we assume the contract has enough balance)
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate the pending reward for a user.
     * @param user The address of the user.
     * @return The pending reward amount.
     */
    function calculateReward(address user) public view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastClaimTime[user];
        return (stakedBalances[user] * rewardRate * timeElapsed) / 1e18; // Adjust precision if needed
    }

    /**
     * @dev Set a new reward rate.
     * @param newRewardRate The new reward rate per second.
     */
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }
}

/**
 * @dev ERC20 token interface required for interacting with the staking token.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
