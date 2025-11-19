"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oddfellowsnft.com
Prompt: Generate a smart contract for an NFT collection based on the Secret Society of Odd Fellows concept.
Generated: DETERMINISTIC_871b06d63bff7f75
Batch ID: 20250612_160625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a clean and well-documented Solidity smart contract for an NFT collection inspired by the "Secret Society of Odd Fellows" concept:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin's ERC721 implementation and other utilities
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title SecretSocietyNFT
 * @dev A smart contract for an NFT collection inspired by the Secret Society of Odd Fellows.
 */
contract SecretSocietyNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter to track token IDs
    Counters.Counter private _tokenIdCounter;

    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Base URI for metadata
    string private _baseTokenURI;

    // Mint price per NFT
    uint256 public mintPrice = 0.05 ether;

    // Mapping to store whitelist addresses
    mapping(address => bool) public whitelist;

    // Event for minting an NFT
    event NFTMinted(address indexed minter, uint256 tokenId);

    /**
     * @dev Constructor that initializes the collection with a name and symbol.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol, string memory baseURI) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Function to mint an NFT. Requires payment of the mint price.
     */
    function mint() external payable {
        // Ensure the maximum supply is not exceeded
        require(totalSupply() < MAX_SUPPLY, "All NFTs have been minted.");

        // Check that the sender has provided the correct mint price
        require(msg.value >= mintPrice, "Insufficient funds to mint.");

        // Increment token ID counter
        _tokenIdCounter.increment();

        // Mint the NFT to the sender
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(msg.sender, tokenId);

        // Emit the minting event
        emit NFTMinted(msg.sender, tokenId);
    }

    /**
     * @dev Owner-only function to mint an NFT to a specific address. Useful for giveaways.
     * @param to Address to receive the NFT.
     */
    function ownerMint(address to) external onlyOwner {
        // Ensure the maximum supply is not exceeded
        require(totalSupply() < MAX_SUPPLY, "All NFTs have been minted.");

        // Increment token ID counter
        _tokenIdCounter.increment();

        // Mint the NFT to the specified address
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(to, tokenId);

        // Emit the minting event
        emit NFTMinted(to, tokenId);
    }

    /**
     * @dev Function to check total supply of minted NFTs.
     */
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }

    /**
     * @dev Function to set a new base URI for metadata. Only callable by the owner.
     * @param baseURI New base URI.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Function to get the base URI for metadata.
     * @return Base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Function to set a new mint price. Only callable by the owner.
     * @param newPrice New mint price in wei.
     */
    function setMintPrice(uint256 newPrice) external onlyOwner {
        mintPrice = newPrice;
    }

    /**
     * @dev Function to add an address to the whitelist. Only callable by the owner.
     * @param addr Address to whitelist.
     */
    function addToWhitelist(address addr) external onlyOwner {
        whitelist[addr] = true;
    }

    /**
     * @dev Function to remove an address from the whitelist. Only callable by the owner.
     * @param addr Address to remove from the whitelist.
     */
    function removeFromWhitelist(address addr) external onlyOwner {
        whitelist[addr] = false;
    }

    /**
     * @dev Withdraw function allowing the owner to collect all contract funds.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw.");
        payable(owner()).transfer(balance);
    }
}
```

Make sure to test the contract thoroughly before deploying it to production. Also, you'll need to adjust parameters such as the `MAX_SUPPLY`, `mintPrice`, and metadata `baseURI` to suit your specific project.
