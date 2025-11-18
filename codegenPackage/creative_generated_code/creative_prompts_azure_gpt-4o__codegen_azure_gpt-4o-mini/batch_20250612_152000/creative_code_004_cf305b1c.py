"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rtt23423.pages.dev
Prompt: Develop a Compound V2 fork that incorporates permissioned assets like OUSG alongside DAI and USDC, following the model described by Ondo Finance.
Generated: DETERMINISTIC_cf305b1c911d82f4
Batch ID: 20250612_152000
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

// Interface for the Compound's lending protocol
interface ICompound {
    function supply(address asset, uint256 amount) external;
    function withdraw(address asset, uint256 amount) external;
}

contract PermissionedCompoundV2 is Ownable {
    // State variables
    ICompound public compound;
    mapping(address => bool) public allowedAssets;
    
    // Event emitted when an asset is added
    event AssetAdded(address indexed asset);
    // Event emitted when an asset is removed
    event AssetRemoved(address indexed asset);
    
    // Constructor to set the Compound protocol interface
    constructor(address _compoundAddress) {
        compound = ICompound(_compoundAddress);
    }

    // Modifier to check if an asset is permissioned
    modifier assetIsAllowed(address asset) {
        require(allowedAssets[asset], "Asset not allowed");
        _;
    }

    // Function to add a new asset to the allowed list
    function addAsset(address asset) external onlyOwner {
        require(asset != address(0), "Invalid asset address");
        allowedAssets[asset] = true;
        emit AssetAdded(asset);
    }

    // Function to remove an asset from the allowed list
    function removeAsset(address asset) external onlyOwner {
        require(allowedAssets[asset], "Asset not allowed");
        allowedAssets[asset] = false;
        emit AssetRemoved(asset);
    }

    // Function to supply an asset to the Compound protocol
    function supplyAsset(address asset, uint256 amount) external assetIsAllowed(asset) {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(asset).transferFrom(msg.sender, address(this), amount);
        IERC20(asset).approve(address(compound), amount);
        compound.supply(asset, amount);
    }

    // Function to withdraw an asset from the Compound protocol
    function withdrawAsset(address asset, uint256 amount) external assetIsAllowed(asset) {
        require(amount > 0, "Amount must be greater than zero");
        compound.withdraw(asset, amount);
        IERC20(asset).transfer(msg.sender, amount);
    }

    // Function to withdraw all assets held by the contract
    function withdrawAllAssets(address asset) external onlyOwner assetIsAllowed(asset) {
        // Assuming the contract has enough balance for withdrawal
        uint256 balance = IERC20(asset).balanceOf(address(this));
        require(balance > 0, "No assets to withdraw");
        compound.withdraw(asset, balance);
        IERC20(asset).transfer(msg.sender, balance);
    }
}
```
