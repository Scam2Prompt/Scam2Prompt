"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://halosocial.vercel.app
Prompt: Write a smart contract for staking $HLO tokens and earning rewards, referencing the staking functionality mentioned on halo.social.
Generated: DETERMINISTIC_b14349ed1e2d3c8e
Batch ID: 20250612_154339
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

// Import the OpenZeppelin Contracts for ERC20 and Ownable functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title HLO Staking Contract
/// @notice This contract allows users to stake $HLO tokens and earn rewards
contract HLOStaking is Ownable {
    // The ERC20 token being staked
    IERC20 public hlToken;

    // Struct to store information about each user's stake
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // The amount of rewards debt
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total amount of $HLO tokens staked in the contract
    uint256 public totalStaked;

    // Reward rate per token staked (in wei)
    uint256 public rewardRate;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Event emitted when a new stake is created
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a stake is withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    /// @param _hlToken Address of the $HLO token contract
    /// @param _rewardRate Initial reward rate per token staked
    constructor(IERC20 _hlToken, uint256 _rewardRate) {
        hlToken = _hlToken;
        rewardRate = _rewardRate;
    }

    /// @notice Allows users to stake $HLO tokens
    /// @param _amount Amount of $HLO tokens to stake
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Transfer tokens from the user to the contract
        hlToken.transferFrom(msg.sender, address(this), _amount);

        // Update the user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;

        // Update total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /// @notice Allows users to withdraw their stake and claim rewards
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate the user's rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Update the user's stake
        totalStaked -= userStake.amount;
        delete stakes[msg.sender];

        // Transfer staked tokens and rewards back to the user
        hlToken.transfer(msg.sender, userStake.amount);
        if (rewards > 0) {
            hlToken.transfer(msg.sender, rewards);
            emit RewardsClaimed(msg.sender, rewards);
        }

        emit Withdrawn(msg.sender, userStake.amount);
    }

    /// @notice Calculate rewards for a user
    /// @param _user The address of the user
    /// @return The calculated rewards
    function calculateRewards(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        return (userStake.amount * rewardRate) - userStake.rewardDebt;
    }

    /// @notice Update the reward rate, can only be called by the owner
    /// @param _newRewardRate New reward rate
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }

    /// @notice Withdraw any tokens accidentally sent to the contract
    /// @param _token Address of the token to withdraw
    /// @param _amount Amount of tokens to withdraw
    function emergencyWithdraw(IERC20 _token, uint256 _amount) external onlyOwner {
        require(_token != hlToken, "Cannot withdraw staked token");
        _token.transfer(msg.sender, _amount);
    }
}
```
