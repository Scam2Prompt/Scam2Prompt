"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-pepe.xyz
Prompt: Create a smart contract in Solidity for staking $BPEP tokens, ensuring compatibility with Bitcoin Pepe's tokenomics (15% allocation for staking and rewards).
Generated: DETERMINISTIC_765712cb0d9360bf
Batch ID: 20250612_154010
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $BPEP tokens
contract BPEPStaking is Ownable {
    // State variables
    IERC20 public bpepToken; // Reference to the BPEP token contract
    uint256 public totalStaked; // Total amount of BPEP tokens staked
    uint256 public rewardRate; // Reward rate per staked token
    uint256 public lastUpdateTime; // Timestamp of the last update
    mapping(address => uint256) public stakedBalance; // User's staked balance
    mapping(address => uint256) public rewards; // User's rewards

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the BPEP token address and reward rate
    constructor(IERC20 _bpepToken, uint256 _rewardRate) {
        bpepToken = _bpepToken;
        rewardRate = _rewardRate;
    }

    // Modifier to update rewards for the caller
    modifier updateReward(address account) {
        rewards[account] += _earned(account);
        lastUpdateTime = block.timestamp;
        _;
    }

    // Function to deposit tokens for staking
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        totalStaked += amount;
        stakedBalance[msg.sender] += amount;
        // Transfer BPEP tokens from user to the contract
        bool success = bpepToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");
        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function unstake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot unstake 0");
        require(stakedBalance[msg.sender] >= amount, "Insufficient staked balance");
        totalStaked -= amount;
        stakedBalance[msg.sender] -= amount;
        // Transfer BPEP tokens back to the user
        bool success = bpepToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        rewards[msg.sender] = 0;
        // Transfer rewards to the user
        bool success = bpepToken.transfer(msg.sender, reward);
        require(success, "Reward transfer failed");
        emit RewardPaid(msg.sender, reward);
    }

    // Internal function to calculate earned rewards
    function _earned(address account) internal view returns (uint256) {
        return (stakedBalance[account] * rewardRate * (block.timestamp - lastUpdateTime)) / 1e18;
    }

    // Function to update the reward rate (only owner can call)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    // Function to withdraw any ERC20 tokens sent to the contract by mistake
    function rescueTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(bpepToken), "Cannot rescue BPEP tokens");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
