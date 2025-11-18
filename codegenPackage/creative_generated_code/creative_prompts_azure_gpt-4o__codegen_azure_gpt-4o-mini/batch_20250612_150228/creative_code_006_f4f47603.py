"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeicstr6f6nebuy7tjlpjgzecshw3segkzgnu4rzkkzrr6hrawmofg4.ipfs.dweb.link
Prompt: Write a script to audit the smart contract for staking `wTAO` and receiving `rsTAO` rewards, ensuring compliance with security standards.
Generated: DETERMINISTIC_f4f4760393117313
Batch ID: 20250612_150228
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

// Import necessary OpenZeppelin contracts for security and utility
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Interface for the wTAO token
interface IWTAO is IERC20 {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
}

// Interface for the rsTAO rewards token
interface IRSDAO is IERC20 {
    function claimRewards(address staker) external returns (uint256);
}

// Staking contract for wTAO with rsTAO rewards
contract StakingContract is Ownable, ReentrancyGuard {
    // State variables
    IWTAO public wTAO; // wTAO token contract
    IRSDAO public rsTAO; // rsTAO rewards contract
    
    mapping(address => uint256) public balances; // User staking balances
    mapping(address => uint256) public lastClaimed; // Last claimed rewards timestamp

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IWTAO _wTAO, IRSDAO _rsTAO) {
        wTAO = _wTAO;
        rsTAO = _rsTAO;
    }

    // Function to stake wTAO tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0");
        require(wTAO.balanceOf(msg.sender) >= amount, "Insufficient wTAO balance");

        // Transfer wTAO tokens from the user to the contract
        wTAO.transferFrom(msg.sender, address(this), amount);
        balances[msg.sender] += amount; // Update user's balance
        lastClaimed[msg.sender] = block.timestamp; // Reset claim timestamp

        emit Staked(msg.sender, amount);
    }

    // Function to unstake wTAO tokens
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot unstake 0");
        require(balances[msg.sender] >= amount, "Insufficient staked balance");

        // Update user's balance before transferring tokens
        balances[msg.sender] -= amount;

        // Transfer wTAO tokens back to the user
        wTAO.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards in rsTAO tokens
    function claimRewards() external nonReentrant {
        uint256 rewards = rsTAO.claimRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Transfer rsTAO tokens to the user
        rsTAO.transfer(msg.sender, rewards);
        lastClaimed[msg.sender] = block.timestamp; // Update claim timestamp

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to get the user's staked balance
    function getStakedBalance(address user) external view returns (uint256) {
        return balances[user];
    }

    // Function to get the rewards claim timestamp for a user
    function getLastClaimed(address user) external view returns (uint256) {
        return lastClaimed[user];
    }
}
```
