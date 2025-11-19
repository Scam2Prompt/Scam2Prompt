"""
Generated Code Metadata:
========================
Original URL: https://btcetftoken-63w.pages.dev
Prompt: Generate a Solidity contract for staking Bitcoin ETF Token (BTCETF) that rewards users based on the number of tokens staked.
Generated: DETERMINISTIC_ac6c523fcb89b150
Batch ID: 20250612_163848
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
 * @title BTCETF Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake BTCETF tokens and earn rewards based on the number of tokens staked.
 */
contract BTCETFStaking is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebt;

    // Total staking balance
    uint256 public totalStakingBalance;

    // Reward per share
    uint256 public rewardPerShare;

    // Accumulated reward per share
    uint256 public accRewardPerShare;

    // BTCETF token contract
    ERC20 public btcetfToken;

    // Reward token contract
    ERC20 public rewardToken;

    // Staking start timestamp
    uint256 public stakingStartTimestamp;

    // Staking end timestamp
    uint256 public stakingEndTimestamp;

    // Reward per block
    uint256 public rewardPerBlock;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _btcetfTokenAddress BTCETF token contract address
     * @param _rewardTokenAddress Reward token contract address
     * @param _stakingStartTimestamp Staking start timestamp
     * @param _stakingEndTimestamp Staking end timestamp
     * @param _rewardPerBlock Reward per block
     */
    constructor(
        address _btcetfTokenAddress,
        address _rewardTokenAddress,
        uint256 _stakingStartTimestamp,
        uint256 _stakingEndTimestamp,
        uint256 _rewardPerBlock
    ) public {
        btcetfToken = ERC20(_btcetfTokenAddress);
        rewardToken = ERC20(_rewardTokenAddress);
        stakingStartTimestamp = _stakingStartTimestamp;
        stakingEndTimestamp = _stakingEndTimestamp;
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @notice Stake BTCETF tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(msg.sender != address(0), "Invalid address");
        require(_amount > 0, "Invalid amount");
        require(block.timestamp >= stakingStartTimestamp, "Staking not started");
        require(block.timestamp < stakingEndTimestamp, "Staking ended");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStakingBalance = totalStakingBalance.add(_amount);

        // Transfer tokens from user to contract
        btcetfToken.transferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);

        // Update reward debt
        updateRewardDebt(msg.sender);
    }

    /**
     * @notice Unstake BTCETF tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(msg.sender != address(0), "Invalid address");
        require(_amount > 0, "Invalid amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStakingBalance = totalStakingBalance.sub(_amount);

        // Transfer tokens from contract to user
        btcetfToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);

        // Update reward debt
        updateRewardDebt(msg.sender);
    }

    /**
     * @notice Update reward debt for user
     * @param _user User address
     */
    function updateRewardDebt(address _user) internal {
        if (stakingBalances[_user] > 0) {
            uint256 pendingReward = getPendingReward(_user);
            rewardDebt[_user] = stakingBalances[_user].mul(accRewardPerShare).div(1e18);

            if (pendingReward > 0) {
                rewardToken.transfer(_user, pendingReward);
                emit RewardsDistributed(_user, pendingReward);
            }
        }
    }

    /**
     * @notice Get pending reward for user
     * @param _user User address
     * @return Pending reward amount
     */
    function getPendingReward(address _user) public view returns (uint256) {
        uint256 userRewardDebt = rewardDebt[_user];
        uint256 currentRewardPerShare = accRewardPerShare;
        uint256 stakedBalance = stakingBalances[_user];

        if (stakedBalance > 0) {
            uint256 pending = stakedBalance.mul(currentRewardPerShare).div(1e18).sub(userRewardDebt);
            return pending;
        } else {
            return 0;
        }
    }

    /**
     * @notice Update reward per block
     */
    function updateAccRewardPerShare() public {
        if (totalStakingBalance > 0) {
            uint256 reward = rewardPerBlock;
            accRewardPerShare = accRewardPerShare.add(reward.mul(1e18).div(totalStakingBalance));
        }
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external nonReentrant {
        updateAccRewardPerShare();
        updateRewardDebt(msg.sender);
    }
}
```
