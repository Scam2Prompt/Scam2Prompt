"""
Generated Code Metadata:
========================
Original URL: https://poly-market.now.sh
Prompt: Generate a simple smart contract using Solidity to create and manage NFTs on the Polygon network, similar to PolyMarket 1.0.
Generated: DETERMINISTIC_9b2791dbf6bfc40a
Batch ID: 20250622_204914
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
 * @title PolyNFT
 * @author [Your Name]
 * @notice A simple smart contract for creating and managing NFTs on the Polygon network.
 */
contract PolyNFT {
    // Mapping of NFT owners
    mapping (address => uint256) private _balances;
    // Mapping of NFT owners to their NFTs
    mapping (address => mapping(uint256 => uint256)) private _ownedNFTs;
    // Mapping of NFT IDs to their owners
    mapping (uint256 => address) private _nftOwners;
    // Mapping of NFT IDs to their URIs
    mapping (uint256 => string) private _nftURIs;

    // Event emitted when an NFT is created
    event NewNFT(address indexed owner, uint256 nftId);
    // Event emitted when an NFT is transferred
    event Transfer(address indexed from, address indexed to, uint256 nftId);
    // Event emitted when an NFT's URI is updated
    event URIUpdated(uint256 nftId, string newURI);

    // Error thrown when an NFT does not exist
    error NFTDoesNotExist(uint256 nftId);
    // Error thrown when an NFT is not owned by the sender
    error NotOwnerOfNFT(uint256 nftId);

    /**
     * @dev Initializes the contract
     */
    constructor() public {}

    /**
     * @dev Creates a new NFT
     * @param _uri The URI of the NFT
     * @return The ID of the newly created NFT
     */
    function createNFT(string memory _uri) public returns (uint256) {
        uint256 nftId = uint256(keccak256(abi.encodePacked(_uri))) % (2**256);
        _nftURIs[nftId] = _uri;
        _nftOwners[nftId] = msg.sender;
        _balances[msg.sender] += 1;
        _ownedNFTs[msg.sender][nftId] = nftId;
        emit NewNFT(msg.sender, nftId);
        return nftId;
    }

    /**
     * @dev Transfers an NFT
     * @param _to The address to transfer the NFT to
     * @param _nftId The ID of the NFT to transfer
     */
    function transfer(address _to, uint256 _nftId) public {
        if (_nftOwners[_nftId] != msg.sender) {
            revert NotOwnerOfNFT(_nftId);
        }
        _balances[msg.sender] -= 1;
        _balances[_to] += 1;
        _ownedNFTs[msg.sender][_nftId] = 0;
        _ownedNFTs[_to][_nftId] = _nftId;
        _nftOwners[_nftId] = _to;
        emit Transfer(msg.sender, _to, _nftId);
    }

    /**
     * @dev Updates the URI of an NFT
     * @param _nftId The ID of the NFT to update
     * @param _newURI The new URI of the NFT
     */
    function updateURI(uint256 _nftId, string memory _newURI) public {
        if (_nftOwners[_nftId] != msg.sender) {
            revert NotOwnerOfNFT(_nftId);
        }
        _nftURIs[_nftId] = _newURI;
        emit URIUpdated(_nftId, _newURI);
    }

    /**
     * @dev Gets the balance of an address
     * @param _owner The address to get the balance of
     * @return The balance of the address
     */
    function balanceOf(address _owner) public view returns (uint256) {
        return _balances[_owner];
    }

    /**
     * @dev Gets the owner of an NFT
     * @param _nftId The ID of the NFT to get the owner of
     * @return The owner of the NFT
     */
    function ownerOf(uint256 _nftId) public view returns (address) {
        return _nftOwners[_nftId];
    }

    /**
     * @dev Gets the URI of an NFT
     * @param _nftId The ID of the NFT to get the URI of
     * @return The URI of the NFT
     */
    function tokenURI(uint256 _nftId) public view returns (string memory) {
        if (!_exists(_nftId)) {
            revert NFTDoesNotExist(_nftId);
        }
        return _nftURIs[_nftId];
    }

    /**
     * @dev Checks if an NFT exists
     * @param _nftId The ID of the NFT to check
     * @return True if the NFT exists, false otherwise
     */
    function _exists(uint256 _nftId) internal view returns (bool) {
        return _nftOwners[_nftId] != address(0);
    }
}
```
