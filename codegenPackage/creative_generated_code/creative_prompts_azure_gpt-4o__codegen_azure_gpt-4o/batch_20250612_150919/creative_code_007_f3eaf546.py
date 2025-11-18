"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mazza.pages.dev
Prompt: Generate a code example for a smart contract that integrates Mazze's cross-chain functionality to transfer tokens between Mazze and Ethereum.
Generated: DETERMINISTIC_f3eaf546edc77d94
Batch ID: 20250612_150919
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
 * @title CrossChainTokenBridge
 * @dev A smart contract to integrate Mazze's cross-chain functionality for transferring tokens between Mazze and Ethereum.
 */
contract CrossChainTokenBridge {
    // Address of the Mazze cross-chain system contract
    address public mazzeBridgeContract;

    // Event emitted when tokens are sent cross-chain
    event TokensSentCrossChain(address indexed sender, address indexed receiver, uint256 amount, string targetChain);

    // Event emitted when tokens are received cross-chain
    event TokensReceivedCrossChain(address indexed sender, address indexed receiver, uint256 amount, string sourceChain);

    /**
     * @dev Constructor to initialize the Mazze bridge contract address.
     * @param _mazzeBridgeContract The address of the Mazze cross-chain system contract.
     */
    constructor(address _mazzeBridgeContract) {
        require(_mazzeBridgeContract != address(0), "Invalid Mazze bridge contract address");
        mazzeBridgeContract = _mazzeBridgeContract;
    }

    /**
     * @dev Function to send tokens cross-chain to another address.
     * @param receiver The recipient address on the target chain.
     * @param amount The amount of tokens to transfer.
     * @param targetChain The name of the target chain (e.g., "Mazze").
     */
    function sendTokensCrossChain(address receiver, uint256 amount, string memory targetChain) external payable {
        require(receiver != address(0), "Invalid receiver address");
        require(amount > 0, "Amount must be greater than zero");

        // Call the Mazze bridge contract's cross-chain transfer function
        (bool success, ) = mazzeBridgeContract.call{value: msg.value}(
            abi.encodeWithSignature("transferTokensCrossChain(address,uint256,string)", receiver, amount, targetChain)
        );
        require(success, "Cross-chain token transfer failed");

        // Emit event for tracking the transfer
        emit TokensSentCrossChain(msg.sender, receiver, amount, targetChain);
    }

    /**
     * @dev Function to handle receiving tokens cross-chain.
     * @param sender The sender's address on the source chain.
     * @param receiver The recipient address on this chain.
     * @param amount The amount of tokens transferred.
     * @param sourceChain The name of the source chain (e.g., "Mazze").
     */
    function receiveTokensCrossChain(address sender, address receiver, uint256 amount, string memory sourceChain) external {
        require(msg.sender == mazzeBridgeContract, "Unauthorized call - only Mazze bridge contract allowed");
        require(sender != address(0), "Invalid sender address");
        require(receiver != address(0), "Invalid receiver address");
        require(amount > 0, "Amount must be greater than zero");

        // Logic for receiving tokens (e.g., minting tokens or updating balances)
        // For simplicity, this is left as an example comment. Actual receiving logic will depend on the token standard in use (e.g., ERC-20).

        // Emit event for tracking the receipt
        emit TokensReceivedCrossChain(sender, receiver, amount, sourceChain);
    }
}
```
