"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-svd.vercel.app
Prompt: Create a Solidity contract that includes functionality for minting, staking, and withdrawing "FREE SHAVACADOO" tokens, ensuring proper security measures are implemented.
Generated: DETERMINISTIC_2da420dfed1a4869
Batch ID: 20250612_150440
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

contract FreeShavacadoo is ERC20, ERC20Burnable, Ownable, ReentrancyGuard {
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    mapping(address => Stake) public stakes;
    uint256 public rewardRate = 100; // 100 tokens per second per staked token (example rate)
    uint256 public minStakeDuration = 1 days;

    event TokensMinted(address indexed to, uint256 amount);
    event TokensStaked(address indexed staker, uint256 amount);
    event TokensWithdrawn(address indexed staker, uint256 amount, uint256 reward);

    constructor() ERC20("FREE SHAVACADOO", "FSH") {
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Amount must be positive");
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be positive");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        if (stakes[msg.sender].amount > 0) {
            _calculateAndMintReward(msg.sender);
        }

        _transfer(msg.sender, address(this), amount);
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount + amount,
            timestamp: block.timestamp
        });

        emit TokensStaked(msg.sender, amount);
    }

    function withdraw() external nonReentrant {
        require(stakes[msg.sender].amount > 0, "No stake found");
        require(
            block.timestamp >= stakes[msg.sender].timestamp + minStakeDuration,
            "Minimum stake duration not reached"
        );

        uint256 stakedAmount = stakes[msg.sender].amount;
        uint256 reward = _calculateAndMintReward(msg.sender);

        _transfer(address(this), msg.sender, stakedAmount);
        delete stakes[msg.sender];

        emit TokensWithdrawn(msg.sender, stakedAmount, reward);
    }

    function _calculateAndMintReward(address staker) private returns (uint256) {
        Stake memory stakeInfo = stakes[staker];
        uint256 stakedDuration = block.timestamp - stakeInfo.timestamp;
        uint256 reward = (stakeInfo.amount * stakedDuration * rewardRate) / 1e18;

        if (reward > 0) {
            _mint(staker, reward);
        }

        stakes[staker].timestamp = block.timestamp;
        return reward;
    }

    function setRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Rate must be positive");
        rewardRate = newRate;
    }

    function setMinStakeDuration(uint256 newDuration) external onlyOwner {
        require(newDuration > 0, "Duration must be positive");
        minStakeDuration = newDuration;
    }
}
```
