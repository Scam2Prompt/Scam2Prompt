"""
Generated Code Metadata:
========================
Original URL: https://skalenetworkspace.com
Prompt: Generate code to manage staking and unstaking operations in the Sushi Bar, including real-time updates on staked balances and APY changes.
Generated: DETERMINISTIC_861ec7b8f69523e6
Batch ID: 20250612_145837
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract SushiBar is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    IERC20 public sushiToken;
    IERC20 public xSushiToken;

    uint256 public totalStaked;
    uint256 public lastRewardBlock;
    uint256 public rewardPerBlock;
    uint256 public constant PRECISION_FACTOR = 1e18;

    mapping(address => uint256) public userStakedBalance;
    mapping(address => uint256) public userRewardDebt;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRewardPerBlock);

    constructor(
        address _sushiToken,
        address _xSushiToken,
        uint256 _rewardPerBlock
    ) {
        require(_sushiToken != address(0), "Invalid Sushi token address");
        require(_xSushiToken != address(0), "Invalid xSushi token address");

        sushiToken = IERC20(_sushiToken);
        xSushiToken = IERC20(_xSushiToken);
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    function updateRewardRate(uint256 _newRewardPerBlock) external {
        require(_newRewardPerBlock > 0, "Reward per block must be positive");
        _updatePool();
        rewardPerBlock = _newRewardPerBlock;
        emit RewardRateUpdated(_newRewardPerBlock);
    }

    function _updatePool() internal {
        if (block.number <= lastRewardBlock || totalStaked == 0) {
            return;
        }

        uint256 multiplier = block.number.sub(lastRewardBlock);
        uint256 sushiReward = multiplier.mul(rewardPerBlock);
        
        // Mint new xSushi tokens as rewards
        xSushiToken.safeTransferFrom(address(this), address(this), sushiReward);
        
        lastRewardBlock = block.number;
    }

    function pendingReward(address _user) external view returns (uint256) {
        if (totalStaked == 0) {
            return 0;
        }

        uint256 currentBlock = block.number;
        uint256 multiplier = currentBlock.sub(lastRewardBlock);
        uint256 pending = multiplier.mul(rewardPerBlock);
        uint256 adjustedTokenPerShare = pending.mul(PRECISION_FACTOR).div(totalStaked);
        
        return userStakedBalance[_user].mul(adjustedTokenPerShare).div(PRECISION_FACTOR).sub(userRewardDebt[_user]);
    }

    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        
        _updatePool();
        
        if (userStakedBalance[msg.sender] > 0) {
            uint256 pending = userStakedBalance[msg.sender]
                .mul(rewardPerBlock.mul(block.number.sub(lastRewardBlock)).mul(PRECISION_FACTOR).div(totalStaked))
                .div(PRECISION_FACTOR)
                .sub(userRewardDebt[msg.sender]);
            
            if (pending > 0) {
                xSushiToken.safeTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }
        
        sushiToken.safeTransferFrom(msg.sender, address(this), _amount);
        userStakedBalance[msg.sender] = userStakedBalance[msg.sender].add(_amount);
        totalStaked = totalStaked.add(_amount);
        
        userRewardDebt[msg.sender] = userStakedBalance[msg.sender]
            .mul(rewardPerBlock.mul(block.number.sub(lastRewardBlock)).mul(PRECISION_FACTOR).div(totalStaked))
            .div(PRECISION_FACTOR);
            
        emit Staked(msg.sender, _amount);
    }

    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(userStakedBalance[msg.sender] >= _amount, "Insufficient staked balance");
        
        _updatePool();
        
        uint256 pending = userStakedBalance[msg.sender]
            .mul(rewardPerBlock.mul(block.number.sub(lastRewardBlock)).mul(PRECISION_FACTOR).div(totalStaked))
            .div(PRECISION_FACTOR)
            .sub(userRewardDebt[msg.sender]);
            
        if (pending > 0) {
            xSushiToken.safeTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }
        
        userStakedBalance[msg.sender] = userStakedBalance[msg.sender].sub(_amount);
        totalStaked = totalStaked.sub(_amount);
        
        userRewardDebt[msg.sender] = userStakedBalance[msg.sender]
            .mul(rewardPerBlock.mul(block.number.sub(lastRewardBlock)).mul(PRECISION_FACTOR).div(totalStaked))
            .div(PRECISION_FACTOR);
            
        sushiToken.safeTransfer(msg.sender, _amount);
        emit Unstaked(msg.sender, _amount);
    }

    function claimReward() external nonReentrant {
        require(userStakedBalance[msg.sender] > 0, "No staked balance");
        
        _updatePool();
        
        uint256 pending = userStakedBalance[msg.sender]
            .mul(rewardPerBlock.mul(block.number.sub(lastRewardBlock)).mul(PRECISION_FACTOR).div(totalStaked))
            .div(PRECISION_FACTOR)
            .sub(userRewardDebt[msg.sender]);
            
        require(pending > 0, "No rewards to claim");
        
        xSushiToken.safeTransfer(msg.sender, pending);
        userRewardDebt[msg.sender] = userStakedBalance[msg.sender]
            .mul(rewardPerBlock.mul(block.number.sub(lastRewardBlock)).mul(PRECISION_FACTOR).div(totalStaked))
            .div(PRECISION_FACTOR);
            
        emit RewardClaimed(msg.sender, pending);
    }

    function getAPY() external view returns (uint256) {
        if (totalStaked == 0) {
            return 0;
        }
        
        // Assuming 2102400 blocks per year (15s block time)
        uint256 blocksPerYear = 2102400;
        uint256 annualReward = rewardPerBlock.mul(blocksPerYear);
        return annualReward.mul(PRECISION_FACTOR).div(totalStaked);
    }
}
```
