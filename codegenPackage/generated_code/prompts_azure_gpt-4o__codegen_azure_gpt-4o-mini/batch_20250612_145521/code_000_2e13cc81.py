"""
Generated Code Metadata:
========================
Original URL: https://presalenest-goodeggtoken.web.app
Prompt: Write a smart contract in Solidity for a token similar to $GEGG, including features for presale stages, token distribution percentages (e.g., liquidity, marketing, ecosystem), and staking functionality.
Generated: DETERMINISTIC_2e13cc8143cc093e
Batch ID: 20250612_145521
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract GEGGToken is ERC20, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Presale stages
    enum PresaleStage { NotStarted, Stage1, Stage2, Ended }
    PresaleStage public currentStage;

    // Token distribution percentages
    uint256 public liquidityPercentage = 20; // 20% for liquidity
    uint256 public marketingPercentage = 10; // 10% for marketing
    uint256 public ecosystemPercentage = 15; // 15% for ecosystem
    uint256 public totalDistributionPercentage = 45; // Total distribution percentage

    // Staking variables
    mapping(address => uint256) public stakedTokens;
    mapping(address => uint256) public stakingStartTime;
    uint256 public stakingRewardRate = 100; // Reward rate per second
    uint256 public totalStaked;

    // Events
    event TokensStaked(address indexed user, uint256 amount);
    event TokensUnstaked(address indexed user, uint256 amount);
    event PresaleStageUpdated(PresaleStage newStage);

    // Constructor to initialize the token
    constructor() ERC20("GEGG Token", "GEGG") {
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint initial supply
        currentStage = PresaleStage.NotStarted; // Set initial presale stage
    }

    // Function to start presale
    function startPresale() external onlyOwner {
        require(currentStage == PresaleStage.NotStarted, "Presale already started");
        currentStage = PresaleStage.Stage1;
        emit PresaleStageUpdated(currentStage);
    }

    // Function to update presale stage
    function updatePresaleStage(PresaleStage newStage) external onlyOwner {
        require(newStage > currentStage, "New stage must be greater than current stage");
        currentStage = newStage;
        emit PresaleStageUpdated(currentStage);
    }

    // Function to distribute tokens based on percentages
    function distributeTokens() external onlyOwner {
        require(currentStage == PresaleStage.Ended, "Presale must be ended to distribute tokens");
        uint256 totalSupply = totalSupply();
        uint256 liquidityAmount = totalSupply.mul(liquidityPercentage).div(100);
        uint256 marketingAmount = totalSupply.mul(marketingPercentage).div(100);
        uint256 ecosystemAmount = totalSupply.mul(ecosystemPercentage).div(100);

        // Distribute tokens (implement your distribution logic here)
        // Example: _transfer(owner(), liquidityAddress, liquidityAmount);
        // Example: _transfer(owner(), marketingAddress, marketingAmount);
        // Example: _transfer(owner(), ecosystemAddress, ecosystemAmount);
    }

    // Function to stake tokens
    function stakeTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

        // Transfer tokens to the contract
        _transfer(msg.sender, address(this), amount);
        stakedTokens[msg.sender] = stakedTokens[msg.sender].add(amount);
        stakingStartTime[msg.sender] = block.timestamp;
        totalStaked = totalStaked.add(amount);

        emit TokensStaked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstakeTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedTokens[msg.sender] >= amount, "Insufficient staked balance");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);
        stakedTokens[msg.sender] = stakedTokens[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Transfer staked tokens and rewards back to the user
        _transfer(address(this), msg.sender, amount.add(rewards));

        emit TokensUnstaked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        uint256 stakedAmount = stakedTokens[user];
        uint256 stakingDuration = block.timestamp.sub(stakingStartTime[user]);
        return stakedAmount.mul(stakingRewardRate).mul(stakingDuration);
    }

    // Function to get the current presale stage
    function getCurrentPresaleStage() external view returns (PresaleStage) {
        return currentStage;
    }
}
```
