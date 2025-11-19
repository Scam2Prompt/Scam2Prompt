"""
Generated Code Metadata:
========================
Original URL: https://hummingbirdonbnb.pages.dev
Prompt: Create a smart contract in Solidity for an NFT launchpad similar to Mint Magic, allowing users to mint NFTs and integrate utilities for businesses and celebrities.
Generated: DETERMINISTIC_b3b87eda26e50de2
Batch ID: 20250612_151343
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/utils/Address.sol": {
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
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/utils/Address.sol";

/**
 * @title MintMagic NFT Launchpad
 * @author [Your Name]
 * @notice A smart contract for minting NFTs and providing utilities for businesses and celebrities.
 */
contract MintMagicLaunchpad {
    // Mapping of NFT creators to their respective NFT collections
    mapping(address => mapping(uint256 => NFT)) public nftCollections;

    // Mapping of NFT IDs to their owners
    mapping(uint256 => address) public nftOwners;

    // Mapping of business/celebrity addresses to their utility functions
    mapping(address => mapping(string => UtilityFunction)) public utilityFunctions;

    // Event emitted when an NFT is minted
    event NewNFT(address indexed creator, uint256 indexed nftId);

    // Event emitted when an NFT is transferred
    event Transfer(address indexed from, address indexed to, uint256 indexed nftId);

    // Event emitted when a utility function is added
    event UtilityFunctionAdded(address indexed business, string indexed functionName);

    // Struct representing an NFT
    struct NFT {
        string name;
        string description;
        string imageURI;
    }

    // Struct representing a utility function
    struct UtilityFunction {
        string functionName;
        string functionDescription;
    }

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner(), "Only the contract owner can perform this action");
        _;
    }

    // Contract owner
    address private _owner;

    /**
     * @notice Constructor
     */
    constructor() public {
        _owner = msg.sender;
    }

    /**
     * @notice Mint a new NFT
     * @param _nftName Name of the NFT
     * @param _nftDescription Description of the NFT
     * @param _nftImageURI Image URI of the NFT
     */
    function mintNFT(string memory _nftName, string memory _nftDescription, string memory _nftImageURI) public {
        // Create a new NFT
        NFT memory newNFT = NFT(_nftName, _nftDescription, _nftImageURI);

        // Generate a unique NFT ID
        uint256 nftId = uint256(keccak256(abi.encodePacked(_nftName, _nftDescription, _nftImageURI)));

        // Add the NFT to the creator's collection
        nftCollections[msg.sender][nftId] = newNFT;

        // Set the NFT owner
        nftOwners[nftId] = msg.sender;

        // Emit the NewNFT event
        emit NewNFT(msg.sender, nftId);
    }

    /**
     * @notice Transfer an NFT
     * @param _nftId ID of the NFT to transfer
     * @param _to Address of the recipient
     */
    function transferNFT(uint256 _nftId, address _to) public {
        // Check if the sender is the NFT owner
        require(msg.sender == nftOwners[_nftId], "Only the NFT owner can transfer the NFT");

        // Update the NFT owner
        nftOwners[_nftId] = _to;

        // Emit the Transfer event
        emit Transfer(msg.sender, _to, _nftId);
    }

    /**
     * @notice Add a utility function for a business/celebrity
     * @param _business Address of the business/celebrity
     * @param _functionName Name of the utility function
     * @param _functionDescription Description of the utility function
     */
    function addUtilityFunction(address _business, string memory _functionName, string memory _functionDescription) public onlyOwner {
        // Create a new utility function
        UtilityFunction memory newUtilityFunction = UtilityFunction(_functionName, _functionDescription);

        // Add the utility function to the business/celebrity's mapping
        utilityFunctions[_business][_functionName] = newUtilityFunction;

        // Emit the UtilityFunctionAdded event
        emit UtilityFunctionAdded(_business, _functionName);
    }

    /**
     * @notice Execute a utility function
     * @param _business Address of the business/celebrity
     * @param _functionName Name of the utility function
     */
    function executeUtilityFunction(address _business, string memory _functionName) public {
        // Check if the utility function exists
        require(utilityFunctions[_business][_functionName].functionName != "", "Utility function does not exist");

        // Execute the utility function (TO DO: implement function execution logic)
        // ...
    }

    /**
     * @notice Get the contract owner
     * @return address The contract owner
     */
    function owner() public view returns (address) {
        return _owner;
    }
}
```
