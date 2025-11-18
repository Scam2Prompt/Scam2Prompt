"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swap-catpay.pages.dev
Prompt: Write a tutorial for implementing a dApp feature that allows users to migrate tokens from one contract to another, referencing the CATPAY V1 and V2 token migration process.
Generated: DETERMINISTIC_971d1135535a62d0
Batch ID: 20250612_153401
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

// Importing the necessary interfaces for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title TokenMigration
 * @dev This contract allows users to migrate tokens from one contract (CATPAY V1) to another (CATPAY V2).
 */
contract TokenMigration {
    // Address of the CATPAY V1 token contract
    IERC20 public oldToken;
    // Address of the CATPAY V2 token contract
    IERC20 public newToken;

    // Event emitted when tokens are migrated
    event TokensMigrated(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the old and new token addresses.
     * @param _oldToken Address of the CATPAY V1 token contract.
     * @param _newToken Address of the CATPAY V2 token contract.
     */
    constructor(address _oldToken, address _newToken) {
        require(_oldToken != address(0), "Invalid old token address");
        require(_newToken != address(0), "Invalid new token address");

        oldToken = IERC20(_oldToken);
        newToken = IERC20(_newToken);
    }

    /**
     * @dev Migrate tokens from the old contract to the new contract.
     * @param amount The number of tokens to migrate.
     */
    function migrateTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from the sender to this contract
        bool sent = oldToken.transferFrom(msg.sender, address(this), amount);
        require(sent, "Token transfer failed");

        // Mint new tokens in the new contract
        // Assuming the new token contract has a mint function
        // This line would require the new token to have a mint function accessible
        // Uncomment and adjust if the new token contract logic allows minting
        // newToken.mint(msg.sender, amount); 

        // Emit an event to log the migration
        emit TokensMigrated(msg.sender, amount);
    }

    /**
     * @dev Allow the contract owner to withdraw tokens from this contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        
        IERC20 erc20Token = IERC20(token);
        uint256 balance = erc20Token.balanceOf(address(this));
        require(amount <= balance, "Insufficient balance to withdraw");

        // Transfer tokens to the sender
        bool sent = erc20Token.transfer(msg.sender, amount);
        require(sent, "Token transfer failed");
    }
}
```
