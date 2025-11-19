"""
Generated Code Metadata:
========================
Original URL: https://cyberlama-tyn.pages.dev
Prompt: Develop a Solidity smart contract that limits the circulation of NFTs and ensures uniqueness for each token, as described in Phase 2 of the Cyber Lama roadmap.
Generated: DETERMINISTIC_44f788e9803adb22
Batch ID: 20250612_145625
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
 * @title CyberLamaNFT
 * @dev A limited edition NFT contract with unique tokens and controlled circulation
 */
contract CyberLamaNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    // Maximum number of NFTs that can be minted
    uint256 public immutable MAX_SUPPLY;
    
    // Counter for token IDs
    Counters.Counter private _tokenIdCounter;
    
    // Base URI for token metadata
    string private _baseTokenURI;
    
    // Mapping to ensure token uniqueness
    mapping(bytes32 => bool) private _uniqueHashes;
    
    // Event emitted when a new NFT is minted
    event Minted(address indexed to, uint256 indexed tokenId, bytes32 uniqueHash);
    
    /**
     * @dev Constructor
     * @param name_ Name of the NFT collection
     * @param symbol_ Symbol of the NFT collection
     * @param maxSupply_ Maximum supply of NFTs
     * @param baseTokenURI_ Base URI for token metadata
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 maxSupply_,
        string memory baseTokenURI_
    ) ERC721(name_, symbol_) {
        require(maxSupply_ > 0, "CyberLamaNFT: Max supply must be greater than 0");
        MAX_SUPPLY = maxSupply_;
        _baseTokenURI = baseTokenURI_;
    }
    
    /**
     * @dev Mints a new NFT with a unique hash
     * @param to Address to mint the NFT to
     * @param uniqueHash Unique hash representing the NFT's uniqueness
     */
    function mint(address to, bytes32 uniqueHash) external onlyOwner {
        require(totalSupply() < MAX_SUPPLY, "CyberLamaNFT: Max supply reached");
        require(!_uniqueHashes[uniqueHash], "CyberLamaNFT: Token with this hash already exists");
        
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        
        _safeMint(to, tokenId);
        _uniqueHashes[uniqueHash] = true;
        
        emit Minted(to, tokenId, uniqueHash);
    }
    
    /**
     * @dev Returns the total number of tokens minted
     * @return uint256 Total supply
     */
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }
    
    /**
     * @dev Sets the base URI for all tokens
     * @param baseTokenURI New base URI
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }
    
    /**
     * @dev Returns the base URI for token metadata
     * @return string Base URI
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }
    
    /**
     * @dev Checks if a unique hash has been used
     * @param uniqueHash Hash to check
     * @return bool True if hash has been used
     */
    function isHashUsed(bytes32 uniqueHash) external view returns (bool) {
        return _uniqueHashes[uniqueHash];
    }
}
```
