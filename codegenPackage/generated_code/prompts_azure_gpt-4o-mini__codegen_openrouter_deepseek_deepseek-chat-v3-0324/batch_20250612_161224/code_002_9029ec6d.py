"""
Generated Code Metadata:
========================
Original URL: https://everyworld4.pages.dev
Prompt: Can you provide an example of a smart contract that manages a drawing system for a web3 platform, inspired by the dual incentivization model used by Everyworld?
Generated: DETERMINISTIC_9029ec6d4d0c176f
Batch ID: 20250612_161224
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract DrawingManager is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Drawing structure
    struct Drawing {
        uint256 id;
        string name;
        uint256 prizePool;
        uint256 startTime;
        uint256 endTime;
        uint256 maxParticipants;
        uint256 participantCount;
        address[] participants;
        address winner;
        bool isCompleted;
    }

    // Token used for participation
    IERC20 public participationToken;

    // Fee percentage for the platform (1-100)
    uint256 public platformFeePercentage;

    // Drawings mapping
    mapping(uint256 => Drawing) public drawings;
    uint256 public nextDrawingId;

    // User balances for unclaimed prizes
    mapping(address => uint256) public userBalances;

    // Events
    event DrawingCreated(
        uint256 indexed id,
        string name,
        uint256 prizePool,
        uint256 startTime,
        uint256 endTime,
        uint256 maxParticipants
    );
    event ParticipantAdded(uint256 indexed drawingId, address participant);
    event DrawingCompleted(uint256 indexed drawingId, address winner, uint256 prize);
    event PrizeClaimed(address indexed user, uint256 amount);
    event PlatformFeeWithdrawn(address owner, uint256 amount);

    constructor(address _participationToken, uint256 _platformFeePercentage) {
        require(_platformFeePercentage <= 100, "Fee percentage must be <= 100");
        participationToken = IERC20(_participationToken);
        platformFeePercentage = _platformFeePercentage;
    }

    /**
     * @dev Creates a new drawing
     */
    function createDrawing(
        string memory _name,
        uint256 _prizePool,
        uint256 _startTime,
        uint256 _duration,
        uint256 _maxParticipants
    ) external onlyOwner {
        require(_prizePool > 0, "Prize pool must be greater than 0");
        require(_duration > 0, "Duration must be greater than 0");
        require(_maxParticipants > 0, "Max participants must be greater than 0");

        uint256 endTime = _startTime.add(_duration);
        require(endTime > block.timestamp, "End time must be in the future");

        uint256 drawingId = nextDrawingId++;
        drawings[drawingId] = Drawing({
            id: drawingId,
            name: _name,
            prizePool: _prizePool,
            startTime: _startTime,
            endTime: endTime,
            maxParticipants: _maxParticipants,
            participantCount: 0,
            participants: new address[](0),
            winner: address(0),
            isCompleted: false
        });

        emit DrawingCreated(drawingId, _name, _prizePool, _startTime, endTime, _maxParticipants);
    }

    /**
     * @dev Allows a user to participate in a drawing
     */
    function participate(uint256 _drawingId) external nonReentrant {
        Drawing storage drawing = drawings[_drawingId];
        require(drawing.id == _drawingId, "Drawing does not exist");
        require(block.timestamp >= drawing.startTime, "Drawing has not started");
        require(block.timestamp <= drawing.endTime, "Drawing has ended");
        require(!drawing.isCompleted, "Drawing is completed");
        require(drawing.participantCount < drawing.maxParticipants, "Drawing is full");
        require(!_hasParticipated(_drawingId, msg.sender), "Already participated");

        // Transfer participation fee (1 token)
        uint256 participationFee = 1 ether; // Assuming token has 18 decimals
        require(
            participationToken.transferFrom(msg.sender, address(this), participationFee),
            "Token transfer failed"
        );

        // Add participant
        drawing.participants.push(msg.sender);
        drawing.participantCount++;
        drawing.prizePool = drawing.prizePool.add(participationFee);

        emit ParticipantAdded(_drawingId, msg.sender);
    }

    /**
     * @dev Completes a drawing and selects a winner
     */
    function completeDrawing(uint256 _drawingId) external onlyOwner nonReentrant {
        Drawing storage drawing = drawings[_drawingId];
        require(drawing.id == _drawingId, "Drawing does not exist");
        require(block.timestamp > drawing.endTime, "Drawing has not ended");
        require(!drawing.isCompleted, "Drawing already completed");
        require(drawing.participantCount > 0, "No participants");

        // Select random winner
        uint256 randomIndex = _getRandomNumber(drawing.participantCount);
        address winner = drawing.participants[randomIndex];

        // Calculate prize (prize pool minus platform fee)
        uint256 platformFee = drawing.prizePool.mul(platformFeePercentage).div(100);
        uint256 prize = drawing.prizePool.sub(platformFee);

        // Update drawing state
        drawing.winner = winner;
        drawing.isCompleted = true;

        // Add prize to winner's balance
        userBalances[winner] = userBalances[winner].add(prize);

        emit DrawingCompleted(_drawingId, winner, prize);
    }

    /**
     * @dev Allows users to claim their prizes
     */
    function claimPrize() external nonReentrant {
        uint256 amount = userBalances[msg.sender];
        require(amount > 0, "No prize to claim");

        userBalances[msg.sender] = 0;
        require(participationToken.transfer(msg.sender, amount), "Token transfer failed");

        emit PrizeClaimed(msg.sender, amount);
    }

    /**
     * @dev Allows owner to withdraw platform fees
     */
    function withdrawPlatformFees() external onlyOwner nonReentrant {
        uint256 balance = participationToken.balanceOf(address(this));
        uint256 totalUserBalances = 0;

        // Calculate total user balances to ensure we don't withdraw user funds
        for (uint256 i = 0; i < nextDrawingId; i++) {
            if (!drawings[i].isCompleted) {
                totalUserBalances = totalUserBalances.add(drawings[i].prizePool);
            }
        }

        uint256 availableFees = balance.sub(totalUserBalances);
        require(availableFees > 0, "No fees available");

        require(participationToken.transfer(owner(), availableFees), "Token transfer failed");
        emit PlatformFeeWithdrawn(owner(), availableFees);
    }

    /**
     * @dev Checks if a user has participated in a drawing
     */
    function _hasParticipated(uint256 _drawingId, address _participant) internal view returns (bool) {
        for (uint256 i = 0; i < drawings[_drawingId].participants.length; i++) {
            if (drawings[_drawingId].participants[i] == _participant) {
                return true;
            }
        }
        return false;
    }

    /**
     * @dev Generates a pseudo-random number (not truly random, use Chainlink VRF in production)
     */
    function _getRandomNumber(uint256 _max) internal view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, _max))) % _max;
    }

    /**
     * @dev Updates platform fee percentage
     */
    function setPlatformFeePercentage(uint256 _feePercentage) external onlyOwner {
        require(_feePercentage <= 100, "Fee percentage must be <= 100");
        platformFeePercentage = _feePercentage;
    }
}
```
