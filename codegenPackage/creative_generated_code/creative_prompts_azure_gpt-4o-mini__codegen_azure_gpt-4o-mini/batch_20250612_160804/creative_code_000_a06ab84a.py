"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-io.web.app
Prompt: How can I implement a staking smart contract for DOGE20 on Ethereum to distribute rewards over two years?
Generated: DETERMINISTIC_a06ab84aeead537c
Batch ID: 20250612_160804
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

// Import OpenZeppelin Contracts for safe math and ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract Doge20Staking {
    using SafeMath for uint256;

    // The ERC20 token being staked
    IERC20 public doge20Token;

    // Duration for rewards distribution (in seconds)
    uint256 public rewardDuration = 730 days; // 2 years

    // Total staked amount and total rewards
    uint256 public totalStaked;
    uint256 public totalRewards;

    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastStakedTime;
    }

    // Mapping to track stakers
    mapping(address => Staker) public stakers;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the DOGE20 token address
    constructor(address _doge20Token) {
        doge20Token = IERC20(_doge20Token);
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        Staker storage staker = stakers[msg.sender];

        // Update staker's information
        staker.amountStaked = staker.amountStaked.add(amount);
        staker.lastStakedTime = block.timestamp;

        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake DOGE20 tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Calculate and distribute rewards before unstaking
        distributeRewards(msg.sender);

        staker.amountStaked = staker.amountStaked.sub(amount);
        totalStaked = totalStaked.sub(amount);

        require(doge20Token.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        distributeRewards(msg.sender);
    }

    // Internal function to distribute rewards
    function distributeRewards(address user) internal {
        Staker storage staker = stakers[user];
        uint256 timeStaked = block.timestamp.sub(staker.lastStakedTime);
        if (timeStaked > 0) {
            uint256 reward = calculateReward(staker.amountStaked, timeStaked);
            require(reward <= totalRewards, "Insufficient rewards available");
            staker.rewardDebt = staker.rewardDebt.add(reward);
            staker.lastStakedTime = block.timestamp;

            // Transfer rewards to the user
            require(doge20Token.transfer(user, reward), "Transfer failed");
            totalRewards = totalRewards.sub(reward);

            emit RewardsClaimed(user, reward);
        }
    }

    // Function to calculate rewards based on staked amount and time
    function calculateReward(uint256 amount, uint256 time) internal view returns (uint256) {
        // Example reward calculation logic (to be replaced with actual logic)
        return amount.mul(time).div(rewardDuration);
    }

    // Function to add rewards to the contract (only owner should be allowed)
    function addRewards(uint256 amount) external {
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        totalRewards = totalRewards.add(amount);
    }

    // Function to get current staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakers[user].amountStaked;
    }

    // Function to get total rewards for a user
    function getPendingRewards(address user) external view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 timeStaked = block.timestamp.sub(staker.lastStakedTime);
        return calculateReward(staker.amountStaked, timeStaked).add(staker.rewardDebt);
    }
}
```
