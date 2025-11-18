"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://graph-protocol.vercel.app
Prompt: Write a smart contract in Solidity for a random winner selection game, similar to the "Random Game" described, and deploy it on the Mumbai Testnet using the Graph Protocol.
Generated: DETERMINISTIC_e91b90ebc1003bbb
Batch ID: 20250612_150316
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

// Import Chainlink VRF for random number generation
import "@chainlink/contracts/src/v0.8/interfaces/VRFCoordinatorV2Interface.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";

contract RandomWinnerGame is VRFConsumerBaseV2 {
    // Events
    event PlayerJoined(address indexed player);
    event WinnerSelected(address indexed winner);
    event RandomNumberRequested(uint256 indexed requestId);

    // Chainlink VRF Variables
    VRFCoordinatorV2Interface private immutable vrfCoordinator;
    bytes32 private immutable keyHash;
    uint64 private immutable subscriptionId;
    uint16 private constant requestConfirmations = 3;
    uint32 private constant callbackGasLimit = 100000;
    uint32 private constant numWords = 1;

    // Game-related Variables
    address[] public players; // List of players
    address public owner; // Owner of the contract
    bool public isGameActive = false; // Status of the game
    uint256 public entryFee; // Entry fee in wei

    // Random number request ID to track Chainlink responses
    uint256 public currentRequestId;

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier gameIsActive() {
        require(isGameActive, "Game is not active");
        _;
    }

    constructor(
        address _vrfCoordinator,
        bytes32 _keyHash,
        uint64 _subscriptionId,
        uint256 _entryFee
    ) VRFConsumerBaseV2(_vrfCoordinator) {
        vrfCoordinator = VRFCoordinatorV2Interface(_vrfCoordinator);
        keyHash = _keyHash;
        subscriptionId = _subscriptionId;
        entryFee = _entryFee;
        owner = msg.sender;
    }

    /**
     * @dev Start the game.
     */
    function startGame() external onlyOwner {
        require(!isGameActive, "Game is already active");
        isGameActive = true;
    }

    /**
     * @dev Stop the game.
     */
    function stopGame() external onlyOwner {
        require(isGameActive, "Game is not active");
        isGameActive = false;
    }

    /**
     * @dev Join the game by paying the entry fee.
     */
    function joinGame() external payable gameIsActive {
        require(msg.value == entryFee, "Incorrect entry fee");
        players.push(msg.sender);
        emit PlayerJoined(msg.sender);
    }

    /**
     * @dev Request a random number from Chainlink VRF to select a winner.
     */
    function selectWinner() external onlyOwner gameIsActive {
        require(players.length > 0, "No players joined");
        currentRequestId = vrfCoordinator.requestRandomWords(
            keyHash,
            subscriptionId,
            requestConfirmations,
            callbackGasLimit,
            numWords
        );
        emit RandomNumberRequested(currentRequestId);
    }

    /**
     * @dev Callback function for Chainlink VRF. Receives the random number.
     * @param requestId The request ID for which the random number was generated.
     * @param randomWords The array containing the random number.
     */
    function fulfillRandomWords(
        uint256 requestId,
        uint256[] memory randomWords
    ) internal override {
        require(requestId == currentRequestId, "Invalid request ID");

        // Use modulo operation to select a winner index
        uint256 winnerIndex = randomWords[0] % players.length;
        address winner = players[winnerIndex];

        // Transfer the collected funds to the winner
        (bool sent, ) = winner.call{value: address(this).balance}("");
        require(sent, "Failed to transfer funds to winner");

        emit WinnerSelected(winner);

        // Reset the game
        players = new address[](0);
        isGameActive = false;
    }

    /**
     * @dev Get the list of players in the current game.
     */
    function getPlayers() external view returns (address[] memory) {
        return players;
    }

    /**
     * @dev Withdraw funds (only for owner in case of emergencies).
     */
    function emergencyWithdraw() external onlyOwner {
        (bool sent, ) = owner.call{value: address(this).balance}("");
        require(sent, "Failed to withdraw funds");
    }

    /**
     * @dev Fallback function to receive ETH.
     */
    receive() external payable {}

    fallback() external payable {}
}
```

**Note**: To deploy this smart contract on the Mumbai Testnet using The Graph Protocol, you will need to write indexing rules and subgraph mappings for event tracking (not included here). Make sure to configure and deploy a Chainlink VRF subscription for testing on Mumbai.
