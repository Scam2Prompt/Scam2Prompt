"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-opsec-computer.pages.dev
Prompt: Develop a smart contract that integrates with the $OPSEC token for staking and governance, following the roadmap specifications outlined for Q2 2024.
Generated: DETERMINISTIC_2de9034e0e7c3c5e
Batch ID: 20250612_145933
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for staking and governance using the $OPSEC token
contract OpsecStaking is Ownable {
    using SafeMath for uint256;

    // State variables
    IERC20 public opsecToken; // The OPSEC token contract
    uint256 public totalStaked; // Total amount of staked tokens
    uint256 public rewardRate; // Rate of rewards for stakers
    mapping(address => uint256) public stakedBalance; // User's staked balance
    mapping(address => uint256) public rewards; // User's accumulated rewards

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the OPSEC token address and reward rate
    constructor(address _opsecToken, uint256 _rewardRate) {
        require(_opsecToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        
        opsecToken = IERC20(_opsecToken);
        rewardRate = _rewardRate;
    }

    // Function to stake OPSEC tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(opsecToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        totalStaked = totalStaked.add(amount);
        stakedBalance[msg.sender] = stakedBalance[msg.sender].add(amount);
        emit Staked(msg.sender, amount);
    }

    // Function to unstake OPSEC tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedBalance[msg.sender] >= amount, "Insufficient staked balance");

        totalStaked = totalStaked.sub(amount);
        stakedBalance[msg.sender] = stakedBalance[msg.sender].sub(amount);
        require(opsecToken.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate the rewards for a user
    function calculateRewards(address user) internal view returns (uint256) {
        return stakedBalance[user].mul(rewardRate).div(1e18); // Assuming rewardRate is in wei
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = rewards[msg.sender].add(reward);
        require(opsecToken.transfer(msg.sender, reward), "Transfer failed");
        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to withdraw any ERC20 tokens from the contract
    function withdrawERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(opsecToken), "Cannot withdraw OPSEC token");
        require(IERC20(tokenAddress).transfer(msg.sender, amount), "Transfer failed");
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be greater than zero");
        rewardRate = newRate;
    }

    // Function to withdraw contract balance (only owner)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```
