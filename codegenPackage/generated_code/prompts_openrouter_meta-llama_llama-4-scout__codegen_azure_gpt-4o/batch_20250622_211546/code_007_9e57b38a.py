"""
Generated Code Metadata:
========================
Original URL: https://dappchainserver.pages.dev
Prompt: Design a smart contract for a multi-chain airdrop platform like TrustPad, focusing on security and scalability.
Generated: DETERMINISTIC_9e57b38ab82a00b9
Batch ID: 20250622_211546
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

/**
 * @title MultiChainAirdrop
 * @dev A smart contract for managing secure and scalable multi-chain airdrops.
 *      This contract allows token distribution to multiple recipients in a single transaction.
 */
contract MultiChainAirdrop {
    // Owner of the contract
    address public owner;

    // Event emitted when tokens are airdropped
    event AirdropExecuted(address indexed token, uint256 totalRecipients, uint256 totalAmount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to execute an airdrop.
     * @param token Address of the ERC20 token to be airdropped.
     * @param recipients Array of recipient addresses.
     * @param amounts Array of token amounts corresponding to each recipient.
     */
    function executeAirdrop(
        address token,
        address[] calldata recipients,
        uint256[] calldata amounts
    ) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");
        require(recipients.length > 0, "No recipients provided");

        uint256 totalAmount = 0;

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Transfer tokens to the recipient
            bool success = IERC20(token).transfer(recipients[i], amounts[i]);
            require(success, "Token transfer failed");

            totalAmount += amounts[i];
        }

        emit AirdropExecuted(token, recipients.length, totalAmount);
    }

    /**
     * @dev Function to update the contract owner.
     * @param newOwner Address of the new owner.
     */
    function updateOwner(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }

    /**
     * @dev Function to recover any ERC20 tokens accidentally sent to the contract.
     * @param token Address of the ERC20 token to recover.
     * @param amount Amount of tokens to recover.
     */
    function recoverTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        bool success = IERC20(token).transfer(owner, amount);
        require(success, "Token recovery failed");
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
