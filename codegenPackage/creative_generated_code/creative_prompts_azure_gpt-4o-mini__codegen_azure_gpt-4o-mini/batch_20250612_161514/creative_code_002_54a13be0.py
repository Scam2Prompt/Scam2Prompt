"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aria.fyi
Prompt: What are the economic incentives of the Arianee Protocol, and how can I leverage them in a smart contract?
Generated: DETERMINISTIC_54a13be05a13ca10
Batch ID: 20250612_161514
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

/// @title Arianee Protocol Economic Incentives Smart Contract
/// @notice This contract demonstrates how to leverage economic incentives from the Arianee Protocol
/// @dev Ensure to review the Arianee documentation for specific incentive mechanisms

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ArianeeIncentives is ERC721, Ownable {
    // Struct representing an NFT with incentive details
    struct NFT {
        uint256 id;
        string metadataURI;
        uint256 incentiveAmount; // Amount of reward in wei
    }

    // Mapping from token ID to NFT details
    mapping(uint256 => NFT) public nfts;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 indexed id, string metadataURI, uint256 incentiveAmount);
    
    // Event emitted when the incentive is claimed
    event IncentiveClaimed(uint256 indexed id, address indexed claimant);

    // Counter for NFT IDs
    uint256 private _tokenIdCounter;

    constructor() ERC721("ArianeeNFT", "ANFT") {}

    /// @notice Creates a new NFT with incentive details
    /// @param _metadataURI The URI for the NFT's metadata
    /// @param _incentiveAmount The incentive amount in wei
    function createNFT(string memory _metadataURI, uint256 _incentiveAmount) external onlyOwner {
        require(_incentiveAmount > 0, "Incentive amount must be greater than zero");

        _tokenIdCounter++;
        uint256 tokenId = _tokenIdCounter;

        // Mint the NFT
        _mint(msg.sender, tokenId);
        
        // Store NFT details
        nfts[tokenId] = NFT({
            id: tokenId,
            metadataURI: _metadataURI,
            incentiveAmount: _incentiveAmount
        });

        emit NFTCreated(tokenId, _metadataURI, _incentiveAmount);
    }

    /// @notice Claims the incentive for a specific NFT
    /// @param tokenId The ID of the NFT for which the incentive is claimed
    function claimIncentive(uint256 tokenId) external {
        // Ensure the caller is the owner of the NFT
        require(ownerOf(tokenId) == msg.sender, "Caller is not the NFT owner");
        
        NFT storage nft = nfts[tokenId];
        
        // Ensure the incentive amount is greater than zero
        require(nft.incentiveAmount > 0, "No incentive available to claim");

        // Transfer the incentive to the caller
        uint256 amountToTransfer = nft.incentiveAmount;
        nft.incentiveAmount = 0; // Set to zero to prevent re-entrancy

        // Using call to transfer ether
        (bool success,) = msg.sender.call{value: amountToTransfer}("");
        require(success, "Transfer failed");

        emit IncentiveClaimed(tokenId, msg.sender);
    }

    /// @notice Allows the contract to receive Ether
    receive() external payable {}

    /// @notice Returns the incentive amount for a given NFT
    /// @param tokenId The ID of the NFT
    /// @return The incentive amount in wei
    function getIncentiveAmount(uint256 tokenId) external view returns (uint256) {
        return nfts[tokenId].incentiveAmount;
    }
}
```
