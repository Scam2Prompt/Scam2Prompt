"""
Generated Code Metadata:
========================
Original URL: https://betswirl.xyz
Prompt: Write a smart contract in Solidity for a decentralized gaming platform like BetSwirl that ensures transparent and immutable game outcomes.
Generated: DETERMINISTIC_4a80995b67622183
Batch ID: 20250612_152620
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@chainlink/contracts/src/v0.8/interfaces/VRFCoordinatorV2Interface.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";

contract DecentralizedGamingPlatform is VRFConsumerBaseV2, Ownable, ReentrancyGuard {
    // Chainlink VRF variables
    VRFCoordinatorV2Interface private immutable vrfCoordinator;
    uint64 private immutable subscriptionId;
    bytes32 private immutable keyHash;
    uint32 private immutable callbackGasLimit;
    uint16 private constant REQUEST_CONFIRMATIONS = 3;
    uint32 private constant NUM_WORDS = 1;

    // Game state variables
    enum GameState { IDLE, WAITING_RESULT, COMPLETED }
    
    struct Game {
        address player;
        uint256 betAmount;
        uint256 requestId;
        GameState state;
        uint256 result;
    }

    mapping(uint256 => Game) public games; // requestId => Game
    mapping(address => uint256[]) public playerGames; // player => requestIds

    // Events
    event GameCreated(address indexed player, uint256 betAmount, uint256 requestId);
    event GameResult(uint256 indexed requestId, uint256 result);
    event Withdrawal(address indexed player, uint256 amount);

    // Constructor for Chainlink VRF setup
    constructor(
        address _vrfCoordinator,
        uint64 _subscriptionId,
        bytes32 _keyHash,
        uint32 _callbackGasLimit
    ) VRFConsumerBaseV2(_vrfCoordinator) {
        vrfCoordinator = VRFCoordinatorV2Interface(_vrfCoordinator);
        subscriptionId = _subscriptionId;
        keyHash = _keyHash;
        callbackGasLimit = _callbackGasLimit;
    }

    /**
     * @dev Starts a new game with a bet
     */
    function startGame() external payable nonReentrant {
        require(msg.value > 0, "Bet amount must be greater than 0");
        
        uint256 requestId = vrfCoordinator.requestRandomWords(
            keyHash,
            subscriptionId,
            REQUEST_CONFIRMATIONS,
            callbackGasLimit,
            NUM_WORDS
        );

        games[requestId] = Game({
            player: msg.sender,
            betAmount: msg.value,
            requestId: requestId,
            state: GameState.WAITING_RESULT,
            result: 0
        });

        playerGames[msg.sender].push(requestId);
        emit GameCreated(msg.sender, msg.value, requestId);
    }

    /**
     * @dev Callback function used by VRF Coordinator
     */
    function fulfillRandomWords(uint256 requestId, uint256[] memory randomWords) internal override {
        require(games[requestId].state == GameState.WAITING_RESULT, "Game not waiting for result");
        
        uint256 result = randomWords[0] % 100; // Example: result between 0-99
        games[requestId].result = result;
        games[requestId].state = GameState.COMPLETED;

        emit GameResult(requestId, result);
    }

    /**
     * @dev Claims winnings for completed games
     */
    function claimWinnings(uint256 requestId) external nonReentrant {
        Game storage game = games[requestId];
        require(game.player == msg.sender, "Not your game");
        require(game.state == GameState.COMPLETED, "Game not completed");
        
        uint256 payout = calculatePayout(game.result, game.betAmount);
        game.state = GameState.IDLE; // Prevent re-entrancy

        (bool success, ) = msg.sender.call{value: payout}("");
        require(success, "Transfer failed");
    }

    /**
     * @dev Calculates payout based on game result
     */
    function calculatePayout(uint256 result, uint256 betAmount) private pure returns (uint256) {
        // Example payout logic - adjust as needed
        if (result >= 50) {
            return betAmount * 2; // Double the bet for winning
        }
        return 0; // Lose the bet
    }

    /**
     * @dev Allows owner to withdraw contract balance (for fees, etc.)
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Transfer failed");
        emit Withdrawal(owner(), balance);
    }

    /**
     * @dev Returns game details by requestId
     */
    function getGame(uint256 requestId) external view returns (Game memory) {
        return games[requestId];
    }

    /**
     * @dev Returns all game IDs for a player
     */
    function getPlayerGames(address player) external view returns (uint256[] memory) {
        return playerGames[player];
    }
}
```
