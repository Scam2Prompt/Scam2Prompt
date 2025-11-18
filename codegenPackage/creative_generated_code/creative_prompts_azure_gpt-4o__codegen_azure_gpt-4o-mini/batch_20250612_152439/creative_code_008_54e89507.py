"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefxyz.pages.dev
Prompt: Develop a smart contract in Solidity that rewards users with BEEF Coin for participating in community-driven events or staking Ethereum.
Generated: DETERMINISTIC_54e8950718763549
Batch ID: 20250612_152439
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

// Import the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the SmartContract for rewarding users with BEEF Coin
contract BeefRewardSystem is Ownable {
    IERC20 public beefCoin; // BEEF Coin token contract address
    uint256 public rewardPerEvent; // Amount of BEEF Coin rewarded per event

    struct User {
        uint256 stakedAmount; // Amount of ETH staked by the user
        uint256 lastEventParticipation; // Timestamp of last event participation
        uint256 totalRewards; // Total rewards earned by the user
    }

    mapping(address => User) public users; // Mapping of user addresses to their data

    // Events for logging activities
    event RewardClaimed(address indexed user, uint256 amount);
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event EventParticipated(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the BEEF Coin address
    constructor(address _beefCoinAddress, uint256 _rewardPerEvent) {
        require(_beefCoinAddress != address(0), "Invalid BEEF Coin address");
        require(_rewardPerEvent > 0, "Reward must be greater than zero");

        beefCoin = IERC20(_beefCoinAddress);
        rewardPerEvent = _rewardPerEvent;
    }

    // Function to stake ETH
    function stake() external payable {
        require(msg.value > 0, "Must send ETH to stake");
        
        // Update user's staking amount
        users[msg.sender].stakedAmount += msg.value;

        emit Staked(msg.sender, msg.value);
    }

    // Function to unstake ETH
    function unstake(uint256 amount) external {
        require(users[msg.sender].stakedAmount >= amount, "Insufficient staked amount");

        // Update user's staking amount
        users[msg.sender].stakedAmount -= amount;
        payable(msg.sender).transfer(amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function for users to participate in an event
    function participateInEvent() external {
        require(users[msg.sender].stakedAmount > 0, "Must stake ETH to participate");
        
        // Reward the user with BEEF Coin
        users[msg.sender].totalRewards += rewardPerEvent;
        beefCoin.transfer(msg.sender, rewardPerEvent);

        // Update last participation time
        users[msg.sender].lastEventParticipation = block.timestamp;

        emit EventParticipated(msg.sender, rewardPerEvent);
    }

    // Function for users to claim their total rewards
    function claimRewards() external {
        uint256 rewardsToClaim = users[msg.sender].totalRewards;
        require(rewardsToClaim > 0, "No rewards available to claim");

        // Reset user's rewards and transfer BEEF Coin
        users[msg.sender].totalRewards = 0;
        beefCoin.transfer(msg.sender, rewardsToClaim);

        emit RewardClaimed(msg.sender, rewardsToClaim);
    }

    // Function to update reward amount (only owner)
    function updateRewardPerEvent(uint256 newReward) external onlyOwner {
        require(newReward > 0, "Reward must be greater than zero");
        rewardPerEvent = newReward;
    }
}
```
