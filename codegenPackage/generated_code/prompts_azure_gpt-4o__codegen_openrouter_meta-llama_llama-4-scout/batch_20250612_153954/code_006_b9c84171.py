"""
Generated Code Metadata:
========================
Original URL: https://basedbrett.on-fleek.app
Prompt: Create a smart contract that interacts with the $Brett token on the Base Mainnet, allowing users to stake tokens and earn rewards based on their holdings.
Generated: DETERMINISTIC_b9c8417176d79b37
Batch ID: 20250612_153954
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title BrettStakingContract
 * @author [Your Name]
 * @notice A staking contract for the $Brett token on the Base Mainnet.
 */
contract BrettStakingContract is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Token contract instance
    IERC20 public brettToken;

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

    // Reward distribution interval (in seconds)
    uint256 public rewardInterval;

    // Last reward distribution timestamp
    uint256 public lastRewardDistribution;

    // Reward token address
    address public rewardToken;

    // Reward amount per interval
    uint256 public rewardAmount;

    /**
     * @notice Constructor
     * @param _brettToken $Brett token contract address
     * @param _rewardToken Reward token contract address
     * @param _rewardAmount Reward amount per interval
     * @param _rewardInterval Reward distribution interval (in seconds)
     */
    constructor(
        address _brettToken,
        address _rewardToken,
        uint256 _rewardAmount,
        uint256 _rewardInterval
    ) public {
        brettToken = IERC20(_brettToken);
        rewardToken = _rewardToken;
        rewardAmount = _rewardAmount;
        rewardInterval = _rewardInterval;
        lastRewardDistribution = block.timestamp;
    }

    /**
     * @notice Stake $Brett tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "Invalid stake amount");

        // Transfer tokens from user to contract
        brettToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStakingBalance = totalStakingBalance.add(_amount);

        // Update user's reward debt
        updateRewardDebt(msg.sender);
    }

    /**
     * @notice Unstake $Brett tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) public {
        require(_amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStakingBalance = totalStakingBalance.sub(_amount);

        // Transfer tokens from contract to user
        brettToken.safeTransfer(msg.sender, _amount);

        // Update user's reward debt
        updateRewardDebt(msg.sender);
    }

    /**
     * @notice Update user's reward debt
     * @param _user User address
     */
    function updateRewardDebt(address _user) internal {
        // Calculate accumulated reward per share
        accRewardPerShare = accRewardPerShare.add(
            getRewardPerShare()
        );

        // Update user's reward debt
        rewardDebt[_user] = stakingBalances[_user].mul(accRewardPerShare).div(1e18);
    }

    /**
     * @notice Get reward per share
     * @return Reward per share
     */
    function getRewardPerShare() public view returns (uint256) {
        // Calculate reward per share
        uint256 _rewardPerShare = 0;
        if (totalStakingBalance > 0) {
            _rewardPerShare = rewardAmount.mul(1e18).div(totalStakingBalance);
        }
        return _rewardPerShare;
    }

    /**
     * @notice Distribute rewards
     */
    function distributeRewards() public {
        // Check if reward distribution interval has passed
        require(
            block.timestamp.sub(lastRewardDistribution) >= rewardInterval,
            "Reward distribution interval has not passed"
        );

        // Update last reward distribution timestamp
        lastRewardDistribution = block.timestamp;

        // Calculate accumulated reward per share
        accRewardPerShare = accRewardPerShare.add(getRewardPerShare());

        // Transfer reward tokens to contract
        IERC20(rewardToken).safeTransfer(address(this), rewardAmount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() public {
        // Calculate user's reward
        uint256 _reward = stakingBalances[msg.sender].mul(accRewardPerShare).div(1e18).sub(rewardDebt[msg.sender]);

        // Update user's reward debt
        rewardDebt[msg.sender] = stakingBalances[msg.sender].mul(accRewardPerShare).div(1e18);

        // Transfer reward tokens to user
        IERC20(rewardToken).safeTransfer(msg.sender, _reward);
    }
}
```
