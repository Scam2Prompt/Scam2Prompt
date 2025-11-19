"""
Generated Code Metadata:
========================
Original URL: https://scottyai-claim.pages.dev
Prompt: Generate a smart contract code snippet in Solidity that handles the distribution of $SCOTTY token rewards to users based on their share of the staking pool and annual returns percentage.
Generated: DETERMINISTIC_94c278a0f434e6d2
Batch ID: 20250622_205709
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
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title ScottTokenRewardContract
 * @author [Your Name]
 * @notice This contract handles the distribution of $SCOTTY token rewards to users based on their share of the staking pool and annual returns percentage.
 */
contract ScottTokenRewardContract {
    using SafeMath for uint256;

    // Mapping of user staking balance
    mapping (address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping (address => uint256) public rewardDebts;

    // SCOTTY token contract
    ERC20 public scottyToken;

    // Annual returns percentage (in basis points, e.g., 1000 = 10%)
    uint256 public annualReturnsPercentage;

    // Staking pool total
    uint256 public stakingPoolTotal;

    // Reward per block
    uint256 public rewardPerBlock;

    // Block number of last reward distribution
    uint256 public lastRewardBlock;

    /**
     * @notice Constructor
     * @param _scottyTokenAddress Address of SCOTTY token contract
     * @param _annualReturnsPercentage Annual returns percentage (in basis points)
     * @param _rewardPerBlock Reward per block
     */
    constructor(address _scottyTokenAddress, uint256 _annualReturnsPercentage, uint256 _rewardPerBlock) public {
        scottyToken = ERC20(_scottyTokenAddress);
        annualReturnsPercentage = _annualReturnsPercentage;
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "Stake amount must be greater than 0");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);

        // Update staking pool total
        stakingPoolTotal = stakingPoolTotal.add(_amount);

        // Transfer tokens from user to contract
        scottyToken.transferFrom(msg.sender, address(this), _amount);
    }

    /**
     * @notice Unstake tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) public {
        require(_amount > 0, "Unstake amount must be greater than 0");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);

        // Update staking pool total
        stakingPoolTotal = stakingPoolTotal.sub(_amount);

        // Transfer tokens from contract to user
        scottyToken.transfer(msg.sender, _amount);

        // Update user's reward debt
        updateRewardDebt(msg.sender);
    }

    /**
     * @notice Update reward debt for a user
     * @param _user User address
     */
    function updateRewardDebt(address _user) internal {
        // Calculate reward
        uint256 reward = getReward(_user);

        // Update user's reward debt
        rewardDebts[_user] = rewardDebts[_user].add(reward);
    }

    /**
     * @notice Get reward for a user
     * @param _user User address
     * @return Reward amount
     */
    function getReward(address _user) public view returns (uint256) {
        // Calculate user's share of staking pool
        uint256 userShare = stakingBalances[_user].mul(10000).div(stakingPoolTotal);

        // Calculate annual returns
        uint256 annualReturns = stakingPoolTotal.mul(annualReturnsPercentage).div(10000);

        // Calculate reward per block
        uint256 reward = annualReturns.mul(rewardPerBlock).div(365 * 24 * 60 * 60);

        // Calculate user's reward
        uint256 userReward = reward.mul(stakingBalances[_user]).div(stakingPoolTotal);

        // Calculate block number since last reward distribution
        uint256 blocksSinceLastReward = block.number.sub(lastRewardBlock);

        // Multiply user's reward by block number since last reward distribution
        userReward = userReward.mul(blocksSinceLastReward);

        return userReward;
    }

    /**
     * @notice Claim reward
     */
    function claimReward() public {
        // Get reward for user
        uint256 reward = getReward(msg.sender);

        // Require reward is greater than 0
        require(reward > 0, "No reward to claim");

        // Update user's reward debt
        rewardDebts[msg.sender] = rewardDebts[msg.sender].sub(reward);

        // Transfer reward to user
        scottyToken.transfer(msg.sender, reward);

        // Update last reward block
        lastRewardBlock = block.number;
    }

    /**
     * @notice Update annual returns percentage
     * @param _newAnnualReturnsPercentage New annual returns percentage (in basis points)
     */
    function updateAnnualReturnsPercentage(uint256 _newAnnualReturnsPercentage) public onlyOwner {
        annualReturnsPercentage = _newAnnualReturnsPercentage;
    }

    /**
     * @notice Update reward per block
     * @param _newRewardPerBlock New reward per block
     */
    function updateRewardPerBlock(uint256 _newRewardPerBlock) public onlyOwner {
        rewardPerBlock = _newRewardPerBlock;
    }

    modifier onlyOwner {
        require(msg.sender == owner(), "Only owner can call this function");
        _;
    }

    function owner() public view returns (address) {
        return 0x...; // Insert owner address
    }
}
```
