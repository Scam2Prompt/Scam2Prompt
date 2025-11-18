"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange-changelly-com.pages.dev
Prompt: Recommend a method to implement decentralized cross-chain bridges using Changelly's upcoming Bridge Protocol. Include details on how the smart router optimizes routes among DEXs and bridges.
Generated: DETERMINISTIC_0068a8401243c7ec
Batch ID: 20250612_150226
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Changelly Bridge Protocol
interface IBridgeProtocol {
    function swapAndBridge(
        address fromToken,
        address toToken,
        uint256 amount,
        address recipient,
        bytes calldata bridgeData
    ) external returns (bool success);
}

// Smart router for optimizing routes among DEXs and bridges
contract SmartRouter is Ownable {
    // Mapping to keep track of supported DEXs and Bridges
    mapping(address => bool) public supportedDEXs;
    mapping(address => bool) public supportedBridges;

    // Event to log successful swaps
    event SwapAndBridgeExecuted(address indexed fromToken, address indexed toToken, uint256 amount, address recipient);

    // Function to add supported DEXs
    function addSupportedDEX(address dex) external onlyOwner {
        supportedDEXs[dex] = true;
    }

    // Function to remove supported DEXs
    function removeSupportedDEX(address dex) external onlyOwner {
        supportedDEXs[dex] = false;
    }

    // Function to add supported Bridges
    function addSupportedBridge(address bridge) external onlyOwner {
        supportedBridges[bridge] = true;
    }

    // Function to remove supported Bridges
    function removeSupportedBridge(address bridge) external onlyOwner {
        supportedBridges[bridge] = false;
    }

    // Main function to optimize and execute swaps and bridging
    function executeSwapAndBridge(
        address fromToken,
        address toToken,
        uint256 amount,
        address recipient,
        bytes calldata bridgeData
    ) external {
        require(supportedDEXs[fromToken], "Unsupported from token");
        require(supportedBridges[toToken], "Unsupported to token");

        // Transfer tokens from the sender to this contract
        IERC20(fromToken).transferFrom(msg.sender, address(this), amount);

        // Approve the Bridge Protocol to spend the tokens
        IERC20(fromToken).approve(address(this), amount);

        // Execute the swap and bridge
        IBridgeProtocol bridgeProtocol = IBridgeProtocol(toToken);
        bool success = bridgeProtocol.swapAndBridge(fromToken, toToken, amount, recipient, bridgeData);
        require(success, "Swap and bridge failed");

        emit SwapAndBridgeExecuted(fromToken, toToken, amount, recipient);
    }

    // Function to withdraw tokens from the contract (for emergency use)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
