"""
Generated Code Metadata:
========================
Original URL: https://app-pepecoin-io.pages.dev
Prompt: Write a Solidity smart contract for staking PepeCoin and earning BasedAI rewards. Include functionality for farming and bridging as described in the PepeOS staking application.
Generated: DETERMINISTIC_d0b074a009a42d4e
Batch ID: 20250612_145723
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PepeStakingContract
 * @author [Your Name]
 * @notice This contract allows users to stake PepeCoin and earn BasedAI rewards.
 */
contract PepeStakingContract is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Token addresses
    address public pepeCoinAddress;
    address public basedAIAddress;

    // Staking pool structure
    struct StakingPool {
        uint256 totalStaked;
        uint256 totalRewards;
        uint256 rewardRate; // rewards per second
        uint256 lastUpdateTime;
    }

    // User staking information
    struct UserInfo {
        uint256 stakedAmount;
        uint256 rewardDebt;
        uint256 lastUpdateTime;
    }

    // Mapping of staking pools
    mapping(address => StakingPool) public stakingPools;

    // Mapping of user staking information
    mapping(address => mapping(address => UserInfo)) public userInfos;

    // Event emitted when user stakes
    event Stake(address indexed user, address indexed token, uint256 amount);

    // Event emitted when user unstakes
    event Unstake(address indexed user, address indexed token, uint256 amount);

    // Event emitted when rewards are claimed
    event ClaimRewards(address indexed user, address indexed token, uint256 amount);

    /**
     * @notice Constructor
     * @param _pepeCoinAddress PepeCoin token address
     * @param _basedAIAddress BasedAI token address
     */
    constructor(address _pepeCoinAddress, address _basedAIAddress) {
        pepeCoinAddress = _pepeCoinAddress;
        basedAIAddress = _basedAIAddress;

        // Initialize staking pool for PepeCoin
        stakingPools[pepeCoinAddress] = StakingPool(0, 0, 1e18, block.timestamp);
    }

    /**
     * @notice Stake PepeCoin
     * @param amount Amount to stake
     */
    function stake(uint256 amount) public {
        require(amount > 0, "Invalid stake amount");

        IERC20(pepeCoinAddress).safeTransferFrom(msg.sender, address(this), amount);

        StakingPool storage pool = stakingPools[pepeCoinAddress];
        UserInfo storage userInfo = userInfos[msg.sender][pepeCoinAddress];

        pool.totalStaked = pool.totalStaked.add(amount);
        userInfo.stakedAmount = userInfo.stakedAmount.add(amount);

        // Update reward debt
        userInfo.rewardDebt = userInfo.stakedAmount.mul(pool.rewardRate).div(1e18);

        emit Stake(msg.sender, pepeCoinAddress, amount);
    }

    /**
     * @notice Unstake PepeCoin
     * @param amount Amount to unstake
     */
    function unstake(uint256 amount) public {
        require(amount > 0, "Invalid unstake amount");

        UserInfo storage userInfo = userInfos[msg.sender][pepeCoinAddress];
        StakingPool storage pool = stakingPools[pepeCoinAddress];

        require(userInfo.stakedAmount >= amount, "Insufficient staked amount");

        // Update reward debt
        userInfo.rewardDebt = userInfo.stakedAmount.sub(amount).mul(pool.rewardRate).div(1e18);

        userInfo.stakedAmount = userInfo.stakedAmount.sub(amount);
        pool.totalStaked = pool.totalStaked.sub(amount);

        IERC20(pepeCoinAddress).safeTransfer(msg.sender, amount);

        emit Unstake(msg.sender, pepeCoinAddress, amount);
    }

    /**
     * @notice Claim BasedAI rewards
     */
    function claimRewards() public {
        UserInfo storage userInfo = userInfos[msg.sender][pepeCoinAddress];
        StakingPool storage pool = stakingPools[pepeCoinAddress];

        uint256 rewards = userInfo.stakedAmount.mul(pool.rewardRate).div(1e18).sub(userInfo.rewardDebt);

        require(rewards > 0, "No rewards to claim");

        // Update reward debt
        userInfo.rewardDebt = userInfo.stakedAmount.mul(pool.rewardRate).div(1e18);

        IERC20(basedAIAddress).safeTransfer(msg.sender, rewards);

        emit ClaimRewards(msg.sender, pepeCoinAddress, rewards);
    }

    /**
     * @notice Farm BasedAI rewards
     * @param amount Amount to farm
     */
    function farm(uint256 amount) public {
        require(amount > 0, "Invalid farm amount");

        IERC20(basedAIAddress).safeTransferFrom(msg.sender, address(this), amount);

        // Add to staking pool rewards
        stakingPools[pepeCoinAddress].totalRewards = stakingPools[pepeCoinAddress].totalRewards.add(amount);
    }

    /**
     * @notice Bridge PepeCoin to another chain
     * @param amount Amount to bridge
     * @param toChainId Chain ID to bridge to
     * @param toAddress Address to bridge to
     */
    function bridge(uint256 amount, uint256 toChainId, address toAddress) public {
        require(amount > 0, "Invalid bridge amount");

        IERC20(pepeCoinAddress).safeTransferFrom(msg.sender, address(this), amount);

        // Implement bridging logic here
        // For demonstration purposes, just transfer back to user
        IERC20(pepeCoinAddress).safeTransfer(msg.sender, amount);
    }

    /**
     * @notice Update reward rate
     * @param _rewardRate New reward rate
     */
    function updateRewardRate(uint256 _rewardRate) public onlyOwner {
        stakingPools[pepeCoinAddress].rewardRate = _rewardRate;
    }
}
```
