"""
Generated Code Metadata:
========================
Original URL: https://duty-starheroescommunity.pages.dev
Prompt: Create a Solidity smart contract that verifies user eligibility for claiming NFTs based on external API data, referencing the JungleArt.ai integration mentioned on the StarHeroes website.
Generated: DETERMINISTIC_2a913d06e80fdc9b
Batch ID: 20250612_151018
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

// Interface for the external API interaction
interface IExternalAPI {
    function getUserEligibility(address user) external view returns (bool);
}

// Smart contract for verifying user eligibility for claiming NFTs
contract NFTClaimEligibility is Ownable {
    // Address of the external API contract
    IExternalAPI public externalAPI;

    // Mapping to track claimed NFTs
    mapping(address => bool) public hasClaimed;

    // Event emitted when an NFT is claimed
    event NFTClaimed(address indexed user);

    // Constructor to set the external API contract address
    constructor(address _externalAPI) {
        require(_externalAPI != address(0), "Invalid API address");
        externalAPI = IExternalAPI(_externalAPI);
    }

    // Function to claim NFT
    function claimNFT() external {
        // Check if the user has already claimed
        require(!hasClaimed[msg.sender], "NFT already claimed");

        // Verify user eligibility via external API
        bool eligible = externalAPI.getUserEligibility(msg.sender);
        require(eligible, "User is not eligible to claim NFT");

        // Mark the user as having claimed the NFT
        hasClaimed[msg.sender] = true;

        // Emit the NFT claimed event
        emit NFTClaimed(msg.sender);

        // Logic to mint or transfer the NFT would go here
        // For example: mintNFT(msg.sender);
    }

    // Function to update the external API address (only owner can update)
    function updateExternalAPI(address _externalAPI) external onlyOwner {
        require(_externalAPI != address(0), "Invalid API address");
        externalAPI = IExternalAPI(_externalAPI);
    }

    // Function to check if a user has claimed an NFT
    function hasUserClaimed(address user) external view returns (bool) {
        return hasClaimed[user];
    }
}
```
