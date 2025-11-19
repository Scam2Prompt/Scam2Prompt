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

// Import the ERC721 standard interface and utility extensions from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title NFT Charity Contract
/// @notice This contract handles minting of NFTs while tracking donations made to the charity.
contract CharityNFT is ERC721Enumerable, Ownable {
    // State variable to store the base URI for token metadata
    string private baseTokenURI;

    // Counter for token ID to ensure unique IDs
    uint256 private _nextTokenId;

    // Mapping to track donations made by each address
    mapping(address => uint256) public donations;

    // Event emitted whenever a donation is made
    event DonationReceived(address indexed donor, uint256 amount);

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed recipient, uint256 tokenId);

    /// @notice Constructor to initialize the token name and symbol
    /// @param name Name of the ERC721 token
    /// @param symbol Symbol of the ERC721 token
    constructor(string memory name, string memory symbol, string memory _baseTokenURI) ERC721(name, symbol) {
        baseTokenURI = _baseTokenURI;
    }

    /// @notice Function to make a donation and optionally mint an NFT
    /// @dev The donation amount must be sent along with the transaction
    /// @param mintNFT Boolean indicating whether to mint an NFT for the donor
    function donate(bool mintNFT) external payable {
        require(msg.value > 0, "Donation must be greater than zero");

        // Track the donation amount for the donor
        donations[msg.sender] += msg.value;

        emit DonationReceived(msg.sender, msg.value);

        // Mint an NFT for the donor if requested
        if (mintNFT) {
            _mintNFT(msg.sender);
        }
    }

    /// @notice Function to mint an NFT
    /// @dev Only callable internally after a donation
    /// @param recipient Address to receive the minted NFT
    function _mintNFT(address recipient) internal {
        // Increment the token ID counter
        uint256 newTokenId = _nextTokenId;
        _nextTokenId++;

        // Mint the NFT to the recipient address
        _safeMint(recipient, newTokenId);

        emit NFTMinted(recipient, newTokenId);
    }

    /// @notice Function to set the base URI for token metadata
    /// @dev Only callable by the contract owner
    /// @param _baseTokenURI The new base URI for token metadata
    function setBaseURI(string memory _baseTokenURI) external onlyOwner {
        baseTokenURI = _baseTokenURI;
    }

    /// @notice Function to retrieve the base URI for token metadata
    /// @dev Overrides the baseURI function from ERC721
    /// @return The current base URI for token metadata
    function _baseURI() internal view override returns (string memory) {
        return baseTokenURI;
    }

    /// @notice Function to withdraw funds accumulated in the contract
    /// @dev Only callable by the contract owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");

        // Transfer the contract balance to the owner
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /// @notice Fallback function to accept donations
    /// @dev Allows donations to be sent directly to the contract
    receive() external payable {
        require(msg.value > 0, "Donation must be greater than zero");

        // Track the donation amount for the sender
        donations[msg.sender] += msg.value;

        emit DonationReceived(msg.sender, msg.value);
    }
}
```
