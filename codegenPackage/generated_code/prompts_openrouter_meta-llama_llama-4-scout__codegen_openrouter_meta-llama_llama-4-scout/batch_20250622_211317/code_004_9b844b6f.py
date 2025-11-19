"""
Generated Code Metadata:
========================
Original URL: https://nteai.icu
Prompt: "Design a basic staking smart contract for Ethereum 2.0 using Solidity, focusing on security considerations."
Generated: DETERMINISTIC_9b844b6f360f9c31
Batch ID: 20250622_211317
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Staking Contract for Ethereum 2.0
 * @author [Your Name]
 * @notice This contract allows users to stake their ETH and earn rewards.
 * @dev This contract is designed with security considerations in mind.
 */
contract StakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of staker addresses to their staking information
    mapping (address => Staker) public stakers;

    // Mapping of validator indices to their staking information
    mapping (uint256 => Validator) public validators;

    // Total staked amount
    uint256 public totalStaked;

    // Staking reward per block
    uint256 public rewardPerBlock;

    // Address of the reward token (ETH in this case)
    address public rewardToken;

    // Event emitted when a user stakes
    event Staked(address indexed staker, uint256 amount);

    // Event emitted when a user unstakes
    event Unstaked(address indexed staker, uint256 amount);

    // Event emitted when a reward is claimed
    event RewardClaimed(address indexed staker, uint256 amount);

    /**
     * @dev Constructor function
     * @param _rewardPerBlock The staking reward per block
     */
    constructor(uint256 _rewardPerBlock) public {
        rewardPerBlock = _rewardPerBlock;
        rewardToken = 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2; // ETH
    }

    /**
     * @dev Stakes a certain amount of ETH
     * @param _amount The amount to stake
     */
    function stake(uint256 _amount) public payable nonReentrant {
        require(_amount > 0, "Staking amount must be greater than 0");

        // Check if the staker already exists
        if (stakers[msg.sender].exists) {
            // Update the staker's information
            stakers[msg.sender].amount = stakers[msg.sender].amount.add(_amount);
            stakers[msg.sender].lastClaimedBlock = block.number;
        } else {
            // Create a new staker
            stakers[msg.sender] = Staker(_amount, block.number, true);
        }

        // Update the total staked amount
        totalStaked = totalStaked.add(_amount);

        // Emit the Staked event
        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstakes a certain amount of ETH
     * @param _amount The amount to unstake
     */
    function unstake(uint256 _amount) public nonReentrant {
        require(_amount > 0, "Unstaking amount must be greater than 0");
        require(stakers[msg.sender].exists, "Staker does not exist");
        require(stakers[msg.sender].amount >= _amount, "Unstaking amount exceeds staked amount");

        // Update the staker's information
        stakers[msg.sender].amount = stakers[msg.sender].amount.sub(_amount);

        // Update the total staked amount
        totalStaked = totalStaked.sub(_amount);

        // Emit the Unstaked event
        emit Unstaked(msg.sender, _amount);

        // Transfer the unstaked amount to the staker
        payable(msg.sender).transfer(_amount);
    }

    /**
     * @dev Claims the staking reward
     */
    function claimReward() public nonReentrant {
        require(stakers[msg.sender].exists, "Staker does not exist");

        // Calculate the reward
        uint256 reward = calculateReward(msg.sender);

        // Update the staker's last claimed block
        stakers[msg.sender].lastClaimedBlock = block.number;

        // Emit the RewardClaimed event
        emit RewardClaimed(msg.sender, reward);

        // Transfer the reward to the staker
        IERC20(rewardToken).transfer(msg.sender, reward);
    }

    /**
     * @dev Calculates the staking reward for a staker
     * @param _staker The address of the staker
     * @return The staking reward
     */
    function calculateReward(address _staker) internal view returns (uint256) {
        uint256 blocksElapsed = block.number.sub(stakers[_staker].lastClaimedBlock);
        uint256 reward = blocksElapsed.mul(rewardPerBlock).mul(stakers[_staker].amount);
        return reward;
    }

    /**
     * @dev Struct representing a staker
     */
    struct Staker {
        uint256 amount;
        uint256 lastClaimedBlock;
        bool exists;
    }

    /**
     * @dev Struct representing a validator
     */
    struct Validator {
        uint256 index;
        // Additional validator information can be added here
    }
}
```
