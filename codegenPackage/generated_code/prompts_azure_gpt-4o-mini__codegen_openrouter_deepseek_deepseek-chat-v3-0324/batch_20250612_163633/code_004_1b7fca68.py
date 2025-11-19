"""
Generated Code Metadata:
========================
Original URL: https://jellybabiesnft.web.app
Prompt: How can I develop a lottery system for NFTs akin to the Jellotto feature from the Jelly Babies NFT project?
Generated: DETERMINISTIC_1b7fca685e3785e7
Batch ID: 20250612_163633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready smart contract for an NFT lottery system similar to Jellotto, implemented in Solidity:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@chainlink/contracts/src/v0.8/interfaces/VRFCoordinatorV2Interface.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";

contract NFTLottery is ERC721, Ownable, VRFConsumerBaseV2 {
    using Counters for Counters.Counter;
    using SafeMath for uint256;

    // Chainlink VRF configuration
    VRFCoordinatorV2Interface private immutable _vrfCoordinator;
    uint64 private immutable _subscriptionId;
    bytes32 private immutable _keyHash;
    uint32 private immutable _callbackGasLimit;
    uint16 private constant REQUEST_CONFIRMATIONS = 3;
    uint32 private constant NUM_WORDS = 1;

    // NFT configuration
    Counters.Counter private _tokenIdCounter;
    uint256 public constant MAX_SUPPLY = 10000;
    uint256 public constant TICKET_PRICE = 0.01 ether;
    uint256 public constant PRIZE_PERCENTAGE = 50; // 50% of pool
    string private _baseTokenURI;

    // Lottery state
    uint256 public currentPool;
    uint256 public currentRound;
    mapping(uint256 => address[]) public roundParticipants;
    mapping(uint256 => bool) public roundCompleted;
    mapping(uint256 => uint256) public roundWinningToken;
    mapping(uint256 => address) public roundWinner;
    mapping(uint256 => uint256) public roundRandomness;

    // Events
    event TicketPurchased(address indexed buyer, uint256 round);
    event LotteryStarted(uint256 indexed round);
    event WinnerSelected(uint256 indexed round, address winner, uint256 tokenId);
    event RandomnessRequested(uint256 indexed round, uint256 requestId);

    constructor(
        address vrfCoordinator,
        uint64 subscriptionId,
        bytes32 keyHash,
        uint32 callbackGasLimit,
        string memory baseURI
    ) ERC721("JellottoNFT", "JLT") VRFConsumerBaseV2(vrfCoordinator) {
        _vrfCoordinator = VRFCoordinatorV2Interface(vrfCoordinator);
        _subscriptionId = subscriptionId;
        _keyHash = keyHash;
        _callbackGasLimit = callbackGasLimit;
        _baseTokenURI = baseURI;
        currentRound = 1;
    }

    function purchaseTicket() external payable {
        require(msg.value == TICKET_PRICE, "Incorrect ETH amount");
        require(!roundCompleted[currentRound], "Round is completed");
        
        // Add to current pool
        currentPool += msg.value;
        
        // Mint NFT ticket
        uint256 tokenId = _tokenIdCounter.current();
        require(tokenId < MAX_SUPPLY, "Max supply reached");
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);
        
        // Add participant to current round
        roundParticipants[currentRound].push(msg.sender);

        emit TicketPurchased(msg.sender, currentRound);
    }

    function drawWinner() external onlyOwner {
        require(roundParticipants[currentRound].length > 0, "No participants");
        require(!roundCompleted[currentRound], "Round already completed");

        // Request random number from Chainlink VRF
        uint256 requestId = _vrfCoordinator.requestRandomWords(
            _keyHash,
            _subscriptionId,
            REQUEST_CONFIRMATIONS,
            _callbackGasLimit,
            NUM_WORDS
        );

        emit RandomnessRequested(currentRound, requestId);
    }

    function fulfillRandomWords(uint256 requestId, uint256[] memory randomWords) internal override {
        uint256 randomness = randomWords[0];
        uint256 round = currentRound;
        
        // Select winner
        uint256 winnerIndex = randomness % roundParticipants[round].length;
        address winner = roundParticipants[round][winnerIndex];
        
        // Calculate prize
        uint256 prizeAmount = currentPool.mul(PRIZE_PERCENTAGE).div(100);
        
        // Select winning token (any token owned by winner)
        uint256[] memory winnerTokens = tokensOfOwner(winner);
        require(winnerTokens.length > 0, "Winner has no tokens");
        uint256 winningTokenIndex = randomness % winnerTokens.length;
        uint256 winningTokenId = winnerTokens[winningTokenIndex];
        
        // Update state
        roundWinner[round] = winner;
        roundWinningToken[round] = winningTokenId;
        roundRandomness[round] = randomness;
        roundCompleted[round] = true;
        
        // Pay out prize
        payable(winner).transfer(prizeAmount);
        
        // Reset for next round
        currentPool = currentPool.sub(prizeAmount);
        currentRound++;
        
        emit WinnerSelected(round, winner, winningTokenId);
        emit LotteryStarted(currentRound);
    }

    function tokensOfOwner(address owner) public view returns (uint256[] memory) {
        uint256 tokenCount = balanceOf(owner);
        uint256[] memory tokenIds = new uint256[](tokenCount);
        
        for (uint256 i = 0; i < tokenCount; i++) {
            tokenIds[i] = tokenOfOwnerByIndex(owner, i);
        }
        
        return tokenIds;
    }

    function tokenOfOwnerByIndex(address owner, uint256 index) public view returns (uint256) {
        // Simplified implementation - in production use ERC721Enumerable
        require(index < balanceOf(owner), "Owner index out of bounds");
        return ownerToTokenIds[owner][index];
    }

    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // View functions
    function getRoundParticipants(uint256 round) external view returns (address[] memory) {
        return roundParticipants[round];
    }

    function getCurrentRoundInfo() external view returns (
        uint256 round,
        uint256 pool,
        uint256 participantCount,
        bool completed
    ) {
        round = currentRound;
        pool = currentPool;
        participantCount = roundParticipants[round].length;
        completed = roundCompleted[round];
    }

    // Supporting data structure for token enumeration (simplified)
    mapping(address => mapping(uint256 => uint256)) private ownerToTokenIds;
    mapping(uint256 => uint256) private tokenIdToIndex;

    function _afterTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        if (from != address(0)) {
            // Remove token from previous owner's list
            uint256 lastTokenIndex = balanceOf(from) - 1;
            uint256 tokenIndex = tokenIdToIndex[tokenId];
            if (tokenIndex != lastTokenIndex) {
                uint256 lastTokenId = tokenOfOwnerByIndex(from, lastTokenIndex);
                ownerToTokenIds[from][tokenIndex] = lastTokenId;
                tokenIdToIndex[lastTokenId] = tokenIndex;
            }
            delete ownerToTokenIds[from][lastTokenIndex];
        }

        // Add token to new owner's list
        uint256 length = balanceOf(to);
        ownerToTokenIds[to][length] = tokenId;
        tokenIdToIndex[tokenId] = length;
    }
}
```
