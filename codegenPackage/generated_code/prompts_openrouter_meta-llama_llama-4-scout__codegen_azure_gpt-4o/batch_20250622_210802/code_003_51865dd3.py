"""
Generated Code Metadata:
========================
Original URL: https://cctpbridge.vercel.app
Prompt: Generate a smart contract code for a CCTP-powered cross-chain bridge.
Generated: DETERMINISTIC_51865dd3bb3aa4db
Batch ID: 20250622_210802
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
 * @title CrossChainBridge
 * @dev A smart contract for a CCTP-powered cross-chain bridge.
 *      This contract allows users to transfer tokens between chains securely.
 */
contract CrossChainBridge {
    // Events
    event TokenDeposited(address indexed sender, uint256 amount, string destinationChain, string destinationAddress);
    event TokenWithdrawn(address indexed receiver, uint256 amount);

    // State variables
    address public owner; // Owner of the contract
    mapping(address => uint256) public balances; // User balances

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Deposit tokens into the bridge for cross-chain transfer.
     * @param destinationChain The name of the destination chain.
     * @param destinationAddress The address on the destination chain to receive the tokens.
     */
    function depositTokens(string memory destinationChain, string memory destinationAddress) external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Update user balance
        balances[msg.sender] += msg.value;

        // Emit deposit event
        emit TokenDeposited(msg.sender, msg.value, destinationChain, destinationAddress);
    }

    /**
     * @dev Withdraw tokens from the bridge (used for refunds or receiving tokens on the source chain).
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update user balance
        balances[msg.sender] -= amount;

        // Transfer tokens back to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Token transfer failed");

        // Emit withdrawal event
        emit TokenWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Emergency withdrawal by the owner to recover stuck funds.
     * @param amount The amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Token transfer failed");
    }

    /**
     * @dev Fallback function to accept Ether directly.
     */
    receive() external payable {}

    /**
     * @dev Get the contract's balance.
     * @return The balance of the contract in wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
