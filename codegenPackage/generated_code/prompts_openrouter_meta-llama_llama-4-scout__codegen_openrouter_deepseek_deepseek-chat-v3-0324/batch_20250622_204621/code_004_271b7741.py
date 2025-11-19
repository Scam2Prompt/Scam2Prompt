"""
Generated Code Metadata:
========================
Original URL: https://migrateold-vrdtoken.pages.dev
Prompt: "Design a simple token migration interface with steps for migrate, approve, and swap tokens for a ReFi protocol token like $REFI."
Generated: DETERMINISTIC_271b774102101f85
Batch ID: 20250622_204621
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

contract TokenMigrator is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Token interfaces
    IERC20 public oldToken;
    IERC20 public newToken;

    // Migration state
    bool public migrationActive;
    uint256 public migrationRate; // Number of new tokens per old token (e.g., 1:1 = 1e18)

    // Events
    event TokensApproved(address indexed user, uint256 amount);
    event TokensMigrated(address indexed user, uint256 oldAmount, uint256 newAmount);
    event MigrationStateChanged(bool active);
    event MigrationRateChanged(uint256 newRate);

    /**
     * @dev Constructor
     * @param _oldToken Address of the old token contract
     * @param _newToken Address of the new token contract
     * @param _migrationRate Initial migration rate (in wei)
     */
    constructor(
        address _oldToken,
        address _newToken,
        uint256 _migrationRate
    ) {
        require(_oldToken != address(0), "Invalid old token address");
        require(_newToken != address(0), "Invalid new token address");
        require(_migrationRate > 0, "Migration rate must be > 0");

        oldToken = IERC20(_oldToken);
        newToken = IERC20(_newToken);
        migrationRate = _migrationRate;
    }

    /**
     * @dev Approve old tokens for migration
     * @param amount Amount of tokens to approve
     */
    function approveMigration(uint256 amount) external {
        require(amount > 0, "Amount must be > 0");
        oldToken.safeApprove(address(this), amount);
        emit TokensApproved(msg.sender, amount);
    }

    /**
     * @dev Migrate old tokens to new tokens
     * @param amount Amount of old tokens to migrate
     */
    function migrateTokens(uint256 amount) external nonReentrant {
        require(migrationActive, "Migration is not active");
        require(amount > 0, "Amount must be > 0");

        uint256 newTokenAmount = amount * migrationRate / 1e18;
        require(newToken.balanceOf(address(this)) >= newTokenAmount, "Insufficient new token balance");

        // Transfer old tokens from user
        oldToken.safeTransferFrom(msg.sender, address(this), amount);

        // Transfer new tokens to user
        newToken.safeTransfer(msg.sender, newTokenAmount);

        emit TokensMigrated(msg.sender, amount, newTokenAmount);
    }

    /**
     * @dev Toggle migration state
     * @param active Whether migration should be active
     */
    function setMigrationState(bool active) external onlyOwner {
        migrationActive = active;
        emit MigrationStateChanged(active);
    }

    /**
     * @dev Update migration rate
     * @param newRate New migration rate (in wei)
     */
    function setMigrationRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Migration rate must be > 0");
        migrationRate = newRate;
        emit MigrationRateChanged(newRate);
    }

    /**
     * @dev Withdraw any remaining old tokens (after migration period)
     */
    function withdrawOldTokens() external onlyOwner {
        uint256 balance = oldToken.balanceOf(address(this));
        require(balance > 0, "No old tokens to withdraw");
        oldToken.safeTransfer(owner(), balance);
    }

    /**
     * @dev Withdraw any remaining new tokens (in case of emergency)
     */
    function withdrawNewTokens() external onlyOwner {
        uint256 balance = newToken.balanceOf(address(this));
        require(balance > 0, "No new tokens to withdraw");
        newToken.safeTransfer(owner(), balance);
    }

    /**
     * @dev Get user's approved amount
     * @param user Address to check
     */
    function getApprovedAmount(address user) external view returns (uint256) {
        return oldToken.allowance(user, address(this));
    }
}
```
