"""
Generated Code Metadata:
========================
Original URL: https://mega-rabbit.com
Prompt: Develop a code snippet in Solidity to implement a whitelist (WL) and allowlist (FCFS) system for minting NFTs in groups, similar to the MegaRabbit collection.
Generated: DETERMINISTIC_35d01a2f9b7bca21
Batch ID: 20250622_212626
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

contract WhitelistMintingNFT is ERC721Enumerable, Ownable {
    using ECDSA for bytes32;

    // Mapping to track whitelisted addresses
    mapping(address => bool) public whitelisted;
    // Mapping to track allowed addresses for first-come, first-served (FCFS) minting
    mapping(address => bool) public allowedFCFS;
    // Total supply of NFTs
    uint256 public totalSupply;
    // Maximum supply of NFTs
    uint256 public maxSupply;
    // Minting price
    uint256 public mintPrice;
    // Minting phase flags
    bool public isWhitelistActive;
    bool public isFCFSActive;

    // Event emitted when an NFT is minted
    event NFTMinted(address indexed to, uint256 tokenId);

    constructor(string memory name, string memory symbol, uint256 _maxSupply, uint256 _mintPrice) 
        ERC721(name, symbol) {
        maxSupply = _maxSupply;
        mintPrice = _mintPrice;
    }

    // Modifier to check if minting is allowed
    modifier mintingAllowed() {
        require(totalSupply < maxSupply, "Max supply reached");
        _;
    }

    // Function to add addresses to the whitelist
    function addToWhitelist(address[] calldata addresses) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            whitelisted[addresses[i]] = true;
        }
    }

    // Function to remove addresses from the whitelist
    function removeFromWhitelist(address[] calldata addresses) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            whitelisted[addresses[i]] = false;
        }
    }

    // Function to start/stop the whitelist minting phase
    function toggleWhitelistActive() external onlyOwner {
        isWhitelistActive = !isWhitelistActive;
    }

    // Function to start/stop the FCFS minting phase
    function toggleFCFSActive() external onlyOwner {
        isFCFSActive = !isFCFSActive;
    }

    // Whitelist minting function
    function mintWhitelist() external payable mintingAllowed {
        require(isWhitelistActive, "Whitelist minting is not active");
        require(whitelisted[msg.sender], "You are not whitelisted");
        require(msg.value >= mintPrice, "Insufficient funds");

        uint256 tokenId = totalSupply + 1;
        totalSupply++;
        _safeMint(msg.sender, tokenId);
        emit NFTMinted(msg.sender, tokenId);
    }

    // FCFS minting function
    function mintFCFS() external payable mintingAllowed {
        require(isFCFSActive, "FCFS minting is not active");
        require(!allowedFCFS[msg.sender], "You have already minted");
        require(msg.value >= mintPrice, "Insufficient funds");

        uint256 tokenId = totalSupply + 1;
        totalSupply++;
        allowedFCFS[msg.sender] = true;
        _safeMint(msg.sender, tokenId);
        emit NFTMinted(msg.sender, tokenId);
    }

    // Function to withdraw contract balance to the owner's address
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to set the mint price
    function setMintPrice(uint256 _mintPrice) external onlyOwner {
        mintPrice = _mintPrice;
    }

    // Function to get the current total supply
    function getCurrentSupply() external view returns (uint256) {
        return totalSupply;
    }
}
```
