"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperbridge.mobi
Prompt: Create a smart contract example for bridging assets between HyperCore and HyperEVM using the Hyper liquid Bridge.
Generated: DETERMINISTIC_8bf737dd43096685
Batch ID: 20250612_154057
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

// Import necessary interfaces for the HyperLiquid Bridge
import "@hyperliquid/hyperliquid-bridge/contracts/IHyperLiquidBridge.sol";

/**
 * @title HyperCore to HyperEVM Asset Bridge
 * @dev This smart contract facilitates asset bridging between HyperCore and HyperEVM using the Hyper Liquid Bridge
 */
contract HyperBridge {
    // Instance of the Hyper Liquid Bridge
    IHyperLiquidBridge private bridge;

    // Event emitted when an asset is successfully bridged
    event AssetsBridged(address indexed from, string toChain, uint256 amount, string assetId);

    // Constructor to initialize the bridge
    constructor(address _bridgeAddress) {
        require(_bridgeAddress != address(0), "Bridge address cannot be zero");
        bridge = IHyperLiquidBridge(_bridgeAddress);
    }

    /**
     * @dev Bridges assets from HyperCore to HyperEVM
     * @param toChain The target blockchain where the asset will be sent
     * @param amount The amount of asset to bridge
     * @param assetId The identifier of the asset being bridged
     */
    function bridgeAssets(string memory toChain, uint256 amount, string memory assetId) external {
        require(amount > 0, "Amount must be greater than zero");
        require(bytes(toChain).length > 0, "Target chain must be specified");

        // Transfer the asset from the sender to this contract
        // Assuming that the asset follows ERC20 standard
        require(ERC20(assetId).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Approve the bridge to transfer the asset
        ERC20(assetId).approve(address(bridge), amount);

        // Bridge the asset to the target chain
        bridge.bridge(msg.sender, toChain, amount, assetId);

        emit AssetsBridged(msg.sender, toChain, amount, assetId);
    }

    /**
     * @dev Fallback function to prevent sending Ether directly to the contract
     */
    receive() external payable {
        revert("This contract does not accept Ether");
    }
}

// ERC20 interface used for asset transfer
interface ERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
}
```
