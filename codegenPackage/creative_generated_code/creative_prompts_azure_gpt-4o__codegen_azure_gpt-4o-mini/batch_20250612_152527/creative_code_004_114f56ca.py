"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakestone-protocalrpc.pages.dev
Prompt: Write a Solidity contract that supports StakeStone's "multi-underlying asset compatibility" feature, allowing staking pools and retaking protocols to be integrated.
Generated: DETERMINISTIC_114f56caf64b38cd
Batch ID: 20250612_152527
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

/**
 * @title MultiAssetStaking
 * @dev A staking contract that supports multiple underlying assets for staking pools.
 */
contract MultiAssetStaking is Ownable {
    // Structure for storing information about each staking pool
    struct Pool {
        IERC20 asset; // The token that can be staked
        uint256 totalStaked; // Total amount of tokens staked in the pool
        mapping(address => uint256) stakedAmount; // User's staked amount per address
    }

    // Mapping from pool index to Pool structure
    mapping(uint256 => Pool) public pools;
    uint256 public poolCount;

    // Events for staking and unstaking actions
    event Staked(uint256 indexed poolId, address indexed user, uint256 amount);
    event Unstaked(uint256 indexed poolId, address indexed user, uint256 amount);

    /**
     * @dev Create a new staking pool.
     * @param _asset Address of the ERC20 token to be used in this pool.
     */
    function createPool(IERC20 _asset) external onlyOwner {
        require(address(_asset) != address(0), "Invalid asset address");
        
        pools[poolCount] = Pool({
            asset: _asset,
            totalStaked: 0
        });
        poolCount++;
    }

    /**
     * @dev Stake tokens in a specified pool.
     * @param _poolId The ID of the pool to stake in.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _poolId, uint256 _amount) external {
        require(_poolId < poolCount, "Pool does not exist");
        require(_amount > 0, "Amount must be greater than zero");
        
        Pool storage pool = pools[_poolId];

        // Transfer tokens from user to the contract
        pool.asset.transferFrom(msg.sender, address(this), _amount);
        
        // Update staking information
        pool.stakedAmount[msg.sender] += _amount;
        pool.totalStaked += _amount;

        emit Staked(_poolId, msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens from a specified pool.
     * @param _poolId The ID of the pool to unstake from.
     * @param _amount The amount of tokens to unstake.
     */
    function unstake(uint256 _poolId, uint256 _amount) external {
        require(_poolId < poolCount, "Pool does not exist");
        require(_amount > 0, "Amount must be greater than zero");
        
        Pool storage pool = pools[_poolId];

        // Ensure the user has enough staked tokens to unstake
        require(pool.stakedAmount[msg.sender] >= _amount, "Insufficient staked amount");

        // Update staking information
        pool.stakedAmount[msg.sender] -= _amount;
        pool.totalStaked -= _amount;

        // Transfer tokens back to user
        pool.asset.transfer(msg.sender, _amount);

        emit Unstaked(_poolId, msg.sender, _amount);
    }

    /**
     * @dev Get the staked amount of a user in a specified pool.
     * @param _poolId The ID of the pool.
     * @param _user The address of the user.
     * @return The amount staked by the user in the specified pool.
     */
    function getStakedAmount(uint256 _poolId, address _user) external view returns (uint256) {
        require(_poolId < poolCount, "Pool does not exist");
        return pools[_poolId].stakedAmount[_user];
    }
}
```
