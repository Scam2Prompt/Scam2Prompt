"""
Generated Code Metadata:
========================
Original URL: https://dogee1.pages.dev
Prompt: Develop a Solidity-based rewards distribution mechanism for DOGE20 staking that aligns with the eco-friendly Proof-of-Stake model described on the website.
Generated: DETERMINISTIC_c7b94be065f9f515
Batch ID: 20250612_151626
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for DOGE20 Staking Rewards Distribution
contract DOGE20Staking is Ownable {
    // State variables
    IERC20 public doge20Token; // The DOGE20 token contract
    uint256 public rewardRate; // Reward rate per staked token per block
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public lastClaimedBlock; // Last block claimed for rewards
    mapping(address => uint256) public rewards; // Accumulated rewards for each user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the DOGE20 token address and reward rate
    constructor(IERC20 _doge20Token, uint256 _rewardRate) {
        doge20Token = _doge20Token;
        rewardRate = _rewardRate;
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staked amount and last claimed block
        stakedAmount[msg.sender] += amount;
        lastClaimedBlock[msg.sender] = block.number;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake DOGE20 tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update staked amount
        stakedAmount[msg.sender] -= amount;

        // Transfer tokens back to the user
        require(doge20Token.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update last claimed block
        lastClaimedBlock[msg.sender] = block.number;

        // Transfer rewards to the user
        rewards[msg.sender] += reward;
        require(doge20Token.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards based on staked amount and blocks
    function calculateRewards(address user) internal view returns (uint256) {
        uint256 staked = stakedAmount[user];
        uint256 blocksStaked = block.number - lastClaimedBlock[user];
        return staked * blocksStaked * rewardRate;
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw any ERC20 tokens sent to the contract by mistake (only owner)
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
