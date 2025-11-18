"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedogeverse-com.pages.dev
Prompt: Write a smart contract in Solidity that facilitates staking $DOGEVERSE tokens on the Ethereum blockchain, allowing users to lock their tokens and earn rewards over time.
Generated: DETERMINISTIC_391900f8f3f165d4
Batch ID: 20250612_153606
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

// Import the ERC20 interface to interact with the $DOGEVERSE token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the Staking contract
contract DogeverseStaking is Ownable {
    // Token to be staked
    IERC20 public dogeverseToken;

    // Structure to hold information about each user's stake
    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Reward rate per second (in wei, adjust as necessary)
    uint256 public rewardRate = 1e18; // Example reward rate of 1 DOGEVERSE token per second

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the DOGEVERSE token address
    constructor(IERC20 _dogeverseToken) {
        dogeverseToken = _dogeverseToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        
        // Transfer $DOGEVERSE tokens from the user to the contract
        dogeverseToken.transferFrom(msg.sender, address(this), _amount);

        // Update the user's stake information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0) return 0;

        uint256 timeStaked = block.timestamp - userStake.timestamp;
        return userStake.amount * rewardRate * timeStaked / 1e18;
    }

    // Function to unstake tokens and claim rewards
    function unstake(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Calculate rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);

        // Update user's stake
        userStake.amount -= _amount;
        userStake.timestamp = block.timestamp;

        // Transfer staked tokens back to the user
        dogeverseToken.transfer(msg.sender, _amount);

        // Transfer calculated rewards to the user
        dogeverseToken.transfer(msg.sender, rewards);

        emit Unstaked(msg.sender, _amount);
        emit RewardClaimed(msg.sender, rewards);
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }
}
```
