"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimspopofrog.web.app
Prompt: Write a smart contract in Solidity for staking $FROP tokens, ensuring compatibility with multichain functionality as described in the Popo ecosystem.
Generated: DETERMINISTIC_53bb566404b117ad
Batch ID: 20250612_153512
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
 * @title FROPTokenStaking
 * @notice Smart contract for staking FROP tokens with multichain compatibility.
 * @dev Ensure compatibility with the Popo ecosystem's multichain features.
 */

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract FROPTokenStaking {
    // State Variables
    IERC20 public immutable fropToken; // ERC20 token interface
    uint256 public totalStaked; // Total amount of tokens staked in the contract
    mapping(address => uint256) public stakedBalance; // Tracks staked balance of each user
    mapping(address => uint256) public rewardsBalance; // Tracks rewards balance of each user
    mapping(address => uint256) public lastStakeTimestamp; // Tracks the time of last stake for each user

    uint256 public rewardRatePerSecond = 10; // Reward rate per second per token staked
    address public owner; // Owner of the contract

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    modifier updateRewards(address user) {
        if (stakedBalance[user] > 0) {
            uint256 timeElapsed = block.timestamp - lastStakeTimestamp[user];
            rewardsBalance[user] += timeElapsed * stakedBalance[user] * rewardRatePerSecond;
        }
        lastStakeTimestamp[user] = block.timestamp;
        _;
    }

    // Constructor
    constructor(address _fropTokenAddress) {
        require(_fropTokenAddress != address(0), "Invalid FROP token address");
        fropToken = IERC20(_fropTokenAddress);
        owner = msg.sender;
    }

    /**
     * @notice Stake FROP tokens in the contract.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Cannot stake zero tokens");
        require(fropToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        stakedBalance[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake FROP tokens from the contract.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Cannot unstake zero tokens");
        require(stakedBalance[msg.sender] >= amount, "Insufficient staked balance");

        stakedBalance[msg.sender] -= amount;
        totalStaked -= amount;

        require(fropToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Claim accumulated rewards.
     */
    function claimRewards() external updateRewards(msg.sender) {
        uint256 rewards = rewardsBalance[msg.sender];
        require(rewards > 0, "No rewards available");

        rewardsBalance[msg.sender] = 0;

        // Assuming rewards are distributed in the same FROP token
        require(fropToken.transfer(msg.sender, rewards), "Token transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Set a new reward rate per second.
     * @dev Only callable by the contract owner.
     * @param newRewardRate The new reward rate per second.
     */
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        require(newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRatePerSecond = newRewardRate;
    }

    /**
     * @notice Emergency withdrawal of any tokens from the contract.
     * @dev Only callable by the contract owner.
     * @param tokenAddress The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function emergencyWithdraw(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20(tokenAddress).transfer(owner, amount);
    }
}
```
