"""
Generated Code Metadata:
========================
Original URL: https://monarch-game.pages.dev
Prompt: Describe how to use the ERC404 standard in the context of evolving NFTs through on-chain activity in the Monarch Dungeon.
Generated: DETERMINISTIC_f048527539a1c026
Batch ID: 20250612_162325
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
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ERC404
 * @dev Hybrid ERC20/ERC721 implementation with evolving NFT traits based on on-chain activity
 */
contract ERC404 is ERC721, ERC20, Ownable {
    using Counters for Counters.Counter;
    
    // Token counters
    Counters.Counter private _tokenIdCounter;
    
    // Base URI for NFT metadata
    string private _baseTokenURI;
    
    // Mapping from token ID to evolution level
    mapping(uint256 => uint256) private _evolutionLevels;
    
    // Mapping from token ID to on-chain activity score
    mapping(uint256 => uint256) private _activityScores;
    
    // Thresholds for evolution levels
    uint256[] public evolutionThresholds;
    
    // Address of the Monarch Dungeon game contract
    address public monarchDungeonContract;
    
    // Events
    event Evolved(uint256 indexed tokenId, uint256 newLevel);
    event ActivityUpdated(uint256 indexed tokenId, uint256 newScore);
    
    /**
     * @dev Constructor
     * @param name_ ERC20/ERC721 token name
     * @param symbol_ ERC20/ERC721 token symbol
     * @param baseURI_ Base URI for NFT metadata
     * @param thresholds Evolution level thresholds
     */
    constructor(
        string memory name_,
        string memory symbol_,
        string memory baseURI_,
        uint256[] memory thresholds
    ) ERC721(name_, symbol_) ERC20(name_, symbol_) {
        _baseTokenURI = baseURI_;
        evolutionThresholds = thresholds;
    }
    
    /**
     * @dev Set the Monarch Dungeon contract address
     * @param dungeonAddress Address of the game contract
     */
    function setMonarchDungeonContract(address dungeonAddress) external onlyOwner {
        require(dungeonAddress != address(0), "Invalid address");
        monarchDungeonContract = dungeonAddress;
    }
    
    /**
     * @dev Mint new tokens (both ERC20 and ERC721)
     * @param to Address to mint to
     * @param amount Amount of ERC20 tokens to mint
     */
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
        
        // Convert ERC20 to ERC721 if whole tokens are held
        _syncERC721Holdings(to);
    }
    
    /**
     * @dev Update on-chain activity for a token
     * @param tokenId NFT token ID
     * @param activityPoints Points to add to activity score
     */
    function updateActivity(uint256 tokenId, uint256 activityPoints) external {
        require(msg.sender == monarchDungeonContract, "Only Monarch Dungeon can update activity");
        require(_exists(tokenId), "Token does not exist");
        
        _activityScores[tokenId] += activityPoints;
        emit ActivityUpdated(tokenId, _activityScores[tokenId]);
        
        // Check for evolution
        _checkEvolution(tokenId);
    }
    
    /**
     * @dev Check if token should evolve based on activity score
     * @param tokenId NFT token ID
     */
    function _checkEvolution(uint256 tokenId) internal {
        uint256 currentLevel = _evolutionLevels[tokenId];
        uint256 activityScore = _activityScores[tokenId];
        
        // Check if score meets next threshold
        if (currentLevel < evolutionThresholds.length && 
            activityScore >= evolutionThresholds[currentLevel]) {
            _evolutionLevels[tokenId] = currentLevel + 1;
            emit Evolved(tokenId, currentLevel + 1);
        }
    }
    
    /**
     * @dev Get the evolution level of a token
     * @param tokenId NFT token ID
     * @return Current evolution level
     */
    function getEvolutionLevel(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        return _evolutionLevels[tokenId];
    }
    
    /**
     * @dev Get the activity score of a token
     * @param tokenId NFT token ID
     * @return Current activity score
     */
    function getActivityScore(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        return _activityScores[tokenId];
    }
    
    /**
     * @dev Override ERC20 transfer to handle ERC721 sync
     */
    function _transfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        super._transfer(from, to, amount);
        _syncERC721Holdings(from);
        _syncERC721Holdings(to);
    }
    
    /**
     * @dev Sync ERC721 holdings based on ERC20 balance
     * @param holder Address to sync
     */
    function _syncERC721Holdings(address holder) internal {
        uint256 balance = balanceOf(holder);
        uint256 tokenCount = _tokenCountForAddress(holder);
        
        // Mint new NFTs if balance increased
        while (tokenCount < balance && tokenCount < 100) { // Limit to prevent gas issues
            _mintNFT(holder);
            tokenCount++;
        }
        
        // Burn NFTs if balance decreased
        while (tokenCount > balance && tokenCount > 0) {
            _burnNFTForAddress(holder);
            tokenCount--;
        }
    }
    
    /**
     * @dev Mint a new NFT for an address
     * @param to Address to mint to
     */
    function _mintNFT(address to) internal {
        _tokenIdCounter.increment();
        uint256 newTokenId = _tokenIdCounter.current();
        _safeMint(to, newTokenId);
    }
    
    /**
     * @dev Burn an NFT for an address
     * @param holder Address to burn from
     */
    function _burnNFTForAddress(address holder) internal {
        uint256 tokenId = _tokenOfOwnerByIndex(holder, 0); // Get first token
        _burn(tokenId);
    }
    
    /**
     * @dev Get token count for an address
     * @param owner Address to check
     * @return Number of NFTs owned
     */
    function _tokenCountForAddress(address owner) internal view returns (uint256) {
        return balanceOf(owner);
    }
    
    /**
     * @dev Get token ID by index for an owner
     * @param owner Address to check
     * @param index Index of token
     * @return Token ID
     */
    function _tokenOfOwnerByIndex(address owner, uint256 index) internal view returns (uint256) {
        // In a real implementation, you would need to track owner's tokens
        // This is simplified for demonstration
        return index + 1; // Placeholder
    }
    
    /**
     * @dev Override tokenURI to include evolution level
     * @param tokenId NFT token ID
     * @return Token URI
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return string(abi.encodePacked(_baseTokenURI, Strings.toString(tokenId), "/", Strings.toString(_evolutionLevels[tokenId])));
    }
    
    /**
     * @dev Override supportsInterface for ERC721 and ERC20
     */
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721, ERC20) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
```
