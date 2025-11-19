"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitechpad-io.pages.dev
Prompt: How can I implement a staking mechanism for AITECH tokens that allows users to earn varying APY based on lock terms, as described on the Solidus AI Tech website?
Generated: DETERMINISTIC_7cd52cc878f1a84f
Batch ID: 20250612_161500
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

// Interface for the AITECH token
interface IAITECH is IERC20 {
    function mint(address to, uint256 amount) external;
}

// Staking contract for AITECH tokens
contract AITECHStaking is Ownable {
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 lockTerm; // in seconds
        uint256 apy; // annual percentage yield (in basis points)
    }

    IAITECH public aitechToken; // AITECH token contract
    mapping(address => Stake[]) public stakes; // Mapping of user addresses to their stakes
    uint256 public totalStaked; // Total amount of tokens staked

    event Staked(address indexed user, uint256 amount, uint256 lockTerm, uint256 apy);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the AITECH token contract
    constructor(IAITECH _aitechToken) {
        aitechToken = _aitechToken;
    }

    // Allows users to stake AITECH tokens
    function stake(uint256 amount, uint256 lockTerm, uint256 apy) external {
        require(amount > 0, "Amount must be greater than 0");
        require(lockTerm > 0, "Lock term must be greater than 0");
        require(apy > 0, "APY must be greater than 0");

        // Transfer tokens from user to this contract
        aitechToken.transferFrom(msg.sender, address(this), amount);

        // Create a new stake
        stakes[msg.sender].push(Stake({
            amount: amount,
            startTime: block.timestamp,
            lockTerm: lockTerm,
            apy: apy
        }));

        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount, lockTerm, apy);
    }

    // Allows users to unstake their tokens after the lock term has expired
    function unstake(uint256 stakeIndex) external {
        require(stakeIndex < stakes[msg.sender].length, "Invalid stake index");
        Stake storage userStake = stakes[msg.sender][stakeIndex];

        // Check if the lock term has expired
        require(block.timestamp >= userStake.startTime + userStake.lockTerm, "Lock term has not expired");

        // Calculate the rewards (APY)
        uint256 rewards = calculateRewards(userStake.amount, userStake.apy, userStake.lockTerm);

        // Transfer staked tokens and rewards back to the user
        totalStaked -= userStake.amount;
        aitechToken.transfer(msg.sender, userStake.amount + rewards);

        // Remove the stake from the array
        stakes[msg.sender][stakeIndex] = stakes[msg.sender][stakes[msg.sender].length - 1];
        stakes[msg.sender].pop();

        emit Unstaked(msg.sender, userStake.amount);
    }

    // Calculates the rewards based on APY and lock term
    function calculateRewards(uint256 amount, uint256 apy, uint256 lockTerm) internal pure returns (uint256) {
        // APY is in basis points (e.g., 10000 = 100%)
        uint256 reward = (amount * apy * lockTerm) / (365 days * 10000);
        return reward;
    }

    // Function to withdraw tokens in case of emergency
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= totalStaked, "Insufficient funds");
        aitechToken.transfer(msg.sender, amount);
    }
}
```
