"""
Generated Code Metadata:
========================
Original URL: https://pablo-defis.web.app
Prompt: Develop a staking protocol for $PABLO tokens, providing a function to stake tokens, earn rewards, and claim rewards, with considerations for the 0% to 10% tax rate and community engagement.
Generated: DETERMINISTIC_f48fe7780d9fe06d
Batch ID: 20250622_204809
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
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $PABLO tokens
contract PabloStaking is Ownable {
    // Token to be staked
    IERC20 public pabloToken;

    // Struct to hold user staking data
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the user
        uint256 lastStakedTime; // Last time the user staked
    }

    // Mapping of user addresses to their staking data
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate (in tokens per second)
    uint256 public rewardRate;

    // Tax rate (0% to 10%)
    uint256 public taxRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event Claimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _pabloToken, uint256 _rewardRate, uint256 _taxRate) {
        require(_taxRate <= 10, "Tax rate must be between 0% and 10%");
        pabloToken = _pabloToken;
        rewardRate = _rewardRate;
        taxRate = _taxRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(pabloToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.rewardDebt += calculatePendingRewards(msg.sender);
        userStake.lastStakedTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate pending rewards for a user
    function calculatePendingRewards(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 timeStaked = block.timestamp - userStake.lastStakedTime;
        return (userStake.amount * rewardRate * timeStaked) / 1e18; // Adjust for precision
    }

    // Function to claim rewards
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        uint256 pendingRewards = calculatePendingRewards(msg.sender);

        require(pendingRewards > 0, "No rewards to claim");

        // Update reward debt
        userStake.rewardDebt += pendingRewards;
        userStake.lastStakedTime = block.timestamp;

        // Apply tax
        uint256 tax = (pendingRewards * taxRate) / 100;
        uint256 netRewards = pendingRewards - tax;

        // Transfer rewards to user
        require(pabloToken.transfer(msg.sender, netRewards), "Transfer failed");

        emit Claimed(msg.sender, netRewards);
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    // Function to set a new tax rate (only owner)
    function setTaxRate(uint256 newTaxRate) external onlyOwner {
        require(newTaxRate <= 10, "Tax rate must be between 0% and 10%");
        taxRate = newTaxRate;
    }

    // Function to withdraw staked tokens (only owner)
    function withdrawStakedTokens(uint256 amount) external onlyOwner {
        require(amount <= totalStaked, "Insufficient staked amount");
        totalStaked -= amount;
        require(pabloToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
