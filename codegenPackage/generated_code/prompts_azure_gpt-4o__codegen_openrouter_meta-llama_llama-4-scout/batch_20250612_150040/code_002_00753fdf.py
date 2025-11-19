"""
Generated Code Metadata:
========================
Original URL: https://ddllweb3.com
Prompt: Generate Solidity code for a smart contract that facilitates decentralized data sharing, inspired by 去中心化网络3 principles.
Generated: DETERMINISTIC_00753fdf7b6c29d7
Batch ID: 20250612_150040
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

/**
 * @title DecentralizedDataSharing
 * @author [Your Name]
 * @notice A smart contract for decentralized data sharing inspired by 去中心化网络3 principles.
 */
contract DecentralizedDataSharing is ERC721URIStorage, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    // Mapping of data owners to their data tokens
    mapping(address => uint256[]) public ownerDataTokens;

    // Mapping of data tokens to their owners
    mapping(uint256 => address) public dataTokenOwners;

    // Event emitted when data is shared
    event DataShared(address indexed owner, uint256 indexed tokenId);

    // Event emitted when data is accessed
    event DataAccessed(address indexed accessor, uint256 indexed tokenId);

    /**
     * @dev Constructor for the DecentralizedDataSharing contract.
     * @param name_ The name of the NFT.
     * @param symbol_ The symbol of the NFT.
     */
    constructor(string memory name_, string memory symbol_) ERC721(name_, symbol_) {}

    /**
     * @dev Creates a new data token and assigns it to the owner.
     * @param owner The owner of the data token.
     * @param dataUri The URI of the data.
     * @return uint256 The ID of the newly created data token.
     */
    function createDataToken(address owner, string memory dataUri) public returns (uint256) {
        _tokenIds.increment();

        uint256 newTokenId = _tokenIds.current();
        _mint(owner, newTokenId);
        _setTokenURI(newTokenId, dataUri);

        ownerDataTokens[owner].push(newTokenId);
        dataTokenOwners[newTokenId] = owner;

        return newTokenId;
    }

    /**
     * @dev Shares data with a new owner.
     * @param tokenId The ID of the data token to share.
     * @param newOwner The new owner of the data token.
     */
    function shareData(uint256 tokenId, address newOwner) public {
        require(msg.sender == dataTokenOwners[tokenId], "Only the owner can share the data");

        _transfer(msg.sender, newOwner, tokenId);

        // Update owner data tokens
        for (uint256 i = 0; i < ownerDataTokens[msg.sender].length; i++) {
            if (ownerDataTokens[msg.sender][i] == tokenId) {
                ownerDataTokens[msg.sender].pop();
                break;
            }
        }

        ownerDataTokens[newOwner].push(tokenId);
        dataTokenOwners[tokenId] = newOwner;

        emit DataShared(msg.sender, tokenId);
    }

    /**
     * @dev Accesses the data.
     * @param tokenId The ID of the data token to access.
     */
    function accessData(uint256 tokenId) public {
        require(dataTokenOwners[tokenId] != address(0), "Data token does not exist");

        emit DataAccessed(msg.sender, tokenId);
    }

    /**
     * @dev Gets the data tokens owned by an address.
     * @param owner The address to get the data tokens for.
     * @return uint256[] The data tokens owned by the address.
     */
    function getDataTokens(address owner) public view returns (uint256[] memory) {
        return ownerDataTokens[owner];
    }

    /**
     * @dev Gets the owner of a data token.
     * @param tokenId The ID of the data token.
     * @return address The owner of the data token.
     */
    function getDataTokenOwner(uint256 tokenId) public view returns (address) {
        return dataTokenOwners[tokenId];
    }
}
```
