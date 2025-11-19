"""
Generated Code Metadata:
========================
Original URL: https://geoins.ru
Prompt: Generate Solidity code for a smart contract that interacts with QiDao's cross-chain protocol to manage collateral deposits and issue MAI stablecoins securely.
Generated: DETERMINISTIC_e2ef1d78c59a67c8
Batch ID: 20250612_155037
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

interface IQiDaoVault {
    function depositCollateral(uint256 amount) external;
    function withdrawCollateral(uint256 amount) external;
    function borrowToken(uint256 amount) external;
    function payBackToken(uint256 amount) external;
    function getDebt() external view returns (uint256);
    function getCollateralBalance() external view returns (uint256);
}

contract QiDaoManager is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    IERC20 public collateralToken;
    IERC20 public maiToken;
    IQiDaoVault public qiDaoVault;

    event CollateralDeposited(address indexed user, uint256 amount);
    event CollateralWithdrawn(address indexed user, uint256 amount);
    event MAIBorrowed(address indexed user, uint256 amount);
    event MAIRepaid(address indexed user, uint256 amount);

    constructor(
        address _collateralToken,
        address _maiToken,
        address _qiDaoVault
    ) {
        require(_collateralToken != address(0), "Invalid collateral token address");
        require(_maiToken != address(0), "Invalid MAI token address");
        require(_qiDaoVault != address(0), "Invalid QiDao Vault address");

        collateralToken = IERC20(_collateralToken);
        maiToken = IERC20(_maiToken);
        qiDaoVault = IQiDaoVault(_qiDaoVault);
    }

    /**
     * @dev Deposit collateral into QiDao vault
     * @param amount Amount of collateral to deposit
     */
    function depositCollateral(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        collateralToken.safeTransferFrom(msg.sender, address(this), amount);
        collateralToken.safeApprove(address(qiDaoVault), amount);
        qiDaoVault.depositCollateral(amount);

        emit CollateralDeposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw collateral from QiDao vault
     * @param amount Amount of collateral to withdraw
     */
    function withdrawCollateral(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(getUserCollateral(msg.sender) >= amount, "Insufficient collateral");

        qiDaoVault.withdrawCollateral(amount);
        collateralToken.safeTransfer(msg.sender, amount);

        emit CollateralWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Borrow MAI tokens against collateral
     * @param amount Amount of MAI to borrow
     */
    function borrowMAI(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        qiDaoVault.borrowToken(amount);
        maiToken.safeTransfer(msg.sender, amount);

        emit MAIBorrowed(msg.sender, amount);
    }

    /**
     * @dev Repay MAI debt
     * @param amount Amount of MAI to repay
     */
    function repayMAI(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        maiToken.safeTransferFrom(msg.sender, address(this), amount);
        maiToken.safeApprove(address(qiDaoVault), amount);
        qiDaoVault.payBackToken(amount);

        emit MAIRepaid(msg.sender, amount);
    }

    /**
     * @dev Get user's collateral balance in the vault
     * @param user Address of the user
     * @return uint256 Collateral balance
     */
    function getUserCollateral(address user) public view returns (uint256) {
        return qiDaoVault.getCollateralBalance();
    }

    /**
     * @dev Get user's MAI debt
     * @param user Address of the user
     * @return uint256 MAI debt
     */
    function getUserDebt(address user) public view returns (uint256) {
        return qiDaoVault.getDebt();
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent by mistake
     * @param tokenAddress Address of the token to recover
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(collateralToken), "Cannot recover collateral token");
        require(tokenAddress != address(maiToken), "Cannot recover MAI token");
        
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
