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
pragma solidity ^0.8.17;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

contract NobodyNFT is ERC721Enumerable, Ownable, ReentrancyGuard {
    using ECDSA for bytes32;

    // Events
    event NFTMinted(address indexed to, uint256 tokenId);
    event RaffleWinnerSelected(address indexed winner, uint256 tokenId);
    event AirdropCompleted(address indexed recipient, uint256 tokenId);
    event RefundIssued(address indexed user, uint256 amount);

    // Variables
    uint256 public constant MAX_SUPPLY = 10000;
    uint256 public constant MINT_PRICE = 0.05 ether;
    uint256 public constant MAX_MINT_PER_TX = 5;
    uint256 public totalMinted;
    mapping(address => bool) public refundClaimed;
    mapping(address => bool) public raffleEntered;

    bool public raffleActive = false;
    address[] public raffleParticipants;

    // Constructor
    constructor() ERC721("Nobody NFT", "NOBODY") {}

    // Mint function
    function mint(uint256 quantity) external payable nonReentrant {
        require(quantity > 0 && quantity <= MAX_MINT_PER_TX, "Invalid mint quantity");
        require(totalMinted + quantity <= MAX_SUPPLY, "Exceeds max supply");
        require(msg.value == quantity * MINT_PRICE, "Incorrect ETH amount");

        for (uint256 i = 0; i < quantity; i++) {
            uint256 tokenId = totalMinted + 1;
            _safeMint(msg.sender, tokenId);
            totalMinted++;

            emit NFTMinted(msg.sender, tokenId);
        }
    }

    // Raffles
    function enterRaffle() external nonReentrant {
        require(raffleActive, "Raffle is not active");
        require(balanceOf(msg.sender) > 0, "Must own an NFT to enter");
        require(!raffleEntered[msg.sender], "Already entered raffle");

        raffleParticipants.push(msg.sender);
        raffleEntered[msg.sender] = true;
    }

    function selectRaffleWinner() external onlyOwner nonReentrant {
        require(raffleParticipants.length > 0, "No raffle participants");

        uint256 randomIndex = uint256(
            keccak256(abi.encodePacked(block.timestamp, block.difficulty, msg.sender))
        ) % raffleParticipants.length;

        address winner = raffleParticipants[randomIndex];
        uint256 tokenId = totalMinted + 1;

        require(totalMinted + 1 <= MAX_SUPPLY, "Exceeds max supply");

        _safeMint(winner, tokenId);
        totalMinted++;

        emit RaffleWinnerSelected(winner, tokenId);

        // Reset raffle
        raffleParticipants = new address[](0);
    }

    // Airdrop
    function airdrop(address recipient) external onlyOwner nonReentrant {
        require(totalMinted + 1 <= MAX_SUPPLY, "Exceeds max supply");

        uint256 tokenId = totalMinted + 1;
        _safeMint(recipient, tokenId);
        totalMinted++;

        emit AirdropCompleted(recipient, tokenId);
    }

    // Refunds
    function claimRefund() external nonReentrant {
        require(balanceOf(msg.sender) > 0, "Must own an NFT");
        require(!refundClaimed[msg.sender], "Refund already claimed");

        refundClaimed[msg.sender] = true;
        uint256 refundAmount = MINT_PRICE;

        (bool success, ) = msg.sender.call{value: refundAmount}("");
        require(success, "Refund transfer failed");

        emit RefundIssued(msg.sender, refundAmount);
    }

    // Withdraw funds
    function withdraw() external onlyOwner {
        (bool success, ) = msg.sender.call{value: address(this).balance}("");
        require(success, "Withdraw failed");
    }

    // Fallback/Receive
    receive() external payable {}
    fallback() external payable {}
}
```
