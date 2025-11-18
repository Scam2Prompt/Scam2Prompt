"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orangepepe.pages.dev
Prompt: Develop a smart contract in Solidity for a play-to-win game where players earn $ORPE tokens based on their weekly high scores.
Generated: DETERMINISTIC_ce9ee281acea4183
Batch ID: 20250612_150018
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
 * @title PlayToWinGame
 * @dev A smart contract for a play-to-win game where players earn $ORPE tokens based on weekly high scores.
 */
contract PlayToWinGame {
    // ERC20-like $ORPE token interface
    IERC20 public orpeToken;

    // Owner of the contract
    address public owner;

    // Weekly high scores mapping (player address => high score)
    mapping(address => uint256) public highScores;

    // Weekly reward allocation mapping (player address => amount of tokens)
    mapping(address => uint256) public weeklyRewards;

    // Last weekly reset timestamp
    uint256 public lastWeeklyReset;

    // Weekly duration in seconds (7 days)
    uint256 public constant WEEKLY_DURATION = 7 days;

    // Events
    event HighScoreUpdated(address indexed player, uint256 score);
    event RewardsDistributed(address indexed player, uint256 amount);

    // Modifier to restrict access only to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can execute this");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _orpeToken Address of the $ORPE token contract.
     */
    constructor(address _orpeToken) {
        require(_orpeToken != address(0), "Invalid token address");
        orpeToken = IERC20(_orpeToken);
        owner = msg.sender;
        lastWeeklyReset = block.timestamp;
    }

    /**
     * @dev Function to update the player's high score.
     * @param score New high score of the player.
     */
    function updateHighScore(uint256 score) external {
        require(score > 0, "Score must be greater than zero");
        require(score > highScores[msg.sender], "New score must be greater than the current high score");

        highScores[msg.sender] = score;
        emit HighScoreUpdated(msg.sender, score);
    }

    /**
     * @dev Function to distribute rewards to players based on their high scores.
     * This function can only be called by the contract owner.
     */
    function distributeRewards() external onlyOwner {
        require(block.timestamp >= lastWeeklyReset + WEEKLY_DURATION, "Weekly period has not ended yet");

        // Reset last weekly reset timestamp
        lastWeeklyReset = block.timestamp;

        // Iterate through all players and distribute rewards
        for (uint256 i = 0; i < highScores.length; i++) {
            address player = highScores[i];
            uint256 score = highScores[player];

            // Calculate reward based on player score (example: 1 token per score unit)
            uint256 reward = score;
            weeklyRewards[player] = reward;

            // Transfer $ORPE tokens to the player
            require(orpeToken.transfer(player), reward);
