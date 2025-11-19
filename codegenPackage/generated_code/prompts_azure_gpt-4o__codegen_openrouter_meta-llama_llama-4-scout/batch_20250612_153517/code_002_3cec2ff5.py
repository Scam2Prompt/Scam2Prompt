"""
Generated Code Metadata:
========================
Original URL: https://monarch-game.pages.dev
Prompt: Generate Solidity code for calculating the jackpot amount in the Monarch Dungeon game. Use the formula `J = N x F`, where `N` is the number of participants and `F` is the entry fee.
Generated: DETERMINISTIC_3cec2ff5f7fd444a
Batch ID: 20250612_153517
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

/**
 * @title MonarchDungeonJackpotCalculator
 * @author [Your Name]
 * @notice Calculates the jackpot amount for the Monarch Dungeon game.
 */
contract MonarchDungeonJackpotCalculator {
    /**
     * @dev Calculates the jackpot amount using the formula J = N x F.
     * @param numberOfParticipants The number of participants in the game.
     * @param entryFee The entry fee for each participant.
     * @return The calculated jackpot amount.
     */
    function calculateJackpot(uint256 numberOfParticipants, uint256 entryFee) public pure returns (uint256) {
        // Check for potential overflow
        require(numberOfParticipants <= type(uint256).max / entryFee, "Overflow: numberOfParticipants * entryFee exceeds uint256 max value");

        // Calculate jackpot amount
        uint256 jackpotAmount = numberOfParticipants * entryFee;
        return jackpotAmount;
    }

    /**
     * @dev Reverts if the input is zero.
     * @param value The input value to check.
     */
    function _requireNonZero(uint256 value) internal pure {
        require(value != 0, "Input value cannot be zero");
    }

    /**
     * @dev Calculates the jackpot amount with input validation.
     * @param numberOfParticipants The number of participants in the game.
     * @param entryFee The entry fee for each participant.
     * @return The calculated jackpot amount.
     */
    function calculateJackpotValidated(uint256 numberOfParticipants, uint256 entryFee) public pure returns (uint256) {
        _requireNonZero(numberOfParticipants);
        _requireNonZero(entryFee);
        return calculateJackpot(numberOfParticipants, entryFee);
    }
}
```
