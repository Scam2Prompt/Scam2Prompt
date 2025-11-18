"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hypurrnft.org
Prompt: Generate a smart contract in Solidity for minting NFTs, specifically for a Genesis Collection, and include terms and conditions handling as outlined on the Hypurr NFT Mint Portal.
Generated: DETERMINISTIC_89b37bd154fa5d47
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title GenesisNFTCollection
 * @dev Smart contract for minting NFTs in a Genesis Collection with terms and conditions handling.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GenesisNFTCollection is ERC721Enumerable, Ownable {
    // Metadata for the collection
    string private _baseTokenURI;

    // Minting price in Wei
    uint256 public mintPrice;

    // Maximum supply for the Genesis Collection
    uint256 public maxSupply;

    // Terms and conditions acceptance
    mapping(address => bool) private _termsAccepted;

    /**
     * @dev Contract constructor. Sets the token name and symbol, base URI, mint price, and max supply.
     * @param name Token name
     * @param symbol Token symbol
     * @param baseTokenURI Base URI for token metadata
     * @param _mintPrice Price to mint each NFT (in wei)
     * @param _maxSupply Total maximum supply of NFTs
     */
    constructor(
        string memory name,
        string memory symbol,
        string memory baseTokenURI,
        uint256 _mintPrice,
        uint256 _maxSupply
    ) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
        mintPrice = _mintPrice;
        maxSupply = _maxSupply;
    }

    /**
     * @dev Public function to mint an NFT. Requires terms and conditions acceptance and enough ether.
     */
    function mintNFT(uint256 quantity) external payable {
        require(quantity > 0, "Must mint at least one NFT");
        require(totalSupply() + quantity <= maxSupply, "Exceeds maximum supply");
        require(msg.value >= mintPrice * quantity, "Insufficient ether sent");
        require(hasAcceptedTerms(msg.sender), "Must accept terms and conditions");

        for (uint256 i = 0; i < quantity; i++) {
            uint256 tokenId = totalSupply() + 1;
            _safeMint(msg.sender, tokenId);
        }
    }

    /**
     * @dev Function to accept terms and conditions. Must be called before minting.
     */
    function acceptTermsAndConditions() external {
        require(!_termsAccepted[msg.sender], "Terms already accepted");
        _termsAccepted[msg.sender] = true;
    }

    /**
     * @dev Check if an address has accepted terms and conditions.
     * @param account Address to check
     * @return True if terms are accepted, false otherwise
     */
    function hasAcceptedTerms(address account) public view returns (bool) {
        return _termsAccepted[account];
    }

    /**
     * @dev Override for _baseURI to set the base token URI.
     * @return Base URI for token metadata
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Owner-only function to update the base URI for metadata.
     * @param baseTokenURI New base URI for metadata
     */
    function setBaseTokenURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Owner-only function to update the mint price.
     * @param newMintPrice New mint price in wei
     */
    function setMintPrice(uint256 newMintPrice) external onlyOwner {
        mintPrice = newMintPrice;
    }

    /**
     * @dev Owner-only function to withdraw contract balance.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        (bool success, ) = payable(owner()).call{value: balance}("");
        require(success, "Withdrawal failed");
    }
}
```
