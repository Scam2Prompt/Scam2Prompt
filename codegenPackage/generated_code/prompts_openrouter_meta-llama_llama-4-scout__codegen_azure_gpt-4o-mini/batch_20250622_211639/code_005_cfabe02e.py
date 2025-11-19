"""
Generated Code Metadata:
========================
Original URL: https://memes-index.pages.dev
Prompt: Design a smart contract using Solidity to facilitate the $MEMEX presale, including functions for buying, staking, and claiming rewards, while ensuring security and transparency.
Generated: DETERMINISTIC_cfabe02ebe9782f6
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MemexPresale is ReentrancyGuard, Ownable {
    // State variables
    IERC20 public memexToken; // The MEMEX token contract
    uint256 public presalePrice; // Price of MEMEX token in wei
    uint256 public totalTokensSold; // Total tokens sold in presale
    uint256 public totalStaked; // Total tokens staked
    uint256 public rewardRate; // Rate of rewards for stakers
    uint256 public presaleEndTime; // End time for the presale

    // Mapping to track user balances and stakes
    mapping(address => uint256) public balances;
    mapping(address => uint256) public stakes;
    mapping(address => uint256) public rewards;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensStaked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed claimer, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _memexToken, uint256 _presalePrice, uint256 _duration, uint256 _rewardRate) {
        memexToken = _memexToken;
        presalePrice = _presalePrice;
        presaleEndTime = block.timestamp + _duration;
        rewardRate = _rewardRate;
    }

    // Modifier to check if presale is active
    modifier isPresaleActive() {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        _;
    }

    // Function to buy MEMEX tokens during the presale
    function buyTokens(uint256 amount) external payable isPresaleActive nonReentrant {
        require(msg.value == amount * presalePrice, "Incorrect Ether value sent");
        require(amount > 0, "Amount must be greater than zero");

        // Update state
        balances[msg.sender] += amount;
        totalTokensSold += amount;

        // Emit event
        emit TokensPurchased(msg.sender, amount);
    }

    // Function to stake MEMEX tokens for rewards
    function stakeTokens(uint256 amount) external nonReentrant {
        require(balances[msg.sender] >= amount, "Insufficient balance to stake");
        require(amount > 0, "Amount must be greater than zero");

        // Update state
        balances[msg.sender] -= amount;
        stakes[msg.sender] += amount;
        totalStaked += amount;

        // Emit event
        emit TokensStaked(msg.sender, amount);
    }

    // Function to claim rewards based on staked tokens
    function claimRewards() external nonReentrant {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available to claim");

        // Update state
        rewards[msg.sender] = 0; // Reset rewards after claiming
        payable(msg.sender).transfer(reward); // Transfer rewards

        // Emit event
        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards for a user
    function calculateRewards(address user) internal view returns (uint256) {
        return stakes[user] * rewardRate;
    }

    // Function to withdraw unsold tokens after presale ends
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp >= presaleEndTime, "Presale is still active");
        uint256 unsoldTokens = memexToken.balanceOf(address(this)) - totalTokensSold;
        require(unsoldTokens > 0, "No unsold tokens to withdraw");

        // Transfer unsold tokens to owner
        memexToken.transfer(owner(), unsoldTokens);
    }

    // Function to withdraw Ether from the contract
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");

        // Transfer Ether to owner
        payable(owner()).transfer(balance);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
