"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealyi.github.io
Prompt: Generate Solidity code for a smart contract that allows users to stake ORB tokens on the Zealy platform and earn rewards in Ethereum and stablecoins.
Generated: DETERMINISTIC_38bc4b8943107539
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

// Import the necessary interfaces for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// A simple staking contract for ORB tokens
contract OrbStaking is ReentrancyGuard, Ownable {
    // Define the ERC20 token interface for ORB
    IERC20 public orbToken;
    
    // Define the reward tokens (ETH and stablecoin)
    IERC20 public stablecoinToken;
    
    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of ORB staked
        uint256 timestamp; // Timestamp of the last stake
    }
    
    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;
    
    // Declare events for staking and reward
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 ethAmount, uint256 stablecoinAmount);

    // Constructor to set token addresses
    constructor(address _orbToken, address _stablecoinToken) {
        orbToken = IERC20(_orbToken);
        stablecoinToken = IERC20(_stablecoinToken);
    }

    // Function to stake ORB tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(orbToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update user's stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake ORB tokens
    function unstake(uint256 _amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Deduct the amount and update the timestamp
        userStake.amount -= _amount;
        userStake.timestamp = block.timestamp;

        require(orbToken.transfer(msg.sender, _amount), "Transfer failed");
        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards (ETH and stablecoins)
    function claimRewards() external nonReentrant {
        // Calculate rewards based on the staked amount and duration
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked amount found");

        uint256 ethReward = calculateEthReward(userStake.amount, userStake.timestamp);
        uint256 stablecoinReward = calculateStablecoinReward(userStake.amount, userStake.timestamp);

        // Reset the timestamp after claiming
        userStake.timestamp = block.timestamp;

        // Transfer rewards
        if (ethReward > 0) {
            payable(msg.sender).transfer(ethReward);
        }
        if (stablecoinReward > 0) {
            require(stablecoinToken.transfer(msg.sender, stablecoinReward), "Stablecoin transfer failed");
        }

        emit RewardsClaimed(msg.sender, ethReward, stablecoinReward);
    }

    // Function to calculate ETH reward based on staked amount and duration
    function calculateEthReward(uint256 _amount, uint256 _timestamp) internal view returns (uint256) {
        // Placeholder for reward calculation logic
        return (_amount * (block.timestamp - _timestamp)) / 1e18; // Example calculation
    }

    // Function to calculate stablecoin reward based on staked amount and duration
    function calculateStablecoinReward(uint256 _amount, uint256 _timestamp) internal view returns (uint256) {
        // Placeholder for reward calculation logic
        return (_amount * (block.timestamp - _timestamp)) / 1e18; // Example calculation
    }

    // Allow the contract to receive ether
    receive() external payable {}
}
```
