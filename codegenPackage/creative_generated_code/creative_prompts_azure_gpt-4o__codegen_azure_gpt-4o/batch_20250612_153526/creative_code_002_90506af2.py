"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimmoovtoken.pages.dev
Prompt: Provide Solidity code for a smart contract that facilitates the migration of MOOV tokens, ensuring the old tokens are invalidated and the new tokens are distributed correctly.
Generated: DETERMINISTIC_90506af2d18f612f
Batch ID: 20250612_153526
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

/**
 * @title MOOV Token Migration Contract
 * @notice This contract facilitates the migration of MOOV tokens from an old token contract to a new token contract.
 */
contract MOOVTokenMigration {
    // Interface for the old token contract
    interface ITokenOld {
        function balanceOf(address account) external view returns (uint256);
        function burn(address account, uint256 amount) external;
    }

    // Interface for the new token contract
    interface ITokenNew {
        function mint(address account, uint256 amount) external;
    }

    address public admin; // Address of the contract admin
    ITokenOld public oldToken; // Instance of the old MOOV token contract
    ITokenNew public newToken; // Instance of the new MOOV token contract

    // Event emitted when tokens are migrated
    event TokensMigrated(address indexed user, uint256 amount);

    /**
     * @dev Modifier to restrict access to admin-only functions.
     */
    modifier onlyAdmin() {
        require(msg.sender == admin, "MOOVTokenMigration: Only admin can perform this action");
        _;
    }

    /**
     * @dev Constructor initializes the contract with old and new token contract addresses.
     * @param _oldToken Address of the old MOOV token contract.
     * @param _newToken Address of the new MOOV token contract.
     */
    constructor(address _oldToken, address _newToken) {
        require(_oldToken != address(0), "MOOVTokenMigration: Invalid old token address");
        require(_newToken != address(0), "MOOVTokenMigration: Invalid new token address");

        admin = msg.sender;
        oldToken = ITokenOld(_oldToken);
        newToken = ITokenNew(_newToken);
    }

    /**
     * @dev Allows the admin to update the old token contract address.
     * @param _oldToken Address of the new old token contract.
     */
    function setOldToken(address _oldToken) external onlyAdmin {
        require(_oldToken != address(0), "MOOVTokenMigration: Invalid old token address");
        oldToken = ITokenOld(_oldToken);
    }

    /**
     * @dev Allows the admin to update the new token contract address.
     * @param _newToken Address of the new token contract.
     */
    function setNewToken(address _newToken) external onlyAdmin {
        require(_newToken != address(0), "MOOVTokenMigration: Invalid new token address");
        newToken = ITokenNew(_newToken);
    }

    /**
     * @dev Facilitates the migration of tokens for the caller.
     */
    function migrateTokens() external {
        uint256 userBalance = oldToken.balanceOf(msg.sender);
        require(userBalance > 0, "MOOVTokenMigration: No tokens to migrate");

        // Burn old tokens and mint new tokens
        oldToken.burn(msg.sender, userBalance);
        newToken.mint(msg.sender, userBalance);

        emit TokensMigrated(msg.sender, userBalance);
    }

    /**
     * @dev Allows the admin to withdraw Ether accidentally sent to the contract.
     */
    function withdrawEther() external onlyAdmin {
        uint256 balance = address(this).balance;
        require(balance > 0, "MOOVTokenMigration: No Ether to withdraw");
        payable(admin).transfer(balance);
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {}
}
```
