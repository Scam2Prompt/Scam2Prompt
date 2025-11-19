"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doggocoin.web.app
Prompt: Provide an example of a smart contract that utilizes DOGGO COIN for staking rewards in NFT projects.
Generated: DETERMINISTIC_881f7de355470826
Batch ID: 20250612_162707
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

// Importing the interface for ERC20 token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
// Importing the interface for ERC721 token
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
// Importing SafeMath for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Defining the Staking contract
contract StakingContract {
    using SafeMath for uint256;

    // Struct to hold information about each stake
    struct Stake {
        uint256 amount;       // Amount of DOGGO COIN staked
        uint256 rewardDebt;   // Reward debt for the staker
        uint256 lastUpdated;  // Last timestamp when rewards were updated
    }

    // State variables
    IERC20 public doggoCoin;          // DOGGO COIN token contract
    IERC721 public nftCollection;     // NFT collection contract
    uint256 public rewardRate;        // Rewards per token staked per second
    mapping(address => Stake) public stakes; // Mapping to track stakes by user
    uint256 public totalStaked;       // Total amount of DOGGO COIN staked

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(IERC20 _doggoCoin, IERC721 _nftCollection, uint256 _rewardRate) {
        doggoCoin = _doggoCoin;
        nftCollection = _nftCollection;
        rewardRate = _rewardRate;
    }

    // Function to stake DOGGO COIN
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Update the user's stake information
        Stake storage userStake = stakes[msg.sender];
        userStake.rewardDebt = userStake.rewardDebt.add(calculatePendingReward(msg.sender));
        userStake.amount = userStake.amount.add(amount);
        userStake.lastUpdated = block.timestamp;

        // Transfer DOGGO COIN to this contract
        require(doggoCoin.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        totalStaked = totalStaked.add(amount);
        emit Staked(msg.sender, amount);
    }

    // Function to unstake DOGGO COIN
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update the user's reward before unstaking
        userStake.rewardDebt = userStake.rewardDebt.add(calculatePendingReward(msg.sender));

        userStake.amount = userStake.amount.sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Transfer DOGGO COIN back to the user
        require(doggoCoin.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculatePendingReward(msg.sender);
        require(reward > 0, "No rewards available");

        // Update reward debt
        stakes[msg.sender].rewardDebt = stakes[msg.sender].rewardDebt.add(reward);
        // Transfer DOGGO COIN as rewards
        require(doggoCoin.transfer(msg.sender, reward), "Transfer failed");
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to calculate pending rewards
    function calculatePendingReward(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 timeStaked = block.timestamp.sub(userStake.lastUpdated);
        return userStake.amount.mul(timeStaked).mul(rewardRate).div(1e18);
    }

    // Function to view staked amount
    function stakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to view pending rewards
    function pendingRewards(address user) external view returns (uint256) {
        return calculatePendingReward(user).add(stakes[user].rewardDebt);
    }
}
```
