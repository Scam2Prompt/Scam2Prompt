"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularity-dao.pages.dev
Prompt: Develop a smart contract snippet that facilitates token migration from RJV OLD to RJV NEW, ensuring compatibility with the SingularityDAO system.
Generated: DETERMINISTIC_e87b9a009d7b3718
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing required OpenZeppelin contracts for ERC20 functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenMigration
 * @dev Smart contract to facilitate migration of tokens from RJV OLD to RJV NEW
 */
contract TokenMigration is Ownable {
    using SafeERC20 for IERC20;

    // Address of the old token contract (RJV OLD)
    IERC20 public oldToken;
    // Address of the new token contract (RJV NEW)
    IERC20 public newToken;

    // Event emitted when tokens are migrated
    event TokensMigrated(address indexed user, uint256 amount);

    // Mapping to track migrated balances
    mapping(address => uint256) private _migratedAmounts;

    /**
     * @dev Constructor to initialize the old and new token addresses
     * @param _oldToken Address of the old token contract
     * @param _newToken Address of the new token contract
     */
    constructor(address _oldToken, address _newToken) {
        require(_oldToken != address(0), "Old token address cannot be zero");
        require(_newToken != address(0), "New token address cannot be zero");

        oldToken = IERC20(_oldToken);
        newToken = IERC20(_newToken);
    }

    /**
     * @dev Function to migrate tokens from RJV OLD to RJV NEW
     * @param amount The amount of old tokens to migrate
     */
    function migrateTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(_migratedAmounts[msg.sender] + amount <= oldToken.balanceOf(msg.sender), "Insufficient old token balance");

        // Transfer OLD tokens from the user to this contract
        oldToken.safeTransferFrom(msg.sender, address(this), amount);

        // Calculate the amount of new tokens to mint (1:1 ratio)
        uint256 newTokenAmount = amount;

        // Transfer NEW tokens to the user
        newToken.safeTransfer(msg.sender, newTokenAmount);

        // Update the migrated amount for the user
        _migratedAmounts[msg.sender] += amount;

        // Emit the migration event
        emit TokensMigrated(msg.sender, amount);
    }

    /**
     * @dev Function to retrieve the amount of old tokens a user has migrated
     * @param user The address of the user
     * @return The amount of old tokens migrated by the user
     */
    function getMigratedAmount(address user) external view returns (uint256) {
        return _migratedAmounts[user];
    }

    /**
     * @dev Function to withdraw any tokens accidentally sent to the contract
     * @param tokenAddress The address of the token to withdraw
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Token address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");

        IERC20(tokenAddress).safeTransfer(msg.sender, amount);
    }
}
```
