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

/// @title Reveel Campaign Commemorative NFT Contract
/// @author Your Name
/// @notice This smart contract allows minting commemorative NFTs for Reveel campaigns and unlocks rewards for holders.
/// @dev ERC721 is implemented along with reward distribution functionality.

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ReveelCampaignNFT is ERC721URIStorage, Ownable {
    // State variables
    uint256 private _tokenIdCounter; // Counter for token IDs
    mapping(uint256 => string) private _rewardData; // Mapping token ID to reward data
    mapping(uint256 => bool) private _rewardUnlocked; // Mapping token ID to unlock status

    /// @dev Event emitted when a new NFT is minted
    event NFTMinted(address indexed recipient, uint256 tokenId, string tokenURI);

    /// @dev Event emitted when rewards are unlocked for an NFT holder
    event RewardUnlocked(uint256 tokenId, string rewardData);

    /// @notice Constructor initializes the ERC721 token with name and symbol
    /// @param name Name of the NFT collection
    /// @param symbol Symbol of the NFT collection
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /// @notice Mint a new NFT with specified metadata and reward data
    /// @param recipient Address to receive the minted NFT
    /// @param tokenURI URI pointing to the NFT metadata
    /// @param rewardData Data for the reward associated with the NFT
    /// @dev Only the contract owner can mint new NFTs
    function mintNFT(
        address recipient,
        string memory tokenURI,
        string memory rewardData
    ) external onlyOwner {
        // Increment the token ID counter
        _tokenIdCounter += 1;
        uint256 newTokenId = _tokenIdCounter;

        // Mint the NFT to the recipient
        _mint(recipient, newTokenId);

        // Set the token URI
        _setTokenURI(newTokenId, tokenURI);

        // Store the reward data for the new token
        _rewardData[newTokenId] = rewardData;

        // Emit the NFTMinted event
        emit NFTMinted(recipient, newTokenId, tokenURI);
    }

    /// @notice Unlock the reward for the holder of a specific NFT token ID
    /// @param tokenId Token ID of the NFT whose reward is to be unlocked
    /// @dev Only the contract owner can unlock rewards
    function unlockReward(uint256 tokenId) external onlyOwner {
        require(_exists(tokenId), "NFT does not exist"); // Ensure NFT exists
        require(!_rewardUnlocked[tokenId], "Reward already unlocked"); // Ensure reward is not already unlocked

        // Mark the reward as unlocked
        _rewardUnlocked[tokenId] = true;

        // Emit the RewardUnlocked event
        emit RewardUnlocked(tokenId, _rewardData[tokenId]);
    }

    /// @notice Check if a reward is unlocked for a specific NFT
    /// @param tokenId Token ID of the NFT
    /// @return bool True if reward is unlocked, otherwise false
    function isRewardUnlocked(uint256 tokenId) external view returns (bool) {
        require(_exists(tokenId), "NFT does not exist"); // Ensure NFT exists
        return _rewardUnlocked[tokenId];
    }

    /// @notice Get reward data for a specific NFT
    /// @param tokenId Token ID of the NFT
    /// @return string Reward data associated with the NFT
    /// @dev Reward data is only accessible if the reward is unlocked
    function getRewardData(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "NFT does not exist"); // Ensure NFT exists
        require(_rewardUnlocked[tokenId], "Reward not unlocked"); // Ensure reward is unlocked
        return _rewardData[tokenId];
    }
}
```
