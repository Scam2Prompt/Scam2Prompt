"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adexnetwork.vercel.app
Prompt: Create a smart contract for staking ADX tokens to support the AdEx ecosystem, incorporating DeFi protocol integration.
Generated: DETERMINISTIC_598176265a501566
Batch ID: 20250612_155032
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the StakingContract
contract StakingContract is Ownable {
    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 reward);

    // Mapping to keep track of user stakes
    mapping(address => uint256) public stakes;
    // Mapping to keep track of user rewards
    mapping(address => uint256) public rewards;

    // Total amount of staked tokens
    uint256 public totalStaked;
    // The address of the ADX token contract
    IERC20 public adxToken;

    // Reward rate per token staked (e.g., 1 token per week)
    uint256 public rewardRate = 1e18; // 1 ADX reward
    // Duration for reward calculation (in seconds)
    uint256 public rewardDuration = 1 weeks;

    // Constructor to initialize the contract with the ADX token address
    constructor(address _adxToken) {
        require(_adxToken != address(0), "StakingContract: Invalid token address");
        adxToken = IERC20(_adxToken);
    }

    // Function to stake ADX tokens
    function stake(uint256 amount) external {
        require(amount > 0, "StakingContract: Cannot stake 0");
        require(adxToken.transferFrom(msg.sender, address(this), amount), "StakingContract: Transfer failed");

        // Update user's stake and total staked amount
        stakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake ADX tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "StakingContract: Cannot unstake 0");
        require(stakes[msg.sender] >= amount, "StakingContract: Insufficient stake");

        // Update user's stake and total staked amount
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        require(adxToken.transfer(msg.sender, amount), "StakingContract: Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate and claim rewards
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "StakingContract: No rewards to claim");

        rewards[msg.sender] = 0; // Reset reward balance for the user
        require(adxToken.transfer(msg.sender, reward), "StakingContract: Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to calculate the reward for a user
    function calculateReward(address user) public view returns (uint256) {
        return (stakes[user] * rewardRate * rewardDuration) / 1e18; // Adjusted for decimals
    }

    // Function to set the reward rate (only owner can call)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw tokens accidentally sent to the contract
    function recoverTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(adxToken), "StakingContract: Cannot withdraw staked tokens");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
