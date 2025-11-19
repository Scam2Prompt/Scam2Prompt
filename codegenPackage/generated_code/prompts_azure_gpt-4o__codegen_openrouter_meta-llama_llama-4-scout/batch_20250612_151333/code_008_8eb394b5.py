"""
Generated Code Metadata:
========================
Original URL: https://bitzino.vip
Prompt: Write a Solidity smart contract for managing high-limit tables and exclusive bonuses for top casino gamblers, similar to the features described on Bitzino.vip.
Generated: DETERMINISTIC_8eb394b572234d76
Batch ID: 20250612_151333
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title HighLimitTableManager
 * @author [Your Name]
 * @notice Manages high-limit tables and exclusive bonuses for top casino gamblers.
 */
contract HighLimitTableManager is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of high-limit tables
    mapping(address => HighLimitTable) public tables;

    // Mapping of player bonuses
    mapping(address => uint256) public playerBonuses;

    // Mapping of player bets
    mapping(address => uint256) public playerBets;

    // Event emitted when a new high-limit table is created
    event NewTable(address indexed tableAddress);

    // Event emitted when a player's bonus is updated
    event BonusUpdated(address indexed player, uint256 bonus);

    // Event emitted when a player's bet is recorded
    event BetRecorded(address indexed player, uint256 bet);

    // Struct representing a high-limit table
    struct HighLimitTable {
        uint256 minBet;
        uint256 maxBet;
        uint256 exclusiveBonus;
    }

    /**
     * @notice Creates a new high-limit table.
     * @param _minBet The minimum bet for the table.
     * @param _maxBet The maximum bet for the table.
     * @param _exclusiveBonus The exclusive bonus for the table.
     */
    function createTable(uint256 _minBet, uint256 _maxBet, uint256 _exclusiveBonus) public onlyOwner {
        require(_minBet > 0, "Minimum bet must be greater than 0");
        require(_maxBet > _minBet, "Maximum bet must be greater than minimum bet");
        require(_exclusiveBonus > 0, "Exclusive bonus must be greater than 0");

        HighLimitTable memory newTable;
        newTable.minBet = _minBet;
        newTable.maxBet = _maxBet;
        newTable.exclusiveBonus = _exclusiveBonus;

        tables[msg.sender] = newTable;

        emit NewTable(msg.sender);
    }

    /**
     * @notice Updates a player's bonus.
     * @param _player The player to update.
     * @param _bonus The new bonus amount.
     */
    function updateBonus(address _player, uint256 _bonus) public onlyOwner {
        require(_bonus > 0, "Bonus must be greater than 0");

        playerBonuses[_player] = _bonus;

        emit BonusUpdated(_player, _bonus);
    }

    /**
     * @notice Records a player's bet.
     * @param _player The player to record the bet for.
     * @param _bet The bet amount.
     */
    function recordBet(address _player, uint256 _bet) public {
        require(_bet > 0, "Bet must be greater than 0");

        // Check if player is eligible for high-limit table
        if (playerBets[_player] == 0) {
            // Check if player has a high-limit table
            if (tables[_player].minBet > 0) {
                // Check if bet is within table limits
                require(_bet >= tables[_player].minBet && _bet <= tables[_player].maxBet, "Bet is out of table limits");
            }
        }

        playerBets[_player] = playerBets[_player].add(_bet);

        emit BetRecorded(_player, _bet);
    }

    /**
     * @notice Claims a player's exclusive bonus.
     * @param _player The player to claim the bonus for.
     */
    function claimBonus(address _player) public {
        require(playerBonuses[_player] > 0, "Player has no bonus to claim");

        // Check if player has made a qualifying bet
        require(playerBets[_player] >= tables[_player].minBet, "Player has not made a qualifying bet");

        // Transfer bonus to player
        // NOTE: This line assumes the contract has the ability to transfer tokens.
        // You may need to modify this line depending on your specific use case.
        // For example, you might use a token contract's transfer function.

        playerBonuses[_player] = 0;
    }

    /**
     * @notice Withdraws from the contract.
     * @param _amount The amount to withdraw.
     */
    function withdraw(uint256 _amount) public onlyOwner {
        require(_amount > 0, "Withdrawal amount must be greater than 0");
        require(address(this).balance >= _amount, "Insufficient balance");

        // NOTE: This line assumes the contract has the ability to send Ether.
        // You may need to modify this line depending on your specific use case.

        payable(msg.sender).transfer(_amount);
    }
}
```
