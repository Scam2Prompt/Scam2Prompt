"""
Generated Code Metadata:
========================
Original URL: https://popofrog-io.web.app
Prompt: Write a smart contract in Solidity for a multichain token similar to $FROP, ensuring transparency and security through auditability. Include staking functionality with two pools: one with locked schedules and one with flexible withdrawal options.
Generated: DETERMINISTIC_029607243c3f5fb1
Batch ID: 20250612_145625
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
 * @title MultichainToken
 * @author [Your Name]
 * @notice A multichain token with staking functionality
 */
contract MultichainToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of stakers and their stakes
    mapping(address => Staker) public stakers;

    // Mapping of stake pools
    mapping(uint256 => StakePool) public stakePools;

    // Total staked amount
    uint256 public totalStaked;

    // Number of stake pools
    uint256 public numStakePools;

    // Events
    event Staked(address indexed staker, uint256 amount, uint256 poolId);
    event Unstaked(address indexed staker, uint256 amount, uint256 poolId);
    event StakePoolAdded(uint256 poolId, uint256 lockDuration, bool flexible);

    // Struct for staker
    struct Staker {
        uint256[] stakeIds;
    }

    // Struct for stake pool
    struct StakePool {
        uint256 id;
        uint256 lockDuration; // Lock duration in seconds
        bool flexible; // Flexible withdrawal option
        uint256 totalLocked; // Total locked amount
    }

    // Constructor
    constructor() ERC20("MultichainToken", "MCT") {
        // Initialize stake pools
        stakePools[1] = StakePool(1, 30 days, false); // Locked for 30 days
        stakePools[2] = StakePool(2, 0, true); // Flexible withdrawal

        numStakePools = 2;

        // Emit event for initial stake pools
        emit StakePoolAdded(1, 30 days, false);
        emit StakePoolAdded(2, 0, true);
    }

    // Function to add stake pool
    function addStakePool(uint256 lockDuration, bool flexible) public onlyOwner {
        numStakePools++;
        stakePools[numStakePools] = StakePool(numStakePools, lockDuration, flexible);

        emit StakePoolAdded(numStakePools, lockDuration, flexible);
    }

    // Function to stake
    function stake(uint256 amount, uint256 poolId) public {
        require(amount > 0, "Invalid stake amount");
        require(stakePools[poolId].id != 0, "Invalid stake pool");

        // Transfer tokens from staker to contract
        _transfer(msg.sender, address(this), amount);

        // Update staker info
        stakers[msg.sender].stakeIds.push(poolId);

        // Update stake pool info
        stakePools[poolId].totalLocked = stakePools[poolId].totalLocked.add(amount);

        // Update total staked amount
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount, poolId);
    }

    // Function to unstake
    function unstake(uint256 amount, uint256 poolId) public {
        require(amount > 0, "Invalid unstake amount");
        require(stakePools[poolId].id != 0, "Invalid stake pool");

        // Check if staker has stake in pool
        bool hasStake = false;
        for (uint256 i = 0; i < stakers[msg.sender].stakeIds.length; i++) {
            if (stakers[msg.sender].stakeIds[i] == poolId) {
                hasStake = true;
                break;
            }
        }
        require(hasStake, "Staker does not have stake in pool");

        // Check if pool is flexible or lock duration has passed
        if (!stakePools[poolId].flexible) {
            require(block.timestamp >= stakePools[poolId].lockDuration, "Lock duration not passed");
        }

        // Update stake pool info
        stakePools[poolId].totalLocked = stakePools[poolId].totalLocked.sub(amount);

        // Update total staked amount
        totalStaked = totalStaked.sub(amount);

        // Transfer tokens from contract to staker
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount, poolId);
    }

    // Function to get stake pool info
    function getStakePoolInfo(uint256 poolId) public view returns (uint256, uint256, bool) {
        return (stakePools[poolId].id, stakePools[poolId].lockDuration, stakePools[poolId].flexible);
    }

    // Function to get staker info
    function getStakerInfo(address staker) public view returns (uint256[] memory) {
        return stakers[staker].stakeIds;
    }
}
```
