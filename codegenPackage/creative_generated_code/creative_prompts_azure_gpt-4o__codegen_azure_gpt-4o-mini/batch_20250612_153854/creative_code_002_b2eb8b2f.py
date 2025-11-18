"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mega-rabbit.com
Prompt: Generate Solidity code for a smart contract that implements a minting mechanism similar to the MegaRabbit NFT collection, including features like mint groups, wallet limits, and maximum supply.
Generated: DETERMINISTIC_b2eb8b2f31db223d
Batch ID: 20250612_153854
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
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title MegaRabbit NFT Collection
 * @dev This contract implements a minting mechanism for a Non-Fungible Token collection.
 * It supports mint groups, wallet limits, and a maximum supply.
 */
contract MegaRabbit is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Define the structure for mint groups
    struct MintGroup {
        uint256 maxSupply;        // Maximum supply for the group
        uint256 price;            // Price per NFT in the group
        uint256 mintLimit;        // Limit for how many can be minted per wallet
        uint256 mintedCount;      // Counter for minted NFTs in the group
    }

    // Mapping of mint groups by their ID
    mapping(uint256 => MintGroup) public mintGroups;

    // Mapping to track how many NFTs each address has minted per group
    mapping(address => mapping(uint256 => uint256)) public mintedByWallet;

    // Total maximum supply of the collection
    uint256 public constant TOTAL_MAX_SUPPLY = 10000;

    // Counter to track total minted NFTs
    Counters.Counter private _tokenIdCounter;

    // Event emitted when a new mint group is created
    event MintGroupCreated(uint256 indexed groupId, uint256 maxSupply, uint256 price, uint256 mintLimit);
    // Event emitted when a minting occurs
    event Minted(address indexed owner, uint256 indexed tokenId, uint256 groupId);

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     */
    constructor() ERC721("MegaRabbit", "MRB") {}

    /**
     * @dev Create a new mint group.
     * @param groupId The unique ID for the mint group.
     * @param maxSupply The maximum supply of this mint group.
     * @param price The price required to mint an NFT from this group.
     * @param mintLimit The limit of NFTs that can be minted per wallet.
     */
    function createMintGroup(
        uint256 groupId,
        uint256 maxSupply,
        uint256 price,
        uint256 mintLimit
    ) external onlyOwner {
        require(maxSupply > 0, "Max supply must be greater than zero");
        require(price > 0, "Price must be greater than zero");
        require(mintLimit > 0, "Mint limit must be greater than zero");

        mintGroups[groupId] = MintGroup(maxSupply, price, mintLimit, 0);
        emit MintGroupCreated(groupId, maxSupply, price, mintLimit);
    }

    /**
     * @dev Mint a new NFT from a specified mint group.
     * @param groupId The ID of the mint group to mint from.
     * @param amount The number of NFTs to mint.
     */
    function mint(uint256 groupId, uint256 amount) external payable {
        MintGroup storage group = mintGroups[groupId];
        require(group.maxSupply > 0, "Invalid mint group");
        require(group.mintedCount + amount <= group.maxSupply, "Exceeds max supply for the group");
        require(mintedByWallet[msg.sender][groupId] + amount <= group.mintLimit, "Exceeds wallet mint limit");
        require(msg.value >= group.price * amount, "Insufficient ETH sent");

        for (uint256 i = 0; i < amount; i++) {
            uint256 tokenId = _tokenIdCounter.current();
            require(tokenId < TOTAL_MAX_SUPPLY, "Exceeds total max supply");

            _tokenIdCounter.increment();
            group.mintedCount++;
            mintedByWallet[msg.sender][groupId]++;

            _safeMint(msg.sender, tokenId);
            emit Minted(msg.sender, tokenId, groupId);
        }
    }

    /**
     * @dev Withdraw the contract balance to the owner's address.
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Get the total minted supply across all groups.
     * @return The total minted supply.
     */
    function totalMintedSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
