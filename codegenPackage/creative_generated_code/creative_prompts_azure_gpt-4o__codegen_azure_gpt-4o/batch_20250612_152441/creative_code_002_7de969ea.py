"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthr-verification.pages.dev
Prompt: Create a smart contract example for staking SYNTH tokens to earn veSYNTH and access boosted syASSET/ASSET LP farming rewards.
Generated: DETERMINISTIC_7de969ea6a10b7c4
Batch ID: 20250612_152441
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

/**
 * @title SYNTH Token Staking Smart Contract
 * @notice This contract allows users to stake SYNTH tokens to earn veSYNTH and access boosted LP farming rewards.
 */
contract SYNTHStaking {
    // State variables
    IERC20 public immutable synthToken; // SYNTH token interface
    IERC20 public immutable veSynthToken; // veSYNTH token interface
    address public owner; // Contract owner
    
    uint256 public totalStaked; // Total SYNTH tokens staked
    uint256 public rewardRate = 1e18; // Reward rate (veSYNTH per SYNTH staked per block)

    struct Stake {
        uint256 amount; // Amount of SYNTH tokens staked
        uint256 rewardDebt; // veSYNTH rewards debt
    }

    mapping(address => Stake) public stakes; // Tracks staking details per user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier updateRewards(address _user) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount > 0) {
            uint256 pendingReward = ((userStake.amount * rewardRate) * (block.number - userStake.rewardDebt)) / 1e18;
            veSynthToken.transfer(_user, pendingReward);
            emit RewardClaimed(_user, pendingReward);
        }
        userStake.rewardDebt = block.number;
        _;
    }

    // Constructor
    constructor(address _synthToken, address _veSynthToken) {
        require(_synthToken != address(0) && _veSynthToken != address(0), "Invalid token addresses");
        synthToken = IERC20(_synthToken);
        veSynthToken = IERC20(_veSynthToken);
        owner = msg.sender;
    }

    /**
     * @notice Stake SYNTH tokens to earn veSYNTH rewards
     * @param _amount Amount of SYNTH tokens to stake
     */
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Cannot stake zero tokens");
        synthToken.transferFrom(msg.sender, address(this), _amount); // Transfer SYNTH to contract

        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount; // Update staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Withdraw staked SYNTH tokens
     * @param _amount Amount of SYNTH tokens to withdraw
     */
    function withdraw(uint256 _amount) external updateRewards(msg.sender) {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        userStake.amount -= _amount; // Update staked amount
        totalStaked -= _amount;

        synthToken.transfer(msg.sender, _amount); // Transfer SYNTH back to user

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @notice Claim accumulated veSYNTH rewards
     */
    function claimRewards() external updateRewards(msg.sender) {
        // Rewards are automatically updated and transferred in the modifier
    }

    /**
     * @notice Update the reward rate (only owner)
     * @param _newRewardRate New reward rate (veSYNTH per SYNTH staked per block)
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;
    }
}

// Minimal IERC20 interface for token interactions
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
