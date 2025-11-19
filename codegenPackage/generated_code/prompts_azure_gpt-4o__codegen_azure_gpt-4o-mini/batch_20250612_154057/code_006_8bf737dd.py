"""
Generated Code Metadata:
========================
Original URL: https://hyperbridge.mobi
Prompt: Create a smart contract example for bridging assets between HyperCore and HyperEVM using the Hyper liquid Bridge.
Generated: DETERMINISTIC_8bf737dd43096685
Batch ID: 20250612_154057
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the HyperLiquidBridge
interface IHyperLiquidBridge {
    function bridgeAssets(address token, uint256 amount, address recipient) external;
}

// Smart contract for bridging assets between HyperCore and HyperEVM
contract AssetBridge is Ownable {
    // Instance of the HyperLiquidBridge
    IHyperLiquidBridge public hyperLiquidBridge;

    // Event emitted when assets are bridged
    event AssetsBridged(address indexed token, uint256 amount, address indexed recipient);

    // Constructor to set the HyperLiquidBridge address
    constructor(address _hyperLiquidBridge) {
        require(_hyperLiquidBridge != address(0), "Invalid bridge address");
        hyperLiquidBridge = IHyperLiquidBridge(_hyperLiquidBridge);
    }

    // Function to bridge assets
    function bridgeAssets(address token, uint256 amount, address recipient) external {
        require(amount > 0, "Amount must be greater than zero");
        require(recipient != address(0), "Invalid recipient address");

        // Transfer the specified amount of tokens from the sender to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Approve the bridge to spend the tokens
        IERC20(token).approve(address(hyperLiquidBridge), amount);

        // Call the bridge function to transfer assets
        hyperLiquidBridge.bridgeAssets(token, amount, recipient);

        // Emit an event for the bridging action
        emit AssetsBridged(token, amount, recipient);
    }

    // Function to withdraw tokens in case of emergency
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to update the HyperLiquidBridge address
    function updateBridgeAddress(address newBridge) external onlyOwner {
        require(newBridge != address(0), "Invalid bridge address");
        hyperLiquidBridge = IHyperLiquidBridge(newBridge);
    }
}
```
