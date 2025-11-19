"""
Generated Code Metadata:
========================
Original URL: https://v1-sturdy.pages.dev
Prompt: How can I implement isolated lending with shared liquidity using the Sturdy platform?
Generated: DETERMINISTIC_424fb4bb211d5753
Batch ID: 20250612_161420
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

interface ISturdyLendingPool {
    function deposit(address asset, uint256 amount, address onBehalfOf, uint16 referralCode) external;
    function withdraw(address asset, uint256 amount, address to) external;
    function borrow(address asset, uint256 amount, uint256 interestRateMode, uint16 referralCode, address onBehalfOf) external;
    function repay(address asset, uint256 amount, uint256 rateMode, address onBehalfOf) external;
}

contract IsolatedLendingWithSharedLiquidity is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    ISturdyLendingPool public immutable sturdyLendingPool;
    mapping(address => bool) public supportedAssets;
    mapping(address => mapping(address => uint256)) public userDeposits;

    event AssetSupported(address indexed asset, bool supported);
    event Deposited(address indexed user, address indexed asset, uint256 amount);
    event Withdrawn(address indexed user, address indexed asset, uint256 amount);
    event Borrowed(address indexed user, address indexed asset, uint256 amount);
    event Repaid(address indexed user, address indexed asset, uint256 amount);

    constructor(address _sturdyLendingPool) {
        require(_sturdyLendingPool != address(0), "Invalid lending pool address");
        sturdyLendingPool = ISturdyLendingPool(_sturdyLendingPool);
    }

    function setSupportedAsset(address asset, bool supported) external onlyOwner {
        supportedAssets[asset] = supported;
        emit AssetSupported(asset, supported);
    }

    function deposit(address asset, uint256 amount) external nonReentrant {
        require(supportedAssets[asset], "Asset not supported");
        require(amount > 0, "Amount must be greater than 0");

        IERC20(asset).safeTransferFrom(msg.sender, address(this), amount);
        IERC20(asset).approve(address(sturdyLendingPool), amount);
        sturdyLendingPool.deposit(asset, amount, msg.sender, 0);

        userDeposits[msg.sender][asset] += amount;
        emit Deposited(msg.sender, asset, amount);
    }

    function withdraw(address asset, uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(userDeposits[msg.sender][asset] >= amount, "Insufficient balance");

        sturdyLendingPool.withdraw(asset, amount, msg.sender);
        userDeposits[msg.sender][asset] -= amount;
        emit Withdrawn(msg.sender, asset, amount);
    }

    function borrow(address asset, uint256 amount, uint256 interestRateMode) external nonReentrant {
        require(supportedAssets[asset], "Asset not supported");
        require(amount > 0, "Amount must be greater than 0");

        sturdyLendingPool.borrow(asset, amount, interestRateMode, 0, msg.sender);
        emit Borrowed(msg.sender, asset, amount);
    }

    function repay(address asset, uint256 amount, uint256 interestRateMode) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        IERC20(asset).safeTransferFrom(msg.sender, address(this), amount);
        IERC20(asset).approve(address(sturdyLendingPool), amount);
        sturdyLendingPool.repay(asset, amount, interestRateMode, msg.sender);
        emit Repaid(msg.sender, asset, amount);
    }

    function getUserDeposit(address user, address asset) external view returns (uint256) {
        return userDeposits[user][asset];
    }
}
```
