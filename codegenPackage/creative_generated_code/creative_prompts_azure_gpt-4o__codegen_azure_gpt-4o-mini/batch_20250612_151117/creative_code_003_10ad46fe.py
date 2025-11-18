"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zora-7pj.pages.dev
Prompt: Write a smart contract that facilitates minting commemorative NFTs for Reveel Campaigns, ensuring rewards are unlocked for holders.
Generated: DETERMINISTIC_10ad46fe43beb0b6
Batch ID: 20250612_151117
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title ReveelCampaignNFT
// @dev This contract allows for minting commemorative NFTs for Reveel campaigns and rewards holders.
contract ReveelCampaignNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed recipient, uint256 tokenId);
    
    // Event emitted when rewards are unlocked for a holder
    event RewardsUnlocked(address indexed holder, uint256 tokenId, uint256 rewardAmount);

    // Variables to manage the NFT supply and rewards
    Counters.Counter private _tokenIdCounter;
    string public baseURI;
    mapping(uint256 => uint256) public rewards; // Maps tokenId to reward amount
    uint256 public rewardRate; // Rate at which rewards accumulate

    // @dev Constructor to initialize the contract with the name and symbol
    constructor(string memory name, string memory symbol, string memory initialBaseURI, uint256 initialRewardRate) 
        ERC721(name, symbol) 
    {
        baseURI = initialBaseURI;
        rewardRate = initialRewardRate;
    }

    // @dev Allows the owner to set a new base URI for the NFTs
    // @param newBaseURI The new base URI for the NFT metadata
    function setBaseURI(string memory newBaseURI) external onlyOwner {
        baseURI = newBaseURI;
    }

    // @dev Allows the owner to set a new reward rate
    // @param newRewardRate The new reward rate for holders
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    // @dev Mint a new NFT to the specified address
    // @param recipient The address receiving the NFT
    function mintNFT(address recipient) external onlyOwner {
        require(recipient != address(0), "Invalid address");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _mint(recipient, tokenId);
        rewards[tokenId] = 0; // Initialize rewards for the new NFT
        
        emit NFTMinted(recipient, tokenId);
    }

    // @dev Unlock rewards for the holder of a specific NFT
    // @param tokenId The token ID of the NFT
    function unlockRewards(uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "Not the NFT holder");
        
        uint256 rewardAmount = calculateRewards(tokenId);
        rewards[tokenId] += rewardAmount;
        
        emit RewardsUnlocked(msg.sender, tokenId, rewardAmount);
    }

    // @dev Calculate rewards for a specific NFT
    // @param tokenId The token ID for which to calculate rewards
    // @return The amount of rewards calculated
    function calculateRewards(uint256 tokenId) internal view returns (uint256) {
        // For simplicity, we return a calculated reward based on the tokenId and rewardRate
        return (tokenId + 1) * rewardRate; // Example calculation
    }

    // @dev Override the base token URI function to use the set base URI
    // @return The base URI for the NFT metadata
    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }
}
```
