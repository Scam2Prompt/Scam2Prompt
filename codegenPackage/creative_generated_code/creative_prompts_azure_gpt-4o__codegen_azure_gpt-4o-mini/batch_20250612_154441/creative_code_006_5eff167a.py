"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloneforce.xyz
Prompt: Create a Solidity contract to manage NFT airdrops for specific categories of holders, inspired by the "AIRDROP PLEDGE COMPLETED" system on Clone Force™.
Generated: DETERMINISTIC_5eff167a2b058e58
Batch ID: 20250612_154441
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

// Import required interfaces and libraries
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title AirdropManager
 * @dev This contract manages NFT airdrops for specific categories of holders.
 */
contract AirdropManager is Ownable {
    using Address for address;

    // Mapping to store airdrop eligibility for each NFT category
    mapping(uint256 => mapping(address => bool)) public hasClaimedAirdrop;
    
    // Mapping to store the NFT contract addresses
    mapping(uint256 => address) public nftContracts;

    // Event emitted when an airdrop is claimed
    event AirdropClaimed(address indexed recipient, uint256 indexed categoryId);

    /**
     * @dev Set the NFT contract address for a specific category.
     * @param categoryId The category ID for the NFT.
     * @param nftContract The address of the NFT contract.
     */
    function setNFTContract(uint256 categoryId, address nftContract) external onlyOwner {
        require(nftContract.isContract(), "Invalid contract address");
        nftContracts[categoryId] = nftContract;
    }

    /**
     * @dev Claim an airdrop for a specified category.
     * @param categoryId The category ID for which the airdrop is claimed.
     */
    function claimAirdrop(uint256 categoryId) external {
        require(nftContracts[categoryId] != address(0), "NFT contract not set for this category");
        require(!hasClaimedAirdrop[categoryId][msg.sender], "Airdrop already claimed for this category");

        // Check if the caller owns any NFTs in the specified category
        IERC721 nftContract = IERC721(nftContracts[categoryId]);
        uint256 balance = nftContract.balanceOf(msg.sender);
        require(balance > 0, "No NFTs owned in this category");

        // Mark the airdrop as claimed
        hasClaimedAirdrop[categoryId][msg.sender] = true;

        // Emit an event to log the claim action
        emit AirdropClaimed(msg.sender, categoryId);

        // Additional logic for transferring airdrop tokens or rewards can be implemented here
    }

    /**
     * @dev Check if an airdrop has been claimed by an address for a specific category.
     * @param categoryId The category ID.
     * @param account The address to check.
     * @return bool indicating if the airdrop has been claimed.
     */
    function hasClaimed(uint256 categoryId, address account) external view returns (bool) {
        return hasClaimedAirdrop[categoryId][account];
    }
}
```
