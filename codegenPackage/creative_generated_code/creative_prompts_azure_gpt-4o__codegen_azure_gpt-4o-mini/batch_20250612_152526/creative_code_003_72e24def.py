"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://satoshivmsquad.army
Prompt: Create a smart contract in Solidity for staking tokens and distributing airdrops, inspired by the SatoshiVM Squad staking model.
Generated: DETERMINISTIC_72e24defdb3dad2e
Batch ID: 20250612_152526
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

// Interface for the Staking Contract
interface IStaking {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function claimRewards() external;
}

contract StakingContract is IStaking, Ownable {
    // State variables
    IERC20 public stakingToken; // ERC20 token used for staking
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public lastClaimed; // Last claim timestamp for each user
    uint256 public rewardRate = 100; // Reward rate per block
    uint256 public totalStaked; // Total amount staked in the contract
    uint256 public airdropAmount; // Amount of tokens for airdrop

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);
    event AirdropDistributed(uint256 amount, address indexed recipient);

    // Constructor to initialize the contract
    constructor(IERC20 _stakingToken, uint256 _airdropAmount) {
        stakingToken = _stakingToken;
        airdropAmount = _airdropAmount;
    }

    // Function to stake tokens
    function stake(uint256 amount) external override {
        require(amount > 0, "Stake amount must be greater than 0");
        
        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        // Update staked amount and total staked
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;
        lastClaimed[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external override {
        require(amount > 0, "Withdraw amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update staked amount and total staked
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards based on staked amount and time
    function claimRewards() external override {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available to claim");

        // Update last claimed timestamp
        lastClaimed[msg.sender] = block.timestamp;

        // Transfer rewards to user
        stakingToken.transfer(msg.sender, reward);
        
        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards
    function calculateRewards(address user) internal view returns (uint256) {
        uint256 staked = stakedAmount[user];
        uint256 timeStaked = (block.timestamp - lastClaimed[user]) / 1 seconds;
        return staked * rewardRate * timeStaked;
    }

    // Function to distribute airdrop tokens to a specific address
    function distributeAirdrop(address recipient) external onlyOwner {
        require(airdropAmount > 0, "Airdrop amount must be greater than 0");
        require(stakingToken.balanceOf(address(this)) >= airdropAmount, "Insufficient contract balance for airdrop");

        // Transfer airdrop amount to recipient
        stakingToken.transfer(recipient, airdropAmount);
        
        emit AirdropDistributed(airdropAmount, recipient);
    }
}
```
