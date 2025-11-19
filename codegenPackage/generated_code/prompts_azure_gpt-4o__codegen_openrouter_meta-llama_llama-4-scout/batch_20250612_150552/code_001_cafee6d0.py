"""
Generated Code Metadata:
========================
Original URL: https://oraclememe-sale.pages.dev
Prompt: Generate code to create a staking smart contract on Binance Smart Chain (BSC) that mimics the staking rewards system described for OMEME, including dynamic reward percentages.
Generated: DETERMINISTIC_cafee6d038e58116
Batch ID: 20250612_150552
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

contract OMEDESTaking is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token used for staking and rewards
    IERC20 public token;

    // Reward token
    IERC20 public rewardToken;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebt;

    // Total staking amount
    uint256 public totalStaked;

    // Reward per share
    uint256 public accRewardPerShare;

    // Reward distribution interval in seconds
    uint256 public rewardInterval;

    // Last reward distribution timestamp
    uint256 public lastRewardTimestamp;

    // Dynamic reward percentage
    uint256 public rewardPercentage;

    // Maximum reward percentage
    uint256 public maxRewardPercentage;

    // Minimum reward percentage
    uint256 public minRewardPercentage;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    constructor(
        IERC20 _token,
        IERC20 _rewardToken,
        uint256 _rewardInterval,
        uint256 _maxRewardPercentage,
        uint256 _minRewardPercentage
    ) public {
        require(
            address(_token) != address(0) && address(_rewardToken) != address(0),
            "Token addresses cannot be zero"
        );
        require(_rewardInterval > 0, "Reward interval must be greater than 0");
        require(
            _maxRewardPercentage > _minRewardPercentage,
            "Max reward percentage must be greater than min reward percentage"
        );

        token = _token;
        rewardToken = _rewardToken;
        rewardInterval = _rewardInterval;
        maxRewardPercentage = _maxRewardPercentage;
        minRewardPercentage = _minRewardPercentage;
        lastRewardTimestamp = block.timestamp;
        rewardPercentage = _minRewardPercentage;
    }

    // Update reward variables
    function updateRewardVariables() internal {
        uint256 currentTimestamp = block.timestamp;
        if (currentTimestamp.sub(lastRewardTimestamp) >= rewardInterval) {
            uint256 totalReward = calculateTotalReward();
            accRewardPerShare = accRewardPerShare.add(
                totalReward.mul(1e18).div(totalStaked)
            );
            lastRewardTimestamp = currentTimestamp;
        }
    }

    // Calculate total reward
    function calculateTotalReward() public view returns (uint256) {
        uint256 elapsedTime = block.timestamp.sub(lastRewardTimestamp);
        uint256 totalReward = rewardToken.balanceOf(address(this)).mul(
            rewardPercentage
        ).mul(elapsedTime).div(100).div(1 days);
        return totalReward;
    }

    // Stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than 0");
        require(
            token.balanceOf(msg.sender) >= _amount,
            "Insufficient token balance"
        );

        // Transfer tokens to contract
        token.transferFrom(msg.sender, address(this), _amount);

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStaked = totalStaked.add(_amount);

        // Update user's reward debt
        uint256 currentRewardPerShare = accRewardPerShare;
        rewardDebt[msg.sender] = rewardDebt[msg.sender].add(
            _amount.mul(currentRewardPerShare).div(1e18)
        );

        emit Staked(msg.sender, _amount);
    }

    // Unstake tokens
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than 0");
        require(
            stakingBalances[msg.sender] >= _amount,
            "Insufficient staking balance"
        );

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        // Update user's reward debt
        uint256 currentRewardPerShare = accRewardPerShare;
        uint256 reward = rewardDebt[msg.sender].sub(
            _amount.mul(currentRewardPerShare).div(1e18)
        );
        rewardDebt[msg.sender] = 0;

        // Distribute rewards
        if (reward > 0) {
            rewardToken.transfer(msg.sender, reward);
            emit RewardsDistributed(msg.sender, reward);
        }

        // Transfer tokens to user
        token.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Harvest rewards
    function harvest() external {
        uint256 currentRewardPerShare = accRewardPerShare;
        uint256 userReward = stakingBalances[msg.sender].mul(
            currentRewardPerShare
        ).div(1e18) - rewardDebt[msg.sender];

        if (userReward > 0) {
            rewardToken.transfer(msg.sender, userReward);
            rewardDebt[msg.sender] = stakingBalances[msg.sender].mul(
                currentRewardPerShare
            ).div(1e18);
            emit RewardsDistributed(msg.sender, userReward);
        }
    }

    // Update reward percentage
    function updateRewardPercentage(uint256 _newRewardPercentage) external onlyOwner {
        require(
            _newRewardPercentage >= minRewardPercentage &&
                _newRewardPercentage <= maxRewardPercentage,
            "Reward percentage must be within allowed range"
        );
        rewardPercentage = _newRewardPercentage;
    }

    // Withdraw tokens from contract
    function withdrawTokens(IERC20 _token, uint256 _amount) external onlyOwner {
        require(
            address(_token) != address(0),
            "Token address cannot be zero"
        );
        require(_amount > 0, "Withdrawal amount must be greater than 0");
        require(
            _token.balanceOf(address(this)) >= _amount,
            "Insufficient token balance in contract"
        );

        _token.transfer(msg.sender, _amount);
    }
}
```
