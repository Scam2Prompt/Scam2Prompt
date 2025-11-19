"""
Generated Code Metadata:
========================
Original URL: https://mainnet-nobody.pages.dev
Prompt: Create a smart contract in Solidity for an NFT minting process that includes features like raffles, airdrops, and refund mechanisms, as described in the "Nobody NFT" project.
Generated: DETERMINISTIC_41ff7c46d730b67c
Batch ID: 20250612_152326
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
import "@openzeppelin/contracts/utils/Address.sol";

contract NobodyNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    using Address for address payable;

    // State variables
    Counters.Counter private _tokenIdCounter;
    uint256 public mintPrice;
    uint256 public maxSupply;
    mapping(address => uint256) public airdropClaimed;
    mapping(address => uint256) public raffleEntries;

    // Events
    event Minted(address indexed owner, uint256 tokenId);
    event AirdropClaimed(address indexed recipient, uint256 amount);
    event RaffleEntered(address indexed participant, uint256 entries);

    // Constructor to initialize the contract
    constructor(uint256 _mintPrice, uint256 _maxSupply) ERC721("Nobody NFT", "NOBODY") {
        mintPrice = _mintPrice;
        maxSupply = _maxSupply;
    }

    // Minting function
    function mint() external payable {
        require(msg.value >= mintPrice, "Insufficient funds to mint");
        require(totalSupply() < maxSupply, "Max supply reached");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);

        emit Minted(msg.sender, tokenId);
    }

    // Airdrop function
    function airdrop(address[] calldata recipients) external onlyOwner {
        require(totalSupply() + recipients.length <= maxSupply, "Exceeds max supply");

        for (uint256 i = 0; i < recipients.length; i++) {
            uint256 tokenId = _tokenIdCounter.current();
            _tokenIdCounter.increment();
            _safeMint(recipients[i], tokenId);
            emit AirdropClaimed(recipients[i], tokenId);
        }
    }

    // Raffle entry function
    function enterRaffle(uint256 entries) external payable {
        require(msg.value >= entries * mintPrice, "Insufficient funds for raffle entries");
        raffleEntries[msg.sender] += entries;

        emit RaffleEntered(msg.sender, entries);
    }

    // Refund function
    function refund() external {
        require(raffleEntries[msg.sender] > 0, "No entries to refund");

        uint256 entries = raffleEntries[msg.sender];
        uint256 refundAmount = entries * mintPrice;
        raffleEntries[msg.sender] = 0;

        payable(msg.sender).sendValue(refundAmount);
    }

    // Withdraw function for owner to withdraw funds
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).sendValue(balance);
    }

    // Override supportsInterface to include ERC721
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721Enumerable) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
```
