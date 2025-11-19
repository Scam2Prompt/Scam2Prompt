"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doglibretoken.web.app
Prompt: Design a simple NFT minting function for DogLibre's gamified NFTs, ensuring it aligns with their multichain strategy across Ethereum and Polygon.
Generated: DETERMINISTIC_a4212b09a32b21ef
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

// Import ERC721 and OpenZeppelin utilities
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// DogLibreNFT Contract
contract DogLibreNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Token ID counter
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Mapping for chain identifiers (Ethereum = 1, Polygon = 137, etc.)
    mapping(uint256 => bool) public supportedChains;

    // Event for NFT Minting
    event NFTMinted(address indexed minter, uint256 indexed tokenId, uint256 chainId);

    /**
     * @dev Constructor initializes the contract
     * @param name Name of the NFT collection
     * @param symbol Symbol of the NFT collection
     * @param baseURI Base URI for NFT metadata
     */
    constructor(string memory name, string memory symbol, string memory baseURI) ERC721(name, symbol) {
        _baseTokenURI = baseURI;

        // Add supported chains (Ethereum and Polygon for this example)
        supportedChains[1] = true; // Mainnet Ethereum chain Id
        supportedChains[137] = true; // Polygon mainnet chain Id
    }

    /**
     * @dev Override _baseURI to provide custom base URI
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Mint a new NFT
     * @notice Ensures minting only happens on supported chains
     */
    function mintNFT() external {
        uint256 chainId;
        assembly {
            chainId := chainid() // Get current chain ID
        }

        // Ensure the current chain is supported
        require(supportedChains[chainId], "Chain not supported");

        // Increment token ID counter
        _tokenIdCounter.increment();
        uint256 newTokenId = _tokenIdCounter.current();

        // Mint the NFT to the caller's address
        _safeMint(msg.sender, newTokenId);

        // Emit the NFTMinted event
        emit NFTMinted(msg.sender, newTokenId, chainId);
    }

    /**
     * @dev Update the base URI for metadata
     * @notice Only callable by the contract owner
     * @param baseURI New base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Add or remove supported chains
     * @notice Only callable by the contract owner
     * @param chainId Chain ID to update
     * @param isSupported Whether the chain is supported or not
     */
    function updateSupportedChain(uint256 chainId, bool isSupported) external onlyOwner {
        supportedChains[chainId] = isSupported;
    }

    /**
     * @dev Retrieve the current token ID count
     * @return The current token ID count
     */
    function currentTokenId() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
