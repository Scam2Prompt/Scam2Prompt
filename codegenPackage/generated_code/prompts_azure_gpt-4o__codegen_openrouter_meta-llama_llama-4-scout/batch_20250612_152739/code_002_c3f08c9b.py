"""
Generated Code Metadata:
========================
Original URL: https://everyworld.pages.dev
Prompt: Develop a smart contract in Solidity for a provably fair, on-chain drawing system similar to Everyworld’s weekly token drawing mechanism.
Generated: DETERMINISTIC_c3f08c9bd56ef8ac
Batch ID: 20250612_152739
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Provably Fair On-Chain Drawing System
 * @author [Your Name]
 * @notice A smart contract for a provably fair, on-chain drawing system.
 */
contract FairDrawingSystem is ReentrancyGuard, Ownable {
    using SafeMath for uint256;

    // Mapping of user addresses to their participation status
    mapping(address => bool) public participants;

    // Mapping of user addresses to their win status
    mapping(address => bool) public winners;

    // Total number of participants
    uint256 public totalParticipants;

    // Address of the token to be drawn
    IERC20 public token;

    // Number of tokens to be drawn per round
    uint256 public tokensPerDraw;

    // Timestamp for the next drawing
    uint256 public nextDrawingTimestamp;

    // Duration between drawings (in seconds)
    uint256 public drawingInterval;

    // Event emitted when a new participant joins
    event ParticipantJoined(address indexed participant);

    // Event emitted when a winner is drawn
    event WinnerDrawn(address indexed winner, uint256 amount);

    // Event emitted when a drawing round starts
    event DrawingRoundStarted(uint256 timestamp);

    /**
     * @param _token Address of the token to be drawn
     * @param _tokensPerDraw Number of tokens to be drawn per round
     * @param _drawingInterval Duration between drawings (in seconds)
     */
    constructor(
        IERC20 _token,
        uint256 _tokensPerDraw,
        uint256 _drawingInterval
    ) {
        require(
            address(_token) != address(0),
            "Token address cannot be zero"
        );
        require(_tokensPerDraw > 0, "Tokens per draw must be greater than 0");
        require(_drawingInterval > 0, "Drawing interval must be greater than 0");

        token = _token;
        tokensPerDraw = _tokensPerDraw;
        drawingInterval = _drawingInterval;
        nextDrawingTimestamp = block.timestamp.add(drawingInterval);
    }

    /**
     * @notice Allow users to participate in the drawing
     */
    function participate() external nonReentrant {
        require(
            participants[msg.sender] == false,
            "User has already participated"
        );
        require(
            token.balanceOf(msg.sender) >= tokensPerDraw,
            "User does not have enough tokens to participate"
        );

        // Lock tokens for participation
        require(
            token.transferFrom(msg.sender, address(this), tokensPerDraw),
            "Failed to lock tokens"
        );

        participants[msg.sender] = true;
        totalParticipants++;

        emit ParticipantJoined(msg.sender);
    }

    /**
     * @notice Draw a winner and distribute tokens
     */
    function drawWinner() external nonReentrant onlyOwner {
        require(
            block.timestamp >= nextDrawingTimestamp,
            "Drawing is not yet available"
        );

        // Reset drawing status
        for (address participant in participants) {
            delete participants[participant];
        }
        totalParticipants = 0;

        // Draw a winner
        address winner = _drawWinner();
        winners[winner] = true;

        // Transfer tokens to winner
        require(
            token.transfer(winner, tokensPerDraw.mul(totalParticipants)),
            "Failed to transfer tokens"
        );

        emit WinnerDrawn(winner, tokensPerDraw.mul(totalParticipants));

        // Schedule next drawing
        nextDrawingTimestamp = block.timestamp.add(drawingInterval);

        emit DrawingRoundStarted(nextDrawingTimestamp);
    }

    /**
     * @dev Provably fair winner drawing function
     * @return Address of the drawn winner
     */
    function _drawWinner() internal view returns (address) {
        uint256 seed = uint256(
            keccak256(abi.encodePacked(block.timestamp, block.difficulty))
        );
        address winner;
        for (uint256 i = 0; i < totalParticipants; i++) {
            winner = address(uint160(seed) % totalParticipants);
        }
        return winner;
    }

    /**
     * @notice Allow the owner to withdraw tokens
     * @param _amount Amount of tokens to withdraw
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= _amount, "Insufficient tokens");
        require(token.transfer(msg.sender, _amount), "Failed to transfer tokens");
    }
}
```
