"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allianceblock-ahz.pages.dev
Prompt: Write a smart contract in Solidity for a decentralized token sale platform that incorporates staking NXRA tokens to earn reward tokens (rALBT) and provides access to private sale token deals, as described on the AllianceBlock Fundrs platform.
Generated: DETERMINISTIC_fd1f9cddec65e90d
Batch ID: 20250612_152739
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

// Importing OpenZeppelin Contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the reward token (rALBT)
interface IRewardToken is IERC20 {
    function mint(address to, uint256 amount) external;
}

// TokenSale contract for managing the token sale and staking
contract TokenSale is Ownable {
    // State variables
    IERC20 public nxraToken; // The NXRA token
    IRewardToken public rewardToken; // The reward token (rALBT)
    
    // Staking structure to hold user information
    struct Stake {
        uint256 amount; // Amount of NXRA staked
        uint256 rewardDebt; // Reward debt for the staker
    }

    mapping(address => Stake) public stakes; // Mapping of user stakes
    uint256 public totalStaked; // Total NXRA tokens staked
    uint256 public constant REWARD_PER_BLOCK = 10 * 10**18; // Example reward rate per block
    uint256 public lastRewardBlock; // Last block that rewards were calculated

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with NXRA and reward token addresses
    constructor(IERC20 _nxraToken, IRewardToken _rewardToken) {
        nxraToken = _nxraToken;
        rewardToken = _rewardToken;
        lastRewardBlock = block.number; // Set the last reward block to the current block
    }

    // Modifier to update rewards before any staking function
    modifier updateRewards() {
        // Update rewards for all stakers
        if (totalStaked > 0) {
            uint256 multiplier = block.number - lastRewardBlock; // Calculate the number of blocks since last update
            uint256 reward = multiplier * REWARD_PER_BLOCK; // Calculate total rewards
            rewardToken.mint(address(this), reward); // Mint new rewards to the contract
        }
        lastRewardBlock = block.number; // Update last reward block
        _; // Continue with the function execution
    }

    // Function to stake NXRA tokens
    function stake(uint256 _amount) external updateRewards {
        require(_amount > 0, "Amount must be greater than zero");
        nxraToken.transferFrom(msg.sender, address(this), _amount); // Transfer NXRA tokens to the contract

        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount; // Update user's stake amount
        totalStaked += _amount; // Update total staked amount

        emit Staked(msg.sender, _amount); // Emit Staked event
    }

    // Function to claim rewards based on staking
    function claimRewards() external updateRewards {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens");

        uint256 pendingReward = (userStake.amount * REWARD_PER_BLOCK) / totalStaked; // Calculate pending rewards
        userStake.rewardDebt += pendingReward; // Update reward debt
        
        rewardToken.mint(msg.sender, pendingReward); // Mint rewards to user
        emit RewardClaimed(msg.sender, pendingReward); // Emit RewardClaimed event
    }

    // Function to unstake NXRA tokens
    function unstake(uint256 _amount) external updateRewards {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        userStake.amount -= _amount; // Decrease user's staked amount
        totalStaked -= _amount; // Decrease total staked amount
        nxraToken.transfer(msg.sender, _amount); // Transfer NXRA tokens back to the user

        emit Unstaked(msg.sender, _amount); // Emit Unstaked event
    }

    // Function to view user's staked amount
    function viewStake(address _user) external view returns (uint256) {
        return stakes[_user].amount; // Return the amount of NXRA staked by the user
    }
}
```
