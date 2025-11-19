"""
Generated Code Metadata:
========================
Original URL: https://whelps.io
Prompt: Develop a smart contract in Solidity to manage entry fees and prize distribution for the competitive mode of WhelpS: Slipstream, including a mechanism to burn a portion of the Dragon tokens.
Generated: DETERMINISTIC_d974ea6e8b2b70ad
Batch ID: 20250612_151539
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title WhelpS Slipstream Competitive Mode Contract
 * @author [Your Name]
 * @notice Manages entry fees and prize distribution for WhelpS: Slipstream competitive mode.
 */
contract WhelpSCompetitiveMode is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of tournament IDs to their respective details
    mapping(uint256 => Tournament) public tournaments;

    // Mapping of user addresses to their tournament entries
    mapping(address => mapping(uint256 => bool)) public userEntries;

    // Address of the Dragon token contract
    IERC20 public dragonToken;

    // Address of the prize pool wallet
    address public prizePoolWallet;

    // Percentage of entry fee to burn (in basis points, e.g., 100 = 1%)
    uint256 public burnPercentage;

    // Event emitted when a new tournament is created
    event NewTournament(uint256 tournamentId, uint256 entryFee, uint256 prizeAmount);

    // Event emitted when a user enters a tournament
    event UserEnteredTournament(address user, uint256 tournamentId);

    // Event emitted when a tournament prize is distributed
    event PrizeDistributed(uint256 tournamentId, address winner, uint256 prizeAmount);

    // Struct to hold tournament details
    struct Tournament {
        uint256 id;
        uint256 entryFee;
        uint256 prizeAmount;
        bool isActive;
        address winner;
    }

    /**
     * @notice Constructor for the WhelpSCompetitiveMode contract.
     * @param _dragonToken Address of the Dragon token contract.
     * @param _prizePoolWallet Address of the prize pool wallet.
     * @param _burnPercentage Percentage of entry fee to burn (in basis points).
     */
    constructor(IERC20 _dragonToken, address _prizePoolWallet, uint256 _burnPercentage) {
        require(_dragonToken != IERC20(address(0)), "Invalid Dragon token address");
        require(_prizePoolWallet != address(0), "Invalid prize pool wallet address");
        require(_burnPercentage <= 10000, "Burn percentage exceeds 100%");

        dragonToken = _dragonToken;
        prizePoolWallet = _prizePoolWallet;
        burnPercentage = _burnPercentage;
    }

    /**
     * @notice Creates a new tournament.
     * @param _entryFee Entry fee for the tournament.
     * @param _prizeAmount Prize amount for the tournament.
     */
    function createTournament(uint256 _entryFee, uint256 _prizeAmount) public {
        require(_entryFee > 0, "Entry fee must be greater than 0");
        require(_prizeAmount > 0, "Prize amount must be greater than 0");

        uint256 tournamentId = uint256(keccak256(abi.encodePacked(msg.sender, block.timestamp)));

        tournaments[tournamentId] = Tournament({
            id: tournamentId,
            entryFee: _entryFee,
            prizeAmount: _prizeAmount,
            isActive: true,
            winner: address(0)
        });

        emit NewTournament(tournamentId, _entryFee, _prizeAmount);
    }

    /**
     * @notice Enters a tournament.
     * @param _tournamentId ID of the tournament to enter.
     */
    function enterTournament(uint256 _tournamentId) public {
        require(tournaments[_tournamentId].isActive, "Tournament is not active");
        require(!userEntries[msg.sender][_tournamentId], "User already entered this tournament");

        userEntries[msg.sender][_tournamentId] = true;

        // Deduct entry fee from user's balance
        uint256 entryFee = tournaments[_tournamentId].entryFee;
        SafeERC20.safeTransferFrom(dragonToken, msg.sender, address(this), entryFee);

        // Burn a portion of the entry fee
        uint256 burnAmount = entryFee.mul(burnPercentage).div(10000);
        SafeERC20.safeTransfer(dragonToken, address(0x000000000000000000000000000000000000dEaD), burnAmount);

        emit UserEnteredTournament(msg.sender, _tournamentId);
    }

    /**
     * @notice Sets the winner of a tournament and distributes the prize.
     * @param _tournamentId ID of the tournament.
     * @param _winner Address of the winner.
     */
    function setWinner(uint256 _tournamentId, address _winner) public {
        require(msg.sender == prizePoolWallet, "Only the prize pool wallet can set the winner");
        require(tournaments[_tournamentId].isActive, "Tournament is not active");
        require(tournaments[_tournamentId].winner == address(0), "Winner already set");

        tournaments[_tournamentId].isActive = false;
        tournaments[_tournamentId].winner = _winner;

        // Transfer prize amount to the winner
        uint256 prizeAmount = tournaments[_tournamentId].prizeAmount;
        SafeERC20.safeTransfer(dragonToken, _winner, prizeAmount);

        emit PrizeDistributed(_tournamentId, _winner, prizeAmount);
    }
}
```
