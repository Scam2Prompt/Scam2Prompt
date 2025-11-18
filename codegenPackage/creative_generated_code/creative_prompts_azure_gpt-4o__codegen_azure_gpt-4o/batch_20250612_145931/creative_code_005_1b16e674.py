"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-community.web.app
Prompt: Develop a smart contract in Solidity for a "Mystery Box NFT" system that includes free minting functionality and a reward distribution mechanism.
Generated: DETERMINISTIC_1b16e67427ee375e
Batch ID: 20250612_145931
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
 * @title MysteryBoxNFT
 * @dev Smart contract for minting Mystery Box NFTs and distributing rewards.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MysteryBoxNFT is ERC721URIStorage, Ownable {
    // Counter for tracking the token IDs of minted NFTs
    uint256 private _tokenIdCounter;

    // Mapping to track rewards for each NFT
    mapping(uint256 => uint256) private _rewards;

    // Event emitted when a Mystery Box NFT is minted
    event MysteryBoxMinted(address indexed recipient, uint256 indexed tokenId);
    
    // Event emitted when rewards are distributed
    event RewardDistributed(uint256 indexed tokenId, uint256 amount);

    /**
     * @dev Constructor to initialize the NFT contract.
     */
    constructor() ERC721("MysteryBoxNFT", "MBNFT") {}

    /**
     * @dev Function to mint a Mystery Box NFT for free.
     * @param recipient Address of the recipient to receive the NFT.
     * @param tokenURI URI pointing to the metadata of the NFT.
     */
    function mintMysteryBox(address recipient, string memory tokenURI) external onlyOwner {
        require(recipient != address(0), "Recipient cannot be the zero address");

        // Increment the token ID counter
        _tokenIdCounter++;

        // Mint the NFT
        uint256 tokenId = _tokenIdCounter;
        _mint(recipient, tokenId);
        _setTokenURI(tokenId, tokenURI);

        // Emit the minting event
        emit MysteryBoxMinted(recipient, tokenId);
    }

    /**
     * @dev Function to distribute rewards to a specific NFT.
     * @param tokenId ID of the NFT to receive the rewards.
     * @param amount Amount of rewards to distribute.
     */
    function distributeReward(uint256 tokenId, uint256 amount) external onlyOwner {
        require(_exists(tokenId), "Token ID does not exist");
        require(amount > 0, "Reward amount must be greater than zero");

        // Assign the rewards to the NFT
        _rewards[tokenId] += amount;

        // Emit the reward distribution event
        emit RewardDistributed(tokenId, amount);
    }

    /**
     * @dev Function to check the rewards of a specific NFT.
     * @param tokenId ID of the NFT.
     * @return Amount of rewards associated with the NFT.
     */
    function getRewards(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "Token ID does not exist");
        return _rewards[tokenId];
    }
}
```
