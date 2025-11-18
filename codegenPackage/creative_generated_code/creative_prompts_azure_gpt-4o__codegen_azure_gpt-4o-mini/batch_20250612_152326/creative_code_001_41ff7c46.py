"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mainnet-nobody.pages.dev
Prompt: Create a smart contract in Solidity for an NFT minting process that includes features like raffles, airdrops, and refund mechanisms, as described in the "Nobody NFT" project.
Generated: DETERMINISTIC_41ff7c46d730b67c
Batch ID: 20250612_152326
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for minting NFTs with raffle, airdrop, and refund mechanisms
contract NobodyNFT is ERC721, ERC721Burnable, Ownable {
    using Counters for Counters.Counter;
    
    Counters.Counter private _tokenIdCounter;

    // Struct to store raffle information
    struct Raffle {
        address[] participants;
        uint256 ticketPrice;
        bool isActive;
    }

    Raffle public raffle;
    mapping(address => uint256) public pendingRefunds;
    mapping(address => bool) public hasMinted;

    event Minted(address indexed owner, uint256 tokenId);
    event RaffleStarted(uint256 ticketPrice);
    event RaffleEnded(address winner);
    event Airdrop(address indexed recipient, uint256 tokenId);
    event RefundIssued(address indexed recipient, uint256 amount);

    constructor() ERC721("NobodyNFT", "NOBODY") {}

    // Function to mint an NFT
    function mint() external payable {
        require(!hasMinted[msg.sender], "You have already minted an NFT.");
        require(msg.value == 0.01 ether, "Incorrect Ether value sent.");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        hasMinted[msg.sender] = true;

        _safeMint(msg.sender, tokenId);
        emit Minted(msg.sender, tokenId);
    }

    // Function to start a raffle
    function startRaffle(uint256 ticketPrice) external onlyOwner {
        require(!raffle.isActive, "Raffle is already active.");
        raffle.ticketPrice = ticketPrice;
        raffle.isActive = true;
        emit RaffleStarted(ticketPrice);
    }

    // Function to participate in the raffle
    function participateInRaffle() external payable {
        require(raffle.isActive, "Raffle is not active.");
        require(msg.value == raffle.ticketPrice, "Incorrect ticket price.");

        raffle.participants.push(msg.sender);
    }

    // Function to end the raffle and select a winner
    function endRaffle() external onlyOwner {
        require(raffle.isActive, "Raffle is not active.");
        require(raffle.participants.length > 0, "No participants in the raffle.");

        uint256 winnerIndex = random() % raffle.participants.length;
        address winner = raffle.participants[winnerIndex];

        raffle.isActive = false;
        delete raffle.participants;

        emit RaffleEnded(winner);
    }

    // Function to handle airdrop of NFTs
    function airdrop(address[] calldata recipients) external onlyOwner {
        for (uint256 i = 0; i < recipients.length; i++) {
            uint256 tokenId = _tokenIdCounter.current();
            _tokenIdCounter.increment();
            _safeMint(recipients[i], tokenId);
            emit Airdrop(recipients[i], tokenId);
        }
    }

    // Function to request a refund
    function requestRefund() external {
        require(hasMinted[msg.sender], "You have not minted an NFT.");
        uint256 refundAmount = 0.01 ether;
        pendingRefunds[msg.sender] += refundAmount;
    }

    // Function to withdraw refund
    function withdrawRefund() external {
        uint256 amount = pendingRefunds[msg.sender];
        require(amount > 0, "No refund available.");
        
        pendingRefunds[msg.sender] = 0;
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Refund transfer failed.");

        emit RefundIssued(msg.sender, amount);
    }

    // Random number generator for raffle winner selection
    function random() private view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.difficulty, block.timestamp, raffle.participants)));
    }

    // Fallback function to receive Ether
    receive() external payable {}

    // Function to withdraw contract balance to the owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Withdrawal failed.");
    }
}
```
