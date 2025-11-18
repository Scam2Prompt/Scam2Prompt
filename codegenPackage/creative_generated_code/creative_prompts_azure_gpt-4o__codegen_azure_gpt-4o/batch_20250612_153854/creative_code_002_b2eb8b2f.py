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
pragma solidity ^0.8.17;

/**
 * @title MegaRabbitNFT
 * @dev A smart contract for minting NFTs with mint groups, wallet limits, and maximum supply.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

contract MegaRabbitNFT is ERC721Enumerable, Ownable {
    using Strings for uint256;

    // Base URI for token metadata
    string private baseURI;

    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Mint groups with maximum allowed mint per group
    mapping(address => uint256) public mintCount;
    mapping(address => bool) public isMintGroup;

    // Wallet mint limit
    uint256 public constant WALLET_LIMIT = 5;

    // Mint price
    uint256 public constant MINT_PRICE = 0.05 ether;

    // Events
    event Mint(address indexed minter, uint256 tokenId);

    /**
     * @dev Constructor initializes the contract with name and symbol.
     * @param _name Name of the NFT collection.
     * @param _symbol Symbol of the NFT collection.
     */
    constructor(string memory _name, string memory _symbol) ERC721(_name, _symbol) {}

    /**
     * @dev Modifier to check if the caller is part of the mint group.
     */
    modifier onlyMintGroup() {
        require(isMintGroup[msg.sender], "Caller is not part of the mint group");
        _;
    }

    /**
     * @dev Function to set the base URI for the metadata.
     * @param _baseURI Base URI string.
     */
    function setBaseURI(string memory _baseURI) external onlyOwner {
        baseURI = _baseURI;
    }

    /**
     * @dev Function to add or remove an address from the mint group.
     * @param account Address to be added or removed.
     * @param status True to add, false to remove.
     */
    function updateMintGroup(address account, bool status) external onlyOwner {
        isMintGroup[account] = status;
    }

    /**
     * @dev Function to mint an NFT.
     * @param quantity Number of NFTs to mint.
     */
    function mint(uint256 quantity) external payable onlyMintGroup {
        require(quantity > 0, "Quantity must be greater than zero");
        require(totalSupply() + quantity <= MAX_SUPPLY, "Exceeds maximum supply");
        require(mintCount[msg.sender] + quantity <= WALLET_LIMIT, "Exceeds wallet limit");
        require(msg.value == quantity * MINT_PRICE, "Incorrect Ether value");

        for (uint256 i = 0; i < quantity; i++) {
            uint256 tokenId = totalSupply() + 1;
            _safeMint(msg.sender, tokenId);
            mintCount[msg.sender]++;
            emit Mint(msg.sender, tokenId);
        }
    }

    /**
     * @dev Function to withdraw contract balance.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Override function to return the base URI.
     */
    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }
}
```
