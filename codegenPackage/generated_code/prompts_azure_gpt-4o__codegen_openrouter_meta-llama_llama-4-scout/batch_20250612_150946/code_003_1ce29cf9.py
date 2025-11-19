"""
Generated Code Metadata:
========================
Original URL: https://besureofme.pages.dev
Prompt: Create a smart contract that utilizes ListaDAO's permissionless liquid staking protocol for managing staked assets.
Generated: DETERMINISTIC_1ce29cf9f5d31d5f
Batch ID: 20250612_150946
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
 * @title ListaDAO Liquid Staking Protocol Smart Contract
 * @author [Your Name]
 * @notice This contract manages staked assets using ListaDAO's permissionless liquid staking protocol.
 */
contract ListaDAOLiquidStaking {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebt;

    // Total staking balance
    uint256 public totalStakingBalance;

    // Total reward debt
    uint256 public totalRewardDebt;

    // Reward per share
    uint256 public rewardPerShare;

    // Accrued reward per share
    uint256 public accruedRewardPerShare;

    // Staking token address
    address public stakingToken;

    // Reward token address
    address public rewardToken;

    // Owner address
    address public owner;

    // Emergency withdraw flag
    bool public emergencyWithdraw;

    /**
     * @notice Constructor
     * @param _stakingToken Staking token address
     * @param _rewardToken Reward token address
     * @param _owner Owner address
     */
    constructor(address _stakingToken, address _rewardToken, address _owner) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        owner = _owner;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "Invalid stake amount");
        require(!emergencyWithdraw, "Emergency withdraw is enabled");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStakingBalance = totalStakingBalance.add(_amount);

        IERC20(stakingToken).safeTransferFrom(msg.sender, address(this), _amount);

        updateRewardDebt(msg.sender);
    }

    /**
     * @notice Unstake tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) public {
        require(_amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStakingBalance = totalStakingBalance.sub(_amount);

        IERC20(stakingToken).safeTransfer(msg.sender, _amount);

        updateRewardDebt(msg.sender);
    }

    /**
     * @notice Update reward debt
     * @param _user User address
     */
    function updateRewardDebt(address _user) internal {
        uint256 _rewardPerShare = rewardPerShare;
        uint256 _stakingBalance = stakingBalances[_user];

        if (_stakingBalance > 0) {
            rewardDebt[_user] = _stakingBalance.mul(_rewardPerShare).div(1e18);
        }
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() public {
        uint256 _rewardDebt = rewardDebt[msg.sender];
        uint256 _stakingBalance = stakingBalances[msg.sender];

        if (_stakingBalance > 0) {
            uint256 _reward = _stakingBalance.mul(rewardPerShare).div(1e18).sub(_rewardDebt);
            rewardDebt[msg.sender] = _stakingBalance.mul(rewardPerShare).div(1e18);

            IERC20(rewardToken).safeTransfer(msg.sender, _reward);
        }
    }

    /**
     * @notice Update reward per share
     * @param _reward Amount of reward tokens
     */
    function updateRewardPerShare(uint256 _reward) public {
        require(msg.sender == owner, "Only owner can update reward per share");

        rewardPerShare = rewardPerShare.add(_reward.mul(1e18).div(totalStakingBalance));
        accruedRewardPerShare = accruedRewardPerShare.add(_reward.mul(1e18).div(totalStakingBalance));

        IERC20(rewardToken).safeTransferFrom(owner, address(this), _reward);
    }

    /**
     * @notice Enable emergency withdraw
     */
    function enableEmergencyWithdraw() public {
        require(msg.sender == owner, "Only owner can enable emergency withdraw");
        emergencyWithdraw = true;
    }

    /**
     * @notice Disable emergency withdraw
     */
    function disableEmergencyWithdraw() public {
        require(msg.sender == owner, "Only owner can disable emergency withdraw");
        emergencyWithdraw = false;
    }

    /**
     * @notice Emergency withdraw
     */
    function emergencyWithdraw() public {
        require(emergencyWithdraw, "Emergency withdraw is not enabled");
        require(stakingBalances[msg.sender] > 0, "Insufficient staking balance");

        uint256 _stakingBalance = stakingBalances[msg.sender];
        stakingBalances[msg.sender] = 0;

        IERC20(stakingToken).safeTransfer(msg.sender, _stakingBalance);
    }
}
```
