"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wap.xushuishiwu.cn
Prompt: Develop a smart contract in Solidity that interacts with the MetaMask wallet for token transfers, ensuring the contract supports ERC-20 standards, as mentioned in the "MetaMask钱包虚拟币" section.
Generated: DETERMINISTIC_f7d925ad378d407a
Batch ID: 20250612_142608
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

// Import the ERC-20 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract TokenTransfer {
    // Event emitted when tokens are transferred successfully
    event TokenTransferred(address indexed from, address indexed to, uint256 amount);

    // Constructor - Optional setup can be added here if needed
    constructor() {}

    /**
     * @notice Transfers ERC-20 tokens from the caller's wallet to a specified recipient.
     * @dev Ensure the caller has approved the contract to spend tokens before calling this function.
     * @param tokenAddress Address of the ERC-20 token contract.
     * @param recipient Address of the recipient to whom tokens will be sent.
     * @param amount Number of tokens to transfer.
     */
    function transferTokens(address tokenAddress, address recipient, uint256 amount) external {
        // Validate input parameters
        require(tokenAddress != address(0), "Invalid token address");
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Reference the ERC-20 contract
        IERC20 token = IERC20(tokenAddress);

        // Check the sender's balance
        uint256 senderBalance = token.balanceOf(msg.sender);
        require(senderBalance >= amount, "Insufficient balance");

        // Perform the transfer
        bool success = token.transferFrom(msg.sender, recipient, amount);
        require(success, "Token transfer failed");

        // Emit the transfer event
        emit TokenTransferred(msg.sender, recipient, amount);
    }

    /**
     * @notice Checks the token balance of a specified address.
     * @param tokenAddress Address of the ERC-20 token contract.
     * @param account Address of the account to check balance for.
     * @return The token balance of the specified account.
     */
    function getTokenBalance(address tokenAddress, address account) external view returns (uint256) {
        // Validate input parameters
        require(tokenAddress != address(0), "Invalid token address");
        require(account != address(0), "Invalid account address");

        // Reference the ERC-20 contract
        IERC20 token = IERC20(tokenAddress);

        // Return the balance of the account
        return token.balanceOf(account);
    }
}
```
