"""
Generated Code Metadata:
========================
Original URL: https://synthr-app.pages.dev
Prompt: "Design a staking mechanism for SYNTHR's veSYNTH token, including the distribution of syUSD and SYNTH rewards, and write a Solidity code snippet for it."
Generated: DETERMINISTIC_c3608b587364090d
Batch ID: 20250622_210038
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

    IERC20 public veSYNTH;
    IERC20 public SYNTH;
    IERC20 public syUSD;

    uint256 public accSYNTHPerShare;
    uint256 public accSyUSDPerShare;
    uint256 public lastRewardBlock;
    uint256 public SYNTHPerBlock;
    uint256 public syUSDPerBlock;

    mapping(address => UserInfo) public userInfo;

    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event Claim(address indexed user, uint256 synthAmount, uint256 syUSDAmount);
    event RewardRateUpdated(uint256 synthRate, uint256 syUSDRate);

    constructor(
        address _veSYNTH,
        address _SYNTH,
        address _syUSD,
        uint256 _SYNTHPerBlock,
        uint256 _syUSDPerBlock
    ) {
        veSYNTH = IERC20(_veSYNTH);
        SYNTH = IERC20(_SYNTH);
        syUSD = IERC20(_syUSD);
        SYNTHPerBlock = _SYNTHPerBlock;
        syUSDPerBlock = _syUSDPerBlock;
        lastRewardBlock = block.number;
    }

    function updatePool() public {
        if (block.number <= lastRewardBlock) {
            return;
        }

        uint256 veSYNTHSupply = veSYNTH.balanceOf(address(this));
        if (veSYNTHSupply == 0) {
            lastRewardBlock = block.number;
            return;
        }

        uint256 blocks = block.number - lastRewardBlock;
        uint256 SYNTHReward = blocks * SYNTHPerBlock;
        uint256 syUSDReward = blocks * syUSDPerBlock;

        accSYNTHPerShare += (SYNTHReward * 1e12) / veSYNTHSupply;
        accSyUSDPerShare += (syUSDReward * 1e12) / veSYNTHSupply;
        lastRewardBlock = block.number;
    }

    function deposit(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot stake 0");
        UserInfo storage user = userInfo[msg.sender];

        updatePool();

        if (user.amount > 0) {
            uint256 pendingSYNTH = (user.amount * accSYNTHPerShare) / 1e12 - user.rewardDebt;
            uint256 pendingsyUSD = (user.amount * accSyUSDPerShare) / 1e12 - user.syUSDRewardDebt;
            if (pendingSYNTH > 0) {
                SYNTH.safeTransfer(msg.sender, pendingSYNTH);
            }
            if (pendingsyUSD > 0) {
                syUSD.safeTransfer(msg.sender, pendingsyUSD);
            }
        }

        veSYNTH.safeTransferFrom(msg.sender, address(this), _amount);
        user.amount += _amount;
        user.rewardDebt = (user.amount * accSYNTHPerShare) / 1e12;
        user.syUSDRewardDebt = (user.amount * accSyUSDPerShare) / 1e12;

        emit Deposit(msg.sender, _amount);
    }

    function withdraw(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds balance");

        updatePool();

        uint256 pendingSYNTH = (user.amount * accSYNTHPerShare) / 1e12 - user.rewardDebt;
        uint256 pendingsyUSD = (user.amount * accSyUSDPerShare) / 1e12 - user.syUSDRewardDebt;

        if (pendingSYNTH > 0) {
            SYNTH.safeTransfer(msg.sender, pendingSYNTH);
        }
        if (pendingsyUSD > 0) {
            syUSD.safeTransfer(msg.sender, pendingsyUSD);
        }

        user.amount -= _amount;
        user.rewardDebt = (user.amount * accSYNTHPerShare) / 1e12;
        user.syUSDRewardDebt = (user.amount * accSyUSDPerShare) / 1e12;

        veSYNTH.safeTransfer(msg.sender, _amount);

        emit Withdraw(msg.sender, _amount);
    }

    function claim() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount > 0, "No staked balance");

        updatePool();

        uint256 pendingSYNTH = (user.amount * accSYNTHPerShare) / 1e12 - user.rewardDebt;
        uint256 pendingsyUSD = (user.amount * accSyUSDPerShare) / 1e12 - user.syUSDRewardDebt;

        if (pendingSYNTH > 0) {
            SYNTH.safeTransfer(msg.sender, pendingSYNTH);
        }
        if (pendingsyUSD > 0) {
            syUSD.safeTransfer(msg.sender, pendingsyUSD);
        }

        user.rewardDebt = (user.amount * accSYNTHPerShare) / 1e12;
        user.syUSDRewardDebt = (user.amount * accSyUSDPerShare) / 1e12;

        emit Claim(msg.sender, pendingSYNTH, pendingsyUSD);
    }

    function setRewardRates(uint256 _SYNTHPerBlock, uint256 _syUSDPerBlock) external onlyOwner {
        updatePool();
        SYNTHPerBlock = _SYNTHPerBlock;
        syUSDPerBlock = _syUSDPerBlock;
        emit RewardRateUpdated(_SYNTHPerBlock, _syUSDPerBlock);
    }

    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "No staked balance");

        user.amount = 0;
        user.rewardDebt = 0;
        user.syUSDRewardDebt = 0;

        veSYNTH.safeTransfer(msg.sender, amount);

        emit Withdraw(msg.sender, amount);
    }

    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(veSYNTH), "Cannot recover staking token");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
sfer(owner(), tokenAmount);
    }
}
```
