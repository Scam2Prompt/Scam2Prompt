"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidbzihyinyo7izo2bw76p5ghzvavjsr3c5oqgowyshfuo5g6gfmti.ipfs.dweb.link
Prompt: Write a code snippet using Chainlink CCIP to implement secure cross-chain token transfers, referencing the XSwap protocol for fluid cross-chain liquidity.
Generated: DETERMINISTIC_d68edc3ae2e54b31
Batch ID: 20250612_152235
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

import "@chainlink/contracts/src/v0.8/interfaces/ICrossChainTransfer.sol";
import "@chainlink/contracts/src/v0.8/interfaces/IXSwap.sol";

contract CrossChainTokenTransfer {
    // Chainlink Cross-Chain Transfer interface
    ICrossChainTransfer public crossChainTransfer;
    
    // XSwap protocol interface for cross-chain liquidity
    IXSwap public xswap;

    // Event emitted after a successful cross-chain transfer
    event TransferInitiated(address indexed sender, uint256 amount, string targetChain, address tokenAddress);

    // Constructor to initialize the Chainlink and XSwap interfaces
    constructor(address _crossChainTransferAddress, address _xswapAddress) {
        require(_crossChainTransferAddress != address(0), "Invalid CrossChainTransfer address");
        require(_xswapAddress != address(0), "Invalid XSwap address");

        crossChainTransfer = ICrossChainTransfer(_crossChainTransferAddress);
        xswap = IXSwap(_xswapAddress);
    }

    /**
     * @dev Initiates a cross-chain token transfer using Chainlink CCIP and XSwap protocol.
     * @param amount The amount of tokens to transfer.
     * @param targetChain The target blockchain identifier.
     * @param tokenAddress The address of the token to transfer.
     */
    function initiateTransfer(uint256 amount, string calldata targetChain, address tokenAddress) external {
        require(amount > 0, "Transfer amount must be greater than zero");
        require(tokenAddress != address(0), "Invalid token address");

        // Approve XSwap to spend tokens on behalf of the sender
        require(IERC20(tokenAddress).approve(address(xswap), amount), "Token approval failed");

        // Transfer tokens using XSwap for cross-chain liquidity
        xswap.swap(tokenAddress, amount, targetChain);

        // Emit event for the initiated transfer
        emit TransferInitiated(msg.sender, amount, targetChain, tokenAddress);
    }

    /**
     * @dev Receives the tokens on the target chain after the transfer is completed.
     * This function should be called by the XSwap protocol upon successful transfer completion.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens received.
     * @param tokenAddress The address of the token received.
     */
    function receiveTokens(address recipient, uint256 amount, address tokenAddress) external {
        // Ensure that only the XSwap protocol can call this function
        require(msg.sender == address(xswap), "Unauthorized caller");

        // Transfer tokens to the recipient
        require(IERC20(tokenAddress).transfer(recipient, amount), "Token transfer failed");
    }
}

// Minimal IERC20 interface for token interactions
interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
