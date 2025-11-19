"""
Generated Code Metadata:
========================
Original URL: https://gameswap-org.web.app
Prompt: "Create a simple example of minting or bridging an in-game asset into an Ethereum-compatible standard using adapters or a Mint service."
Generated: DETERMINISTIC_897dabfd356f8c92
Batch ID: 20250622_210348
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title GameAssetBridge
 * @dev A contract that mints ERC721 tokens representing in-game assets
 */
contract GameAssetBridge is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to in-game asset metadata
    mapping(uint256 => string) private _tokenURIs;

    event AssetMinted(address indexed recipient, uint256 tokenId, string tokenURI);
    event AssetBridged(address indexed recipient, uint256 tokenId, string tokenURI);

    constructor() ERC721("GameAsset", "GASSET") {}

    /**
     * @dev Mints a new ERC721 token representing an in-game asset
     * @param recipient Address to receive the minted token
     * @param tokenURI Metadata URI for the in-game asset
     */
    function mintAsset(address recipient, string memory tokenURI) external onlyOwner {
        require(bytes(tokenURI).length > 0, "GameAssetBridge: URI cannot be empty");
        
        _tokenIdCounter.increment();
        uint256 newTokenId = _tokenIdCounter.current();
        
        _mint(recipient, newTokenId);
        _setTokenURI(newTokenId, tokenURI);
        
        emit AssetMinted(recipient, newTokenId, tokenURI);
    }

    /**
     * @dev Bridges an in-game asset by minting an ERC721 token
     * @param recipient Address to receive the bridged token
     * @param tokenURI Metadata URI for the in-game asset
     */
    function bridgeAsset(address recipient, string memory tokenURI) external {
        require(bytes(tokenURI).length > 0, "GameAssetBridge: URI cannot be empty");
        
        _tokenIdCounter.increment();
        uint256 newTokenId = _tokenIdCounter.current();
        
        _mint(recipient, newTokenId);
        _setTokenURI(newTokenId, tokenURI);
        
        emit AssetBridged(recipient, newTokenId, tokenURI);
    }

    /**
     * @dev Returns the URI for a given token ID
     * @param tokenId uint256 ID of the token to query
     * @return string URI of the token
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "GameAssetBridge: URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Sets the URI for a given token ID
     * @param tokenId uint256 ID of the token to set its URI
     * @param tokenURI string URI to assign
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal virtual {
        require(_exists(tokenId), "GameAssetBridge: URI set of nonexistent token");
        _tokenURIs[tokenId] = tokenURI;
    }
}

interface IMintService {
    function requestMint(address recipient, string calldata tokenURI) external returns (uint256);
}

contract MintServiceAdapter is Ownable {
    GameAssetBridge public gameAssetBridge;
    address public mintService;

    event MintRequested(address indexed recipient, string tokenURI, uint256 tokenId);

    constructor(address _gameAssetBridge) {
        gameAssetBridge = GameAssetBridge(_gameAssetBridge);
    }

    function setMintService(address _mintService) external onlyOwner {
        require(_mintService != address(0), "MintServiceAdapter: invalid address");
        mintService = _mintService;
    }

    function bridgeAssetViaService(address recipient, string calldata tokenURI) external {
        require(mintService != address(0), "MintServiceAdapter: mint service not set");
        uint256 tokenId = IMintService(mintService).requestMint(recipient, tokenURI);
        emit MintRequested(recipient, tokenURI, tokenId);
    }
}
```
