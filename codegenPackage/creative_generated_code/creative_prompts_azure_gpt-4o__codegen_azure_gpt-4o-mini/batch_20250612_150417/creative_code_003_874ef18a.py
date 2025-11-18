"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w3eth.app
Prompt: Create a smart contract function for the Web3Q blockchain that handles the minting process of QRobot NFTs, including generating the random traits on-chain.
Generated: DETERMINISTIC_874ef18a28e6d661
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract QRobotNFT is ERC721Enumerable, Ownable {
    using SafeMath for uint256;

    // Event to emit when a new QRobot is minted
    event QRobotMinted(uint256 tokenId, string traits);

    // Structure to represent traits of the QRobot
    struct Traits {
        string color;
        string typeRobot;
        string accessory;
    }

    // Mapping from tokenId to traits
    mapping(uint256 => Traits) private _tokenTraits;

    // Maximum supply of QRobot NFTs
    uint256 public constant MAX_SUPPLY = 10000;
    // Counter for the number of minted tokens
    uint256 private _tokenCounter;

    // Constructor to initialize the NFT collection
    constructor() ERC721("QRobotNFT", "QRBT") {}

    // Function to mint a new QRobot NFT
    function mintQRobot() external {
        require(_tokenCounter < MAX_SUPPLY, "Max supply reached");

        // Increment the token counter
        uint256 newTokenId = _tokenCounter.add(1);
        _tokenCounter = newTokenId;

        // Generate random traits for the QRobot
        Traits memory newTraits = _generateRandomTraits(newTokenId);
        _tokenTraits[newTokenId] = newTraits;

        // Mint the NFT to the caller
        _mint(msg.sender, newTokenId);

        // Emit an event for the new minting
        emit QRobotMinted(newTokenId, _encodeTraits(newTraits));
    }

    // Function to generate random traits based on the tokenId
    function _generateRandomTraits(uint256 tokenId) internal view returns (Traits memory) {
        // Simple pseudo-random generation for demonstration
        string[] memory colors = new string[](3);
        colors[0] = "Red";
        colors[1] = "Blue";
        colors[2] = "Green";

        string[] memory types = new string[](3);
        types[0] = "Warrior";
        types[1] = "Scout";
        types[2] = "Builder";

        string[] memory accessories = new string[](3);
        accessories[0] = "Laser Gun";
        accessories[1] = "Shield";
        accessories[2] = "Jetpack";

        // Use tokenId as a seed for randomness
        uint256 colorIndex = uint256(keccak256(abi.encodePacked(tokenId, "color"))) % colors.length;
        uint256 typeIndex = uint256(keccak256(abi.encodePacked(tokenId, "type"))) % types.length;
        uint256 accessoryIndex = uint256(keccak256(abi.encodePacked(tokenId, "accessory"))) % accessories.length;

        // Return generated traits
        return Traits({
            color: colors[colorIndex],
            typeRobot: types[typeIndex],
            accessory: accessories[accessoryIndex]
        });
    }

    // Function to encode traits into a single string for event emission
    function _encodeTraits(Traits memory traits) internal pure returns (string memory) {
        return string(abi.encodePacked("Color: ", traits.color, ", Type: ", traits.typeRobot, ", Accessory: ", traits.accessory));
    }

    // Function to get the traits of a specific tokenId
    function getTraits(uint256 tokenId) external view returns (Traits memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenTraits[tokenId];
    }
}
```
