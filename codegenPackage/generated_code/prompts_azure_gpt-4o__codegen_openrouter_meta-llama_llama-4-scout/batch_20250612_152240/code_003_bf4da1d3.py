"""
Generated Code Metadata:
========================
Original URL: https://bafybeifcqszleetvbrbaat5ml47lgiktzvmlat4jk765lrsycgk44bifpq.ipfs.dweb.link
Prompt: Write a Solidity smart contract function to stake MOE tokens on the Merchant Moe platform and earn rewards. Include logic for voting on farm emissions.
Generated: DETERMINISTIC_bf4da1d3b227bfdc
Batch ID: 20250612_152240
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MerchantMoeStakingContract
 * @author [Your Name]
 * @notice This contract allows users to stake MOE tokens and earn rewards.
 *         It also includes logic for voting on farm emissions.
 */
contract MerchantMoeStakingContract is Ownable {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward balances
    mapping(address => uint256) public rewardBalances;

    // Mapping of user voting power
    mapping(address => uint256) public votingPower;

    // Total staking balance
    uint256 public totalStakingBalance;

    // MOE token contract
    IERC20 public moeToken;

    // Reward token contract
    IERC20 public rewardToken;

    // Farm emissions voting
    mapping(address => uint256) public farmEmissionsVotes;

    // Total farm emissions votes
    uint256 public totalFarmEmissionsVotes;

    // Event emitted when user stakes MOE tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes MOE tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    // Event emitted when user votes on farm emissions
    event FarmEmissionsVoted(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _moeToken MOE token contract address
     * @param _rewardToken Reward token contract address
     */
    constructor(address _moeToken, address _rewardToken) public {
        require(_moeToken != address(0), "MOE token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");

        moeToken = IERC20(_moeToken);
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @notice Stake MOE tokens
     * @param _amount Amount of MOE tokens to stake
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(moeToken.balanceOf(msg.sender) >= _amount, "Insufficient MOE token balance");

        // Transfer MOE tokens from user to contract
        moeToken.transferFrom(msg.sender, address(this), _amount);

        // Update staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStakingBalance = totalStakingBalance.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake MOE tokens
     * @param _amount Amount of MOE tokens to unstake
     */
    function unstake(uint256 _amount) public {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStakingBalance = totalStakingBalance.sub(_amount);

        // Transfer MOE tokens from contract to user
        moeToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() public {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update reward balance
        rewardBalances[msg.sender] = 0;

        // Transfer reward tokens from contract to user
        rewardToken.transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @notice Vote on farm emissions
     * @param _amount Amount of votes to cast
     */
    function voteOnFarmEmissions(uint256 _amount) public {
        require(_amount > 0, "Vote amount must be greater than zero");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update voting power
        votingPower[msg.sender] = votingPower[msg.sender].add(_amount);

        // Update farm emissions votes
        farmEmissionsVotes[msg.sender] = farmEmissionsVotes[msg.sender].add(_amount);
        totalFarmEmissionsVotes = totalFarmEmissionsVotes.add(_amount);

        emit FarmEmissionsVoted(msg.sender, _amount);
    }

    /**
     * @notice Calculate reward for user
     * @param _user User address
     * @return Reward amount
     */
    function calculateReward(address _user) internal view returns (uint256) {
        // Implement reward calculation logic here
        // For demonstration purposes, return a fixed reward
        return 100;
    }
}
```
