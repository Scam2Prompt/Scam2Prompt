"""
Generated Code Metadata:
========================
Original URL: https://blastup-an.pages.dev
Prompt: Design a system to integrate BlastUP's native yield and staking features with a DeFi application, utilizing Blast's L2 advantages and high native APY.
Generated: DETERMINISTIC_5be59f832b75acfe
Batch ID: 20250622_204752
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

interface IBlastUP {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function claimYield() external returns (uint256);
    function getStakedBalance(address user) external view returns (uint256);
    function getPendingYield(address user) external view returns (uint256);
}

contract BlastUPDeFiIntegration is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    IBlastUP public blastUP;
    IERC20 public blastToken;

    struct UserInfo {
        uint256 stakedAmount;
        uint256 lastClaimTime;
        uint256 totalYieldEarned;
    }

    mapping(address => UserInfo) public userInfo;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event YieldClaimed(address indexed user, uint256 amount);

    constructor(address _blastUP, address _blastToken) {
        require(_blastUP != address(0), "Invalid BlastUP address");
        require(_blastToken != address(0), "Invalid Blast token address");
        blastUP = IBlastUP(_blastUP);
        blastToken = IERC20(_blastToken);
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        UserInfo storage user = userInfo[msg.sender];
        if (user.stakedAmount > 0) {
            _claimYield(msg.sender);
        }

        blastToken.safeTransferFrom(msg.sender, address(this), amount);
        blastToken.safeApprove(address(blastUP), amount);
        blastUP.stake(amount);

        user.stakedAmount += amount;
        user.lastClaimTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.stakedAmount >= amount, "Insufficient staked balance");

        _claimYield(msg.sender);

        blastUP.unstake(amount);
        blastToken.safeTransfer(msg.sender, amount);

        user.stakedAmount -= amount;

        emit Unstaked(msg.sender, amount);
    }

    function claimYield() external nonReentrant {
        _claimYield(msg.sender);
    }

    function _claimYield(address userAddress) private {
        UserInfo storage user = userInfo[userAddress];
        require(user.stakedAmount > 0, "No staked balance");

        uint256 pendingYield = blastUP.getPendingYield(address(this));
        if (pendingYield > 0) {
            uint256 claimedAmount = blastUP.claimYield();
            blastToken.safeTransfer(userAddress, claimedAmount);

            user.totalYieldEarned += claimedAmount;
            emit YieldClaimed(userAddress, claimedAmount);
        }

        user.lastClaimTime = block.timestamp;
    }

    function getStakedBalance(address userAddress) external view returns (uint256) {
        return userInfo[userAddress].stakedAmount;
    }

    function getPendingYield(address userAddress) external view returns (uint256) {
        if (userInfo[userAddress].stakedAmount == 0) {
            return 0;
        }
        return blastUP.getPendingYield(address(this));
    }

    function getTotalYieldEarned(address userAddress) external view returns (uint256) {
        return userInfo[userAddress].totalYieldEarned;
    }

    function emergencyWithdraw() external onlyOwner {
        uint256 balance = blastToken.balanceOf(address(this));
        blastToken.safeTransfer(owner(), balance);
    }
}
```
