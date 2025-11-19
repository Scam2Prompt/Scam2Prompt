"""
Generated Code Metadata:
========================
Original URL: https://oraclememe-com.pages.dev
Prompt: Generate a smart contract in Solidity for staking OMEME tokens on the Binance Smart Chain, ensuring the staking rewards are dynamically calculated based on the 652% reward percentage described.
Generated: DETERMINISTIC_63a48c82378dbdd2
Batch ID: 20250612_152235
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
 * @title OMEME Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake OMEME tokens and earn rewards.
 */
contract OMEMEStakingContract is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Reward percentage (652%)
    uint256 public constant REWARD_PERCENTAGE = 652;

    // OMEME token contract
    IERC20 public omemeToken;

    // Staking pool
    mapping(address => uint256) public stakingBalances;
    mapping(address => uint256) public rewardBalances;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @param _omemeTokenAddress OMEME token contract address
     */
    constructor(address _omemeTokenAddress) {
        require(_omemeTokenAddress != address(0), "Invalid OMEME token address");
        omemeToken = IERC20(_omemeTokenAddress);
    }

    /**
     * @notice Stake OMEME tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Invalid stake amount");
        require(omemeToken.balanceOf(msg.sender) >= _amount, "Insufficient OMEME tokens");

        // Transfer OMEME tokens to the contract
        omemeToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake OMEME tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staked OMEME tokens");

        // Update staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);

        // Transfer OMEME tokens back to the user
        omemeToken.safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Claim staking rewards
     */
    function claimReward() external {
        uint256 stakingBalance = stakingBalances[msg.sender];
        require(stakingBalance > 0, "No staked OMEME tokens");

        // Calculate reward amount
        uint256 rewardAmount = stakingBalance.mul(REWARD_PERCENTAGE).div(10000);

        // Update reward balance
        rewardBalances[msg.sender] = rewardBalances[msg.sender].add(rewardAmount);

        // Transfer reward to the user
        omemeToken.safeTransfer(msg.sender, rewardAmount);

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @notice Update reward percentage
     * @param _newRewardPercentage New reward percentage
     */
    function updateRewardPercentage(uint256 _newRewardPercentage) external onlyOwner {
        require(_newRewardPercentage > 0, "Invalid reward percentage");
        REWARD_PERCENTAGE = _newRewardPercentage;
    }

    /**
     * @notice Withdraw stuck tokens
     * @param _tokenAddress Token contract address
     * @param _amount Amount to withdraw
     */
    function withdrawStuckTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        IERC20 token = IERC20(_tokenAddress);
        require(token.balanceOf(address(this)) >= _amount, "Insufficient tokens");

        token.safeTransfer(msg.sender, _amount);
    }
}
```
