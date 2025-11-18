"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etfswap-in.pages.dev
Prompt: Develop a mechanism in Solidity to calculate and distribute passive income rewards for $ETFS token staking, as described in ETFSwap's staking pool system.
Generated: DETERMINISTIC_593e51d34c45d204
Batch ID: 20250612_153401
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

// Importing the ERC20 interface for interacting with the $ETFS token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ETFSStakingPool is Ownable {
    // State variable to track the $ETFS token
    IERC20 public etfsToken;

    // Struct to represent each staker's details
    struct Staker {
        uint256 amountStaked;  // Amount of $ETFS tokens staked
        uint256 rewardDebt;     // Rewards already claimed
        uint256 lastUpdate;     // Last time rewards were calculated
    }

    // Mapping of staker address to their details
    mapping(address => Staker) public stakers;

    // Total amount of tokens staked in the pool
    uint256 public totalStaked;

    // Total rewards accrued in the pool
    uint256 public totalRewards;

    // Reward per token staked per block
    uint256 public rewardPerTokenStored;

    // Event for when rewards are distributed
    event RewardsDistributed(address indexed staker, uint256 reward);

    // Event for when a user stakes tokens
    event Staked(address indexed staker, uint256 amount);

    // Event for when a user unstakes tokens
    event Unstaked(address indexed staker, uint256 amount);

    // Constructor to initialize the contract with the $ETFS token address
    constructor(address _etfsToken) {
        require(_etfsToken != address(0), "Invalid token address");
        etfsToken = IERC20(_etfsToken);
    }

    // Modifier to update rewards for a staker
    modifier updateRewards(address _staker) {
        if (totalStaked > 0) {
            rewardPerTokenStored = calculateRewardPerToken();
        }
        if (stakers[_staker].amountStaked > 0) {
            uint256 pendingReward = pendingRewards(_staker);
            stakers[_staker].rewardDebt += pendingReward;
        }
        stakers[_staker].lastUpdate = block.timestamp;
        _;
    }

    // Function to calculate reward per token staked
    function calculateRewardPerToken() internal view returns (uint256) {
        if (totalStaked == 0) return rewardPerTokenStored;
        return rewardPerTokenStored + (totalRewards * 1e18 / totalStaked);
    }

    // Function to calculate pending rewards for a staker
    function pendingRewards(address _staker) public view returns (uint256) {
        Staker memory staker = stakers[_staker];
        uint256 updatedRewardPerToken = calculateRewardPerToken();
        return (staker.amountStaked * (updatedRewardPerToken - staker.rewardDebt)) / 1e18;
    }

    // Function to stake $ETFS tokens
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Cannot stake 0");
        etfsToken.transferFrom(msg.sender, address(this), _amount);
        
        stakers[msg.sender].amountStaked += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake $ETFS tokens and claim rewards
    function unstake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Cannot unstake 0");
        require(stakers[msg.sender].amountStaked >= _amount, "Insufficient balance to unstake");

        // Transfer unstaked amount back to the user
        stakers[msg.sender].amountStaked -= _amount;
        totalStaked -= _amount;
        etfsToken.transfer(msg.sender, _amount);

        // Distribute rewards
        uint256 reward = pendingRewards(msg.sender);
        if (reward > 0) {
            totalRewards -= reward;
            etfsToken.transfer(msg.sender, reward);
            emit RewardsDistributed(msg.sender, reward);
        }

        emit Unstaked(msg.sender, _amount);
    }

    // Function to deposit rewards into the staking pool
    function depositRewards(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Must deposit more than 0");
        totalRewards += _amount;
        etfsToken.transferFrom(msg.sender, address(this), _amount);
    }

    // Function to view total staked tokens
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    // Function to view a specific staker's information
    function getStakerInfo(address _staker) external view returns (uint256 stakedAmount, uint256 pendingReward) {
        Staker memory staker = stakers[_staker];
        return (staker.amountStaked, pendingRewards(_staker));
    }
}
```
