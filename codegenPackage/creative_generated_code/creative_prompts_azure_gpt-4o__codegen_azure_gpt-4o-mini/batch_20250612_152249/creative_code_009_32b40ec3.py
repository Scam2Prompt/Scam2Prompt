"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabotaentnet.pages.dev
Prompt: Create a Solidity contract to support Zushi farming, allowing users to deposit $ZUSHI tokens and earn rewards based on the staking pool allocation.
Generated: DETERMINISTIC_32b40ec347f27506
Batch ID: 20250612_152249
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

// Importing the IERC20 interface for token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ZushiFarming
 * @dev A contract for Zushi farming where users can stake their $ZUSHI tokens and earn rewards.
 */
contract ZushiFarming is Ownable {
    // Struct to store user information for staking
    struct UserInfo {
        uint256 amount; // Amount of $ZUSHI tokens staked by the user
        uint256 rewardDebt; // Reward debt, used for calculating pending rewards
    }

    // The $ZUSHI token contract address
    IERC20 public zushiToken;

    // Total amount of $ZUSHI tokens staked
    uint256 public totalStaked;

    // Reward per token per block
    uint256 public rewardPerBlock;

    // Mapping to track user information
    mapping(address => UserInfo) public userInfo;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract with the ZUSHI token address and reward rate.
     * @param _zushiToken Address of the $ZUSHI token contract
     * @param _rewardPerBlock Reward rate per block
     */
    constructor(IERC20 _zushiToken, uint256 _rewardPerBlock) {
        zushiToken = _zushiToken;
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @dev Function to stake $ZUSHI tokens.
     * @param _amount Amount of $ZUSHI tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        
        UserInfo storage user = userInfo[msg.sender];
        
        // Update total staked amount
        totalStaked += _amount;
        
        // Transfer $ZUSHI tokens from user to the contract
        zushiToken.transferFrom(msg.sender, address(this), _amount);
        
        // Update user information
        user.amount += _amount;
        user.rewardDebt = pendingRewards(msg.sender);
        
        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to unstake $ZUSHI tokens and claim rewards.
     * @param _amount Amount of $ZUSHI tokens to unstake
     */
    function unstake(uint256 _amount) external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");

        // Calculate pending rewards and update reward debt
        uint256 pending = pendingRewards(msg.sender);
        user.rewardDebt += pending;
        
        // Update total staked amount
        totalStaked -= _amount;
        
        // Update user information
        user.amount -= _amount;
        
        // Transfer $ZUSHI tokens back to the user
        zushiToken.transfer(msg.sender, _amount);
        
        // Claim rewards if any
        if (pending > 0) {
            _claimRewards(msg.sender, pending);
        }

        emit Unstaked(msg.sender, _amount);
    }
    
    /**
     * @dev View function to calculate pending rewards for a user.
     * @param _user Address of the user
     * @return Pending reward amount
     */
    function pendingRewards(address _user) public view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 pending = (user.amount * rewardPerBlock); // This can be adjusted based on the reward distribution logic
        return pending - user.rewardDebt;
    }

    /**
     * @dev Internal function to handle reward claiming.
     * @param _user Address of the user claiming rewards
     * @param _amount Amount of rewards to claim
     */
    function _claimRewards(address _user, uint256 _amount) internal {
        // In a real scenario, you would transfer rewards here.
        // For now, we just emit an event.
        emit RewardClaimed(_user, _amount);
    }

    /**
     * @dev Function to withdraw any ERC20 tokens mistakenly sent to the contract.
     * @param _token Address of the ERC20 token to withdraw
     * @param _amount Amount to withdraw
     */
    function withdrawToken(IERC20 _token, uint256 _amount) external onlyOwner {
        require(_token.balanceOf(address(this)) >= _amount, "Insufficient balance");
        _token.transfer(owner(), _amount);
    }
}
```
