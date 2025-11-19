"""
Generated Code Metadata:
========================
Original URL: https://mint.mythlcal.market
Prompt: Create a simple smart contract in Solidity for minting random NFT blueprints, similar to those used in the NFL Rivals free minting phase.
Generated: DETERMINISTIC_de8eca924451bb61
Batch ID: 20250622_205842
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
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
  },
  "https://example.com/nft-blueprint-": {
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
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title NFTBlueprintContract
 * @author [Your Name]
 * @notice A simple smart contract for minting random NFT blueprints.
 */
contract NFTBlueprintContract {
    using SafeMath for uint256;
    using SafeERC721 for mapping(address => mapping(uint256 => bool));

    // Mapping of NFT blueprints
    mapping (uint256 => Blueprint) public blueprints;

    // Mapping of minted NFTs
    mapping (address => mapping(uint256 => bool)) public mintedNFTs;

    // Total supply of blueprints
    uint256 public totalSupply;

    // Maximum blueprint ID
    uint256 public maxBlueprintId;

    // Address of the NFT contract
    address public nftContractAddress;

    // Event emitted when a new blueprint is minted
    event NewBlueprint(address indexed owner, uint256 blueprintId);

    // Event emitted when an NFT is minted
    event NewNFT(address indexed owner, uint256 nftId);

    // Struct representing an NFT blueprint
    struct Blueprint {
        uint256 id;
        string name;
        string description;
        string imageURI;
    }

    /**
     * @dev Constructor
     * @param _nftContractAddress Address of the NFT contract
     */
    constructor(address _nftContractAddress) public {
        nftContractAddress = _nftContractAddress;
        totalSupply = 0;
        maxBlueprintId = 0;
    }

    /**
     * @dev Mint a new random NFT blueprint
     * @return The ID of the newly minted blueprint
     */
    function mintBlueprint() public returns (uint256) {
        // Generate a random blueprint ID
        uint256 blueprintId = uint256(keccak256(abi.encodePacked(msg.sender, block.timestamp))) % 10000 + 1;

        // Ensure the blueprint ID does not already exist
        while (blueprints[blueprintId].id != 0) {
            blueprintId = uint256(keccak256(abi.encodePacked(msg.sender, block.timestamp))) % 10000 + 1;
        }

        // Create a new blueprint
        Blueprint memory blueprint;
        blueprint.id = blueprintId;
        blueprint.name = string(abi.encodePacked("NFT Blueprint #", Strings.toString(blueprintId)));
        blueprint.description = "A randomly generated NFT blueprint.";
        blueprint.imageURI = string(abi.encodePacked("https://example.com/nft-blueprint-", Strings.toString(blueprintId), ".png"));

        // Store the blueprint
        blueprints[blueprintId] = blueprint;

        // Update the total supply and maximum blueprint ID
        totalSupply = totalSupply.add(1);
        maxBlueprintId = maxBlueprintId.max(blueprintId);

        // Emit an event
        emit NewBlueprint(msg.sender, blueprintId);

        return blueprintId;
    }

    /**
     * @dev Mint an NFT from a blueprint
     * @param _blueprintId The ID of the blueprint to mint
     * @return The ID of the newly minted NFT
     */
    function mintNFT(uint256 _blueprintId) public returns (uint256) {
        // Ensure the blueprint exists
        require(blueprints[_blueprintId].id != 0, "Blueprint does not exist.");

        // Ensure the NFT has not already been minted
        require(!mintedNFTs[msg.sender][_blueprintId], "NFT has already been minted.");

        // Mint the NFT
        uint256 nftId = uint256(keccak256(abi.encodePacked(msg.sender, block.timestamp))) % 10000 + 1;
        // Call the NFT contract to mint the NFT
        // NOTE: Replace with actual NFT contract minting logic
        // For demonstration purposes, assume the NFT contract has a mint function
        // IExampleNFT(nftContractAddress).mint(msg.sender, nftId);

        // Mark the NFT as minted
        mintedNFTs[msg.sender][_blueprintId] = true;

        // Emit an event
        emit NewNFT(msg.sender, nftId);

        return nftId;
    }
}

// Example usage
contract ExampleNFT {
    mapping (address => mapping(uint256 => bool)) public mintedNFTs;

    function mint(address _owner, uint256 _nftId) public {
        mintedNFTs[_owner][_nftId] = true;
    }
}

interface IExampleNFT {
    function mint(address _owner, uint256 _nftId) external;
}

library Strings {
    function toString(uint256 _value) internal pure returns (string memory) {
        // Implementation omitted for brevity
    }
}
```
