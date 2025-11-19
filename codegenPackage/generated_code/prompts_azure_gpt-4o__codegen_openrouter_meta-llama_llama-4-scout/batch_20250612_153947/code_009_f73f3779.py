"""
Generated Code Metadata:
========================
Original URL: https://bboop.fun
Prompt: Write a smart contract that integrates staking rewards and airdrop distribution, inspired by the cult-like ecosystem described on bboop.fun.
Generated: DETERMINISTIC_f73f3779e94d46c5
Batch ID: 20250612_153947
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title BBoop Staking and Airdrop Contract
 * @author [Your Name]
 * @notice This contract manages staking rewards and airdrop distribution for the BBoop ecosystem.
 */
contract BBoopStakingAirdrop is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebt;

    // Mapping of airdrop recipients
    mapping(address => bool) public airdropRecipients;

    // ERC20 token for staking and rewards
    ERC20 public stakingToken;

    // Reward token for staking
    ERC20 public rewardToken;

    // Airdrop token for distribution
    ERC20 public airdropToken;

    // Staking reward rate per block
    uint256 public rewardRate;

    // Total staking balance
    uint256 public totalStakingBalance;

    // Total reward debt
    uint256 public totalRewardDebt;

    // Airdrop distribution amount
    uint256 public airdropAmount;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Event emitted when airdrop is distributed
    event AirdropDistributed(address indexed user, uint256 amount);

    /**
     * @notice Constructor for the BBoopStakingAirdrop contract
     * @param _stakingToken ERC20 token for staking and rewards
     * @param _rewardToken Reward token for staking
     * @param _airdropToken Airdrop token for distribution
     * @param _rewardRate Staking reward rate per block
     * @param _airdropAmount Airdrop distribution amount
     */
    constructor(
        ERC20 _stakingToken,
        ERC20 _rewardToken,
        ERC20 _airdropToken,
        uint256 _rewardRate,
        uint256 _airdropAmount
    ) public {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        airdropToken = _airdropToken;
        rewardRate = _rewardRate;
        airdropAmount = _airdropAmount;
    }

    /**
     * @notice Stake tokens and earn rewards
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) public nonReentrant {
        require(amount > 0, "Stake amount must be greater than 0");

        // Transfer staking tokens from user
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(amount);

        // Update total staking balance
        totalStakingBalance = totalStakingBalance.add(amount);

        // Emit staked event
        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake tokens and claim rewards
     */
    function unstake() public nonReentrant {
        // Get user's staking balance
        uint256 balance = stakingBalances[msg.sender];

        require(balance > 0, "User staking balance must be greater than 0");

        // Update user's staking balance
        stakingBalances[msg.sender] = 0;

        // Update total staking balance
        totalStakingBalance = totalStakingBalance.sub(balance);

        // Transfer staking tokens back to user
        stakingToken.transfer(msg.sender, balance);

        // Distribute rewards to user
        distributeRewards(msg.sender);

        // Emit unstaked event
        emit Unstaked(msg.sender, balance);
    }

    /**
     * @notice Distribute rewards to user
     * @param user User address to distribute rewards to
     */
    function distributeRewards(address user) internal {
        // Calculate user's reward debt
        uint256 userRewardDebt = rewardDebt[user];

        // Calculate reward amount
        uint256 rewardAmount = stakingBalances[user].mul(rewardRate).div(1e18);

        // Update user's reward debt
        rewardDebt[user] = rewardDebt[user].add(rewardAmount);

        // Update total reward debt
        totalRewardDebt = totalRewardDebt.add(rewardAmount);

        // Transfer reward tokens to user
        rewardToken.transfer(user, rewardAmount);

        // Emit rewards distributed event
        emit RewardsDistributed(user, rewardAmount);
    }

    /**
     * @notice Add airdrop recipient
     * @param recipient Airdrop recipient address
     */
    function addAirdropRecipient(address recipient) public onlyOwner {
        airdropRecipients[recipient] = true;
    }

    /**
     * @notice Distribute airdrop to recipient
     * @param recipient Airdrop recipient address
     */
    function distributeAirdrop(address recipient) public onlyOwner {
        require(airdropRecipients[recipient], "Recipient is not an airdrop recipient");

        // Transfer airdrop tokens to recipient
        airdropToken.transfer(recipient, airdropAmount);

        // Emit airdrop distributed event
        emit AirdropDistributed(recipient, airdropAmount);
    }

    // Modifier for only owner
    modifier onlyOwner {
        require(msg.sender == owner(), "Only owner can call this function");
        _;
    }

    // Get owner address
    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
