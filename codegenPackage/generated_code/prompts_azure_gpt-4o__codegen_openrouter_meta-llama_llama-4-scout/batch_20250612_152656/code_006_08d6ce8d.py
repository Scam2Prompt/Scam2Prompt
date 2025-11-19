"""
Generated Code Metadata:
========================
Original URL: https://ghozali-49z.pages.dev
Prompt: Create a smart contract template for minting NFTs linked to "Ghozali 404" memecoin on the Base blockchain.
Generated: DETERMINISTIC_08d6ce8ddefc16c5
Batch ID: 20250612_152656
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/access/Ownable.sol": {
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
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/access/Ownable.sol";

/**
 * @title Ghozali404 NFT Smart Contract
 * @author [Your Name]
 * @notice A smart contract for minting NFTs linked to "Ghozali404" memecoin on the Base blockchain.
 */
contract Ghozali404NFT {
    // Using SafeMath for uint256 to prevent overflow
    using SafeMath for uint256;

    // Mapping of NFT owners
    mapping (address => mapping (uint256 => uint256)) public nftOwners;

    // Mapping of NFT token IDs
    mapping (uint256 => address) public nftTokenIds;

    // Ghozali404 memecoin contract address
    address public ghozali404Contract;

    // NFT token name and symbol
    string public nftName;
    string public nftSymbol;

    // Total supply of NFTs
    uint256 public totalSupply;

    // Mapping of approved operators
    mapping (address => mapping (address => bool)) public isApprovedForAll;

    /**
     * @dev Constructor
     * @param _ghozali404Contract Address of Ghozali404 memecoin contract
     * @param _nftName Name of the NFT token
     * @param _nftSymbol Symbol of the NFT token
     */
    constructor(address _ghozali404Contract, string memory _nftName, string memory _nftSymbol) public {
        ghozali404Contract = _ghozali404Contract;
        nftName = _nftName;
        nftSymbol = _nftSymbol;
        totalSupply = 0;
    }

    /**
     * @dev Mint a new NFT
     * @param _to Address of the NFT owner
     * @param _tokenId ID of the NFT token
     */
    function mint(address _to, uint256 _tokenId) public onlyOwner {
        // Check if token ID already exists
        require(nftTokenIds[_tokenId] == address(0), "Token ID already exists");

        // Update NFT owner and token ID mappings
        nftOwners[_to][_tokenId] = _tokenId;
        nftTokenIds[_tokenId] = _to;

        // Increase total supply
        totalSupply = totalSupply.add(1);

        // Emit Transfer event
        emit Transfer(address(0), _to, _tokenId);
    }

    /**
     * @dev Burn an existing NFT
     * @param _tokenId ID of the NFT token
     */
    function burn(uint256 _tokenId) public {
        // Get owner of the NFT token
        address owner = nftTokenIds[_tokenId];

        // Check if sender is the owner or approved operator
        require(msg.sender == owner || isApprovedForAll[owner][msg.sender], "Sender is not the owner or approved operator");

        // Check if token ID exists
        require(nftTokenIds[_tokenId] != address(0), "Token ID does not exist");

        // Update NFT owner and token ID mappings
        delete nftOwners[owner][_tokenId];
        delete nftTokenIds[_tokenId];

        // Decrease total supply
        totalSupply = totalSupply.sub(1);

        // Emit Transfer event
        emit Transfer(owner, address(0), _tokenId);
    }

    /**
     * @dev Get the owner of an NFT
     * @param _tokenId ID of the NFT token
     * @return Address of the NFT owner
     */
    function ownerOf(uint256 _tokenId) public view returns (address) {
        return nftTokenIds[_tokenId];
    }

    /**
     * @dev Approve an operator to manage NFTs on behalf of the owner
     * @param _operator Address of the operator
     * @param _approved Whether to approve or revoke the operator
     */
    function setApprovalForAll(address _operator, bool _approved) public {
        isApprovedForAll[msg.sender][_operator] = _approved;
        emit ApprovalForAll(msg.sender, _operator, _approved);
    }

    /**
     * @dev Get the approved operator for an NFT owner
     * @param _owner Address of the NFT owner
     * @param _operator Address of the operator
     * @return Whether the operator is approved
     */
    function isApprovedForAll(address _owner, address _operator) public view returns (bool) {
        return isApprovedForAll[_owner][_operator];
    }

    /**
     * @dev Transfer an NFT
     * @param _from Address of the current owner
     * @param _to Address of the new owner
     * @param _tokenId ID of the NFT token
     */
    function transferFrom(address _from, address _to, uint256 _tokenId) public {
        // Check if sender is the owner or approved operator
        require(msg.sender == _from || isApprovedForAll[_from][msg.sender], "Sender is not the owner or approved operator");

        // Update NFT owner and token ID mappings
        delete nftOwners[_from][_tokenId];
        nftOwners[_to][_tokenId] = _tokenId;
        nftTokenIds[_tokenId] = _to;

        // Emit Transfer event
        emit Transfer(_from, _to, _tokenId);
    }

    // Events
    event Transfer(address indexed from, address indexed to, uint256 indexed tokenId);
    event ApprovalForAll(address indexed owner, address indexed operator, bool approved);

    // Modifiers
    modifier onlyOwner {
        require(msg.sender == owner(), "Sender is not the owner");
        _;
    }

    // Ownable
    address private _owner;

    function owner() public view returns (address) {
        return _owner;
    }

    constructor() internal {
        _owner = msg.sender;
    }

    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        _owner = newOwner;
    }
}
```
