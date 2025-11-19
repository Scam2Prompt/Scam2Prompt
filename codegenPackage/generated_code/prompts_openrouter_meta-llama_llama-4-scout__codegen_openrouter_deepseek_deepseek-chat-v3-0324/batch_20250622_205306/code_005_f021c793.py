"""
Generated Code Metadata:
========================
Original URL: https://neftyartstudio.com
Prompt: "Create a smart contract using Solidity to manage NFT ownership and transfer on a platform similar to Neftyartstudio."
Generated: DETERMINISTIC_f021c793e2464eb0
Batch ID: 20250622_205306
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract NeftyArtNFT is ERC721, ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Base URI for token metadata
    string private _baseTokenURI;

    // Royalty information
    struct RoyaltyInfo {
        address recipient;
        uint24 amount; // basis points (10000 = 100%)
    }

    // Mapping from token ID to royalty info
    mapping(uint256 => RoyaltyInfo) private _royalties;

    // Platform fee (percentage)
    uint24 public platformFee;
    address public platformFeeRecipient;

    // Events
    event Minted(address indexed to, uint256 indexed tokenId);
    event RoyaltySet(uint256 indexed tokenId, address recipient, uint256 amount);
    event PlatformFeeUpdated(uint24 newFee);
    event PlatformFeeRecipientUpdated(address newRecipient);

    constructor(
        string memory name,
        string memory symbol,
        string memory baseTokenURI,
        uint24 _platformFee,
        address _platformFeeRecipient
    ) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
        platformFee = _platformFee;
        platformFeeRecipient = _platformFeeRecipient;
    }

    // Mint a new NFT
    function safeMint(address to, address royaltyRecipient, uint24 royaltyAmount) public onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
        
        if (royaltyRecipient != address(0) && royaltyAmount > 0) {
            _setRoyalty(tokenId, royaltyRecipient, royaltyAmount);
        }

        emit Minted(to, tokenId);
    }

    // Set royalty information for a token
    function setRoyalty(uint256 tokenId, address recipient, uint24 amount) public onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        _setRoyalty(tokenId, recipient, amount);
    }

    function _setRoyalty(uint256 tokenId, address recipient, uint24 amount) private {
        require(amount <= 10000, "Royalty exceeds 100%");
        _royalties[tokenId] = RoyaltyInfo(recipient, amount);
        emit RoyaltySet(tokenId, recipient, amount);
    }

    // Get royalty information for a token
    function getRoyalty(uint256 tokenId) public view returns (address recipient, uint256 amount) {
        require(_exists(tokenId), "Token does not exist");
        RoyaltyInfo memory royalty = _royalties[tokenId];
        return (royalty.recipient, royalty.amount);
    }

    // Update platform fee
    function updatePlatformFee(uint24 newFee) public onlyOwner {
        require(newFee <= 10000, "Fee exceeds 100%");
        platformFee = newFee;
        emit PlatformFeeUpdated(newFee);
    }

    // Update platform fee recipient
    function updatePlatformFeeRecipient(address newRecipient) public onlyOwner {
        require(newRecipient != address(0), "Invalid recipient");
        platformFeeRecipient = newRecipient;
        emit PlatformFeeRecipientUpdated(newRecipient);
    }

    // Override base URI
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    // Update base URI
    function setBaseURI(string memory baseTokenURI) public onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // The following functions are overrides required by Solidity.
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId,
        uint256 batchSize
    ) internal override(ERC721, ERC721Enumerable) {
        super._beforeTokenTransfer(from, to, tokenId, batchSize);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }

    // EIP-2981: NFT Royalty Standard
    function royaltyInfo(uint256 tokenId, uint256 salePrice)
        external
        view
        returns (address receiver, uint256 royaltyAmount)
    {
        require(_exists(tokenId), "Token does not exist");
        RoyaltyInfo memory royalty = _royalties[tokenId];
        receiver = royalty.recipient;
        royaltyAmount = (salePrice * royalty.amount) / 10000;
    }
}
```
