"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memeskombat-io.pages.dev
Prompt: Generate a Solidity smart contract for betting on meme battles using $MK tokens as the currency on the Meme Kombat platform.
Generated: DETERMINISTIC_f0ff8df9bf68b0f2
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title MemeBattleBetting
 * @dev A smart contract for betting on meme battles using $MK tokens.
 */
contract MemeBattleBetting {
    // Address of the $MK token contract
    IERC20 public mkToken;

    // Structure to hold details of each meme battle
    struct MemeBattle {
        string meme1; // Name of the first meme in the battle
        string meme2; // Name of the second meme in the battle
        uint256 endTime; // Timestamp for when betting ends
        uint256 meme1Bets; // Total amount of bets on meme1
        uint256 meme2Bets; // Total amount of bets on meme2
        bool settled; // Flag to indicate whether the battle is settled
        address winner; // Address of the winning meme (can be decided externally)
    }

    // Mapping of battle IDs to MemeBattle structs
    mapping(uint256 => MemeBattle) public memeBattles;

    // Mapping of user bets per battle
    mapping(uint256 => mapping(address => uint256)) public userBetsOnMeme1;
    mapping(uint256 => mapping(address => uint256)) public userBetsOnMeme2;

    // Counter to track the battle IDs
    uint256 public battleCounter;

    // Events
    event MemeBattleCreated(uint256 indexed battleId, string meme1, string meme2, uint256 endTime);
    event BetPlaced(address indexed user, uint256 indexed battleId, uint256 amount, uint8 memeChoice);
    event BattleSettled(uint256 indexed battleId, address winner);

    // Constructor to initialize the $MK token address
    constructor(IERC20 _mkToken) {
        mkToken = _mkToken;
    }

    /**
     * @dev Create a new meme battle.
     * @param meme1 Name of the first meme in the battle.
     * @param meme2 Name of the second meme in the battle.
     * @param endTime Timestamp for when betting on this battle ends.
     */
    function createMemeBattle(string memory meme1, string memory meme2, uint256 endTime) external {
        require(endTime > block.timestamp, "End time must be in the future");

        battleCounter++;
        memeBattles[battleCounter] = MemeBattle({
            meme1: meme1,
            meme2: meme2,
            endTime: endTime,
            meme1Bets: 0,
            meme2Bets: 0,
            settled: false,
            winner: address(0)
        });

        emit MemeBattleCreated(battleCounter, meme1, meme2, endTime);
    }

    /**
     * @dev Place a bet on a meme in a specific battle.
     * @param battleId The ID of the battle to bet on.
     * @param amount The amount of $MK tokens to bet.
     * @param memeChoice The meme to bet on (1 for meme1, 2 for meme2).
     */
    function placeBet(uint256 battleId, uint256 amount, uint8 memeChoice) external {
        require(battleId > 0 && battleId <= battleCounter, "Invalid battle ID");
        MemeBattle storage battle = memeBattles[battleId];
        require(block.timestamp < battle.endTime, "Betting period has ended");
        require(memeChoice == 1 || memeChoice == 2, "Invalid meme choice");
        require(amount > 0, "Bet amount must be greater than zero");

        // Transfer $MK tokens from the user to this contract
        require(mkToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update bets based on the user's choice
        if (memeChoice == 1) {
            battle.meme1Bets += amount;
            userBetsOnMeme1[battleId][msg.sender] += amount;
        } else {
            battle.meme2Bets += amount;
            userBetsOnMeme2[battleId][msg.sender] += amount;
        }

        emit BetPlaced(msg.sender, battleId, amount, memeChoice);
    }

    /**
     * @dev Settle a meme battle and distribute rewards to winners.
     * @param battleId The ID of the battle to settle.
     * @param winnerAddress The address representing the winning meme (can be meme1 or meme2).
     */
    function settleBattle(uint256 battleId, address winnerAddress) external {
        require(battleId > 0 && battleId <= battleCounter, "Invalid battle ID");
        MemeBattle storage battle = memeBattles[battleId];
        require(block.timestamp >= battle.endTime, "Betting period has not ended");
        require(!battle.settled, "Battle already settled");
        require(winnerAddress == address(1) || winnerAddress == address(2), "Invalid winner address");

        battle.settled = true;
        battle.winner = winnerAddress;

        emit BattleSettled(battleId, winnerAddress);

        // Calculate rewards and distribute to winners
        uint256 totalBets = battle.meme1Bets + battle.meme2Bets;
        if (winnerAddress == address(1)) {
            distributeRewards(battleId, battle.meme1Bets, userBetsOnMeme1);
        } else {
            distributeRewards(battleId, battle.meme2Bets, userBetsOnMeme2);
        }
    }

    /**
     * @dev Internal function to distribute rewards to winners.
     * @param battleId The ID of the battle.
     * @param totalWinningBets The total amount of bets placed on the winning meme.
     * @param userBets Mapping of user bets on the winning meme.
     */
    function distributeRewards(
        uint256 battleId,
        uint256 totalWinningBets,
        mapping(uint256 => mapping(address => uint256)) storage userBets
    ) internal {
        MemeBattle storage battle = memeBattles[battleId];

        for (uint256 i = 0; i < userBets[battleId].length; i++) {
            address user = userBets[battleId][i];
            uint256 userBet = userBets[battleId][user];
            uint256 reward = (userBet * (battle.meme1Bet)). / caluctotalBetAmount;

```
