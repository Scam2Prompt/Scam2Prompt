"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge2014-io.pages.dev
Prompt: Generate Solidity code for a staking smart contract that allows users to stake Doge2014 tokens and earn rewards. Ensure the contract is compatible with Ethereum's blockchain and includes transparent reward calculations.
Generated: DETERMINISTIC_c4d8846e20bee854
Batch ID: 20250612_151246
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
 * @title Staking Contract for Doge2014 Token
 * @dev Allows users to stake Doge2014 tokens and earn rewards.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract Doge2014Staking {
    // Address of the Doge2014 token contract
    IERC20 public immutable doge2014Token;

    // Reward rate in percentage (e.g., 10% reward per year)
    uint256 public immutable rewardRate;
    
    // Duration for calculating rewards (in seconds, e.g., 1 year = 31536000 seconds)
    uint256 public immutable rewardDuration;

    // Mapping to track staked balances of users
    mapping(address => uint256) public stakedBalance;

    // Mapping to track the timestamp of last staking action
    mapping(address => uint256) public lastStakedTime;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Owner of the contract
    address public owner;

    // Events
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardClaimed(address indexed staker, uint256 reward);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor initializes the staking contract.
     * @param tokenAddress Address of the Doge2014 token contract.
     * @param _rewardRate Annual reward percentage rate (e.g., 10 for 10%).
     * @param _rewardDuration Reward calculation duration in seconds.
     */
    constructor(address tokenAddress, uint256 _rewardRate, uint256 _rewardDuration) {
        require(tokenAddress != address(0), "Invalid token address");
        require(_rewardRate > 0 && _rewardRate <= 100, "Invalid reward rate");
        require(_rewardDuration > 0, "Invalid reward duration");

        doge2014Token = IERC20(tokenAddress);
        rewardRate = _rewardRate;
        rewardDuration = _rewardDuration;
        owner = msg.sender;
    }

    /**
     * @dev Allows a user to stake tokens.
     * @param amount Amount of Doge2014 tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from user to contract
        require(doge2014Token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the staked balance and total staked amount
        stakedBalance[msg.sender] += amount;
        totalStaked += amount;

        // Update last staking time for the user
        lastStakedTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to unstake tokens.
     */
    function unstake() external {
        uint256 stakedAmount = stakedBalance[msg.sender];
        require(stakedAmount > 0, "No tokens staked");

        // Calculate rewards before unstaking
        uint256 reward = calculateReward(msg.sender);

        // Transfer staked tokens back to the user
        stakedBalance[msg.sender] = 0;
        totalStaked -= stakedAmount;
        require(doge2014Token.transfer(msg.sender, stakedAmount), "Token transfer failed");

        // Transfer rewards to the user
        if (reward > 0) {
            require(doge2014Token.transfer(msg.sender, reward), "Reward transfer failed");
        }

        // Reset last staking time
        lastStakedTime[msg.sender] = 0;

        emit Unstaked(msg.sender, stakedAmount);
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Allows a user to claim staking rewards without unstaking.
     */
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        // Update the last staking time
        lastStakedTime[msg.sender] = block.timestamp;

        // Transfer rewards to the user
        require(doge2014Token.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculates the reward for a user based on their staked amount and staking duration.
     * @param staker Address of the staker.
     * @return Reward amount in tokens.
     */
    function calculateReward(address staker) public view returns (uint256) {
        uint256 stakedAmount = stakedBalance[staker];
        if (stakedAmount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - lastStakedTime[staker];
        uint256 reward = (stakedAmount * rewardRate * stakingDuration) / (100 * rewardDuration);

        return reward;
    }

    /**
     * @dev Allows the owner to withdraw excess tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawExcessTokens(uint256 amount) external onlyOwner {
        require(amount > 0 && doge2014Token.balanceOf(address(this)) >= amount, "Invalid amount");

        require(doge2014Token.transfer(owner, amount), "Token transfer failed");
    }
}
```
