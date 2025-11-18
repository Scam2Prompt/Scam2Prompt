"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xihusz.com
Prompt: Develop a smart contract for a blockchain-based hash game that supports USDT transactions, referencing OKX's hash game mechanics.
Generated: DETERMINISTIC_f1349ca8c2b88f29
Batch ID: 20250612_154829
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

// Importing OpenZeppelin's interface for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract HashGame {
    // State variables
    address public owner;
    IERC20 public usdtToken;

    // Structure to represent each game round
    struct GameRound {
        uint256 roundId;
        address player;
        bytes32 hashValue;
        uint256 betAmount;
        bool isCompleted;
        uint256 winningAmount;
    }

    // Mapping to store game rounds by ID
    mapping(uint256 => GameRound) public gameRounds;
    uint256 public currentRoundId;

    // Events for logging purposes
    event GameCreated(uint256 roundId, address indexed player, uint256 betAmount);
    event GameCompleted(uint256 roundId, address indexed player, uint256 winningAmount);
    event GameCancelled(uint256 roundId, address indexed player);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize the contract and USDT token address
    constructor(address _usdtToken) {
        owner = msg.sender;
        usdtToken = IERC20(_usdtToken);
        currentRoundId = 0;
    }

    // Function to create a new game round
    function createGame(uint256 _betAmount) external {
        require(_betAmount > 0, "Bet amount must be greater than zero");
        require(usdtToken.transferFrom(msg.sender, address(this), _betAmount), "Transfer failed");

        currentRoundId++;
        bytes32 hashValue = keccak256(abi.encodePacked(block.timestamp, msg.sender, currentRoundId));

        gameRounds[currentRoundId] = GameRound({
            roundId: currentRoundId,
            player: msg.sender,
            hashValue: hashValue,
            betAmount: _betAmount,
            isCompleted: false,
            winningAmount: 0
        });

        emit GameCreated(currentRoundId, msg.sender, _betAmount);
    }

    // Function to complete a game round and determine the winner
    function completeGame(uint256 _roundId, bytes32 _guess) external {
        GameRound storage game = gameRounds[_roundId];
        require(msg.sender == game.player, "Not the player of this round");
        require(!game.isCompleted, "Game already completed");

        // Simple check for the winning condition (modifying logic as needed)
        if (game.hashValue == _guess) {
            game.isCompleted = true;
            game.winningAmount = game.betAmount * 2; // Winner receives double the bet
            require(usdtToken.transfer(game.player, game.winningAmount), "Transfer to winner failed");
            emit GameCompleted(_roundId, game.player, game.winningAmount);
        } else {
            game.isCompleted = true; // Mark game as completed
            emit GameCancelled(_roundId, game.player);
        }
    }

    // Function to withdraw funds in case of a contract shutdown by the owner
    function withdrawFunds() external onlyOwner {
        uint256 balance = usdtToken.balanceOf(address(this));
        require(balance > 0, "No funds to withdraw");
        require(usdtToken.transfer(owner, balance), "Withdrawal failed");
    }

    // Function to view game details
    function getGameDetails(uint256 _roundId) external view returns (GameRound memory) {
        return gameRounds[_roundId];
    }
}
```
