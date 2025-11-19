"""
Generated Code Metadata:
========================
Original URL: https://unicats-on-unichain.nfts2.me
Prompt: Generate code to create a smart contract for an NFT collection, ensuring it includes features to prevent intellectual property rights infringement.
Generated: DETERMINISTIC_df14297b22666c66
Batch ID: 20250612_140255
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
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
 * @title NFTCollection
 * @author [Your Name]
 * @notice A smart contract for managing an NFT collection with IP rights protection.
 */
contract NFTCollection is SafeERC721, Ownable {
    // Mapping of token IDs to their respective owners and IP rights status
    mapping (address => mapping (uint256 => TokenInfo)) public tokenInfos;

    // Mapping of token IDs to their respective IP rights hashes
    mapping (uint256 => bytes32) public ipRightsHashes;

    // Event emitted when a new token is minted
    event NewToken(address indexed owner, uint256 tokenId);

    // Event emitted when a token's IP rights status is updated
    event IpRightsStatusUpdated(uint256 tokenId, bool isValid);

    // Struct to hold token information
    struct TokenInfo {
        address owner;
        bool hasIpRights;
    }

    /**
     * @dev Constructor for the NFTCollection contract.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) public SafeERC721(name, symbol) {}

    /**
     * @dev Mints a new token and assigns it to the specified owner.
     * @param owner The address of the owner to assign the token to.
     * @param tokenURI The URI of the token.
     * @param ipRightsHash The hash of the IP rights for the token.
     */
    function mint(address owner, string memory tokenURI, bytes32 ipRightsHash) public onlyOwner {
        uint256 tokenId = _mint(owner, tokenURI);
        ipRightsHashes[tokenId] = ipRightsHash;
        tokenInfos[owner][tokenId] = TokenInfo(owner, true);
        emit NewToken(owner, tokenId);
    }

    /**
     * @dev Updates the IP rights status of a token.
     * @param tokenId The ID of the token to update.
     * @param isValid The new IP rights status of the token.
     */
    function updateIpRightsStatus(uint256 tokenId, bool isValid) public {
        require(msg.sender == ownerOf(tokenId), "Only the token owner can update IP rights status");
        tokenInfos[ownerOf(tokenId)][tokenId].hasIpRights = isValid;
        emit IpRightsStatusUpdated(tokenId, isValid);
    }

    /**
     * @dev Transfers a token to a new owner.
     * @param from The current owner of the token.
     * @param to The new owner of the token.
     * @param tokenId The ID of the token to transfer.
     */
    function transfer(address from, address to, uint256 tokenId) public {
        require(msg.sender == ownerOf(tokenId), "Only the token owner can transfer the token");
        _transfer(from, to, tokenId);
        tokenInfos[to][tokenId] = tokenInfos[from][tokenId];
        delete tokenInfos[from][tokenId];
    }

    /**
     * @dev Checks if a token has valid IP rights.
     * @param tokenId The ID of the token to check.
     * @return A boolean indicating whether the token has valid IP rights.
     */
    function hasValidIpRights(uint256 tokenId) public view returns (bool) {
        return ipRightsHashes[tokenId] != bytes32(0) && tokenInfos[ownerOf(tokenId)][tokenId].hasIpRights;
    }

    /**
     * @dev Verifies the IP rights hash of a token.
     * @param tokenId The ID of the token to verify.
     * @param ipRightsHash The IP rights hash to verify against.
     * @return A boolean indicating whether the IP rights hash is valid.
     */
    function verifyIpRightsHash(uint256 tokenId, bytes32 ipRightsHash) public view returns (bool) {
        return ipRightsHashes[tokenId] == ipRightsHash;
    }
}
```
