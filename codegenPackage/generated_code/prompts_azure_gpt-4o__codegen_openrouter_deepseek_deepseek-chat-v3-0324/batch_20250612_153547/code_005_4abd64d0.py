"""
Generated Code Metadata:
========================
Original URL: https://earnm-rectify-presale-url.pages.dev
Prompt: Create a Solidity function to manage "Mystery Boxes" on a blockchain platform, inspired by EARN'M's gamified tokenomics.
Generated: DETERMINISTIC_4abd64d09cf97455
Batch ID: 20250612_153547
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract MysteryBox is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    struct Box {
        uint256 boxType;
        uint256 minReward;
        uint256 maxReward;
        uint256 price;
        uint256 totalSupply;
        uint256 mintedCount;
    }

    mapping(uint256 => Box) public boxes;
    mapping(uint256 => uint256) public boxTypeByTokenId;
    mapping(address => uint256[]) public userBoxes;

    event BoxPurchased(address indexed buyer, uint256 boxType, uint256 tokenId);
    event BoxOpened(address indexed owner, uint256 tokenId, uint256 reward);

    constructor() ERC721("MysteryBox", "MBX") {}

    /**
     * @dev Add a new box type or update existing one
     * @param boxType The type identifier of the box
     * @param minReward Minimum reward amount
     * @param maxReward Maximum reward amount
     * @param price Price per box
     * @param totalSupply Maximum supply of this box type
     */
    function setBoxType(
        uint256 boxType,
        uint256 minReward,
        uint256 maxReward,
        uint256 price,
        uint256 totalSupply
    ) external onlyOwner {
        require(minReward <= maxReward, "Invalid reward range");
        require(price > 0, "Price must be positive");
        
        boxes[boxType] = Box({
            boxType: boxType,
            minReward: minReward,
            maxReward: maxReward,
            price: price,
            totalSupply: totalSupply,
            mintedCount: boxes[boxType].mintedCount
        });
    }

    /**
     * @dev Purchase a mystery box
     * @param boxType The type of box to purchase
     */
    function purchaseBox(uint256 boxType) external payable nonReentrant {
        Box storage box = boxes[boxType];
        require(box.boxType == boxType, "Box type does not exist");
        require(msg.value >= box.price, "Insufficient payment");
        require(box.mintedCount < box.totalSupply, "Box sold out");

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        
        _safeMint(msg.sender, tokenId);
        boxTypeByTokenId[tokenId] = boxType;
        userBoxes[msg.sender].push(tokenId);
        box.mintedCount++;

        emit BoxPurchased(msg.sender, boxType, tokenId);
    }

    /**
     * @dev Open a mystery box to reveal the reward
     * @param tokenId The ID of the box to open
     */
    function openBox(uint256 tokenId) external nonReentrant {
        require(_exists(tokenId), "Box does not exist");
        require(ownerOf(tokenId) == msg.sender, "Not the box owner");

        uint256 boxType = boxTypeByTokenId[tokenId];
        Box storage box = boxes[boxType];
        
        // Generate pseudo-random reward (not truly random, use Chainlink VRF for production)
        uint256 reward = _generateRandomReward(box.minReward, box.maxReward, tokenId);
        
        _burn(tokenId);
        
        emit BoxOpened(msg.sender, tokenId, reward);
    }

    /**
     * @dev Generate a pseudo-random reward within given range
     * @param min Minimum possible reward
     * @param max Maximum possible reward
     * @param seed Additional entropy for randomness
     */
    function _generateRandomReward(uint256 min, uint256 max, uint256 seed) internal view returns (uint256) {
        require(min <= max, "Invalid range");
        uint256 random = uint256(keccak256(abi.encodePacked(
            block.timestamp,
            block.difficulty,
            msg.sender,
            seed
        ))) % (max - min + 1);
        return min + random;
    }

    /**
     * @dev Get boxes owned by a user
     * @param user Address of the user
     */
    function getUserBoxes(address user) external view returns (uint256[] memory) {
        return userBoxes[user];
    }

    /**
     * @dev Withdraw contract balance (only owner)
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
