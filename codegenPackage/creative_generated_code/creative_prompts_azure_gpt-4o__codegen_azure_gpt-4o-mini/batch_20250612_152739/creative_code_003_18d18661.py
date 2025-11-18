"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-de.web.app
Prompt: Generate code to implement a lootbox system in a blockchain-based game, where lootbox keys and rewards are represented as on-chain NFTs that can be traded on OpenSea.
Generated: DETERMINISTIC_18d1866109277512
Batch ID: 20250612_152739
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

// Import the OpenZeppelin ERC721 contract
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Lootbox contract implementing lootbox system which includes keys and rewards as NFTs
contract Lootbox is ERC721, ERC721Burnable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _keyIdCounter; // Counter for generating key IDs
    Counters.Counter private _rewardIdCounter; // Counter for generating reward IDs

    // Struct to represent a Lootbox Key
    struct LootboxKey {
        uint256 id;
        address owner;
        bool isOpened;
    }

    // Struct to represent a Lootbox Reward
    struct LootboxReward {
        uint256 id;
        string metadataURI; // URI linking to reward metadata
    }

    // Mapping from key ID to LootboxKey
    mapping(uint256 => LootboxKey) public lootboxKeys;
    // Mapping from reward ID to LootboxReward
    mapping(uint256 => LootboxReward) public lootboxRewards;

    // Events for logging
    event KeyMinted(uint256 indexed keyId, address indexed owner);
    event RewardMinted(uint256 indexed rewardId, string metadataURI);
    event LootboxOpened(uint256 indexed keyId, uint256 indexed rewardId);

    // Constructor
    constructor() ERC721("LootboxKey", "LBK") {}

    // Function to mint a new lootbox key
    function mintLootboxKey() external onlyOwner returns (uint256) {
        uint256 keyId = _keyIdCounter.current();
        _keyIdCounter.increment();
        lootboxKeys[keyId] = LootboxKey(keyId, msg.sender, false);
        _safeMint(msg.sender, keyId);
        emit KeyMinted(keyId, msg.sender);
        return keyId;
    }

    // Function to mint a new lootbox reward
    function mintLootboxReward(string memory metadataURI) external onlyOwner returns (uint256) {
        uint256 rewardId = _rewardIdCounter.current();
        _rewardIdCounter.increment();
        lootboxRewards[rewardId] = LootboxReward(rewardId, metadataURI);
        emit RewardMinted(rewardId, metadataURI);
        return rewardId;
    }

    // Function to open a lootbox key and receive a reward
    function openLootbox(uint256 keyId) external {
        require(ownerOf(keyId) == msg.sender, "You do not own this key.");
        require(!lootboxKeys[keyId].isOpened, "Lootbox has already been opened.");

        // Logic for selecting a reward can be implemented here (randomly, etc.)
        uint256 rewardId = _selectReward(); // Placeholder for reward selection logic

        lootboxKeys[keyId].isOpened = true;
        emit LootboxOpened(keyId, rewardId);

        // Transfer reward to the user (could be minting a new NFT or similar)
        // Here we should have a separate contract for rewards that handles minting, trading, etc.
    }

    // Placeholder function to select a reward (to be implemented)
    function _selectReward() private view returns (uint256) {
        // Implement your reward selection logic here
        // For now, we return a dummy reward ID
        return 0; // This should be replaced with the actual reward ID logic
    }
}
```

Note: This code is a simplified example and may require additional features such as actual reward selection logic, transferring rewards to users, and proper integration with OpenSea for trading capabilities. Always ensure to test contracts on a test network before deploying to production.
