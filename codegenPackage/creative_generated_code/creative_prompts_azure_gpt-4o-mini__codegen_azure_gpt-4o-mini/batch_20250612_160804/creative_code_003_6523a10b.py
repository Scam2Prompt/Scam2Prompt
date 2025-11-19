"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://samoyedmint.web.app
Prompt: Generate a smart contract code for a whitelist minting process that allows token holders to mint for free, based on the Samoyed Coin model.
Generated: DETERMINISTIC_6523a10b3316addd
Batch ID: 20250612_160804
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract WhitelistMinting is ERC721Enumerable, Ownable {
    // Mapping to track whitelisted addresses
    mapping(address => bool) public whitelistedAddresses;

    // Mapping to track if the address has minted
    mapping(address => bool) public hasMinted;

    // Base URI for metadata
    string private baseTokenURI;

    // Event emitted when an address is added to the whitelist
    event AddressWhitelisted(address indexed account);
    
    // Event emitted when an address is removed from the whitelist
    event AddressRemovedFromWhitelist(address indexed account);
    
    // Event emitted when a token is minted
    event TokenMinted(address indexed to, uint256 tokenId);

    // Counter for token IDs
    uint256 private currentTokenId;

    // Constructor to set the name and symbol of the ERC721 token
    constructor(string memory name, string memory symbol, string memory baseURI) 
        ERC721(name, symbol) {
        baseTokenURI = baseURI;
    }

    // Function to add an address to the whitelist
    function addToWhitelist(address account) external onlyOwner {
        require(account != address(0), "Cannot whitelist the zero address");
        require(!whitelistedAddresses[account], "Already whitelisted");

        whitelistedAddresses[account] = true;
        emit AddressWhitelisted(account);
    }

    // Function to remove an address from the whitelist
    function removeFromWhitelist(address account) external onlyOwner {
        require(whitelistedAddresses[account], "Address is not whitelisted");

        whitelistedAddresses[account] = false;
        emit AddressRemovedFromWhitelist(account);
    }

    // Function to mint a token for whitelisted addresses
    function mint() external {
        require(whitelistedAddresses[msg.sender], "You are not whitelisted");
        require(!hasMinted[msg.sender], "You have already minted");

        // Increment the token ID and mint the new token
        currentTokenId++;
        hasMinted[msg.sender] = true;
        _mint(msg.sender, currentTokenId);
        emit TokenMinted(msg.sender, currentTokenId);
    }

    // Function to set the base URI for token metadata
    function setBaseURI(string memory baseURI) external onlyOwner {
        baseTokenURI = baseURI;
    }

    // Override the _baseURI function from ERC721
    function _baseURI() internal view virtual override returns (string memory) {
        return baseTokenURI;
    }

    // Function to check if an address is whitelisted
    function isWhitelisted(address account) external view returns (bool) {
        return whitelistedAddresses[account];
    }
}
```
