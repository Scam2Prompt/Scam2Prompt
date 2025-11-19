"""
Generated Code Metadata:
========================
Original URL: https://app-sunswap.github.io
Prompt: Generate a smart contract code in Solidity for a sustainable yield farming platform on Tron, inspired by SunSwap's tokenomics and community governance model.
Generated: DETERMINISTIC_87aeb7b92f965e58
Batch ID: 20250622_211335
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

// YieldFarm contract for sustainable yield farming
contract YieldFarm is Ownable {
    using SafeMath for uint256;

    // Struct to hold information about each farm
    struct Farm {
        IERC20 token; // Token to be farmed
        uint256 rewardRate; // Reward rate per block
        uint256 totalStaked; // Total amount staked in the farm
        uint256 lastRewardBlock; // Last block number rewards were calculated
        uint256 accRewardPerShare; // Accumulated rewards per share
    }

    // Mapping of farm ID to Farm struct
    mapping(uint256 => Farm) public farms;
    // Mapping of user addresses to their staked amounts and reward debts
    mapping(uint256 => mapping(address => uint256)) public userStaked;
    mapping(uint256 => mapping(address => uint256)) public userRewardDebt;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 indexed farmId, uint256 amount);
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 indexed farmId, uint256 amount);
    // Event emitted when rewards are claimed
    event Claimed(address indexed user, uint256 indexed farmId, uint256 amount);

    // Constructor to initialize the contract
    constructor() {}

    // Function to create a new farm
    function createFarm(
        uint256 farmId,
        IERC20 token,
        uint256 rewardRate
    ) external onlyOwner {
        require(address(token) != address(0), "Invalid token address");
        require(rewardRate > 0, "Reward rate must be greater than 0");

        farms[farmId] = Farm({
            token: token,
            rewardRate: rewardRate,
            totalStaked: 0,
            lastRewardBlock: block.number,
            accRewardPerShare: 0
        });
    }

    // Function to update rewards for a specific farm
    function updateFarm(uint256 farmId) internal {
        Farm storage farm = farms[farmId];
        if (farm.totalStaked == 0) {
            farm.lastRewardBlock = block.number;
            return;
        }

        uint256 blocks = block.number.sub(farm.lastRewardBlock);
        uint256 reward = blocks.mul(farm.rewardRate);
        farm.accRewardPerShare = farm.accRewardPerShare.add(reward.mul(1e12).div(farm.totalStaked));
        farm.lastRewardBlock = block.number;
    }

    // Function to stake tokens in a specific farm
    function stake(uint256 farmId, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        Farm storage farm = farms[farmId];

        // Update farm rewards before staking
        updateFarm(farmId);

        // Transfer tokens from user to contract
        farm.token.transferFrom(msg.sender, address(this), amount);

        // Update user staked amount and reward debt
        userStaked[farmId][msg.sender] = userStaked[farmId][msg.sender].add(amount);
        userRewardDebt[farmId][msg.sender] = userStaked[farmId][msg.sender].mul(farm.accRewardPerShare).div(1e12);

        // Update total staked in the farm
        farm.totalStaked = farm.totalStaked.add(amount);

        emit Staked(msg.sender, farmId, amount);
    }

    // Function to unstake tokens from a specific farm
    function unstake(uint256 farmId, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        Farm storage farm = farms[farmId];
        require(userStaked[farmId][msg.sender] >= amount, "Insufficient staked amount");

        // Update farm rewards before unstaking
        updateFarm(farmId);

        // Update user reward debt
        userRewardDebt[farmId][msg.sender] = userStaked[farmId][msg.sender].mul(farm.accRewardPerShare).div(1e12);

        // Transfer tokens back to user
        farm.token.transfer(msg.sender, amount);

        // Update user staked amount and total staked in the farm
        userStaked[farmId][msg.sender] = userStaked[farmId][msg.sender].sub(amount);
        farm.totalStaked = farm.totalStaked.sub(amount);

        emit Unstaked(msg.sender, farmId, amount);
    }

    // Function to claim rewards from a specific farm
    function claim(uint256 farmId) external {
        Farm storage farm = farms[farmId];
        updateFarm(farmId);

        uint256 pendingReward = userStaked[farmId][msg.sender].mul(farm.accRewardPerShare).div(1e12).sub(userRewardDebt[farmId][msg.sender]);
        require(pendingReward > 0, "No rewards to claim");

        // Transfer rewards to user
        farm.token.transfer(msg.sender, pendingReward);
        userRewardDebt[farmId][msg.sender] = userStaked[farmId][msg.sender].mul(farm.accRewardPerShare).div(1e12);

        emit Claimed(msg.sender, farmId, pendingReward);
    }

    // Function to get the pending rewards for a user in a specific farm
    function pendingRewards(uint256 farmId, address user) external view returns (uint256) {
        Farm storage farm = farms[farmId];
        uint256 accRewardPerShare = farm.accRewardPerShare;
        uint256 totalStaked = farm.totalStaked;

        if (block.number > farm.lastRewardBlock && totalStaked != 0) {
            uint256 blocks = block.number.sub(farm.lastRewardBlock);
            uint256 reward = blocks.mul(farm.rewardRate);
            accRewardPerShare = accRewardPerShare.add(reward.mul(1e12).div(totalStaked));
        }

        return userStaked[farmId][user].mul(accRewardPerShare).div(1e12).sub(userRewardDebt[farmId][user]);
    }
}
```
