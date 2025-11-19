"""
Generated Code Metadata:
========================
Original URL: https://claim-doge20coin.pages.dev
Prompt: Design a basic smart contract in Solidity for distributing staking rewards to DOGE20 token holders over a period of two years, similar to the one described on the webpage.
Generated: DETERMINISTIC_bd08ee8f8a97af50
Batch ID: 20250622_205751
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

// Importing the ERC20 interface for DOGE20 token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract StakingRewards {
    // State variables
    IERC20 public doge20Token; // The DOGE20 token contract
    address public owner; // Owner of the contract
    uint256 public totalRewards; // Total rewards to distribute
    uint256 public startTime; // Start time of the reward distribution
    uint256 public endTime; // End time of the reward distribution
    uint256 public rewardRate; // Reward rate per second
    mapping(address => uint256) public rewards; // Mapping of user addresses to their rewards
    mapping(address => uint256) public lastClaimed; // Last claimed timestamp for each user

    // Events
    event RewardsClaimed(address indexed user, uint256 amount);
    event RewardsDistributed(uint256 totalRewards);

    // Constructor to initialize the contract
    constructor(IERC20 _doge20Token, uint256 _totalRewards, uint256 _duration) {
        require(_duration > 0, "Duration must be greater than 0");
        doge20Token = _doge20Token;
        totalRewards = _totalRewards;
        startTime = block.timestamp;
        endTime = startTime + _duration;
        rewardRate = totalRewards / _duration; // Calculate reward rate
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Function to claim rewards
    function claimRewards() external {
        require(block.timestamp >= startTime, "Reward distribution has not started");
        require(block.timestamp <= endTime, "Reward distribution has ended");

        uint256 claimableRewards = calculateRewards(msg.sender);
        require(claimableRewards > 0, "No rewards to claim");

        // Update last claimed time
        lastClaimed[msg.sender] = block.timestamp;

        // Transfer rewards to the user
        require(doge20Token.transfer(msg.sender, claimableRewards), "Transfer failed");

        emit RewardsClaimed(msg.sender, claimableRewards);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastClaimed[user];
        if (timeElapsed > 0 && timeElapsed <= (endTime - startTime)) {
            return timeElapsed * rewardRate;
        }
        return 0;
    }

    // Function to withdraw remaining rewards by the owner
    function withdrawRemainingRewards() external onlyOwner {
        require(block.timestamp > endTime, "Cannot withdraw before distribution ends");
        uint256 remainingBalance = doge20Token.balanceOf(address(this));
        require(remainingBalance > 0, "No remaining rewards to withdraw");

        // Transfer remaining rewards to the owner
        require(doge20Token.transfer(owner, remainingBalance), "Transfer failed");
    }

    // Function to get the current reward balance of a user
    function getRewardBalance(address user) external view returns (uint256) {
        return calculateRewards(user);
    }
}
```
