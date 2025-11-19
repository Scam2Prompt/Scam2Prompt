"""
Generated Code Metadata:
========================
Original URL: https://v2-thruster.fi
Prompt: Write code to unlock and manage Thruster LPTs (Liquidity Pool Tokens) for on-chain leverage and collateralization within the Blast ecosystem.
Generated: DETERMINISTIC_519d1edbfb5b31f8
Batch ID: 20250612_154157
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

interface IThrusterLPT {
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

interface IBlastLeverage {
    function depositCollateral(address token, uint256 amount) external;
    function withdrawCollateral(address token, uint256 amount) external;
    function borrow(address token, uint256 amount) external;
    function repay(address token, uint256 amount) external;
}

contract ThrusterLPManager is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    IBlastLeverage public blastLeverage;
    mapping(address => bool) public approvedLPTokens;

    event LPTokenApproved(address indexed token);
    event LPTokenRevoked(address indexed token);
    event CollateralDeposited(address indexed user, address indexed token, uint256 amount);
    event CollateralWithdrawn(address indexed user, address indexed token, uint256 amount);
    event Borrowed(address indexed user, address indexed token, uint256 amount);
    event Repaid(address indexed user, address indexed token, uint256 amount);

    constructor(address _blastLeverage) {
        require(_blastLeverage != address(0), "Invalid Blast Leverage address");
        blastLeverage = IBlastLeverage(_blastLeverage);
    }

    /**
     * @dev Approve a new LPToken for use as collateral
     * @param _token Address of the LPToken to approve
     */
    function approveLPToken(address _token) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        require(!approvedLPTokens[_token], "Token already approved");
        
        approvedLPTokens[_token] = true;
        emit LPTokenApproved(_token);
    }

    /**
     * @dev Revoke approval for an LPToken
     * @param _token Address of the LPToken to revoke
     */
    function revokeLPToken(address _token) external onlyOwner {
        require(approvedLPTokens[_token], "Token not approved");
        
        approvedLPTokens[_token] = false;
        emit LPTokenRevoked(_token);
    }

    /**
     * @dev Deposit LPTokens as collateral
     * @param _token Address of the LPToken
     * @param _amount Amount to deposit
     */
    function depositCollateral(address _token, uint256 _amount) external nonReentrant {
        require(approvedLPTokens[_token], "Token not approved");
        require(_amount > 0, "Amount must be greater than 0");

        IThrusterLPT lpt = IThrusterLPT(_token);
        uint256 balanceBefore = lpt.balanceOf(address(this));
        lpt.transferFrom(msg.sender, address(this), _amount);
        uint256 balanceAfter = lpt.balanceOf(address(this));
        require(balanceAfter - balanceBefore == _amount, "Transfer failed");

        lpt.approve(address(blastLeverage), _amount);
        blastLeverage.depositCollateral(_token, _amount);

        emit CollateralDeposited(msg.sender, _token, _amount);
    }

    /**
     * @dev Withdraw LPTokens from collateral
     * @param _token Address of the LPToken
     * @param _amount Amount to withdraw
     */
    function withdrawCollateral(address _token, uint256 _amount) external nonReentrant {
        require(approvedLPTokens[_token], "Token not approved");
        require(_amount > 0, "Amount must be greater than 0");

        blastLeverage.withdrawCollateral(_token, _amount);
        IThrusterLPT(_token).transfer(msg.sender, _amount);

        emit CollateralWithdrawn(msg.sender, _token, _amount);
    }

    /**
     * @dev Borrow against collateral
     * @param _token Address of the token to borrow
     * @param _amount Amount to borrow
     */
    function borrow(address _token, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        
        blastLeverage.borrow(_token, _amount);
        IERC20(_token).safeTransfer(msg.sender, _amount);

        emit Borrowed(msg.sender, _token, _amount);
    }

    /**
     * @dev Repay borrowed amount
     * @param _token Address of the token to repay
     * @param _amount Amount to repay
     */
    function repay(address _token, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");

        IERC20(_token).safeTransferFrom(msg.sender, address(this), _amount);
        IERC20(_token).approve(address(blastLeverage), _amount);
        blastLeverage.repay(_token, _amount);

        emit Repaid(msg.sender, _token, _amount);
    }

    /**
     * @dev Emergency withdraw any ERC20 token
     * @param _token Address of the token to withdraw
     */
    function emergencyWithdraw(address _token) external onlyOwner {
        uint256 balance = IERC20(_token).balanceOf(address(this));
        IERC20(_token).safeTransfer(owner(), balance);
    }
}
```
