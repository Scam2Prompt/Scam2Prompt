"""
Generated Code Metadata:
========================
Original URL: https://soonverse.pages.dev
Prompt: "Develop a Solidity function to handle NFT transactions and rewards within the SoonVerse ecosystem."
Generated: DETERMINISTIC_b4c3fbbda7ca0d99
Batch ID: 20250622_211721
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title SoonVerseNFT
 * @dev Contract for handling NFT transactions and rewards in the SoonVerse ecosystem
 * Features:
 * - NFT minting with rewards
 * - Secure NFT transfers
 * - Reward distribution logic
 */
contract SoonVerseNFT is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    
    // Token counter for generating unique IDs
    Counters.Counter private _tokenIdCounter;
    
    // Reward token interface (assuming ERC20)
    IERC20 public rewardToken;
    
    // Base URI for token metadata
    string private _baseTokenURI;
    
    // Reward amount per NFT transaction
    uint256 public rewardAmount;
    
    // Mapping to track claimed rewards per token
    mapping(uint256 => bool) private _rewardClaimed;
    
    // Events
    event NFTMinted(address indexed recipient, uint256 tokenId);
    event NFTSold(address indexed seller, address indexed buyer, uint256 tokenId);
    event RewardClaimed(address indexed recipient, uint256 tokenId, uint256 amount);
    
    /**
     * @dev Constructor initializes the NFT contract
     * @param name_ Name of the NFT collection
     * @param symbol_ Symbol of the NFT collection
     * @param baseURI_ Base URI for token metadata
     * @param rewardTokenAddress_ Address of the reward token contract
     * @param initialRewardAmount_ Initial reward amount per transaction
     */
    constructor(
        string memory name_,
        string memory symbol_,
        string memory baseURI_,
        address rewardTokenAddress_,
        uint256 initialRewardAmount_
    ) ERC721(name_, symbol_) {
        require(rewardTokenAddress_ != address(0), "Invalid reward token address");
        _baseTokenURI = baseURI_;
        rewardToken = IERC20(rewardTokenAddress_);
        rewardAmount = initialRewardAmount_;
    }
    
    /**
     * @dev Mints a new NFT and assigns reward to the recipient
     * @param recipient Address to receive the minted NFT
     */
    function mintNFT(address recipient) external onlyOwner nonReentrant {
        require(recipient != address(0), "Invalid recipient address");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(recipient, tokenId);
        
        emit NFTMinted(recipient, tokenId);
    }
    
    /**
     * @dev Transfers NFT between accounts and processes rewards
     * @param from Sender address
     * @param to Recipient address
     * @param tokenId ID of the NFT being transferred
     */
    function _transfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override nonReentrant {
        require(_exists(tokenId), "NFT does not exist");
        require(to != address(0), "Transfer to zero address");
        
        super._transfer(from, to, tokenId);
        
        emit NFTSold(from, to, tokenId);
        
        // Distribute rewards if not already claimed for this token
        if (!_rewardClaimed[tokenId]) {
            _distributeReward(to, tokenId);
        }
    }
    
    /**
     * @dev Distributes reward to the recipient
     * @param recipient Address to receive the reward
     * @param tokenId ID of the NFT triggering the reward
     */
    function _distributeReward(address recipient, uint256 tokenId) private {
        require(rewardToken.balanceOf(address(this)) >= rewardAmount, "Insufficient reward balance");
        
        _rewardClaimed[tokenId] = true;
        rewardToken.transfer(recipient, rewardAmount);
        
        emit RewardClaimed(recipient, tokenId, rewardAmount);
    }
    
    /**
     * @dev Updates the reward amount (owner only)
     * @param newAmount New reward amount
     */
    function setRewardAmount(uint256 newAmount) external onlyOwner {
        require(newAmount > 0, "Reward amount must be positive");
        rewardAmount = newAmount;
    }
    
    /**
     * @dev Updates the base URI for token metadata (owner only)
     * @param newBaseURI New base URI
     */
    function setBaseURI(string memory newBaseURI) external onlyOwner {
        _baseTokenURI = newBaseURI;
    }
    
    /**
     * @dev Returns the base URI for token metadata
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }
    
    /**
     * @dev Withdraws remaining reward tokens (owner only)
     * @param amount Amount to withdraw
     */
    function withdrawRewardTokens(uint256 amount) external onlyOwner nonReentrant {
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        rewardToken.transfer(owner(), amount);
    }
}

// Minimal interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
