"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nettensor-5u5.pages.dev
Prompt: Create a smart contract in Solidity that interacts with Net Tensor's App Chain and utilizes $NAO tokens for staking and claiming rewards.
Generated: DETERMINISTIC_6bbc158d498d412c
Batch ID: 20250612_152527
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
 * @title NAOStakingContract
 * @dev A smart contract for staking $NAO tokens on Net Tensor's App Chain and claiming rewards.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract NAOStakingContract {
    // Token address for $NAO
    IERC20 public naoToken;

    // Struct to keep track of user stakes and rewards
    struct Stake {
        uint256 amount; // Amount staked
        uint256 reward; // Reward accrued
        uint256 lastUpdated; // Timestamp of the last update
    }

    // Mapping to store stakes for each user
    mapping(address => Stake) public stakes;

    // Reward rate per second (e.g., 10 tokens / year in seconds)
    uint256 public rewardRate = 1 ether / (365 days);

    // Owner of the contract
    address public owner;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 reward);
    event Withdrawn(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier updateReward(address user) {
        Stake storage stake = stakes[user];
        if (stake.amount > 0) {
            uint256 timeElapsed = block.timestamp - stake.lastUpdated;
            stake.reward += timeElapsed * stake.amount * rewardRate / 1 ether;
        }
        stake.lastUpdated = block.timestamp;
        _;
    }

    // Constructor to initialize the contract with the $NAO token address
    constructor(address _naoTokenAddress) {
        require(_naoTokenAddress != address(0), "Invalid token address");
        naoToken = IERC20(_naoTokenAddress);
        owner = msg.sender;
    }

    /**
     * @dev Stake $NAO tokens to start earning rewards.
     * @param amount The number of tokens to stake.
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer $NAO tokens from the user to the contract
        require(naoToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user stake
        stakes[msg.sender].amount += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Claim the rewards accrued so far.
     */
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = stakes[msg.sender].reward;
        require(reward > 0, "No rewards available");

        // Reset reward after claiming
        stakes[msg.sender].reward = 0;

        // Transfer rewards to the user
        require(naoToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit Claimed(msg.sender, reward);
    }

    /**
     * @dev Withdraw staked tokens along with accrued rewards.
     */
    function withdraw() external updateReward(msg.sender) {
        Stake storage stake = stakes[msg.sender];
        uint256 amount = stake.amount;
        uint256 reward = stake.reward;

        require(amount > 0, "No staked tokens to withdraw");

        // Reset user stake and reward
        stake.amount = 0;
        stake.reward = 0;

        // Transfer staked tokens and rewards back to the user
        require(naoToken.transfer(msg.sender, amount + reward), "Withdraw transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Change the reward rate. Only callable by the owner.
     * @param newRewardRate The new reward rate (tokens per second).
     */
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    /**
     * @dev Emergency withdrawal of all tokens in case of issues. Only callable by the owner.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = naoToken.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to withdraw");
        require(naoToken.transfer(owner, contractBalance), "Emergency withdraw failed");
    }
}
```
