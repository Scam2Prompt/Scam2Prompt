"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptotitties.fun
Prompt: Generate a Solidity contract for an NFT charity project similar to CryptOtitties, including features for donation tracking and ERC721 compliance.
Generated: DETERMINISTIC_832cb84233d8e55b
Batch ID: 20250612_135046
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

// Importing the ERC721 interface and implementation
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// CharityNFT is an ERC721 token that also tracks donations
contract CharityNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Struct to hold information about each NFT
    struct NFT {
        uint256 id;
        string tokenURI; // Metadata URI
        uint256 donationAmount; // Amount donated for this NFT
    }

    // Counter for NFT IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to NFT details
    mapping(uint256 => NFT) private _nfts;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 indexed tokenId, string tokenURI, address owner);

    // Event emitted when a donation is made
    event DonationReceived(uint256 indexed tokenId, address donor, uint256 amount);

    constructor() ERC721("CharityNFT", "CNFT") {}

    /**
     * @dev Creates a new NFT with the specified metadata URI.
     * @param tokenURI The metadata URI of the NFT.
     */
    function createNFT(string memory tokenURI) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _nfts[tokenId] = NFT(tokenId, tokenURI, 0);
        
        _tokenIdCounter.increment();
        
        emit NFTCreated(tokenId, tokenURI, msg.sender);
    }

    /**
     * @dev Allows users to donate to a specific NFT.
     * @param tokenId The ID of the NFT to donate to.
     */
    function donate(uint256 tokenId) external payable {
        require(_exists(tokenId), "NFT does not exist");
        require(msg.value > 0, "Donation must be greater than zero");

        // Update the donation amount
        _nfts[tokenId].donationAmount += msg.value;

        // Emit the donation event
        emit DonationReceived(tokenId, msg.sender, msg.value);
    }

    /**
     * @dev Returns the donation amount for a specific NFT.
     * @param tokenId The ID of the NFT.
     * @return The total donation amount for the NFT.
     */
    function getDonationAmount(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "NFT does not exist");
        return _nfts[tokenId].donationAmount;
    }

    /**
     * @dev Withdraw the total donations to the owner's address.
     */
    function withdrawDonations() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");
        
        // Transfer the balance to the owner
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Transfer failed");
    }

    /**
     * @dev Returns the metadata URI for a specific NFT.
     * @param tokenId The ID of the NFT.
     * @return The metadata URI of the NFT.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "NFT does not exist");
        return _nfts[tokenId].tokenURI;
    }
}
```
