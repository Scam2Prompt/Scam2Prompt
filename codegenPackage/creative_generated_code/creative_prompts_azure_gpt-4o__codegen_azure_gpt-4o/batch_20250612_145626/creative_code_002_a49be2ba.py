"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magiccraft-migrate.pages.dev
Prompt: Create a smart contract for MagicCraft that enables token migration for $MCRT, following the guidelines outlined in the MagicCraft whitepaper.
Generated: DETERMINISTIC_a49be2baf9942769
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title MagicCraft Token Migration Contract
 * @notice This contract allows for the migration of $MCRT tokens as outlined in the MagicCraft whitepaper.
 * @author MagicCraft
 */
contract MCRTTokenMigration {
    // Address of the old $MCRT token contract
    address public immutable oldToken;

    // Address of the new $MCRT token contract
    address public immutable newToken;

    // Address of the contract owner
    address public immutable owner;

    // Mapping to track users who have already migrated
    mapping(address => bool) public hasMigrated;

    /**
     * @notice Event emitted when a token migration is successful
     * @param user Address of the user who migrated tokens
     * @param amount Amount of tokens migrated
     */
    event TokensMigrated(address indexed user, uint256 amount);

    /**
     * @notice Modifier to restrict function access to only the owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @notice Constructor function to initialize the migration contract
     * @param _oldToken Address of the old $MCRT token contract
     * @param _newToken Address of the new $MCRT token contract
     */
    constructor(address _oldToken, address _newToken) {
        require(_oldToken != address(0), "Invalid old token address");
        require(_newToken != address(0), "Invalid new token address");

        oldToken = _oldToken;
        newToken = _newToken;
        owner = msg.sender;
    }

    /**
     * @notice Function to migrate $MCRT tokens from the old contract to the new contract
     * @dev Users must approve this contract to access their old token balance before calling this function
     */
    function migrateTokens() external {
        require(!hasMigrated[msg.sender], "Tokens already migrated for this address");

        uint256 userBalance = IERC20(oldToken).balanceOf(msg.sender);
        require(userBalance > 0, "User has no tokens to migrate");

        // Transfer tokens from the user to this contract (old token)
        bool oldTransfer = IERC20(oldToken).transferFrom(msg.sender, address(this), userBalance);
        require(oldTransfer, "Failed to transfer old tokens");

        // Mint equivalent tokens in the new contract
        bool newMint = IMCRTNewToken(newToken).mint(msg.sender, userBalance);
        require(newMint, "Failed to mint new tokens");

        // Mark user as migrated
        hasMigrated[msg.sender] = true;

        emit TokensMigrated(msg.sender, userBalance);
    }

    /**
     * @notice Function to withdraw any stuck tokens in this contract (failsafe for admin)
     * @dev Can only be called by the owner
     * @param token Address of the token to withdraw
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(IERC20(token).transfer(owner, amount), "Token withdrawal failed");
    }
}

/**
 * @title Interface for the old $MCRT token
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);

    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}

/**
 * @title Interface for the new $MCRT token, which includes a mint function
 */
interface IMCRTNewToken {
    function mint(address account, uint256 amount) external returns (bool);
}
```
