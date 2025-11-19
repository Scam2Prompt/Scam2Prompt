"""
Generated Code Metadata:
========================
Original URL: https://fineturtie.events
Prompt: Write a smart contract in Solidity to manage the minting process for FineTurtle Mint, ensuring the supply limit of 4,333 and the tiered pricing structure (OG 2.0: 0.0099 ETH, FL: 0.015 ETH, Public: 0.02 ETH).
Generated: DETERMINISTIC_d7dfceff12ed8f3b
Batch ID: 20250612_151024
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
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

/**
 * @title FineTurtleMint
 * @author [Your Name]
 * @notice A smart contract for managing the minting process of FineTurtle Mint NFTs.
 */
contract FineTurtleMint {
    using SafeMath for uint256;
    using SafeERC721 for IERC721;

    // Constants
    uint256 public constant SUPPLY_LIMIT = 4333;
    uint256 public constant OG_TIER_PRICE = 0.0099 ether;
    uint256 public constant FL_TIER_PRICE = 0.015 ether;
    uint256 public constant PUBLIC_TIER_PRICE = 0.02 ether;

    // Mapping for tracking user tiers
    mapping(address => uint256) public userTiers;

    // Mapping for tracking minted NFTs
    mapping(address => uint256) public mintedCounts;

    // Event emitted when a new NFT is minted
    event NewNFTMinted(address indexed minter, uint256 tokenId);

    // Event emitted when a user claims a tier
    event TierClaimed(address indexed user, uint256 tier);

    // Reentrancy guard
    bool private reentrancyGuard;

    // Modifier to prevent reentrancy attacks
    modifier noReentrancy() {
        require(!reentrancyGuard, "Reentrancy attack detected");
        reentrancyGuard = true;
        _;
        reentrancyGuard = false;
    }

    /**
     * @dev Initializes the contract.
     */
    constructor() public {}

    /**
     * @dev Allows the contract owner to set a user's tier.
     * @param user The address of the user.
     * @param tier The tier of the user (1 = OG, 2 = FL, 3 = Public).
     */
    function setUserTier(address user, uint256 tier) public onlyOwner {
        require(tier >= 1 && tier <= 3, "Invalid tier");
        userTiers[user] = tier;
        emit TierClaimed(user, tier);
    }

    /**
     * @dev Mints a new NFT.
     */
    function mint() public payable noReentrancy {
        require(totalSupply() < SUPPLY_LIMIT, "Supply limit reached");
        require(msg.value >= getTierPrice(msg.sender), "Insufficient payment");

        uint256 tokenId = totalSupply() + 1;
        mintedCounts[msg.sender] = mintedCounts[msg.sender].add(1);

        // Perform minting logic (e.g., transfer NFT to minter)
        // For demonstration purposes, we assume the NFT is transferred successfully
        emit NewNFTMinted(msg.sender, tokenId);
    }

    /**
     * @dev Gets the total supply of minted NFTs.
     * @return The total supply.
     */
    function totalSupply() public view returns (uint256) {
        return mintedCounts[msg.sender].add(mintedCounts[address(0)]);
    }

    /**
     * @dev Gets the price for a user's tier.
     * @param user The address of the user.
     * @return The price in wei.
     */
    function getTierPrice(address user) public view returns (uint256) {
        uint256 tier = userTiers[user];
        if (tier == 1) {
            return OG_TIER_PRICE;
        } else if (tier == 2) {
            return FL_TIER_PRICE;
        } else {
            return PUBLIC_TIER_PRICE;
        }
    }

    // Restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner(), "Access restricted to contract owner");
        _;
    }

    // Get contract owner
    function owner() public view returns (address) {
        return 0x...; // Replace with actual contract owner address
    }
}
```
