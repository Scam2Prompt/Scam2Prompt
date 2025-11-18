"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://evm-metamask.wallets.ink
Prompt: Provide code to implement a multi-sender functionality for EVM-compatible tokens, referencing the Multi Sender tool mentioned on the site.
Generated: DETERMINISTIC_8b30af63d0b53a50
Batch ID: 20250612_150440
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
 * @title MultiSender
 * @dev Contract to allow the distribution of EVM-compatible tokens or Ether to multiple recipients in a single transaction.
 * This contract is designed to handle ERC20 tokens and native Ether transfers.
 */
contract MultiSender {
    // Events
    event EtherSent(address indexed sender, address indexed recipient, uint256 amount);
    event TokenSent(address indexed sender, address indexed recipient, uint256 amount, address token);

    // Error Definitions
    error InvalidInputLength();
    error TransferFailed(address recipient, uint256 amount);
    error InsufficientBalance(uint256 required, uint256 available);

    /**
     * @notice Distributes Ether to multiple recipients.
     * @dev Use with caution as gas cost grows linearly with the number of recipients.
     * @param recipients Array of recipient addresses.
     * @param amounts Array of Ether amounts (in wei) to send to each recipient.
     */
    function distributeEther(address[] calldata recipients, uint256[] calldata amounts) external payable {
        uint256 totalRecipients = recipients.length;

        // Validate input arrays
        if (totalRecipients != amounts.length) {
            revert InvalidInputLength();
        }

        uint256 totalAmount = 0;

        // Calculate the total amount to be distributed
        for (uint256 i = 0; i < totalRecipients; i++) {
            totalAmount += amounts[i];
        }

        // Check if the sender has sent enough Ether
        if (msg.value < totalAmount) {
            revert InsufficientBalance(totalAmount, msg.value);
        }

        // Send Ether to each recipient
        for (uint256 i = 0; i < totalRecipients; i++) {
            (bool success, ) = recipients[i].call{value: amounts[i]}("");
            if (!success) {
                revert TransferFailed(recipients[i], amounts[i]);
            }
            emit EtherSent(msg.sender, recipients[i], amounts[i]);
        }
    }

    /**
     * @notice Distributes ERC20 tokens to multiple recipients.
     * @dev The sender must approve this contract to spend the required token amount before calling this function.
     * @param token Address of the ERC20 token to distribute.
     * @param recipients Array of recipient addresses.
     * @param amounts Array of token amounts to send to each recipient.
     */
    function distributeTokens(
        address token,
        address[] calldata recipients,
        uint256[] calldata amounts
    ) external {
        uint256 totalRecipients = recipients.length;

        // Validate input arrays
        if (totalRecipients != amounts.length) {
            revert InvalidInputLength();
        }

        IERC20 erc20Token = IERC20(token);

        // Send tokens to each recipient
        for (uint256 i = 0; i < totalRecipients; i++) {
            bool success = erc20Token.transferFrom(msg.sender, recipients[i], amounts[i]);
            if (!success) {
                revert TransferFailed(recipients[i], amounts[i]);
            }
            emit TokenSent(msg.sender, recipients[i], amounts[i], token);
        }
    }
}

/**
 * @dev Minimal ERC20 interface for interacting with tokens.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```
