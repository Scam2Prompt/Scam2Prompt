"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-launch.firebaseapp.com
Prompt: Develop a smart contract that supports staking rewards for multiple meme coins while prioritizing $STARS holders, modeled after the Crypto All-Stars MemeVault.
Generated: DETERMINISTIC_8ced0b5668554bbe
Batch ID: 20250612_153722
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

// Importing OpenZeppelin's ERC20 interface and Ownable contract for security and standardization
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for staking rewards for multiple meme coins
contract MemeVault is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the staker
    }

    // Mapping of stakers to their information
    mapping(address => Staker) public stakers;

    // Mapping of token addresses to their respective reward rates
    mapping(address => uint256) public rewardRates;

    // Total staked amount
    uint256 public totalStaked;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);
    
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with reward rates
    constructor(address[] memory tokens, uint256[] memory rates) {
        require(tokens.length == rates.length, "Tokens and rates length mismatch");
        for (uint256 i = 0; i < tokens.length; i++) {
            rewardRates[tokens[i]] = rates[i];
        }
    }

    // Function to stake tokens
    function stake(address token, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardRates[token] > 0, "Token not supported");

        // Transfer tokens from the user to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amount += amount;
        staker.rewardDebt += calculatePendingRewards(msg.sender);
        
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(address token, uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");

        // Update staker information
        staker.amount -= amount;
        staker.rewardDebt += calculatePendingRewards(msg.sender);
        
        totalStaked -= amount;

        // Transfer tokens back to the user
        IERC20(token).transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 pendingRewards = calculatePendingRewards(msg.sender);
        require(pendingRewards > 0, "No rewards to claim");

        // Reset reward debt
        stakers[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        IERC20 rewardToken = IERC20(address(this)); // Assuming rewards are paid in the contract's token
        rewardToken.transfer(msg.sender, pendingRewards);

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    // Internal function to calculate pending rewards for a staker
    function calculatePendingRewards(address stakerAddress) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 rewardRate = rewardRates[address(this)]; // Assuming rewards are paid in the contract's token
        return (staker.amount * rewardRate) / 1e18 - staker.rewardDebt; // Adjusting for precision
    }

    // Function to update reward rates (only owner)
    function updateRewardRate(address token, uint256 rate) external onlyOwner {
        rewardRates[token] = rate;
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
