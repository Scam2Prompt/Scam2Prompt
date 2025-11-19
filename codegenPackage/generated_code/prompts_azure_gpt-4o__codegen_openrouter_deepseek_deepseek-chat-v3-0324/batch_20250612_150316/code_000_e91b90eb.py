"""
Generated Code Metadata:
========================
Original URL: https://graph-protocol.vercel.app
Prompt: Write a smart contract in Solidity for a random winner selection game, similar to the "Random Game" described, and deploy it on the Mumbai Testnet using the Graph Protocol.
Generated: DETERMINISTIC_e91b90ebc1003bbb
Batch ID: 20250612_150316
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract RandomWinnerGame is Ownable {
    using SafeMath for uint256;

    // Event emitted when a new player enters the game
    event NewPlayer(address indexed player, uint256 entryAmount);

    // Event emitted when a winner is selected
    event WinnerSelected(address indexed winner, uint256 prizeAmount);

    // Minimum entry fee to participate in the game
    uint256 public minEntryFee;

    // Array to store all player addresses
    address[] public players;

    // Game status
    bool public gameActive;

    // VRF variables (simplified for testnet)
    uint256 private nonce;

    /**
     * @dev Constructor sets the minimum entry fee and initializes the game
     * @param _minEntryFee Minimum amount required to enter the game (in wei)
     */
    constructor(uint256 _minEntryFee) {
        minEntryFee = _minEntryFee;
        gameActive = true;
    }

    /**
     * @dev Allows a player to enter the game by sending the entry fee
     */
    function enterGame() external payable {
        require(gameActive, "Game is not active");
        require(msg.value >= minEntryFee, "Insufficient entry fee");
        require(!isPlayer(msg.sender), "Already entered the game");

        players.push(msg.sender);
        emit NewPlayer(msg.sender, msg.value);
    }

    /**
     * @dev Selects a random winner and transfers the prize pool
     */
    function selectWinner() external onlyOwner {
        require(gameActive, "Game is not active");
        require(players.length > 0, "No players in the game");

        // Simplified random number generation for testnet
        uint256 randomIndex = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, nonce))) % players.length;
        nonce++;

        address winner = players[randomIndex];
        uint256 prizeAmount = address(this).balance;

        // Reset game state
        delete players;
        gameActive = false;

        // Transfer prize to winner
        (bool success, ) = winner.call{value: prizeAmount}("");
        require(success, "Transfer failed");

        emit WinnerSelected(winner, prizeAmount);
    }

    /**
     * @dev Checks if an address is already a player
     * @param _player Address to check
     * @return bool True if player exists, false otherwise
     */
    function isPlayer(address _player) public view returns (bool) {
        for (uint256 i = 0; i < players.length; i++) {
            if (players[i] == _player) {
                return true;
            }
        }
        return false;
    }

    /**
     * @dev Returns the current number of players
     * @return uint256 Number of players
     */
    function getPlayerCount() external view returns (uint256) {
        return players.length;
    }

    /**
     * @dev Returns the current prize pool amount
     * @return uint256 Prize pool in wei
     */
    function getPrizePool() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Allows owner to restart the game
     */
    function restartGame() external onlyOwner {
        require(!gameActive, "Game is already active");
        gameActive = true;
    }

    /**
     * @dev Allows owner to update the minimum entry fee
     * @param _newFee New minimum entry fee in wei
     */
    function updateEntryFee(uint256 _newFee) external onlyOwner {
        minEntryFee = _newFee;
    }
}
```

```javascript
// Deployment script (using Hardhat)
const hre = require("hardhat");

async function main() {
  const [deployer] = await hre.ethers.getSigners();
  console.log("Deploying contracts with the account:", deployer.address);

  const RandomWinnerGame = await hre.ethers.getContractFactory("RandomWinnerGame");
  const game = await RandomWinnerGame.deploy(hre.ethers.utils.parseEther("0.01"));

  await game.deployed();
  console.log("RandomWinnerGame deployed to:", game.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
```

```graphql
# GraphQL Schema for The Graph Protocol
type Player @entity {
  id: ID!
  address: Bytes!
  entryAmount: BigInt!
  timestamp: BigInt!
}

type Winner @entity {
  id: ID!
  address: Bytes!
  prizeAmount: BigInt!
  timestamp: BigInt!
}

type GameStatus @entity {
  id: ID!
  active: Boolean!
  playerCount: BigInt!
  prizePool: BigInt!
}
```

```javascript
// Subgraph mappings (The Graph)
const { NewPlayer, WinnerSelected } = require("../generated/RandomWinnerGame/RandomWinnerGame");
const { Player, Winner, GameStatus } = require("../generated/schema");

function getOrCreateGameStatus(): GameStatus {
  let gameStatus = GameStatus.load("1");
  if (!gameStatus) {
    gameStatus = new GameStatus("1");
    gameStatus.active = true;
    gameStatus.playerCount = BigInt.fromI32(0);
    gameStatus.prizePool = BigInt.fromI32(0);
  }
  return gameStatus;
}

export function handleNewPlayer(event: NewPlayer): void {
  let player = new Player(event.transaction.hash.toHex() + "-" + event.logIndex.toString());
  player.address = event.params.player;
  player.entryAmount = event.params.entryAmount;
  player.timestamp = event.block.timestamp;
  player.save();

  let gameStatus = getOrCreateGameStatus();
  gameStatus.playerCount = gameStatus.playerCount.plus(BigInt.fromI32(1));
  gameStatus.prizePool = gameStatus.prizePool.plus(event.params.entryAmount);
  gameStatus.save();
}

export function handleWinnerSelected(event: WinnerSelected): void {
  let winner = new Winner(event.transaction.hash.toHex() + "-" + event.logIndex.toString());
  winner.address = event.params.winner;
  winner.prizeAmount = event.params.prizeAmount;
  winner.timestamp = event.block.timestamp;
  winner.save();

  let gameStatus = getOrCreateGameStatus();
  gameStatus.active = false;
  gameStatus.playerCount = BigInt.fromI32(0);
  gameStatus.prizePool = BigInt.fromI32(0);
  gameStatus.save();
}
```
