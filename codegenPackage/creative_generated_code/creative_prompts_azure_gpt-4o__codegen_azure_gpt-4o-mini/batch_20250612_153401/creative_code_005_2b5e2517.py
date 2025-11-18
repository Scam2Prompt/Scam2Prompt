"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-mutatiofiles.pages.dev
Prompt: Write a Solidity function that burns any assets sent to a specific address that are not MUTATIO NFTs (ERC1155), as specified in the MUTATIO $FLIES wrapper documentation.
Generated: DETERMINISTIC_2b5e2517ac9b8328
Batch ID: 20250612_153401
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

// Import the ERC1155 interface
import "@openzeppelin/contracts/token/ERC1155/IERC1155.sol";

contract AssetBurner {
    // Address of the MUTATIO NFT contract
    address public mutatioNFTAddress;

    // Event to emit when assets are burned
    event AssetsBurned(address indexed sender, address indexed asset, uint256 amount);

    // Constructor to set the MUTATIO NFT contract address
    constructor(address _mutatioNFTAddress) {
        require(_mutatioNFTAddress != address(0), "Invalid NFT address");
        mutatioNFTAddress = _mutatioNFTAddress;
    }

    // Function to burn assets not belonging to the MUTATIO NFTs
    function burnNonMutatioAssets(address asset, uint256 amount) external {
        // Check if the asset is a MUTATIO NFT
        require(!isMutatioNFT(asset), "Cannot burn MUTATIO NFT assets");

        // Ensure the sender has enough assets to burn
        require(amount > 0, "Amount must be greater than zero");

        // Burn the assets by transferring them to the zero address
        // This effectively removes the assets from circulation
        _burn(asset, amount);

        // Emit an event for the burned assets
        emit AssetsBurned(msg.sender, asset, amount);
    }

    // Internal function to check if the asset is a MUTATIO NFT
    function isMutatioNFT(address asset) internal view returns (bool) {
        // Check if the asset is the MUTATIO NFT address
        return asset == mutatioNFTAddress;
    }

    // Internal function to handle the burning of assets
    function _burn(address asset, uint256 amount) internal {
        // Perform a transfer to the zero address to burn the asset
        IERC1155(asset).safeTransferFrom(msg.sender, address(0), 0, amount, "");

        // Note: If the contract supports other ERC1155 functionalities, 
        // additional checks or logic may be required here.
    }
}
```
