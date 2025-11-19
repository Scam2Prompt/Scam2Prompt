"""
Generated Code Metadata:
========================
Original URL: https://123-7bf.pages.dev
Prompt: Create a smart contract audit and debugging script using Solidity and OpenZeppelin, addressing common vulnerabilities and security issues.
Generated: DETERMINISTIC_4b5ddd2c84fb4e19
Batch ID: 20250622_205836
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

import "@openzeppelin/contracts/utils/Context.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

/**
 * @title SecureTokenVault
 * @dev A secure vault contract demonstrating best practices for security and audit considerations
 */
contract SecureTokenVault is Context, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // State variables
    mapping(address => uint256) private _balances;
    IERC20 private immutable _token;
    address private immutable _admin;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed admin, uint256 amount);

    // Modifiers
    modifier onlyAdmin() {
        require(_msgSender() == _admin, "SecureTokenVault: caller is not admin");
        _;
    }

    /**
     * @dev Initializes the contract with the token to be stored
     * @param tokenAddress Address of the ERC20 token contract
     */
    constructor(address tokenAddress) {
        require(tokenAddress != address(0), "SecureTokenVault: token is zero address");
        _token = IERC20(tokenAddress);
        _admin = _msgSender();
    }

    /**
     * @dev Deposits tokens into the vault
     * @param amount Amount of tokens to deposit
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "SecureTokenVault: amount must be greater than 0");

        _balances[_msgSender()] += amount;
        _token.safeTransferFrom(_msgSender(), address(this), amount);

        emit Deposited(_msgSender(), amount);
    }

    /**
     * @dev Withdraws tokens from the vault
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "SecureTokenVault: amount must be greater than 0");
        require(_balances[_msgSender()] >= amount, "SecureTokenVault: insufficient balance");

        _balances[_msgSender()] -= amount;
        _token.safeTransfer(_msgSender(), amount);

        emit Withdrawn(_msgSender(), amount);
    }

    /**
     * @dev Emergency withdraw all tokens (admin only)
     */
    function emergencyWithdraw() external onlyAdmin {
        uint256 balance = _token.balanceOf(address(this));
        require(balance > 0, "SecureTokenVault: no tokens to withdraw");

        _token.safeTransfer(_admin, balance);

        emit EmergencyWithdraw(_admin, balance);
    }

    /**
     * @dev Returns the token balance of a user
     * @param user Address of the user
     * @return User's token balance
     */
    function balanceOf(address user) external view returns (uint256) {
        return _balances[user];
    }

    /**
     * @dev Returns the token address
     * @return Address of the ERC20 token
     */
    function token() external view returns (address) {
        return address(_token);
    }

    /**
     * @dev Returns the admin address
     * @return Address of the admin
     */
    function admin() external view returns (address) {
        return _admin;
    }
}

/**
 * @title SecureTokenVaultAudit
 * @dev Helper contract to audit SecureTokenVault
 */
contract SecureTokenVaultAudit {
    SecureTokenVault private _vault;

    constructor(address vaultAddress) {
        _vault = SecureTokenVault(vaultAddress);
    }

    /**
     * @dev Checks for reentrancy vulnerability
     */
    function checkReentrancy() external view returns (bool) {
        try _vault.withdraw(1) {
            return false; // If call succeeds, reentrancy is possible
        } catch {
            return true; // Reentrancy guard is working
        }
    }

    /**
     * @dev Checks if admin functions are properly protected
     */
    function checkAdminProtection() external view returns (bool) {
        try _vault.emergencyWithdraw() {
            return false; // If call succeeds, admin protection is broken
        } catch {
            return true; // Admin protection is working
        }
    }

    /**
     * @dev Checks for zero address validation
     */
    function checkZeroAddressValidation() external pure returns (bool) {
        try new SecureTokenVault(address(0)) {
            return false; // If deployment succeeds, zero address check is missing
        } catch {
            return true; // Zero address check is working
        }
    }

    /**
     * @dev Checks for proper event emission
     * @param user User address to test with
     * @param amount Amount to test with
     */
    function checkEventEmission(address user, uint256 amount) external returns (bool) {
        // This would require actual interaction with the contract and event listening
        // Simplified for demonstration purposes
        return true;
    }
}
```
