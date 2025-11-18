"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeicstr6f6nebuy7tjlpjgzecshw3segkzgnu4rzkkzrr6hrawmofg4.ipfs.dweb.link
Prompt: Develop a smart contract that integrates staking functionality, allowing users to claim `wTAO` and automatically stake to receive `rsTAO` rewards.
Generated: DETERMINISTIC_1a2c4a7279556ef9
Batch ID: 20250612_150228
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

// Importing interfaces for ERC20 and Ownable contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for staking functionality
contract StakingContract is Ownable {
    // State variables to track tokens
    IERC20 public wTAO; // Wrapped TAO token
    IERC20 public rsTAO; // Rewarded Staked TAO token

    // Struct to hold user staking data
    struct Staker {
        uint256 amount; // Amount of wTAO staked
        uint256 rewards; // Accumulated rewards
    }

    // Mapping to track each user's staking data
    mapping(address => Staker) private stakers;

    // Events for staking and claiming rewards
    event Staked(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with token addresses
    constructor(address _wTAO, address _rsTAO) {
        require(_wTAO != address(0), "Invalid wTAO address");
        require(_rsTAO != address(0), "Invalid rsTAO address");

        wTAO = IERC20(_wTAO);
        rsTAO = IERC20(_rsTAO);
    }

    // Function to stake wTAO tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount should be greater than zero");
        require(wTAO.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the staker's data
        stakers[msg.sender].amount += amount;

        // Emit staking event
        emit Staked(msg.sender, amount);
    }

    // Function to claim rewards and auto-stake rsTAO
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount > 0, "No wTAO staked");

        // Calculate rewards (simple example, can be improved)
        uint256 rewardsToClaim = staker.rewards;
        require(rewardsToClaim > 0, "No rewards to claim");

        // Reset the rewards for the user after claiming
        staker.rewards = 0;

        // Automatically stake the claimed rewards
        require(rsTAO.transferFrom(address(this), msg.sender, rewardsToClaim), "Transfer failed");
        
        // Emit claim event
        emit Claimed(msg.sender, rewardsToClaim);
    }

    // Function to add rewards to a staker (can be called by external contract or admin)
    function addRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Reward amount should be positive");
        
        stakers[user].rewards += amount;
    }

    // Function to check the staker's information
    function getStakerInfo(address user) external view returns (uint256 stakedAmount, uint256 rewards) {
        Staker storage staker = stakers[user];
        return (staker.amount, staker.rewards);
    }
}
```
