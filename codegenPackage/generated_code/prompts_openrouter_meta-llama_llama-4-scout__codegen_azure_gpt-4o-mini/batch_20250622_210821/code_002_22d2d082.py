"""
Generated Code Metadata:
========================
Original URL: https://freedumfighert.pages.dev
Prompt: Design a smart contract for the FreeDum Fighters project, incorporating the staking pool, debate rewards, and tokenomics features.
Generated: DETERMINISTIC_22d2d082c991609c
Batch ID: 20250622_210821
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

// Importing OpenZeppelin contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Smart contract for FreeDum Fighters project
contract FreeDumFighters is ERC20, Ownable, ReentrancyGuard {
    // State variables
    uint256 public stakingPoolBalance;
    uint256 public debateRewardPool;
    uint256 public totalStaked;
    
    // Mapping to track staked amounts
    mapping(address => uint256) public stakedAmounts;
    
    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event DebateRewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the token
    constructor() ERC20("FreeDum Fighters Token", "FIGHT") {
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint initial supply to the contract owner
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from user to contract
        _transfer(msg.sender, address(this), amount);
        
        // Update staking pool and user's staked amount
        stakedAmounts[msg.sender] += amount;
        totalStaked += amount;
        stakingPoolBalance += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked amount");

        // Update staking pool and user's staked amount
        stakedAmounts[msg.sender] -= amount;
        totalStaked -= amount;
        stakingPoolBalance -= amount;

        // Transfer tokens back to user
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to distribute debate rewards
    function distributeDebateRewards(address[] calldata participants, uint256 rewardAmount) external onlyOwner {
        require(rewardAmount > 0, "Reward amount must be greater than zero");
        require(debateRewardPool >= rewardAmount * participants.length, "Insufficient reward pool");

        // Distributing rewards to participants
        for (uint256 i = 0; i < participants.length; i++) {
            _transfer(address(this), participants[i], rewardAmount);
            emit DebateRewardClaimed(participants[i], rewardAmount);
        }

        // Update debate reward pool
        debateRewardPool -= rewardAmount * participants.length;
    }

    // Function to add funds to the debate reward pool
    function addToDebateRewardPool(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        _transfer(msg.sender, address(this), amount);
        debateRewardPool += amount;
    }

    // Function to withdraw tokens from the contract (only for owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient contract balance");
        _transfer(address(this), msg.sender, amount);
    }

    // Function to check the user's staked amount
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmounts[user];
    }
}
```
