"""
Generated Code Metadata:
========================
Original URL: https://synthr.pages.dev
Prompt: "Design a staking mechanism for SYNTHR's veSYNTH token, including the distribution of syUSD and SYNTH rewards, and write a Solidity code snippet for it."
Generated: DETERMINISTIC_c3608b587364090d
Batch ID: 20250622_210027
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
import "@openzeppelin/contracts/access/Ownable.sol";

contract SynthStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    struct UserInfo {
        uint256 amount; // Amount of veSYNTH staked
        uint256 rewardDebt; // Reward debt for SYNTH
        uint256 syUSDRewardDebt; // Reward debt for syUSD
    }

    IERC20 public immutable veSYNTH;
    IERC20 public immutable SYNTH;
    IERC20 public immutable syUSD;

    uint256 public accRewardPerShare; // Accumulated SYNTH per share
    uint256 public accSyUSDRewardPerShare; // Accumulated syUSD per share
    uint256 public lastRewardBlock; // Last block number rewards were calculated

    uint256 public rewardPerBlock; // SYNTH reward per block
    uint256 public syUSDRewardPerBlock; // syUSD reward per block
    uint256 public totalStaked; // Total veSYNTH staked

    mapping(address => UserInfo) public userInfo;

    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event Claim(address indexed user, uint256 synthAmount, uint256 syUSDAmount);
    event RewardUpdated(uint256 rewardPerBlock, uint256 syUSDRewardPerBlock);

    constructor(
        IERC20 _veSYNTH,
        IERC20 _SYNTH,
        IERC20 _syUSD,
        uint256 _rewardPerBlock,
        uint256 _syUSDRewardPerBlock
    ) {
        veSYNTH = _veSYNTH;
        SYNTH = _SYNTH;
        syUSD = _syUSD;
        rewardPerBlock = _rewardPerBlock;
        syUSDRewardPerBlock = _syUSDRewardPerBlock;
        lastRewardBlock = block.number;
    }

    function updateRewardPerBlock(uint256 _rewardPerBlock, uint256 _syUSDRewardPerBlock) external onlyOwner {
        _updatePool();
        rewardPerBlock = _rewardPerBlock;
        syUSDRewardPerBlock = _syUSDRewardPerBlock;
        emit RewardUpdated(_rewardPerBlock, _syUSDRewardPerBlock);
    }

    function pendingRewards(address _user) external view returns (uint256 pendingSYNTH, uint256 pendingsyUSD) {
        UserInfo storage user = userInfo[_user];
        uint256 _accRewardPerShare = accRewardPerShare;
        uint256 _accSyUSDRewardPerShare = accSyUSDRewardPerShare;
        
        if (block.number > lastRewardBlock && totalStaked != 0) {
            uint256 blocks = block.number - lastRewardBlock;
            _accRewardPerShare += (blocks * rewardPerBlock * 1e12) / totalStaked;
            _accSyUSDRewardPerShare += (blocks * syUSDRewardPerBlock * 1e12) / totalStaked;
        }
        
        pendingSYNTH = (user.amount * _accRewardPerShare) / 1e12 - user.rewardDebt;
        pendingsyUSD = (user.amount * _accSyUSDRewardPerShare) / 1e12 - user.syUSDRewardDebt;
    }

    function _updatePool() internal {
        if (block.number <= lastRewardBlock) {
            return;
        }
        
        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }
        
        uint256 blocks = block.number - lastRewardBlock;
        accRewardPerShare += (blocks * rewardPerBlock * 1e12) / totalStaked;
        accSyUSDRewardPerShare += (blocks * syUSDRewardPerBlock * 1e12) / totalStaked;
        lastRewardBlock = block.number;
    }

    function deposit(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        
        UserInfo storage user = userInfo[msg.sender];
        _updatePool();
        
        if (user.amount > 0) {
            uint256 pendingSYNTH = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
            uint256 pendingsyUSD = (user.amount * accSyUSDRewardPerShare) / 1e12 - user.syUSDRewardDebt;
            
            if (pendingSYNTH > 0) {
                SYNTH.safeTransfer(msg.sender, pendingSYNTH);
            }
            if (pendingsyUSD > 0) {
                syUSD.safeTransfer(msg.sender, pendingsyUSD);
            }
        }
        
        veSYNTH.safeTransferFrom(msg.sender, address(this), _amount);
        user.amount += _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        user.syUSDRewardDebt = (user.amount * accSyUSDRewardPerShare) / 1e12;
        totalStaked += _amount;
        
        emit Deposit(msg.sender, _amount);
    }

    function withdraw(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds balance");
        
        _updatePool();
        
        uint256 pendingSYNTH = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        uint256 pendingsyUSD = (user.amount * accSyUSDRewardPerShare) / 1e12 - user.syUSDRewardDebt;
        
        if (pendingSYNTH > 0) {
            SYNTH.safeTransfer(msg.sender, pendingSYNTH);
        }
        if (pendingsyUSD > 0) {
            syUSD.safeTransfer(msg.sender, pendingsyUSD);
        }
        
        user.amount -= _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        user.syUSDRewardDebt = (user.amount * accSyUSDRewardPerShare) / 1e12;
        totalStaked -= _amount;
        
        veSYNTH.safeTransfer(msg.sender, _amount);
        
        emit Withdraw(msg.sender, _amount);
    }

    function claim() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        _updatePool();
        
        uint256 pendingSYNTH = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        uint256 pendingsyUSD = (user.amount * accSyUSDRewardPerShare) / 1e12 - user.syUSDRewardDebt;
        
        require(pendingSYNTH > 0 || pendingsyUSD > 0, "No rewards to claim");
        
        if (pendingSYNTH > 0) {
            SYNTH.safeTransfer(msg.sender, pendingSYNTH);
            user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        }
        if (pendingsyUSD > 0) {
            syUSD.safeTransfer(msg.sender, pendingsyUSD);
            user.syUSDRewardDebt = (user.amount * accSyUSDRewardPerShare) / 1e12;
        }
        
        emit Claim(msg.sender, pendingSYNTH, pendingsyUSD);
    }

    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "Nothing to withdraw");
        
        totalStaked -= amount;
        user.amount = 0;
        user.rewardDebt = 0;
        user.syUSDRewardDebt = 0;
        
        veSYNTH.safeTransfer(msg.sender, amount);
        
        emit Withdraw(msg.sender, amount);
    }

    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(veSYNTH), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(msg.sender, tokenAmount);
    }
}
```
