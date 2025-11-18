"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dueleth.com
Prompt: Create a smart contract example in Solidity for a gaming or transaction platform similar to Duel ETH.
Generated: DETERMINISTIC_06860eed634ade02
Batch ID: 20250612_151659
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DuelETH
 * @dev A smart contract for a simple duel-based game where players can bet ETH.
 */
contract DuelETH is Ownable {
    // Struct to hold duel information
    struct Duel {
        address player1;
        address player2;
        uint256 betAmount;
        bool isActive;
        address winner;
    }

    // Mapping to store duels by ID
    mapping(uint256 => Duel) public duels;
    uint256 public duelCounter;

    // Events for logging duel actions
    event DuelCreated(uint256 duelId, address indexed player1, address indexed player2, uint256 betAmount);
    event DuelFinished(uint256 duelId, address indexed winner);
    event DuelCancelled(uint256 duelId);

    /**
     * @dev Creates a new duel between two players.
     * @param _player2 Address of the second player.
     * @param _betAmount Amount in wei that each player agrees to bet.
     */
    function createDuel(address _player2, uint256 _betAmount) external payable {
        require(msg.value == _betAmount, "Bet amount must match the sent value");
        require(_player2 != msg.sender, "Cannot duel yourself");
        
        duelCounter++;
        duels[duelCounter] = Duel(msg.sender, _player2, _betAmount, true, address(0));
        
        emit DuelCreated(duelCounter, msg.sender, _player2, _betAmount);
    }

    /**
     * @dev Finishes a duel and determines the winner.
     * @param _duelId ID of the duel to finish.
     * @param _winner Address of the winner.
     */
    function finishDuel(uint256 _duelId, address _winner) external onlyOwner {
        Duel storage duel = duels[_duelId];
        require(duel.isActive, "Duel is not active");
        require(_winner == duel.player1 || _winner == duel.player2, "Invalid winner");

        duel.winner = _winner;
        duel.isActive = false;

        // Transfer the bet amount to the winner
        payable(_winner).transfer(duel.betAmount * 2);
        
        emit DuelFinished(_duelId, _winner);
    }

    /**
     * @dev Cancels a duel if it's still active.
     * @param _duelId ID of the duel to cancel.
     */
    function cancelDuel(uint256 _duelId) external {
        Duel storage duel = duels[_duelId];
        require(duel.isActive, "Duel is not active");
        require(msg.sender == duel.player1, "Only player1 can cancel the duel");

        duel.isActive = false;

        // Refund the bet amount to player1
        payable(msg.sender).transfer(duel.betAmount);
        
        emit DuelCancelled(_duelId);
    }
}
```
