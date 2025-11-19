"""
Generated Code Metadata:
========================
Original URL: https://pepearab.pages.dev
Prompt: Generate a Solidity code for creating an NFT contract similar to PepeArab's Arab NFTs, with a supply limit and specific unlock conditions.
Generated: DETERMINISTIC_b8481eb2b356515b
Batch ID: 20250622_211656
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

contract ArabNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;
    
    // Base URI for token metadata
    string private _baseTokenURI;
    
    // Counter for token IDs
    Counters.Counter private _tokenIdCounter;
    
    // Contract state: paused/unpaused
    bool public isPaused = true;
    
    // Mapping to track unlock conditions per token
    mapping(uint256 => uint256) public unlockTimestamps;
    
    // Event emitted when NFT is minted
    event Minted(address indexed to, uint256 indexed tokenId, uint256 unlockTimestamp);

    constructor(string memory baseURI) ERC721("ArabNFT", "ARAB") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Mint a new NFT (only owner)
     * @param to Address to mint the NFT to
     * @param unlockAfterDays Number of days until token is unlocked
     */
    function mint(address to, uint256 unlockAfterDays) external onlyOwner {
        require(!isPaused, "Minting is paused");
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        uint256 unlockTimestamp = block.timestamp + (unlockAfterDays * 1 days);
        unlockTimestamps[tokenId] = unlockTimestamp;
        
        _safeMint(to, tokenId);
        
        emit Minted(to, tokenId, unlockTimestamp);
    }

    /**
     * @dev Batch mint NFTs (only owner)
     * @param to Addresses to mint the NFTs to
     * @param unlockAfterDays Number of days until tokens are unlocked
     */
    function batchMint(address[] calldata to, uint256[] calldata unlockAfterDays) external onlyOwner {
        require(!isPaused, "Minting is paused");
        require(to.length == unlockAfterDays.length, "Arrays length mismatch");
        require(_tokenIdCounter.current() + to.length <= MAX_SUPPLY, "Exceeds max supply");
        
        for (uint256 i = 0; i < to.length; i++) {
            uint256 tokenId = _tokenIdCounter.current();
            _tokenIdCounter.increment();
            
            uint256 unlockTimestamp = block.timestamp + (unlockAfterDays[i] * 1 days);
            unlockTimestamps[tokenId] = unlockTimestamp;
            
            _safeMint(to[i], tokenId);
            
            emit Minted(to[i], tokenId, unlockTimestamp);
        }
    }

    /**
     * @dev Toggle pause state (only owner)
     */
    function togglePause() external onlyOwner {
        isPaused = !isPaused;
    }

    /**
     * @dev Set base URI for token metadata (only owner)
     * @param baseURI New base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Check if token is unlocked
     * @param tokenId Token ID to check
     */
    function isUnlocked(uint256 tokenId) public view returns (bool) {
        require(_exists(tokenId), "Token does not exist");
        return block.timestamp >= unlockTimestamps[tokenId];
    }

    /**
     * @dev Override transfer to check unlock status
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, tokenId);
        
        if (from != address(0) && to != address(0)) { // Skip for minting/burning
            require(isUnlocked(tokenId), "Token is locked");
        }
    }

    /**
     * @dev Returns base URI
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Returns total minted supply
     */
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
