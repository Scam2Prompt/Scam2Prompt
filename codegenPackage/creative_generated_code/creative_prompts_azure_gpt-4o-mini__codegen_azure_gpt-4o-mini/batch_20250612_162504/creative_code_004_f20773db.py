"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogepreneur-in.pages.dev
Prompt: Generate a Solidity contract that represents a DogePreneur token and includes functions for purchasing and staking to earn passive income.
Generated: DETERMINISTIC_f20773db4afe18c1
Batch ID: 20250612_162504
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

// Import OpenZeppelin contracts for ERC20 and Ownable functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract DogePreneurToken is ERC20, Ownable, ReentrancyGuard {
    // Mapping for staking balances
    mapping(address => uint256) private _stakingBalances;
    // Mapping for staking timestamps
    mapping(address => uint256) private _stakingTimestamps;
    // Staking duration in seconds
    uint256 public stakingDuration = 30 days;
    // Reward rate (e.g., 1000 tokens per staking period)
    uint256 public rewardRate = 1000 * 10 ** decimals();

    // Event for token purchase
    event TokensPurchased(address indexed buyer, uint256 amount);
    // Event for staking action
    event Staked(address indexed user, uint256 amount);
    // Event for rewards claimed
    event RewardsClaimed(address indexed user, uint256 reward);

    // Constructor to set token details
    constructor() ERC20("DogePreneur Token", "DPT") {
        // Mint initial supply to the contract creator
        _mint(msg.sender, 1_000_000 * 10 ** decimals());
    }

    // Function to purchase tokens
    function purchaseTokens() external payable {
        require(msg.value > 0, "Must send ETH to purchase tokens");
        uint256 tokensToMint = msg.value * 100; // 1 ETH = 100 Tokens
        _mint(msg.sender, tokensToMint);
        emit TokensPurchased(msg.sender, tokensToMint);
    }

    // Function to stake tokens
    function stakeTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

        // Transfer tokens to the contract
        _transfer(msg.sender, address(this), amount);
        _stakingBalances[msg.sender] += amount;
        _stakingTimestamps[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to claim rewards after staking
    function claimRewards() external nonReentrant {
        require(_stakingBalances[msg.sender] > 0, "No tokens staked");
        require(block.timestamp >= _stakingTimestamps[msg.sender] + stakingDuration, "Staking period not yet ended");

        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Reset staking data
        _stakingBalances[msg.sender] = 0;
        _stakingTimestamps[msg.sender] = 0;

        // Mint rewards to the user
        _mint(msg.sender, reward);
        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards
    function calculateReward(address user) internal view returns (uint256) {
        return (_stakingBalances[user] * rewardRate) / 10 ** decimals();
    }

    // Function to get the user's staked amount
    function stakedAmount(address user) external view returns (uint256) {
        return _stakingBalances[user];
    }

    // Function to withdraw ETH for the owner
    function withdrawETH() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to set the staking duration (only owner)
    function setStakingDuration(uint256 duration) external onlyOwner {
        stakingDuration = duration;
    }

    // Function to set the reward rate (only owner)
    function setRewardRate(uint256 rate) external onlyOwner {
        rewardRate = rate * 10 ** decimals();
    }
}
```
