"""
Generated Code Metadata:
========================
Original URL: https://dcqef.com
Prompt: "Create a basic Ethereum smart contract using Solidity for a DeFi application, inspired by dcqef.com's functionalities."
Generated: DETERMINISTIC_7fe5e85533c5a3aa
Batch ID: 20250622_211317
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

// Importing OpenZeppelin's SafeMath library for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Basic DeFi contract for staking and rewards
contract DeFiStaking is Ownable {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public stakingToken;

    // Struct to hold user staking information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
    }

    // Mapping of user addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total amount of tokens staked
    uint256 public totalStaked;

    // Reward rate per block
    uint256 public rewardRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the staking token and reward rate
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked = staker.amountStaked.add(_amount);
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Insufficient staked amount");

        // Update staker's information
        staker.amountStaked = staker.amountStaked.sub(_amount);
        totalStaked = totalStaked.sub(_amount);
        
        require(stakingToken.transfer(msg.sender, _amount), "Transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update reward debt
        staker.rewardDebt = staker.rewardDebt.add(reward);

        // Transfer rewards to the user (assuming rewards are in the staking token)
        require(stakingToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards based on staked amount and reward rate
    function calculateReward(address _user) internal view returns (uint256) {
        Staker storage staker = stakers[_user];
        return staker.amountStaked.mul(rewardRate).div(1e18).sub(staker.rewardDebt);
    }

    // Function to update the reward rate (only owner can call)
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }
}
```
