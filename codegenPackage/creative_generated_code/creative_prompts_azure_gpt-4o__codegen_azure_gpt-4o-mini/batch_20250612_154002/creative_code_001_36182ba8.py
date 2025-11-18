"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onc185.vip
Prompt: Generate code in Solidity to create a smart contract for a DeFi application that integrates with Ethereum.
Generated: DETERMINISTIC_36182ba81a5554f6
Batch ID: 20250612_154002
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

// Importing OpenZeppelin's SafeMath library for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for a simple Decentralized Finance (DeFi) application
contract DeFiApplication is Ownable {
    using SafeMath for uint256;

    // Token used for staking/rewarding
    IERC20 public stakingToken;

    // Struct representing a user's staking information
    struct Staker {
        uint256 amount; // Amount of tokens staked
        uint256 reward; // Accumulated reward
        uint256 lastStakedTime; // Last time the user staked
    }

    // Mapping of user addresses to their staking information
    mapping(address => Staker) public stakers;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to set the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Transfer tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);
        
        // Update user's staking information
        stakers[msg.sender].amount = stakers[msg.sender].amount.add(_amount);
        stakers[msg.sender].lastStakedTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= _amount, "Insufficient staked amount");

        // Update user's staking information
        staker.amount = staker.amount.sub(_amount);

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, _amount);
        
        emit Unstaked(msg.sender, _amount);
    }

    // Function to calculate and claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculateReward(msg.sender);
        
        require(reward > 0, "No rewards available");

        // Update user's reward information
        staker.reward = 0; // Reset reward after claiming
        
        // Transfer rewards to the user (Assuming the contract has enough balance)
        payable(msg.sender).transfer(reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Function to calculate rewards based on the staker's amount and time staked
    function calculateReward(address _user) public view returns (uint256) {
        Staker storage staker = stakers[_user];
        uint256 timeStaked = block.timestamp.sub(staker.lastStakedTime); // Duration staked
        uint256 rewardRate = 1e18; // Reward rate per second

        // Calculate reward = amount staked * time staked * reward rate
        return staker.amount.mul(timeStaked).mul(rewardRate).div(1e18);
    }

    // Function to withdraw Ether earned (only callable by owner)
    function withdrawEther(uint256 _amount) external onlyOwner {
        require(address(this).balance >= _amount, "Insufficient balance");

        // Transfer Ether to the owner
        payable(owner()).transfer(_amount);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
