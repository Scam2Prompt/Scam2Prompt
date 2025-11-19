"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omninetworkclub.xyz
Prompt: Generate a code example for creating a smart contract on the Binance Smart Chain that supports the FEG token migration process.
Generated: DETERMINISTIC_500a993944ab46a5
Batch ID: 20250612_155752
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
 * @title FEG Token Migration Smart Contract
 * @dev This contract supports the migration process for FEG tokens on Binance Smart Chain.
 * It allows token holders to swap their old tokens for new ones in a secure and controlled manner.
 */
contract FEGTokenMigration {
    // Address of the old FEG token contract
    address public oldTokenAddress;

    // Address of the new FEG token contract
    address public newTokenAddress;

    // Owner of the migration contract
    address public owner;

    // Event emitted when a migration occurs
    event TokensMigrated(address indexed user, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Unauthorized: Only owner can execute this.");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the old and new token addresses.
     * @param _oldTokenAddress Address of the old FEG token contract.
     * @param _newTokenAddress Address of the new FEG token contract.
     */
    constructor(address _oldTokenAddress, address _newTokenAddress) {
        require(_oldTokenAddress != address(0), "Invalid old token address.");
        require(_newTokenAddress != address(0), "Invalid new token address.");
        oldTokenAddress = _oldTokenAddress;
        newTokenAddress = _newTokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Allows token holders to migrate their tokens from the old contract to the new one.
     * @param amount Number of tokens to migrate.
     */
    function migrateTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero.");

        // Interact with the old token contract to transfer tokens to this contract
        IERC20 oldToken = IERC20(oldTokenAddress);
        require(
            oldToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer from old contract failed."
        );

        // Interact with the new token contract to mint new tokens to the user
        IERC20 newToken = IERC20(newTokenAddress);
        require(
            newToken.transfer(msg.sender, amount),
            "Token transfer to new contract failed."
        );

        emit TokensMigrated(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to withdraw tokens remaining in the contract (old or new tokens).
     * @param tokenAddress Address of the token to withdraw.
     * @param amount Number of tokens to withdraw.
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero.");
        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(owner, amount), "Withdrawal failed.");
    }

    /**
     * @dev Allows the owner to update the old or new token contract address.
     * @param _oldTokenAddress New address of the old FEG token contract.
     * @param _newTokenAddress New address of the new FEG token contract.
     */
    function updateTokenAddresses(address _oldTokenAddress, address _newTokenAddress) external onlyOwner {
        require(_oldTokenAddress != address(0), "Invalid old token address.");
        require(_newTokenAddress != address(0), "Invalid new token address.");
        oldTokenAddress = _oldTokenAddress;
        newTokenAddress = _newTokenAddress;
    }
}

// Interface for interacting with ERC20 tokens
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
