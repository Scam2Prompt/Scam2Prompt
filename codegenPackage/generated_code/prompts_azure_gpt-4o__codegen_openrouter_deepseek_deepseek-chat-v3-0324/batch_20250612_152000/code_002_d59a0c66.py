"""
Generated Code Metadata:
========================
Original URL: https://corgiaixyz.pages.dev
Prompt: Create a smart contract in Solidity for the $CORGIAI token that includes staking functionality and token burn mechanisms as outlined in the CorgiAI roadmap.
Generated: DETERMINISTIC_d59a0c6629e502f0
Batch ID: 20250612_152000
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract CorgiAIToken is ERC20, ERC20Burnable, Ownable, ReentrancyGuard {
    // Staking related variables
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 rewardRate;
    }

    mapping(address => Stake) public stakes;
    uint256 public totalStaked;
    uint256 public constant MIN_STAKE_DURATION = 7 days;
    uint256 public constant MAX_STAKE_DURATION = 365 days;
    uint256 public baseRewardRate = 10; // 10% annual reward
    uint256 public burnRate = 2; // 2% of tokens burned on transfer

    // Events
    event Staked(address indexed user, uint256 amount, uint256 duration);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event TokensBurned(address indexed burner, uint256 amount);
    event RewardRateChanged(uint256 newRate);
    event BurnRateChanged(uint256 newRate);

    constructor() ERC20("CorgiAI Token", "CORGIAI") {
        _mint(msg.sender, 1000000000 * 10 ** decimals()); // 1 billion tokens
    }

    // Stake tokens
    function stake(uint256 amount, uint256 duration) external nonReentrant {
        require(amount > 0, "Cannot stake 0 tokens");
        require(duration >= MIN_STAKE_DURATION && duration <= MAX_STAKE_DURATION, "Invalid stake duration");
        require(stakes[msg.sender].amount == 0, "Already staking");

        _burn(msg.sender, amount); // Burn tokens when staking
        totalStaked += amount;

        uint256 rewardRate = calculateRewardRate(duration);
        stakes[msg.sender] = Stake({
            amount: amount,
            startTime: block.timestamp,
            rewardRate: rewardRate
        });

        emit Staked(msg.sender, amount, duration);
    }

    // Unstake tokens and claim rewards
    function unstake() external nonReentrant {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to unstake");
        require(block.timestamp >= userStake.startTime + MIN_STAKE_DURATION, "Stake not mature");

        uint256 stakedAmount = userStake.amount;
        uint256 reward = calculateReward(userStake);
        totalStaked -= stakedAmount;

        delete stakes[msg.sender];

        _mint(msg.sender, stakedAmount + reward);
        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    // Calculate reward based on stake duration and amount
    function calculateReward(Stake memory stakeInfo) internal view returns (uint256) {
        uint256 stakedDuration = block.timestamp - stakeInfo.startTime;
        uint256 annualReward = (stakeInfo.amount * stakeInfo.rewardRate) / 100;
        return (annualReward * stakedDuration) / 365 days;
    }

    // Calculate reward rate based on stake duration
    function calculateRewardRate(uint256 duration) internal view returns (uint256) {
        return baseRewardRate + (duration - MIN_STAKE_DURATION) / (1 days);
    }

    // Override transfer to implement burn mechanism
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        uint256 burnAmount = (amount * burnRate) / 100;
        uint256 transferAmount = amount - burnAmount;

        if (burnAmount > 0) {
            _burn(sender, burnAmount);
            emit TokensBurned(sender, burnAmount);
        }

        super._transfer(sender, recipient, transferAmount);
    }

    // Admin functions
    function setRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0 && newRate <= 50, "Invalid reward rate");
        baseRewardRate = newRate;
        emit RewardRateChanged(newRate);
    }

    function setBurnRate(uint256 newRate) external onlyOwner {
        require(newRate <= 5, "Burn rate too high");
        burnRate = newRate;
        emit BurnRateChanged(newRate);
    }

    // View functions
    function getStakeInfo(address user) external view returns (uint256 amount, uint256 startTime, uint256 rewardRate) {
        Stake memory s = stakes[user];
        return (s.amount, s.startTime, s.rewardRate);
    }

    function getPendingReward(address user) external view returns (uint256) {
        Stake memory s = stakes[user];
        if (s.amount == 0) return 0;
        return calculateReward(s);
    }
}
```
