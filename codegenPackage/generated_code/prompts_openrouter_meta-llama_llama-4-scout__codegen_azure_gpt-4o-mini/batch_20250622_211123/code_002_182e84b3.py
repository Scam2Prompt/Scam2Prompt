"""
Generated Code Metadata:
========================
Original URL: https://www.staderlabs.fi
Prompt: Design a smart contract on BNB Chain that integrates with Stader Labs' liquid staking solution, allowing users to stake BNB and earn rewards while maintaining liquidity.
Generated: DETERMINISTIC_182e84b33e30e2c4
Batch ID: 20250622_211123
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for Stader Labs' liquid staking solution
interface IStader {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function getReward() external;
    function getStakedAmount(address user) external view returns (uint256);
}

// Smart contract for staking BNB with Stader Labs
contract BNBStaking is Ownable {
    using SafeMath for uint256;

    // Address of the Stader Labs staking contract
    IStader public stader;

    // Mapping to track user stakes
    mapping(address => uint256) private userStakes;

    // Event emitted when a user stakes BNB
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes BNB
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to set the Stader contract address
    constructor(address _staderAddress) {
        require(_staderAddress != address(0), "Invalid Stader address");
        stader = IStader(_staderAddress);
    }

    // Function to stake BNB
    function stake() external payable {
        require(msg.value > 0, "Must stake a positive amount");

        // Update user stakes
        userStakes[msg.sender] = userStakes[msg.sender].add(msg.value);

        // Stake the BNB in Stader Labs
        stader.stake(msg.value);

        emit Staked(msg.sender, msg.value);
    }

    // Function to unstake BNB
    function unstake(uint256 amount) external {
        require(amount > 0, "Must unstake a positive amount");
        require(userStakes[msg.sender] >= amount, "Insufficient staked amount");

        // Update user stakes
        userStakes[msg.sender] = userStakes[msg.sender].sub(amount);

        // Unstake the BNB from Stader Labs
        stader.unstake(amount);

        // Transfer the unstaked BNB back to the user
        payable(msg.sender).transfer(amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        // Get the amount of rewards for the user
        uint256 rewardAmount = stader.getReward();

        // Transfer rewards to the user
        payable(msg.sender).transfer(rewardAmount);

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return userStakes[user];
    }

    // Fallback function to accept BNB
    receive() external payable {}
}
```
