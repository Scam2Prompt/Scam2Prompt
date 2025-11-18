"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://base--chain.pages.dev
Prompt: Generate a Solidity function that interacts with Base's rollup architecture for transferring assets between Ethereum L1 and Base.
Generated: DETERMINISTIC_93138cba6477f432
Batch ID: 20250612_151308
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
 * @title AssetBridge
 * @dev A contract to interact with Base's rollup architecture for transferring assets
 *      between Ethereum L1 and Base L2.
 */
contract AssetBridge {
    // Address of the Base rollup bridge contract
    address public immutable baseBridge;

    /**
     * @dev Emitted when assets are successfully transferred to Base L2.
     * @param sender Address initiating the transfer.
     * @param receiver Address receiving the assets on Base L2.
     * @param amount Amount of assets transferred.
     */
    event AssetsTransferredToBase(address indexed sender, address indexed receiver, uint256 amount);

    /**
     * @dev Constructor to initialize the Base bridge address.
     * @param _baseBridge Address of the Base rollup bridge contract.
     */
    constructor(address _baseBridge) {
        require(_baseBridge != address(0), "Invalid Base bridge address");
        baseBridge = _baseBridge;
    }

    /**
     * @notice Transfers assets from Ethereum L1 to Base L2 using the rollup bridge.
     * @dev Calls the Base rollup bridge contract with the appropriate ABI.
     * @param receiver Address on Base L2 to receive the assets.
     * @param amount Amount of assets to transfer.
     */
    function transferToBase(address receiver, uint256 amount) external payable {
        require(receiver != address(0), "Invalid receiver address");
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value == amount, "Insufficient funds sent with transaction");

        // Interact with the Base rollup bridge
        (bool success, ) = baseBridge.call{value: msg.value}(
            abi.encodeWithSignature("deposit(address,uint256)", receiver, amount)
        );

        // Ensure the transaction was successful
        require(success, "Transfer to Base failed");

        // Emit event for asset transfer
        emit AssetsTransferredToBase(msg.sender, receiver, amount);
    }

    /**
     * @notice Fallback function to accept ether for the contract (if needed).
     */
    receive() external payable {}
}
```
