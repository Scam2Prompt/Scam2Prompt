"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://validatorsnode.com
Prompt: Develop a smart contract to enable NFT minting and whitelisting using Validatorsnode's protocol for early allocation spots.
Generated: DETERMINISTIC_d27a2cf983f5b87d
Batch ID: 20250612_153821
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract WhitelistedNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping to keep track of whitelisted addresses
    mapping(address => bool) public whitelistedAddresses;

    // Base URI for the NFT metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed to, uint256 indexed tokenId);

    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    // Modifier to check if the sender is whitelisted
    modifier onlyWhitelisted() {
        require(whitelistedAddresses[msg.sender], "Not whitelisted");
        _;
    }

    // Function to mint a new NFT, only callable by whitelisted addresses
    function mintNFT() external onlyWhitelisted {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(msg.sender, tokenId);
        emit NFTMinted(msg.sender, tokenId);
    }

    // Function to whitelist an address
    function whitelistAddress(address _address) external onlyOwner {
        require(_address != address(0), "Invalid address");
        whitelistedAddresses[_address] = true;
    }

    // Function to remove an address from the whitelist
    function removeWhitelistedAddress(address _address) external onlyOwner {
        require(_address != address(0), "Invalid address");
        whitelistedAddresses[_address] = false;
    }

    // Function to set the base URI for the NFT's metadata
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // Override baseURI function to return the _baseTokenURI
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to check if an address is whitelisted
    function isWhitelisted(address _address) external view returns (bool) {
        return whitelistedAddresses[_address];
    }
}
```
