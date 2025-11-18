"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gameswap-org.web.app
Prompt: Write a smart contract in Solidity to mint and bridge in-game assets into Ethereum-compatible NFTs using ERC721 or ERC1155 standards, as described on GameSwap's platform.
Generated: DETERMINISTIC_3655726aa37dde8e
Batch ID: 20250612_152827
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
 * @title GameAssetBridge
 * @dev A smart contract for minting and bridging in-game assets into Ethereum-compatible NFTs
 * using ERC721 and ERC1155 standards.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GameAssetBridgeERC721 is ERC721, Ownable {
    uint256 private _tokenIdCounter;

    // Event emitted when an asset is bridged
    event AssetBridged(address indexed user, uint256 tokenId, string metadataURI);

    constructor() ERC721("GameAsset", "GASSET") {}

    /**
     * @dev Mint a new ERC721 token representing an in-game asset.
     * @param to Address that will own the minted token.
     * @param metadataURI URI pointing to the metadata of the token.
     */
    function mint(address to, string memory metadataURI) external onlyOwner {
        require(to != address(0), "Invalid address");
        
        _tokenIdCounter += 1;
        uint256 newTokenId = _tokenIdCounter;

        _safeMint(to, newTokenId);
        
        // Optional: Store metadataURI on-chain (or in off-chain storage like IPFS).
        // Emit the event with metadata information.
        emit AssetBridged(to, newTokenId, metadataURI);
    }
}

contract GameAssetBridgeERC1155 is ERC1155, Ownable {
    uint256 private _tokenIdCounter;

    // Event emitted when an asset is bridged
    event AssetBridged(address indexed user, uint256 tokenId, uint256 amount, string metadataURI);

    constructor() ERC1155("") {}

    /**
     * @dev Mint a new ERC1155 token representing in-game assets.
     * @param to Address that will receive the minted tokens.
     * @param amount Number of tokens to mint.
     * @param metadataURI URI pointing to the metadata of the token.
     */
    function mint(
        address to,
        uint256 amount,
        string memory metadataURI
    ) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");

        _tokenIdCounter += 1;
        uint256 newTokenId = _tokenIdCounter;

        _mint(to, newTokenId, amount, "");

        // Optional: Store metadataURI on-chain (or in off-chain storage like IPFS).
        // Emit the event with metadata information.
        emit AssetBridged(to, newTokenId, amount, metadataURI);
    }
}
```
