"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paalai-revshare.pages.dev
Prompt: How can I implement a staking mechanism for $PAAL tokens that allows users to earn ETH rewards over different time periods?
Generated: DETERMINISTIC_18ae440c2743a3c2
Batch ID: 20250612_160656
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingRewards is ReentrancyGuard, Ownable {
    IERC20 public paalToken; // Reference to the $PAAL token contract
    uint256 public constant REWARD_RATE = 100; // Reward rate in wei per block
    uint256 public totalStaked; // Total amount of $PAAL staked
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public lastUpdate; // Last block where rewards were updated
    mapping(address => uint256) public rewards; // Unclaimed rewards for each user

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to set the $PAAL token contract address
    constructor(IERC20 _paalToken) {
        paalToken = _paalToken;
    }

    // Function to stake $PAAL tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0");
        require(paalToken.balanceOf(msg.sender) >= amount, "Insufficient $PAAL balance");

        // Transfer $PAAL tokens from the user to the contract
        paalToken.transferFrom(msg.sender, address(this), amount);

        // Update user staking details
        totalStaked += amount;
        stakedAmount[msg.sender] += amount;

        // Update reward for the user
        rewards[msg.sender] += _earned(msg.sender);
        lastUpdate[msg.sender] = block.number;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $PAAL tokens and claim rewards
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot unstake 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update user rewards before unstaking
        rewards[msg.sender] += _earned(msg.sender);
        lastUpdate[msg.sender] = block.number;

        // Reduce user's staked amount
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer $PAAL tokens back to the user
        paalToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        uint256 reward = _earned(msg.sender);
        require(reward > 0, "No rewards available");

        // Reset user's last update block
        lastUpdate[msg.sender] = block.number;
        rewards[msg.sender] = 0; // Reset rewards after claiming

        // Transfer ETH rewards to the user
        (bool success,) = msg.sender.call{value: reward}("");
        require(success, "Transfer failed");

        emit RewardPaid(msg.sender, reward);
    }

    // Internal function to calculate earned rewards
    function _earned(address account) internal view returns (uint256) {
        uint256 stakedDuration = block.number - lastUpdate[account];
        return stakedAmount[account] * REWARD_RATE * stakedDuration;
    }

    // Function to receive ETH
    receive() external payable {}

    // Function to withdraw unclaimed ETH from the contract (only owner)
    function withdrawETH(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient balance");
        (bool success,) = owner().call{value: amount}("");
        require(success, "Transfer failed");
    }
}
```
