"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appsmuhdorepositoryhub.pages.dev
Prompt: Generate a smart contract that supports staking DNA tokens in the Genesis Staking Pool, following the MuhdoHub ecosystem requirements.
Generated: DETERMINISTIC_a2dcec7ec3ab3616
Batch ID: 20250612_153712
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title GenesisStakingPool
 * @dev A smart contract for staking DNA tokens in the MuhdoHub ecosystem
 */
contract GenesisStakingPool is Ownable, ReentrancyGuard {
    // The DNA token contract
    IERC20 public dnaToken;

    // Struct to hold staking information
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;
    // Total amount of tokens staked in the pool
    uint256 public totalStaked;
    
    // Events for logging stake and unstake actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the DNA token contract address
     * @param _dnaToken Address of the DNA token contract
     */
    constructor(address _dnaToken) {
        require(_dnaToken != address(0), "Invalid token address");
        dnaToken = IERC20(_dnaToken);
    }

    /**
     * @dev Stake DNA tokens in the Genesis Staking Pool
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Stake amount must be greater than 0");
        require(dnaToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        
        // Transfer tokens from the user to this contract
        dnaToken.transferFrom(msg.sender, address(this), amount);

        // Update user stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;
        
        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake DNA tokens from the Genesis Staking Pool
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");
        
        // Update user stake
        userStake.amount -= amount;
        // Update total staked amount
        totalStaked -= amount;

        // Transfer tokens back to the user
        dnaToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Get the staking balance of a user
     * @param user Address of the user
     * @return Amount of tokens staked by the user
     */
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    /**
     * @dev Get the total amount of tokens staked in the pool
     * @return Total staked amount
     */
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```
