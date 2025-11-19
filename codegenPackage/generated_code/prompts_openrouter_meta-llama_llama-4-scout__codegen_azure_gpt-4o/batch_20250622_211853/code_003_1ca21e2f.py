"""
Generated Code Metadata:
========================
Original URL: https://across-to.com
Prompt: Implement a smart contract using Solidity that utilizes Across Protocol's optimized routing for cross-chain transactions.
Generated: DETERMINISTIC_1ca21e2fcd5caf5a
Batch ID: 20250622_211853
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

// Import interfaces for Across Protocol (assume these are available in the project)
import "@across-protocol/interfaces/IAcrossSpokePool.sol";

/// @title CrossChainTransactionManager
/// @notice A smart contract to facilitate cross-chain transactions using Across Protocol's optimized routing.
contract CrossChainTransactionManager {
    // Address of the Across SpokePool contract
    address public immutable spokePool;

    /// @notice Emitted when a cross-chain transaction is initiated
    /// @param sender The address initiating the transaction
    /// @param recipient The address receiving the funds on the destination chain
    /// @param amount The amount of tokens being sent
    /// @param destinationChainId The ID of the destination chain
    event CrossChainTransactionInitiated(
        address indexed sender,
        address indexed recipient,
        uint256 amount,
        uint256 destinationChainId
    );

    /// @notice Constructor to set the Across SpokePool address
    /// @param _spokePool The address of the Across SpokePool contract
    constructor(address _spokePool) {
        require(_spokePool != address(0), "Invalid SpokePool address");
        spokePool = _spokePool;
    }

    /// @notice Initiates a cross-chain transaction using Across Protocol
    /// @param recipient The address to receive the funds on the destination chain
    /// @param amount The amount of tokens to send
    /// @param destinationChainId The ID of the destination chain
    /// @param relayerFeePct The percentage fee for the relayer (in basis points, e.g., 100 = 1%)
    /// @param token The address of the token being sent
    function initiateCrossChainTransaction(
        address recipient,
        uint256 amount,
        uint256 destinationChainId,
        uint64 relayerFeePct,
        address token
    ) external {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        require(destinationChainId > 0, "Invalid destination chain ID");
        require(token != address(0), "Invalid token address");

        // Transfer tokens from the sender to this contract
        bool success = IERC20(token).transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Approve the SpokePool to spend the tokens
        success = IERC20(token).approve(spokePool, amount);
        require(success, "Token approval failed");

        // Call the deposit function on the Across SpokePool
        IAcrossSpokePool(spokePool).deposit(
            recipient,
            token,
            amount,
            destinationChainId,
            relayerFeePct,
            ""
        );

        // Emit an event for the initiated transaction
        emit CrossChainTransactionInitiated(msg.sender, recipient, amount, destinationChainId);
    }
}

// Minimal IERC20 interface for token interactions
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
}
```
