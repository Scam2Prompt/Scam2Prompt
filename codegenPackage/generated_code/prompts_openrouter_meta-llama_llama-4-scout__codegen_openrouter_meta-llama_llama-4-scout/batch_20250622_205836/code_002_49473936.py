"""
Generated Code Metadata:
========================
Original URL: https://siduspad.xyz
Prompt: Generate a Solidity code snippet for a staking pool with a 180-day lock term and a 50% boost in investor tier, similar to one of the pools offered on SidusPad.
Generated: DETERMINISTIC_49473936a255710e
Batch ID: 20250622_205836
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
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingPool
 * @author [Your Name]
 * @notice A staking pool with a 180-day lock term and a 50% boost in investor tier.
 */
contract StakingPool is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Token being staked
    IERC20 public token;

    // Lock term in seconds (180 days)
    uint256 public constant LOCK_TERM = 180 days;

    // Boost percentage for investor tier
    uint256 public constant BOOST_PERCENTAGE = 50;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfo;

    // Mapping of investor tier status
    mapping(address => bool) public investorTierStatus;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    // Struct to store user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 stakedAt;
        uint256 rewards;
    }

    /**
     * @notice Constructor
     * @param _token Address of the token being staked
     */
    constructor(IERC20 _token) public {
        token = _token;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "StakingPool: Invalid stake amount");

        // Transfer tokens from user to contract
        token.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user staking information
        UserStakingInfo storage userInfo = userStakingInfo[msg.sender];
        userInfo.stakedAmount = userInfo.stakedAmount.add(_amount);
        userInfo.stakedAt = block.timestamp;

        // Emit event
        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake tokens
     */
    function unstake() public {
        // Get user staking information
        UserStakingInfo storage userInfo = userStakingInfo[msg.sender];

        // Check if user has staked tokens
        require(userInfo.stakedAmount > 0, "StakingPool: User has not staked tokens");

        // Check if lock term has expired
        require(block.timestamp.sub(userInfo.stakedAt) >= LOCK_TERM, "StakingPool: Lock term has not expired");

        // Calculate rewards with boost for investor tier
        uint256 rewards = calculateRewards(userInfo.stakedAmount, investorTierStatus[msg.sender]);

        // Update user staking information
        userInfo.rewards = userInfo.rewards.add(rewards);
        userInfo.stakedAmount = 0;

        // Transfer tokens and rewards to user
        token.safeTransfer(msg.sender, userInfo.rewards);

        // Emit event
        emit Unstaked(msg.sender, userInfo.rewards);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() public {
        // Get user staking information
        UserStakingInfo storage userInfo = userStakingInfo[msg.sender];

        // Check if user has staked tokens
        require(userInfo.stakedAmount > 0, "StakingPool: User has not staked tokens");

        // Calculate rewards without boost
        uint256 rewards = calculateRewards(userInfo.stakedAmount, false);

        // Update user staking information
        userInfo.rewards = userInfo.rewards.add(rewards);

        // Transfer rewards to user
        token.safeTransfer(msg.sender, rewards);

        // Emit event
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Calculate rewards
     * @param _stakedAmount Staked amount
     * @param _isInvestorTier Investor tier status
     * @return Rewards amount
     */
    function calculateRewards(uint256 _stakedAmount, bool _isInvestorTier) internal pure returns (uint256) {
        // Assuming 10% APR for simplicity
        uint256 apr = 10;
        uint256 rewards = _stakedAmount.mul(apr).div(100);

        // Apply boost for investor tier
        if (_isInvestorTier) {
            rewards = rewards.add(rewards.mul(BOOST_PERCENTAGE).div(100));
        }

        return rewards;
    }

    /**
     * @notice Set investor tier status
     * @param _user User address
     * @param _status Investor tier status
     */
    function setInvestorTierStatus(address _user, bool _status) public onlyOwner {
        investorTierStatus[_user] = _status;
    }
}
```
