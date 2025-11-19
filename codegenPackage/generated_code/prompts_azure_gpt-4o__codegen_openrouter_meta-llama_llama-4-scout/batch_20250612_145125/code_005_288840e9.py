"""
Generated Code Metadata:
========================
Original URL: https://yifistake.finance
Prompt: Develop a Solidity contract to handle staking YI12 tokens paired with ETH, including reward distribution logic as described on the YI12 Stake Finance site.
Generated: DETERMINISTIC_288840e9130fb00f
Batch ID: 20250612_145125
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
 * @title YI12 Stake Finance Contract
 * @author [Your Name]
 * @notice This contract handles staking YI12 tokens paired with ETH and distributes rewards.
 */
contract Yi12StakeFinance is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Token and ETH pair
    IERC20 public yi12Token;
    address public ethAddress = 0xEeeeeeEeEeEeEeeEeEeEeeEeeEeeE;

    // Staking and reward structures
    struct Stake {
        uint256 yi12Amount;
        uint256 ethAmount;
        uint256 rewardDebt;
    }

    mapping(address => Stake) public stakes;

    // Reward distribution parameters
    uint256 public rewardPerBlock;
    uint256 public lastRewardBlock;
    uint256 public accRewardPerShare;

    // Events
    event StakeEvent(address indexed user, uint256 yi12Amount, uint256 ethAmount);
    event UnstakeEvent(address indexed user, uint256 yi12Amount, uint256 ethAmount);
    event RewardDistributionEvent(address indexed user, uint256 rewardAmount);

    /**
     * @param yi12TokenAddress Address of YI12 token
     * @param rewardPerBlock Reward per block
     * @param lastRewardBlock Last reward block
     */
    constructor(
        address yi12TokenAddress,
        uint256 rewardPerBlock,
        uint256 lastRewardBlock
    ) public {
        yi12Token = IERC20(yi12TokenAddress);
        rewardPerBlock = rewardPerBlock;
        lastRewardBlock = lastRewardBlock;
    }

    /**
     * @notice Stake YI12 tokens paired with ETH
     * @param _yi12Amount Amount of YI12 tokens to stake
     * @param _ethAmount Amount of ETH to stake
     */
    function stake(uint256 _yi12Amount, uint256 _ethAmount) public {
        require(_yi12Amount > 0 && _ethAmount > 0, "Invalid stake amount");

        // Transfer YI12 tokens and ETH from user to contract
        yi12Token.safeTransferFrom(msg.sender, address(this), _yi12Amount);
        payable(address(this)).transfer(_ethAmount);

        // Update stake information
        stakes[msg.sender].yi12Amount = stakes[msg.sender].yi12Amount.add(_yi12Amount);
        stakes[msg.sender].ethAmount = stakes[msg.sender].ethAmount.add(_ethAmount);

        // Update reward debt
        updateRewardDebt(msg.sender);

        emit StakeEvent(msg.sender, _yi12Amount, _ethAmount);
    }

    /**
     * @notice Unstake YI12 tokens paired with ETH
     * @param _yi12Amount Amount of YI12 tokens to unstake
     * @param _ethAmount Amount of ETH to unstake
     */
    function unstake(uint256 _yi12Amount, uint256 _ethAmount) public {
        require(_yi12Amount > 0 && _ethAmount > 0, "Invalid unstake amount");
        require(stakes[msg.sender].yi12Amount >= _yi12Amount && stakes[msg.sender].ethAmount >= _ethAmount, "Insufficient stake amount");

        // Update stake information
        stakes[msg.sender].yi12Amount = stakes[msg.sender].yi12Amount.sub(_yi12Amount);
        stakes[msg.sender].ethAmount = stakes[msg.sender].ethAmount.sub(_ethAmount);

        // Transfer YI12 tokens and ETH from contract to user
        yi12Token.safeTransfer(msg.sender, _yi12Amount);
        payable(msg.sender).transfer(_ethAmount);

        // Update reward debt
        updateRewardDebt(msg.sender);

        emit UnstakeEvent(msg.sender, _yi12Amount, _ethAmount);
    }

    /**
     * @notice Update reward debt for user
     * @param _user User address
     */
    function updateRewardDebt(address _user) internal {
        // Calculate reward
        uint256 reward = getReward(_user);

        // Update reward debt
        stakes[_user].rewardDebt = stakes[_user].rewardDebt.add(reward);

        // Update accRewardPerShare
        accRewardPerShare = accRewardPerShare.add(reward);
    }

    /**
     * @notice Get reward for user
     * @param _user User address
     * @return Reward amount
     */
    function getReward(address _user) internal view returns (uint256) {
        // Calculate reward
        uint256 reward = 0;
        uint256 currentBlock = block.number;
        if (currentBlock > lastRewardBlock) {
            uint256 multiplier = currentBlock.sub(lastRewardBlock);
            reward = multiplier.mul(rewardPerBlock);
        }

        return reward;
    }

    /**
     * @notice Distribute reward to user
     */
    function distributeReward() public {
        // Calculate reward
        uint256 reward = getReward(msg.sender);

        // Transfer reward to user
        yi12Token.safeTransfer(msg.sender, reward);

        // Update reward debt
        stakes[msg.sender].rewardDebt = 0;

        emit RewardDistributionEvent(msg.sender, reward);
    }

    /**
     * @notice Update reward per block
     * @param _rewardPerBlock New reward per block
     */
    function updateRewardPerBlock(uint256 _rewardPerBlock) public onlyOwner {
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @notice Update last reward block
     * @param _lastRewardBlock New last reward block
     */
    function updateLastRewardBlock(uint256 _lastRewardBlock) public onlyOwner {
        lastRewardBlock = _lastRewardBlock;
    }
}
```
