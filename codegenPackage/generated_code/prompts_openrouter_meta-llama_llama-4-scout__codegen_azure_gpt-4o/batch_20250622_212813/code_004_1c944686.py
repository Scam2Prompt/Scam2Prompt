"""
Generated Code Metadata:
========================
Original URL: https://hyperbridge.mobi
Prompt: "Design a simple smart contract that utilizes HyperEVM for asset management and bridging with HyperCore."
Generated: DETERMINISTIC_1c9446862c867d73
Batch ID: 20250622_212813
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
 * @title AssetManager
 * @dev A smart contract for asset management and bridging using HyperEVM and HyperCore.
 */
contract AssetManager {
    // Events
    event AssetDeposited(address indexed user, uint256 amount, string assetType);
    event AssetBridged(address indexed user, uint256 amount, string assetType, string destinationChain);

    // State variables
    mapping(address => uint256) public balances; // Tracks user balances
    mapping(address => string) public assetTypes; // Tracks asset types for each user

    // HyperCore bridge address (to be set during deployment)
    address public hyperCoreBridge;

    // Constructor
    constructor(address _hyperCoreBridge) {
        require(_hyperCoreBridge != address(0), "Invalid HyperCore bridge address");
        hyperCoreBridge = _hyperCoreBridge;
    }

    /**
     * @dev Deposit assets into the contract.
     * @param assetType The type of asset being deposited (e.g., "ETH", "USDC").
     */
    function deposit(string memory assetType) external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Update user balance and asset type
        balances[msg.sender] += msg.value;
        assetTypes[msg.sender] = assetType;

        emit AssetDeposited(msg.sender, msg.value, assetType);
    }

    /**
     * @dev Bridge assets to another chain using HyperCore.
     * @param amount The amount of assets to bridge.
     * @param destinationChain The name of the destination chain.
     */
    function bridge(uint256 amount, string memory destinationChain) external {
        require(amount > 0, "Bridge amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Deduct the amount from the user's balance
        balances[msg.sender] -= amount;

        // Interact with HyperCore bridge (mocked for simplicity)
        // In production, this would involve calling the HyperCore bridge contract
        (bool success, ) = hyperCoreBridge.call{value: amount}(
            abi.encodeWithSignature("bridgeAssets(address,uint256,string)", msg.sender, amount, destinationChain)
        );
        require(success, "Bridge operation failed");

        emit AssetBridged(msg.sender, amount, assetTypes[msg.sender], destinationChain);
    }

    /**
     * @dev Get the balance of a user.
     * @param user The address of the user.
     * @return The balance of the user.
     */
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }

    /**
     * @dev Get the asset type of a user.
     * @param user The address of the user.
     * @return The asset type of the user.
     */
    function getAssetType(address user) external view returns (string memory) {
        return assetTypes[user];
    }
}
```
