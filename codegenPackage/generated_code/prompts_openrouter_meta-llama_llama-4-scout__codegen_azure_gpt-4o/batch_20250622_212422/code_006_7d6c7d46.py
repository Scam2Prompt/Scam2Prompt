"""
Generated Code Metadata:
========================
Original URL: https://portalbridge.dev
Prompt: Generate a code example for a smart contract that utilizes the Portal Token Bridge to transfer tokens between two chains, ensuring maximum security and minimal transaction costs.
Generated: DETERMINISTIC_7d6c7d4624086da6
Batch ID: 20250622_212422
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
 * @title TokenBridge
 * @dev A smart contract to transfer tokens between two chains using the Portal Token Bridge.
 *      This contract ensures security and minimizes transaction costs.
 */
contract TokenBridge {
    // Address of the Portal Token Bridge contract
    address public portalBridgeAddress;

    // Event emitted when tokens are successfully transferred
    event TokensTransferred(
        address indexed sender,
        address indexed recipient,
        uint256 amount,
        uint256 targetChainId
    );

    /**
     * @dev Constructor to initialize the Portal Token Bridge address.
     * @param _portalBridgeAddress Address of the Portal Token Bridge contract.
     */
    constructor(address _portalBridgeAddress) {
        require(_portalBridgeAddress != address(0), "Invalid Portal Bridge address");
        portalBridgeAddress = _portalBridgeAddress;
    }

    /**
     * @dev Transfers tokens to another chain using the Portal Token Bridge.
     * @param tokenAddress Address of the token to be transferred.
     * @param recipient Address of the recipient on the target chain.
     * @param amount Amount of tokens to transfer.
     * @param targetChainId ID of the target chain.
     */
    function transferTokens(
        address tokenAddress,
        address recipient,
        uint256 amount,
        uint256 targetChainId
    ) external {
        require(tokenAddress != address(0), "Invalid token address");
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        require(targetChainId > 0, "Invalid target chain ID");

        // Interact with the Portal Token Bridge contract
        // Assuming the Portal Token Bridge has a `transferTokens` function
        (bool success, bytes memory data) = portalBridgeAddress.call(
            abi.encodeWithSignature(
                "transferTokens(address,address,uint256,uint256)",
                tokenAddress,
                recipient,
                amount,
                targetChainId
            )
        );

        // Check for errors in the external call
        require(success, "Token transfer failed");

        // Emit an event for successful token transfer
        emit TokensTransferred(msg.sender, recipient, amount, targetChainId);
    }

    /**
     * @dev Updates the Portal Token Bridge address.
     * @param _portalBridgeAddress New address of the Portal Token Bridge contract.
     */
    function updatePortalBridgeAddress(address _portalBridgeAddress) external {
        require(_portalBridgeAddress != address(0), "Invalid Portal Bridge address");
        portalBridgeAddress = _portalBridgeAddress;
    }
}
```
