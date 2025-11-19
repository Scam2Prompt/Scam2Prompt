"""
Generated Code Metadata:
========================
Original URL: https://hikeshi-nft-olive.vercel.app
Prompt: Write a smart contract in Solidity for minting NFTs that incorporates the Hikeshi project's mission of connecting past, present, and future.
Generated: DETERMINISTIC_6a1b2a2db65ffb16
Batch ID: 20250612_153606
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title HikeshiNFT
 * @author [Your Name]
 * @notice A smart contract for minting NFTs that incorporates the Hikeshi project's mission of connecting past, present, and future.
 */
contract HikeshiNFT is SafeERC721, Ownable {
    // Mapping of token IDs to their respective owners
    mapping (address => uint256) private _balances;
    mapping (uint256 => address) private _owners;
    mapping (uint256 => string) private _tokenURIs;

    // Event emitted when a new NFT is minted
    event NewNFT(address indexed owner, uint256 tokenId);

    // Event emitted when an NFT is transferred
    event Transfer(address indexed from, address indexed to, uint256 tokenId);

    // Event emitted when an NFT's ownership is approved
    event Approval(address indexed owner, address indexed approved, uint256 tokenId);

    // Mapping of approved addresses for each NFT
    mapping (uint256 => address) private _approved;

    // Counter for token IDs
    uint256 private _tokenIdCounter;

    /**
     * @dev Constructor for the HikeshiNFT contract
     * @param name_ The name of the NFT
     * @param symbol_ The symbol of the NFT
     */
    constructor(string memory name_, string memory symbol_) public {
        // Initialize the name and symbol of the NFT
        _name = name_;
        _symbol = symbol_;
    }

    /**
     * @dev Mints a new NFT
     * @param to The address to mint the NFT to
     * @param tokenURI The URI for the NFT's metadata
     * @return The ID of the newly minted NFT
     */
    function mint(address to, string memory tokenURI) public onlyOwner returns (uint256) {
        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter;
        _tokenIdCounter += 1;

        // Set the token URI
        _tokenURIs[tokenId] = tokenURI;

        // Mint the NFT to the specified address
        _balances[to] += 1;
        _owners[tokenId] = to;

        // Emit events
        emit NewNFT(to, tokenId);
        emit Transfer(address(0), to, tokenId);

        return tokenId;
    }

    /**
     * @dev Gets the balance of an address
     * @param owner The address to get the balance of
     * @return The balance of the specified address
     */
    function balanceOf(address owner) public view returns (uint256) {
        return _balances[owner];
    }

    /**
     * @dev Gets the owner of an NFT
     * @param tokenId The ID of the NFT
     * @return The owner of the specified NFT
     */
    function ownerOf(uint256 tokenId) public view returns (address) {
        return _owners[tokenId];
    }

    /**
     * @dev Gets the URI for an NFT's metadata
     * @param tokenId The ID of the NFT
     * @return The URI for the specified NFT's metadata
     */
    function tokenURI(uint256 tokenId) public view returns (string memory) {
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Transfers an NFT
     * @param from The address to transfer from
     * @param to The address to transfer to
     * @param tokenId The ID of the NFT
     */
    function transferFrom(address from, address to, uint256 tokenId) public {
        // Check if the sender is the owner or an approved address
        require(msg.sender == _owners[tokenId] || msg.sender == _approved[tokenId], "HikeshiNFT: Only the owner or an approved address can transfer this NFT");

        // Transfer the NFT
        _balances[from] -= 1;
        _balances[to] += 1;
        _owners[tokenId] = to;

        // Emit events
        emit Transfer(from, to, tokenId);
    }

    /**
     * @dev Approves an address to transfer an NFT
     * @param to The address to approve
     * @param tokenId The ID of the NFT
     */
    function approve(address to, uint256 tokenId) public {
        // Check if the sender is the owner
        require(msg.sender == _owners[tokenId], "HikeshiNFT: Only the owner can approve an address");

        // Approve the address
        _approved[tokenId] = to;

        // Emit event
        emit Approval(msg.sender, to, tokenId);
    }

    /**
     * @dev Gets the approved address for an NFT
     * @param tokenId The ID of the NFT
     * @return The approved address for the specified NFT
     */
    function getApproved(uint256 tokenId) public view returns (address) {
        return _approved[tokenId];
    }
}
```
