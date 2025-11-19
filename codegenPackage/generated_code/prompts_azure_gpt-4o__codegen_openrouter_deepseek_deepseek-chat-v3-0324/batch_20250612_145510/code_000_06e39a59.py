"""
Generated Code Metadata:
========================
Original URL: https://panther-ai.pages.dev
Prompt: Write a smart contract in Solidity that adheres to BEP20 standards for creating a token like PantherAI on the Binance Smart Chain. Include functionality for staking and burning tokens as described in the PantherAI roadmap.
Generated: DETERMINISTIC_06e39a5934ff04f7
Batch ID: 20250612_145510
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract PantherAI is ERC20, ERC20Burnable, Ownable, Pausable {
    uint256 public constant MAX_SUPPLY = 100_000_000 * 10**18; // 100 million tokens
    uint256 public stakingRewardRate = 10; // 10% annual reward rate
    uint256 public lastBurnTimestamp;
    uint256 public burnInterval = 30 days;
    uint256 public burnPercentage = 1; // 1% of total supply
    
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public lastStakeTimestamps;
    uint256 public totalStaked;

    event TokensStaked(address indexed user, uint256 amount);
    event TokensUnstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event TokensBurned(uint256 amount);

    constructor() ERC20("PantherAI", "PAI") {
        _mint(msg.sender, MAX_SUPPLY);
        lastBurnTimestamp = block.timestamp;
    }

    // Stake tokens to earn rewards
    function stake(uint256 amount) external whenNotPaused {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        _claimRewards(msg.sender);

        _transfer(msg.sender, address(this), amount);
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;
        lastStakeTimestamps[msg.sender] = block.timestamp;

        emit TokensStaked(msg.sender, amount);
    }

    // Unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        _claimRewards(msg.sender);

        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;
        _transfer(address(this), msg.sender, amount);

        emit TokensUnstaked(msg.sender, amount);
    }

    // Claim staking rewards
    function claimRewards() external {
        _claimRewards(msg.sender);
    }

    function _claimRewards(address user) internal {
        uint256 rewards = calculateRewards(user);
        if (rewards > 0) {
            _mint(user, rewards);
            emit RewardsClaimed(user, rewards);
        }
        lastStakeTimestamps[user] = block.timestamp;
    }

    // Calculate rewards for a staker
    function calculateRewards(address user) public view returns (uint256) {
        if (stakedBalances[user] == 0) return 0;
        
        uint256 stakedTime = block.timestamp - lastStakeTimestamps[user];
        uint256 reward = (stakedBalances[user] * stakingRewardRate * stakedTime) / (100 * 365 days);
        return reward;
    }

    // Perform periodic token burn
    function performBurn() external onlyOwner {
        require(block.timestamp >= lastBurnTimestamp + burnInterval, "Burn interval not reached");
        
        uint256 burnAmount = (totalSupply() * burnPercentage) / 100;
        require(burnAmount > 0, "No tokens to burn");

        _burn(address(this), burnAmount);
        lastBurnTimestamp = block.timestamp;

        emit TokensBurned(burnAmount);
    }

    // Set staking reward rate (only owner)
    function setStakingRewardRate(uint256 newRate) external onlyOwner {
        require(newRate <= 100, "Rate too high"); // Max 100%
        stakingRewardRate = newRate;
    }

    // Set burn parameters (only owner)
    function setBurnParameters(uint256 interval, uint256 percentage) external onlyOwner {
        require(percentage <= 10, "Percentage too high"); // Max 10%
        burnInterval = interval;
        burnPercentage = percentage;
    }

    // Pause contract (only owner)
    function pause() external onlyOwner {
        _pause();
    }

    // Unpause contract (only owner)
    function unpause() external onlyOwner {
        _unpause();
    }

    // Override transfer to handle pausable
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        super._beforeTokenTransfer(from, to, amount);
        require(!paused(), "Token transfer while paused");
    }
}
```
