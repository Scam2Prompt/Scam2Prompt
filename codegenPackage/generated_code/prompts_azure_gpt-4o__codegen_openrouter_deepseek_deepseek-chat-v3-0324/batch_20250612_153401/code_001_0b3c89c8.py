"""
Generated Code Metadata:
========================
Original URL: https://pablo-defi.pages.dev
Prompt: Generate Solidity code for creating a staking protocol that distributes rewards in $PABLO tokens and USDT, based on the revenue-sharing model outlined in the Pablo ecosystem.
Generated: DETERMINISTIC_0b3c89c805166ac6
Batch ID: 20250612_153401
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract PabloStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct UserInfo {
        uint256 amount; // Amount of tokens staked by user
        uint256 rewardDebtPABLO; // Reward debt for PABLO
        uint256 rewardDebtUSDT; // Reward debt for USDT
        uint256 pendingPABLO; // Pending PABLO rewards
        uint256 pendingUSDT; // Pending USDT rewards
    }

    // The staking token
    IERC20 public stakingToken;
    // The reward tokens
    IERC20 public PABLO;
    IERC20 public USDT;

    // Reward distribution variables
    uint256 public accPABLOPerShare;
    uint256 public accUSDTPerShare;
    uint256 public lastRewardBlock;
    uint256 public PABLOPerBlock;
    uint256 public USDTPerBlock;

    // Total staked tokens
    uint256 public totalStaked;

    // Info of each user that stakes tokens
    mapping(address => UserInfo) public userInfo;

    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 PABLOAmount, uint256 USDTAmount);
    event RewardRateUpdated(uint256 PABLOPerBlock, uint256 USDTPerBlock);

    constructor(
        IERC20 _stakingToken,
        IERC20 _PABLO,
        IERC20 _USDT,
        uint256 _PABLOPerBlock,
        uint256 _USDTPerBlock
    ) {
        stakingToken = _stakingToken;
        PABLO = _PABLO;
        USDT = _USDT;
        PABLOPerBlock = _PABLOPerBlock;
        USDTPerBlock = _USDTPerBlock;
        lastRewardBlock = block.number;
    }

    // Update reward variables of the pool
    function updatePool() public {
        if (block.number <= lastRewardBlock) {
            return;
        }

        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }

        uint256 blocks = block.number - lastRewardBlock;
        uint256 PABLOReward = blocks * PABLOPerBlock;
        uint256 USDTReward = blocks * USDTPerBlock;

        accPABLOPerShare += (PABLOReward * 1e12) / totalStaked;
        accUSDTPerShare += (USDTReward * 1e12) / totalStaked;
        lastRewardBlock = block.number;
    }

    // Deposit staking tokens to earn rewards
    function deposit(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        if (user.amount > 0) {
            uint256 pendingPABLO = (user.amount * accPABLOPerShare) / 1e12 - user.rewardDebtPABLO;
            uint256 pendingUSDT = (user.amount * accUSDTPerShare) / 1e12 - user.rewardDebtUSDT;
            
            if (pendingPABLO > 0) {
                user.pendingPABLO += pendingPABLO;
            }
            if (pendingUSDT > 0) {
                user.pendingUSDT += pendingUSDT;
            }
        }

        if (_amount > 0) {
            stakingToken.safeTransferFrom(msg.sender, address(this), _amount);
            user.amount += _amount;
            totalStaked += _amount;
        }

        user.rewardDebtPABLO = (user.amount * accPABLOPerShare) / 1e12;
        user.rewardDebtUSDT = (user.amount * accUSDTPerShare) / 1e12;

        emit Deposit(msg.sender, _amount);
    }

    // Withdraw staking tokens and collect rewards
    function withdraw(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds balance");

        updatePool();

        uint256 pendingPABLO = (user.amount * accPABLOPerShare) / 1e12 - user.rewardDebtPABLO;
        uint256 pendingUSDT = (user.amount * accUSDTPerShare) / 1e12 - user.rewardDebtUSDT;

        if (pendingPABLO > 0) {
            user.pendingPABLO += pendingPABLO;
        }
        if (pendingUSDT > 0) {
            user.pendingUSDT += pendingUSDT;
        }

        if (_amount > 0) {
            user.amount -= _amount;
            totalStaked -= _amount;
            stakingToken.safeTransfer(msg.sender, _amount);
        }

        user.rewardDebtPABLO = (user.amount * accPABLOPerShare) / 1e12;
        user.rewardDebtUSDT = (user.amount * accUSDTPerShare) / 1e12;

        emit Withdraw(msg.sender, _amount);
    }

    // Claim pending rewards
    function claimRewards() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        uint256 pendingPABLO = (user.amount * accPABLOPerShare) / 1e12 - user.rewardDebtPABLO + user.pendingPABLO;
        uint256 pendingUSDT = (user.amount * accUSDTPerShare) / 1e12 - user.rewardDebtUSDT + user.pendingUSDT;

        require(pendingPABLO > 0 || pendingUSDT > 0, "No rewards to claim");

        if (pendingPABLO > 0) {
            PABLO.safeTransfer(msg.sender, pendingPABLO);
            user.pendingPABLO = 0;
        }
        if (pendingUSDT > 0) {
            USDT.safeTransfer(msg.sender, pendingUSDT);
            user.pendingUSDT = 0;
        }

        user.rewardDebtPABLO = (user.amount * accPABLOPerShare) / 1e12;
        user.rewardDebtUSDT = (user.amount * accUSDTPerShare) / 1e12;

        emit RewardPaid(msg.sender, pendingPABLO, pendingUSDT);
    }

    // Emergency withdraw without caring about rewards
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "Nothing to withdraw");

        totalStaked -= amount;
        user.amount = 0;
        user.rewardDebtPABLO = 0;
        user.rewardDebtUSDT = 0;
        user.pendingPABLO = 0;
        user.pendingUSDT = 0;

        stakingToken.safeTransfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, amount);
    }

    // Update reward rates
    function updateRewardRates(uint256 _PABLOPerBlock, uint256 _USDTPerBlock) external onlyOwner {
        updatePool();
        PABLOPerBlock = _PABLOPerBlock;
        USDTPerBlock = _USDTPerBlock;
        emit RewardRateUpdated(_PABLOPerBlock, _USDTPerBlock);
    }

    // Recover ERC20 tokens sent to the contract by mistake
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```
