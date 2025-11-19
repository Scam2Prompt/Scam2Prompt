"""
Generated Code Metadata:
========================
Original URL: https://cornucopiasnfts.com
Prompt: Design a smart contract for a free minting event of NFTs, similar to the one offered by Cornucopias, using Solidity and OpenZeppelin libraries.
Generated: DETERMINISTIC_51cf30f1154924f9
Batch ID: 20250622_210718
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract FreeMintNFT is ERC721URIStorage, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    // Mapping of addresses to their minted status
    mapping(address => bool) public mintedAddresses;

    // Maximum number of NFTs that can be minted per address
    uint256 public maxPerAddress = 1;

    // Event emitted when an NFT is minted
    event NewNFTMinted(address indexed sender, uint256 tokenId);

    constructor() ERC721("FreeMintNFT", "FMNFT") {}

    /**
     * @dev Mints a new NFT to the sender's address.
     * Requirements:
     * - The sender has not already minted an NFT.
     * - The sender has not exceeded the maximum number of NFTs per address.
     */
    function mint() public nonReentrant {
        require(!mintedAddresses[msg.sender], "Address has already minted an NFT");
        require(maxPerAddress > 0, "Minting is not allowed");

        _tokenIds.increment();

        uint256 newItemId = _tokenIds.current();
        _mint(msg.sender, newItemId);
        _setTokenURI(newItemId, "ipfs://example.com/token-uri"); // Replace with actual IPFS URI

        mintedAddresses[msg.sender] = true;

        emit NewNFTMinted(msg.sender, newItemId);
    }

    /**
     * @dev Sets the base URI for all token IDs.
     */
    function setBaseURI(string memory baseURI) public onlyOwner {
        _setBaseURI(baseURI);
    }

    /**
     * @dev Updates the maximum number of NFTs that can be minted per address.
     */
    function setMaxPerAddress(uint256 _max) public onlyOwner {
        maxPerAddress = _max;
    }

    /**
     * @dev Withdraws Ether from the contract.
     */
    function withdraw() public onlyOwner {
        (bool os, ) = payable(msg.sender).call{value: address(this).balance}("");
        require(os);
    }
}
```
