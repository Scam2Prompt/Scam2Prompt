"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unstake-myblend.pages.dev
Prompt: Develop a smart contract snippet to handle unstaking requests, including reward calculations and token transfers, for a platform like "Unstake | Blend."
Generated: DETERMINISTIC_20116a15f7d2700c
Batch ID: 20250612_145919
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
 * @title UnstakingContract
 * @dev Smart contract to handle unstaking requests, reward calculations, and token transfers
 */
contract UnstakingContract {
    // Events
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // State variables
    address public owner;
    uint256 public rewardRate; // Reward rate as a percentage (e.g., 5 for 5%)
    IERC20 public stakingToken; // The ERC20 token being staked

    mapping(address => uint256) public stakedBalances; // Tracks staked balances for users
    mapping(address => uint256) public stakingTimestamps; // Tracks when users staked

    constructor(address _stakingToken, uint256 _rewardRate) {
        require(_stakingToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        owner = msg.sender;
        stakingToken = IERC20(_stakingToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to restrict access to the owner only
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /**
     * @dev Function to allow users to unstake their tokens and claim rewards
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than 0");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");

        // Calculate the reward based on the staking duration and reward rate
        uint256 stakingDuration = block.timestamp - stakingTimestamps[msg.sender];
        uint256 reward = calculateReward(_amount, stakingDuration);

        // Update the user's staked balance
        stakedBalances[msg.sender] -= _amount;

        // Reset staking timestamp if fully unstaked
        if (stakedBalances[msg.sender] == 0) {
            stakingTimestamps[msg.sender] = 0;
        }

        // Transfer the tokens back to the user
        require(stakingToken.transfer(msg.sender, _amount), "Token transfer failed");

        // Transfer the calculated reward to the user
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit Unstaked(msg.sender, _amount, reward);
    }

    /**
     * @dev Internal function to calculate the reward based on amount and duration
     * @param _amount The amount being unstaked
     * @param _duration The duration for which tokens were staked
     * @return The calculated reward amount
     */
    function calculateReward(uint256 _amount, uint256 _duration) internal view returns (uint256) {
        // Simple reward calculation (rewardRate per year)
        uint256 yearlyReward = (_amount * rewardRate) / 100;
        uint256 reward = (yearlyReward * _duration) / (365 days);
        return reward;
    }

    /**
     * @dev Function to set a new reward rate (onlyOwner)
     * @param _newRate The new reward rate as a percentage
     */
    function setRewardRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Reward rate must be greater than 0");
        rewardRate = _newRate;
    }

    /**
     * @dev Function to stake tokens (for demonstration purposes; not part of unstaking logic)
     * @param _amount The amount of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        stakedBalances[msg.sender] += _amount;
        stakingTimestamps[msg.sender] = block.timestamp;
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
