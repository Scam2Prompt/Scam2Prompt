"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe-in.web.app
Prompt: Generate code to integrate staking functionality for $MPEPE tokens into a DeFi liquidity pool, ensuring rewards are distributed automatically using audited smart contracts.
Generated: DETERMINISTIC_e2f55c74afd7143f
Batch ID: 20250612_154115
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

// Importing required interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Staking contract for $MPEPE tokens
contract MPEPEStaking is Ownable {
    using SafeMath for uint256;

    // ERC20 token to be staked
    IERC20 public mpepeToken;

    // Total staked amount
    uint256 public totalStaked;

    // User stake details
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the $MPEPE token address
    constructor(address _mpepeToken) {
        require(_mpepeToken != address(0), "Invalid token address");
        mpepeToken = IERC20(_mpepeToken);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(mpepeToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to the contract
        mpepeToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].timestamp = block.timestamp;

        // Update total staked amount
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Stake storage stakeData = stakes[msg.sender];
        require(stakeData.amount >= amount, "Insufficient staked amount");

        // Update user's stake
        stakeData.amount = stakeData.amount.sub(amount);

        // Transfer tokens back to the user
        mpepeToken.transfer(msg.sender, amount);

        // Update total staked amount
        totalStaked = totalStaked.sub(amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards (dummy implementation, to be replaced with actual logic)
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory stakeData = stakes[user];
        // Placeholder for reward calculation
        return stakeData.amount.mul(10).div(100); // 10% reward for demonstration
    }

    // Function to withdraw rewards (to be called after calculating rewards)
    function withdrawRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to withdraw");

        // Transfer rewards to the user
        mpepeToken.transfer(msg.sender, rewards);
    }

    // Function to get the details of a user's stake
    function getStakeDetails(address user) external view returns (uint256 amount, uint256 timestamp) {
        Stake memory stakeData = stakes[user];
        return (stakeData.amount, stakeData.timestamp);
    }
}
```
