"""
Generated Code Metadata:
========================
Original URL: https://robots-nft-minting-website.webflow.io
Prompt: Write a Solidity function to implement a breeding mechanism for NFTs, inspired by the roadmap for Robotos Gen 2 discussed on the Robots NFT Minting website.
Generated: DETERMINISTIC_d1f7d4afb94efa3b
Batch ID: 20250612_153606
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
import "@openzeppelin/contracts/utils/Counters.sol";

contract RobotosNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to represent an NFT with its attributes
    struct Robot {
        uint256 id;
        string name;
        uint256 generation;
        uint256 parent1Id;
        uint256 parent2Id;
    }

    // Mapping from token ID to Robot struct
    mapping(uint256 => Robot) public robots;

    // Event emitted when a new robot is bred
    event RobotBred(uint256 indexed tokenId, uint256 parent1Id, uint256 parent2Id);

    // Constructor to initialize the NFT collection
    constructor() ERC721("Robotos", "RBT") {}

    // Function to breed two existing NFTs and create a new one
    function breed(uint256 parent1Id, uint256 parent2Id) external returns (uint256) {
        // Ensure both parents exist
        require(_exists(parent1Id), "Parent 1 does not exist");
        require(_exists(parent2Id), "Parent 2 does not exist");

        // Ensure the caller owns at least one of the parents
        require(ownerOf(parent1Id) == msg.sender || ownerOf(parent2Id) == msg.sender, "Caller must own at least one parent");

        // Increment the token ID counter to get a new token ID
        uint256 newTokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Create the new robot with attributes
        robots[newTokenId] = Robot({
            id: newTokenId,
            name: string(abi.encodePacked("Robot #", uint2str(newTokenId))),
            generation: getGeneration(parent1Id, parent2Id),
            parent1Id: parent1Id,
            parent2Id: parent2Id
        });

        // Mint the new NFT
        _mint(msg.sender, newTokenId);

        // Emit the RobotBred event
        emit RobotBred(newTokenId, parent1Id, parent2Id);

        return newTokenId;
    }

    // Helper function to determine the generation of the new robot
    function getGeneration(uint256 parent1Id, uint256 parent2Id) internal view returns (uint256) {
        uint256 gen1 = robots[parent1Id].generation;
        uint256 gen2 = robots[parent2Id].generation;
        return (gen1 > gen2 ? gen1 : gen2) + 1; // New generation is max of parents' generations + 1
    }

    // Helper function to convert uint256 to string
    function uint2str(uint256 _i) internal pure returns (string memory) {
        if (_i == 0) {
            return "0";
        }
        uint256 j = _i;
        uint256 len;
        while (j != 0) {
            len++;
            j /= 10;
        }
        bytes memory bstr = new bytes(len);
        uint256 k = len;
        j = _i;
        while (j != 0) {
            bstr[--k] = bytes1(uint8(48 + j % 10));
            j /= 10;
        }
        return string(bstr);
    }
}
```
