"""
Generated Code Metadata:
========================
Original URL: https://www.zkfinance.org
Prompt: Write a smart contract for supplying assets to zkFinance to earn yield and use them as collateral, ensuring compatibility with zkSync's zero-knowledge technology.
Generated: DETERMINISTIC_32bf81dc19185bbb
Batch ID: 20250612_153547
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Interface for the zkFinance protocol
interface IzkFinance {
    function supplyAsset(address asset, uint256 amount) external;
    function withdrawAsset(address asset, uint256 amount) external;
    function getYield(address asset) external view returns (uint256);
}

contract AssetManager is Ownable, ReentrancyGuard {
    // State variables
    IzkFinance public zkFinance; // zkFinance contract address
    mapping(address => uint256) public suppliedAssets; // Track supplied assets by user

    // Events
    event AssetSupplied(address indexed user, address indexed asset, uint256 amount);
    event AssetWithdrawn(address indexed user, address indexed asset, uint256 amount);
    
    // Constructor to set the zkFinance contract address
    constructor(address _zkFinance) {
        require(_zkFinance != address(0), "Invalid zkFinance address");
        zkFinance = IzkFinance(_zkFinance);
    }

    // Function to supply assets to zkFinance
    function supply(address asset, uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(asset).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Approve zkFinance to spend the asset
        IERC20(asset).approve(address(zkFinance), amount);
        
        // Supply the asset to zkFinance
        zkFinance.supplyAsset(asset, amount);
        
        // Update the user's supplied assets
        suppliedAssets[msg.sender] += amount;

        emit AssetSupplied(msg.sender, asset, amount);
    }

    // Function to withdraw assets from zkFinance
    function withdraw(address asset, uint256 amount) external nonReentrant {
        require(suppliedAssets[msg.sender] >= amount, "Insufficient supplied assets");

        // Withdraw the asset from zkFinance
        zkFinance.withdrawAsset(asset, amount);
        
        // Transfer the asset back to the user
        require(IERC20(asset).transfer(msg.sender, amount), "Transfer failed");

        // Update the user's supplied assets
        suppliedAssets[msg.sender] -= amount;

        emit AssetWithdrawn(msg.sender, asset, amount);
    }

    // Function to get the yield for a specific asset
    function getYield(address asset) external view returns (uint256) {
        return zkFinance.getYield(asset);
    }

    // Function to set a new zkFinance contract address (only owner)
    function setZkFinanceAddress(address _zkFinance) external onlyOwner {
        require(_zkFinance != address(0), "Invalid zkFinance address");
        zkFinance = IzkFinance(_zkFinance);
    }
}
```
