"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bboop.fun
Prompt: Write a smart contract that integrates staking rewards and airdrop distribution, inspired by the cult-like ecosystem described on bboop.fun.
Generated: DETERMINISTIC_f73f3779e94d46c5
Batch ID: 20250612_153947
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for Staking Rewards and Airdrop Distribution
contract BboopStaking is Ownable {
    using SafeMath for uint256;

    // State variables
    IERC20 public stakingToken; // The ERC20 token used for staking
    IERC20 public rewardToken; // The ERC20 token for rewards distribution

    // Struct to hold staking details
    struct Staker {
        uint256 amountStaked; // Amount staked by the user
        uint256 rewardDebt; // Debt of rewards calculated
        uint256 lastStakeTime; // Last time the user staked
        bool isStaking; // Staking status
    }

    // Mapping of address to staker details
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Reward per block (can be adjusted)
    uint256 public rewardPerBlock = 1e18; // Example: 1 reward token per block

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event AirdropDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the staking and reward token
    constructor(IERC20 _stakingToken, IERC20 _rewardToken) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");

        // Transfer staking tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        // Update staker details
        Staker storage staker = stakers[msg.sender];
        if (staker.isStaking) {
            // Update existing staker rewards
            uint256 pendingReward = calculatePendingReward(msg.sender);
            staker.rewardDebt = staker.rewardDebt.add(pendingReward);
        } else {
            staker.isStaking = true;
            staker.lastStakeTime = block.timestamp;
        }

        staker.amountStaked = staker.amountStaked.add(amount);
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.isStaking, "Not staking");
        require(amount <= staker.amountStaked, "Unstake amount exceeds staked amount");

        // Update rewards before unstaking
        uint256 pendingReward = calculatePendingReward(msg.sender);
        staker.rewardDebt = staker.rewardDebt.add(pendingReward);

        // Reduce the amount staked
        staker.amountStaked = staker.amountStaked.sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);
        
        // If the staker has no more staked amount, reset their status
        if (staker.amountStaked == 0) {
            staker.isStaking = false;
        }

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate pending rewards
    function calculatePendingReward(address user) public view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 blocksStaked = block.number.sub(staker.lastStakeTime);
        uint256 pending = staker.amountStaked.mul(blocksStaked).mul(rewardPerBlock).div(1e18);
        return pending.sub(staker.rewardDebt);
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.isStaking, "Not staking");

        // Calculate and retrieve pending rewards
        uint256 pendingReward = calculatePendingReward(msg.sender);
        require(pendingReward > 0, "No rewards to claim");

        // Update reward debt
        staker.rewardDebt = staker.rewardDebt.add(pendingReward);
        
        // Transfer reward tokens to the user
        rewardToken.transfer(msg.sender, pendingReward);

        emit RewardsClaimed(msg.sender, pendingReward);
    }

    // Function for the owner to distribute airdrops
    function airdrop(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts mismatch");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid address");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Transfer airdrop tokens to the recipient
            rewardToken.transfer(recipients[i], amounts[i]);
            emit AirdropDistributed(recipients[i], amounts[i]);
        }
    }

    // Function to update the reward per block (only owner)
    function updateRewardPerBlock(uint256 newRewardPerBlock) external onlyOwner {
        require(newRewardPerBlock > 0, "Reward must be greater than zero");
        rewardPerBlock = newRewardPerBlock;
    }

    // Function to recover any ERC20 tokens sent to the contract accidentally (only owner)
    function recoverERC20(IERC20 token, uint256 amount) external onlyOwner {
        require(address(token) != address(stakingToken) && address(token) != address(rewardToken), "Cannot recover staking or reward tokens");
        token.transfer(msg.sender, amount);
    }
}
```
