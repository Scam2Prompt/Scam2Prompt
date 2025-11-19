"""
Generated Code Metadata:
========================
Original URL: https://app-basemafia-com.pages.dev
Prompt: Create a smart contract on the Base chain that supports cross-pool staking programs for $MAFIA tokens and other meme coin projects.
Generated: DETERMINISTIC_72cd822d893a8d43
Batch ID: 20250612_145924
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Smart contract for cross-pool staking of $MAFIA tokens and other meme coins
contract CrossPoolStaking is Ownable, ReentrancyGuard {
    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // ERC20 token interface for $MAFIA and other meme coins
    IERC20 public mafiaToken;
    IERC20 public memeCoin;

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with token addresses
    constructor(address _mafiaToken, address _memeCoin) {
        require(_mafiaToken != address(0), "Invalid $MAFIA token address");
        require(_memeCoin != address(0), "Invalid meme coin address");
        
        mafiaToken = IERC20(_mafiaToken);
        memeCoin = IERC20(_memeCoin);
    }

    // Function to stake $MAFIA tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(mafiaToken.balanceOf(msg.sender) >= amount, "Insufficient $MAFIA balance");

        // Transfer $MAFIA tokens from user to contract
        mafiaToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $MAFIA tokens
    function unstake(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user's stake information
        userStake.amount -= amount;

        // Transfer $MAFIA tokens back to user
        mafiaToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards (for demonstration purposes, rewards are calculated as 10% of staked amount)
    function claimRewards() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked amount to claim rewards");

        uint256 reward = (userStake.amount * 10) / 100; // 10% reward
        require(memeCoin.balanceOf(address(this)) >= reward, "Insufficient reward balance in contract");

        // Transfer rewards to user
        memeCoin.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Function to withdraw contract's ERC20 tokens (only owner)
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(IERC20(tokenAddress).balanceOf(address(this)) >= amount, "Insufficient contract balance");

        IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
}
```
