"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ondofoundateon.org
Prompt: Write a Solidity contract to manage treasury assets for a DeFi protocol, incorporating features like those described in Ondo Foundation's treasury management strategies.
Generated: DETERMINISTIC_b78abd4aef392ec2
Batch ID: 20250612_154820
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

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract TreasuryManager {
    address public owner;
    mapping(address => uint256) public assets; // Tracks treasury assets
    address[] public assetTokens; // List of asset tokens managed by the treasury
    uint256 public totalAssets; // Total value of assets held in the treasury

    event AssetAdded(address indexed token, uint256 amount);
    event AssetRemoved(address indexed token, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor() {
        owner = msg.sender; // Set the deployer as the initial owner
    }

    // Function to add assets to the treasury
    function addAsset(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20(token).transferFrom(msg.sender, address(this), amount);
        assets[token] += amount;
        totalAssets += amount;

        // Add token to assetTokens array if it's not already there
        if (assets[token] == amount) {
            assetTokens.push(token);
        }

        emit AssetAdded(token, amount);
    }

    // Function to remove assets from the treasury
    function removeAsset(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(assets[token] >= amount, "Insufficient assets");

        assets[token] -= amount;
        totalAssets -= amount;

        IERC20(token).transfer(msg.sender, amount);

        emit AssetRemoved(token, amount);
    }

    // Function to check the balance of a specific asset
    function getAssetBalance(address token) external view returns (uint256) {
        return assets[token];
    }

    // Function to transfer ownership of the contract
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    // Function to get the list of asset tokens managed
    function getAssetTokens() external view returns (address[] memory) {
        return assetTokens;
    }

    // Function to get the total value of assets held
    function getTotalAssets() external view returns (uint256) {
        return totalAssets;
    }
}
```
