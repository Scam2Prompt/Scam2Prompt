"""
Generated Code Metadata:
========================
Original URL: https://richpepe.vercel.app
Prompt: Design a smart contract for a meme lottery system, like the one mentioned in Rich Pepe's roadmap, and explain how it would work.
Generated: DETERMINISTIC_3d37125a9ad05a94
Batch ID: 20250622_210806
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title Meme Lottery Smart Contract
 * @author [Your Name]
 * @notice A smart contract for a meme lottery system.
 */
contract MemeLottery is ERC721URIStorage, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    // Mapping of meme NFTs to their respective owners
    mapping(address => uint256) public memeOwners;

    // Mapping of meme NFTs to their respective URIs
    mapping(uint256 => string) public memeURIs;

    // Mapping of lottery tickets to their respective owners
    mapping(address => uint256[]) public lotteryTickets;

    // Lottery ticket price
    uint256 public ticketPrice;

    // Lottery jackpot
    uint256 public jackpot;

    // Lottery ticket count
    uint256 public ticketCount;

    // Event emitted when a new meme NFT is created
    event NewMemeNFT(address indexed owner, uint256 tokenId);

    // Event emitted when a lottery ticket is purchased
    event LotteryTicketPurchased(address indexed owner, uint256 ticketId);

    // Event emitted when the lottery is drawn
    event LotteryDrawn(address indexed winner, uint256 winningTicketId);

    /**
     * @dev Initializes the contract with the given parameters.
     * @param _ticketPrice The price of a lottery ticket.
     */
    constructor(uint256 _ticketPrice) ERC721("Meme Lottery", "ML") {
        ticketPrice = _ticketPrice;
        jackpot = 0;
    }

    /**
     * @dev Creates a new meme NFT with the given URI.
     * @param _uri The URI of the meme NFT.
     * @return The token ID of the newly created meme NFT.
     */
    function createMemeNFT(string memory _uri) public returns (uint256) {
        _tokenIds.increment();

        uint256 newItemId = _tokenIds.current();
        _mint(msg.sender, newItemId);
        _setTokenURI(newItemId, _uri);

        memeOwners[msg.sender] = newItemId;
        memeURIs[newItemId] = _uri;

        emit NewMemeNFT(msg.sender, newItemId);

        return newItemId;
    }

    /**
     * @dev Purchases a lottery ticket.
     */
    function purchaseLotteryTicket() public payable nonReentrant {
        require(msg.value >= ticketPrice, "Insufficient funds");

        uint256 ticketId = ticketCount++;
        lotteryTickets[msg.sender].push(ticketId);

        jackpot += msg.value;

        emit LotteryTicketPurchased(msg.sender, ticketId);
    }

    /**
     * @dev Draws the lottery and transfers the jackpot to the winner.
     */
    function drawLottery() public nonReentrant {
        require(ticketCount > 0, "No tickets purchased");

        uint256 winningTicketId = uint256(keccak256(abi.encodePacked(block.timestamp))) % ticketCount;
        address winner = lotteryTickets[lotteryTickets.length - 1][winningTicketId];

        payable(winner).transfer(jackpot);

        emit LotteryDrawn(winner, winningTicketId);

        // Reset lottery state
        ticketCount = 0;
        jackpot = 0;
    }

    /**
     * @dev Returns the balance of the contract.
     * @return The balance of the contract.
     */
    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }
}
```
