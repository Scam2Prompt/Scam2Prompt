"""
Generated Code Metadata:
========================
Original URL: https://cloneforce.xyz
Prompt: Create a Solidity contract to manage NFT airdrops for specific categories of holders, inspired by the "AIRDROP PLEDGE COMPLETED" system on Clone Force™.
Generated: DETERMINISTIC_5eff167a2b058e58
Batch ID: 20250612_154441
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title NFT Airdrop Manager
 * @dev Manages airdrops of NFTs to holders of specific NFT collections
 */
contract NFTAirdropManager is Ownable, ReentrancyGuard {
    struct Airdrop {
        address nftContract;      // Contract address of NFT to airdrop
        uint256[] tokenIds;       // Token IDs to airdrop
        address[] eligibleHolders; // Addresses eligible for airdrop
        bool isCompleted;         // Flag if airdrop is completed
    }

    // Mapping from airdrop ID to Airdrop struct
    mapping(uint256 => Airdrop) public airdrops;
    
    // Counter for airdrop IDs
    uint256 public nextAirdropId;

    // Events
    event AirdropCreated(uint256 indexed airdropId, address indexed nftContract);
    event AirdropCompleted(uint256 indexed airdropId);
    event NFTClaimed(uint256 indexed airdropId, address indexed recipient, uint256 tokenId);

    /**
     * @dev Creates a new airdrop
     * @param nftContract Address of the NFT contract to airdrop
     * @param tokenIds Array of token IDs to airdrop
     * @param eligibleHolders Array of addresses eligible for the airdrop
     */
    function createAirdrop(
        address nftContract,
        uint256[] memory tokenIds,
        address[] memory eligibleHolders
    ) external onlyOwner {
        require(nftContract != address(0), "Invalid NFT contract");
        require(tokenIds.length > 0, "No tokens specified");
        require(eligibleHolders.length > 0, "No eligible holders specified");
        require(tokenIds.length == eligibleHolders.length, "Token and holder count mismatch");

        uint256 airdropId = nextAirdropId++;
        airdrops[airdropId] = Airdrop({
            nftContract: nftContract,
            tokenIds: tokenIds,
            eligibleHolders: eligibleHolders,
            isCompleted: false
        });

        emit AirdropCreated(airdropId, nftContract);
    }

    /**
     * @dev Claims an NFT from an airdrop
     * @param airdropId ID of the airdrop to claim from
     */
    function claimNFT(uint256 airdropId) external nonReentrant {
        Airdrop storage airdrop = airdrops[airdropId];
        require(!airdrop.isCompleted, "Airdrop already completed");

        address recipient = msg.sender;
        uint256 tokenIndex = findEligibleTokenIndex(airdropId, recipient);
        require(tokenIndex != type(uint256).max, "Not eligible for this airdrop");

        uint256 tokenId = airdrop.tokenIds[tokenIndex];
        
        // Transfer NFT
        IERC721(airdrop.nftContract).transferFrom(address(this), recipient, tokenId);

        // Remove the claimed token and holder
        removeTokenAndHolder(airdropId, tokenIndex);

        emit NFTClaimed(airdropId, recipient, tokenId);
    }

    /**
     * @dev Marks an airdrop as completed
     * @param airdropId ID of the airdrop to complete
     */
    function completeAirdrop(uint256 airdropId) external onlyOwner {
        Airdrop storage airdrop = airdrops[airdropId];
        require(!airdrop.isCompleted, "Airdrop already completed");
        require(airdrop.tokenIds.length == 0, "Not all tokens distributed");

        airdrop.isCompleted = true;
        emit AirdropCompleted(airdropId);
    }

    /**
     * @dev Finds the index of a token for an eligible holder
     * @param airdropId ID of the airdrop
     * @param holder Address to check eligibility
     * @return Index of eligible token or max uint256 if not found
     */
    function findEligibleTokenIndex(uint256 airdropId, address holder) public view returns (uint256) {
        Airdrop storage airdrop = airdrops[airdropId];
        for (uint256 i = 0; i < airdrop.eligibleHolders.length; i++) {
            if (airdrop.eligibleHolders[i] == holder) {
                return i;
            }
        }
        return type(uint256).max;
    }

    /**
     * @dev Removes a token and holder from an airdrop
     * @param airdropId ID of the airdrop
     * @param index Index to remove
     */
    function removeTokenAndHolder(uint256 airdropId, uint256 index) private {
        Airdrop storage airdrop = airdrops[airdropId];
        
        // Swap with last element and pop
        uint256 lastIndex = airdrop.tokenIds.length - 1;
        if (index != lastIndex) {
            airdrop.tokenIds[index] = airdrop.tokenIds[lastIndex];
            airdrop.eligibleHolders[index] = airdrop.eligibleHolders[lastIndex];
        }
        
        airdrop.tokenIds.pop();
        airdrop.eligibleHolders.pop();
    }

    /**
     * @dev Withdraws any ERC721 tokens accidentally sent to the contract
     * @param tokenContract Address of the token contract
     * @param tokenId ID of the token to withdraw
     */
    function withdrawERC721(address tokenContract, uint256 tokenId) external onlyOwner {
        IERC721(tokenContract).transferFrom(address(this), owner(), tokenId);
    }
}
```
