"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-scorpion-casino.web.app
Prompt: Explain how to integrate the Scorpion Casino's tokenomics into a decentralized application (dApp) that allows users to buy and stake $SCORP tokens.
Generated: DETERMINISTIC_4ce9f4ceb5e797e0
Batch ID: 20250612_161420
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

// Import the OpenZeppelin ERC20 standard contract and SafeMath library
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ScorpionCasinoDApp is ReentrancyGuard, Ownable {
    // Interface for the $SCORP token
    IERC20 public scorpToken;

    // Struct to manage staking information
    struct StakeInfo {
        uint256 amount;     // Amount of $SCORP staked
        uint256 startTime;  // Timestamp of when staking started
    }

    // Mapping to store staking details for each user
    mapping(address => StakeInfo) public stakes;

    // Staking reward rate per year (e.g., 10% = 0.1 ether)
    uint256 public rewardRate = 0.1 ether;

    // Events for transparency and off-chain tracking
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensStaked(address indexed staker, uint256 amount);
    event TokensUnstaked(address indexed staker, uint256 amount, uint256 rewards);

    // Constructor to initialize the $SCORP token contract address
    constructor(address _scorpTokenAddress) {
        require(_scorpTokenAddress != address(0), "Invalid token address");
        scorpToken = IERC20(_scorpTokenAddress);
    }

    // Function to let users buy $SCORP tokens using Ether
    function buyTokens() external payable nonReentrant {
        require(msg.value > 0, "Ether amount must be greater than zero");

        // Define the conversion rate (e.g., 1 Ether = 1000 $SCORP)
        uint256 tokensToBuy = msg.value * 1000;

        // Transfer $SCORP tokens to the sender
        require(scorpToken.transfer(msg.sender, tokensToBuy), "Token transfer failed");

        emit TokensPurchased(msg.sender, tokensToBuy);
    }

    // Function to let users stake $SCORP tokens
    function stakeTokens(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(scorpToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer $SCORP tokens from the user to this contract
        require(scorpToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking info for the user
        StakeInfo storage stake = stakes[msg.sender];
        stake.amount += _amount;
        stake.startTime = block.timestamp;

        emit TokensStaked(msg.sender, _amount);
    }

    // Function to let users unstake tokens and claim rewards
    function unstakeTokens() external nonReentrant {
        StakeInfo storage stake = stakes[msg.sender];
        require(stake.amount > 0, "No tokens to unstake");

        // Calculate staking duration in seconds
        uint256 stakingDuration = block.timestamp - stake.startTime;

        // Calculate rewards based on the staking duration
        uint256 rewards = (stake.amount * rewardRate * stakingDuration) / (365 days * 1 ether);

        // Transfer staked tokens and rewards back to the user
        uint256 totalAmount = stake.amount + rewards;
        require(scorpToken.balanceOf(address(this)) >= totalAmount, "Insufficient contract balance");

        require(scorpToken.transfer(msg.sender, totalAmount), "Token transfer failed");

        // Reset user's stake info
        stake.amount = 0;
        stake.startTime = 0;

        emit TokensUnstaked(msg.sender, totalAmount, rewards);
    }

    // Function to update the reward rate (only owner can call this)
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        require(_newRate >= 0, "Reward rate must be non-negative");
        rewardRate = _newRate;
    }

    // Function to withdraw Ether from the contract (only owner can call this)
    function withdrawEther(uint256 _amount) external onlyOwner {
        require(address(this).balance >= _amount, "Insufficient contract balance");
        payable(owner()).transfer(_amount);
    }

    // Function to withdraw $SCORP tokens from the contract (only owner can call this)
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(scorpToken.balanceOf(address(this)) >= _amount, "Insufficient token balance");
        require(scorpToken.transfer(owner(), _amount), "Token transfer failed");
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
