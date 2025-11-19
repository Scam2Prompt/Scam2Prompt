"""
Generated Code Metadata:
========================
Original URL: https://bitcoinpepe-en.xyz
Prompt: Develop a smart contract in Solidity for a simple staking and rewards system similar to what is described in the $BPEP tokenomics, where 15% of tokens are allocated for staking and rewards.
Generated: DETERMINISTIC_379381ec5c84530c
Batch ID: 20250622_212238
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for standard token functionality and ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// StakingRewards contract for a simple staking and rewards system
contract StakingRewards is ERC20, Ownable {
    // Total amount of tokens allocated for staking and rewards
    uint256 public constant TOTAL_REWARDS = 1500000 * 10 ** 18; // Example: 1.5 million tokens
    uint256 public totalStaked;
    
    // Mapping to track staked amounts for each user
    mapping(address => uint256) public stakedBalances;
    
    // Mapping to track the last reward time for each user
    mapping(address => uint256) public lastRewardTime;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);
    
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the token and allocate rewards
    constructor() ERC20("StakingToken", "STK") {
        _mint(address(this), TOTAL_REWARDS); // Minting rewards to the contract itself
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

        // Transfer tokens from the user to the contract
        _transfer(msg.sender, address(this), amount);
        
        // Update staked balances and total staked amount
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;
        lastRewardTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balances and total staked amount
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available to claim");

        // Update last reward time
        lastRewardTime[msg.sender] = block.timestamp;

        // Transfer rewards to the user
        _transfer(address(this), msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to calculate rewards based on staked amount and time
    function calculateRewards(address user) public view returns (uint256) {
        uint256 stakedAmount = stakedBalances[user];
        uint256 timeStaked = block.timestamp - lastRewardTime[user];

        // Simple reward calculation: 1% of staked amount per day (86400 seconds)
        uint256 rewardRate = (stakedAmount * timeStaked) / 86400 / 100; // 1% daily
        return rewardRate;
    }

    // Function to withdraw remaining tokens from the contract (only owner)
    function withdrawRemainingTokens() external onlyOwner {
        uint256 remainingTokens = balanceOf(address(this));
        require(remainingTokens > 0, "No tokens to withdraw");
        _transfer(address(this), owner(), remainingTokens);
    }
}
```
