"""
Generated Code Metadata:
========================
Original URL: https://mega-rabbit.com
Prompt: Generate Solidity code for a smart contract that implements a minting mechanism similar to the MegaRabbit NFT collection, including features like mint groups, wallet limits, and maximum supply.
Generated: DETERMINISTIC_b2eb8b2f31db223d
Batch ID: 20250612_153854
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

contract MegaRabbitNFT {
    // Mapping of mint groups
    mapping(address => MintGroup) public mintGroups;

    // Mapping of user mint counts
    mapping(address => uint256) public userMintCounts;

    // Mapping of NFT ownership
    mapping(uint256 => address) public nftOwners;

    // Total supply of NFTs
    uint256 public totalSupply;

    // Maximum supply of NFTs
    uint256 public maxSupply;

    // Event emitted when an NFT is minted
    event Minted(address indexed to, uint256 tokenId);

    // Struct for mint groups
    struct MintGroup {
        uint256 walletLimit;
        uint256 mintCount;
        uint256[] tokenIds;
    }

    // Constructor
    constructor(uint256 _maxSupply) public {
        maxSupply = _maxSupply;
        totalSupply = 0;
    }

    // Function to add a mint group
    function addMintGroup(address _groupAddress, uint256 _walletLimit, uint256 _mintCount) public onlyOwner {
        require(_groupAddress != address(0), "Invalid group address");
        require(_walletLimit > 0, "Wallet limit must be greater than 0");
        require(_mintCount > 0, "Mint count must be greater than 0");

        mintGroups[_groupAddress] = MintGroup(_walletLimit, _mintCount, new uint256[](_mintCount));
    }

    // Function to mint an NFT
    function mint(address _to, uint256 _groupId) public onlyOwner {
        require(mintGroups[_groupId].mintCount > 0, "Mint group does not exist");
        require(totalSupply < maxSupply, "Maximum supply reached");
        require(userMintCounts[_to] < mintGroups[_groupId].walletLimit, "Wallet limit reached");

        uint256 tokenId = totalSupply + 1;
        nftOwners[tokenId] = _to;
        userMintCounts[_to]++;
        totalSupply++;
        mintGroups[_groupId].tokenIds.push(tokenId);
        emit Minted(_to, tokenId);
    }

    // Function to get the token URI
    function tokenURI(uint256 _tokenId) public view returns (string memory) {
        // Implement token URI logic here
        return "";
    }

    // Function to transfer an NFT
    function transfer(address _to, uint256 _tokenId) public {
        require(msg.sender == nftOwners[_tokenId], "Only the owner can transfer");
        nftOwners[_tokenId] = _to;
    }

    // Modifier for only the owner
    modifier onlyOwner {
        require(msg.sender == owner(), "Only the owner can call this function");
        _;
    }

    // Function to get the owner
    function owner() public view returns (address) {
        // Implement owner logic here
        return msg.sender;
    }
}
```
