"""
Generated Code Metadata:
========================
Original URL: https://galaxyfox-en.web.app
Prompt: Generate a smart contract in Solidity for a token with a deflationary process, similar to $GFOX, including a burn mechanism and staking rewards.
Generated: DETERMINISTIC_39c21adafdf4ceca
Batch ID: 20250622_210348
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

contract DeflationaryToken is ERC20, Ownable, ReentrancyGuard {
    // Events
    event TokensBurned(address indexed burner, uint256 amount);
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed staker, uint256 reward);

    // Staking structure
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
    }

    // Mapping of staker addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate (in tokens per block)
    uint256 public rewardRate = 1e18; // 1 token per block

    // Burn percentage (e.g., 2% burn)
    uint256 public burnPercentage = 200; // 200 means 2%

    // Total supply cap
    uint256 public maxSupply = 1000000 * 1e18; // 1 million tokens

    constructor() ERC20("DeflationaryToken", "DFT") {
        _mint(msg.sender, maxSupply);
    }

    // Function to burn tokens
    function burn(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Calculate burn amount
        uint256 burnAmount = (amount * burnPercentage) / 10000;
        _burn(msg.sender, burnAmount);
        emit TokensBurned(msg.sender, burnAmount);
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens to the contract
        _transfer(msg.sender, address(this), amount);

        // Update stake information
        stakes[msg.sender].amount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update stake information
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the staker
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim staking rewards
    function claimRewards() external nonReentrant {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        // Update reward debt
        stakes[msg.sender].rewardDebt += reward;

        // Transfer rewards to the staker
        _mint(msg.sender, reward);
        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to calculate rewards for a staker
    function calculateReward(address staker) public view returns (uint256) {
        Stake memory stakeInfo = stakes[staker];
        return (stakeInfo.amount * rewardRate) / 1e18; // Adjust reward calculation as needed
    }

    // Function to set the reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to set the burn percentage (only owner)
    function setBurnPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= 10000, "Percentage must be <= 100%");
        burnPercentage = newPercentage;
    }
}
```
