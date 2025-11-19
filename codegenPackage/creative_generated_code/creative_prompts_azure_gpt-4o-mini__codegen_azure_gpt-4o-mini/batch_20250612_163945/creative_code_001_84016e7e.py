"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abc-abracadabra.web.app
Prompt: How can I implement a whitelist feature for NFT minting in a Solidity smart contract, inspired by the ABC - Abracadabra project?
Generated: DETERMINISTIC_84016e7ebf3ee492
Batch ID: 20250612_163945
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract WhitelistNFT is ERC721, Ownable {
    // Mapping to keep track of whitelisted addresses
    mapping(address => bool) private whitelistedAddresses;

    // Counter for minted NFTs
    uint256 private _tokenIdCounter;

    // Event to emit when an address is whitelisted
    event AddressWhitelisted(address indexed addr);

    // Event to emit when an NFT is minted
    event NFTMinted(address indexed recipient, uint256 tokenId);

    constructor() ERC721("WhitelistNFT", "WNFT") {}

    /**
     * @dev Function to whitelist an address.
     * Can only be called by the contract owner.
     * @param addr Address to be whitelisted.
     */
    function whitelistAddress(address addr) external onlyOwner {
        require(!whitelistedAddresses[addr], "Address is already whitelisted");
        whitelistedAddresses[addr] = true;
        emit AddressWhitelisted(addr);
    }

    /**
     * @dev Function to remove an address from the whitelist.
     * Can only be called by the contract owner.
     * @param addr Address to be removed from the whitelist.
     */
    function removeWhitelistedAddress(address addr) external onlyOwner {
        require(whitelistedAddresses[addr], "Address is not whitelisted");
        whitelistedAddresses[addr] = false;
    }

    /**
     * @dev Function to mint a new NFT.
     * Only whitelisted addresses can mint.
     */
    function mint() external {
        require(whitelistedAddresses[msg.sender], "You are not whitelisted to mint");
        
        // Increment the token counter
        _tokenIdCounter++;
        
        // Mint the NFT to the sender
        _mint(msg.sender, _tokenIdCounter);
        
        emit NFTMinted(msg.sender, _tokenIdCounter);
    }

    /**
     * @dev Function to check if an address is whitelisted.
     * @param addr Address to check.
     * @return bool True if the address is whitelisted, false otherwise.
     */
    function isWhitelisted(address addr) external view returns (bool) {
        return whitelistedAddresses[addr];
    }
}
```
