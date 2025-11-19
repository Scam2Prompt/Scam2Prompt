"""
Generated Code Metadata:
========================
Original URL: https://iziswap.fi
Prompt: Write a smart contract in Solidity for a liquidity-mining-based bond like iUSD, ensuring it is 100% collateralized and avoids impermanent loss for LP farming.
Generated: DETERMINISTIC_a3659dc8e4072cb0
Batch ID: 20250612_153424
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

contract CollateralizedBond is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Token addresses
    IERC20 public immutable bondToken;
    IERC20 public immutable collateralToken;
    IERC20 public immutable lpToken;

    // Bond parameters
    uint256 public bondPrice; // Price of bond in collateral tokens
    uint256 public bondSupply;
    uint256 public totalCollateral;
    uint256 public bondMaturity; // Timestamp when bonds mature
    uint256 public bondDuration; // Duration in seconds

    // Farming parameters
    uint256 public farmingRewardRate; // Reward rate per second
    uint256 public lastRewardTime;
    uint256 public accRewardPerShare;

    // User info
    struct UserInfo {
        uint256 bondAmount;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }
    mapping(address => UserInfo) public userInfo;

    // Events
    event BondPurchased(address indexed user, uint256 amount, uint256 collateralAmount);
    event BondRedeemed(address indexed user, uint256 amount, uint256 collateralAmount);
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    constructor(
        address _bondToken,
        address _collateralToken,
        address _lpToken,
        uint256 _bondPrice,
        uint256 _bondDuration,
        uint256 _farmingRewardRate
    ) {
        require(_bondToken != address(0), "Invalid bond token");
        require(_collateralToken != address(0), "Invalid collateral token");
        require(_lpToken != address(0), "Invalid LP token");
        require(_bondPrice > 0, "Invalid bond price");
        require(_bondDuration > 0, "Invalid bond duration");

        bondToken = IERC20(_bondToken);
        collateralToken = IERC20(_collateralToken);
        lpToken = IERC20(_lpToken);
        bondPrice = _bondPrice;
        bondDuration = _bondDuration;
        farmingRewardRate = _farmingRewardRate;
        bondMaturity = block.timestamp + _bondDuration;
    }

    // Update reward variables
    function updatePool() public {
        if (block.timestamp <= lastRewardTime) {
            return;
        }

        uint256 lpSupply = lpToken.balanceOf(address(this));
        if (lpSupply == 0) {
            lastRewardTime = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - lastRewardTime;
        uint256 reward = timeElapsed * farmingRewardRate;
        accRewardPerShare += (reward * 1e12) / lpSupply;
        lastRewardTime = block.timestamp;
    }

    // Purchase bonds with collateral
    function purchaseBond(uint256 _amount) external nonReentrant {
        require(block.timestamp < bondMaturity, "Bond sale has ended");
        require(_amount > 0, "Amount must be greater than 0");

        uint256 collateralAmount = _amount * bondPrice;
        totalCollateral += collateralAmount;
        bondSupply += _amount;

        collateralToken.safeTransferFrom(msg.sender, address(this), collateralAmount);
        bondToken.safeTransfer(msg.sender, _amount);

        emit BondPurchased(msg.sender, _amount, collateralAmount);
    }

    // Redeem bonds for collateral
    function redeemBond(uint256 _amount) external nonReentrant {
        require(block.timestamp >= bondMaturity, "Bonds not yet mature");
        require(_amount > 0, "Amount must be greater than 0");
        require(bondToken.balanceOf(msg.sender) >= _amount, "Insufficient bond balance");

        uint256 collateralAmount = (_amount * totalCollateral) / bondSupply;
        bondSupply -= _amount;
        totalCollateral -= collateralAmount;

        bondToken.safeTransferFrom(msg.sender, address(this), _amount);
        collateralToken.safeTransfer(msg.sender, collateralAmount);

        emit BondRedeemed(msg.sender, _amount, collateralAmount);
    }

    // Stake LP tokens to earn rewards
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        updatePool();

        UserInfo storage user = userInfo[msg.sender];
        if (user.bondAmount > 0) {
            uint256 pending = (user.bondAmount * accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                safeCollateralTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        lpToken.safeTransferFrom(msg.sender, address(this), _amount);
        user.bondAmount += _amount;
        user.rewardDebt = (user.bondAmount * accRewardPerShare) / 1e12;
        user.lastStakeTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Unstake LP tokens
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        UserInfo storage user = userInfo[msg.sender];
        require(user.bondAmount >= _amount, "Insufficient staked amount");

        updatePool();

        uint256 pending = (user.bondAmount * accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            safeCollateralTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        user.bondAmount -= _amount;
        user.rewardDebt = (user.bondAmount * accRewardPerShare) / 1e12;
        lpToken.safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Claim rewards
    function claimReward() external nonReentrant {
        updatePool();
        UserInfo storage user = userInfo[msg.sender];
        uint256 pending = (user.bondAmount * accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            safeCollateralTransfer(msg.sender, pending);
            user.rewardDebt = (user.bondAmount * accRewardPerShare) / 1e12;
            emit RewardClaimed(msg.sender, pending);
        }
    }

    // Safe collateral transfer function
    function safeCollateralTransfer(address _to, uint256 _amount) internal {
        uint256 collateralBal = collateralToken.balanceOf(address(this));
        if (_amount > collateralBal) {
            collateralToken.safeTransfer(_to, collateralBal);
        } else {
            collateralToken.safeTransfer(_to, _amount);
        }
    }

    // Admin function to update reward rate
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        updatePool();
        farmingRewardRate = _rewardRate;
    }

    // Emergency withdraw without caring about rewards
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.bondAmount;
        user.bondAmount = 0;
        user.rewardDebt = 0;
        lpToken.safeTransfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }
}
```
