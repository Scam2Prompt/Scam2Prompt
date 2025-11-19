"""
Generated Code Metadata:
========================
Original URL: https://taonutpad.pages.dev
Prompt: Write a smart contract to facilitate the distribution of TAO Inu ($TAONU) tokens in multiple rounds, adhering to the rules specified on TrustPad.
Generated: DETERMINISTIC_ee0512e86fde25cb
Batch ID: 20250612_152422
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title TAOInuTokenDistribution
 * @author [Your Name]
 * @notice Smart contract for distributing TAO Inu ($TAONU) tokens in multiple rounds.
 */
contract TAOInuTokenDistribution is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of round IDs to their respective details
    mapping(uint256 => Round) public rounds;

    // Mapping of user addresses to their claimed token amounts
    mapping(address => mapping(uint256 => uint256)) public userClaims;

    // TAO Inu token instance
    ERC20 public token;

    // Total number of rounds
    uint256 public totalRounds;

    // Current round ID
    uint256 public currentRoundId;

    /**
     * @notice Event emitted when a new round is created
     * @param roundId ID of the newly created round
     * @param startTime Start time of the round
     * @param endTime End time of the round
     * @param tokensPerRound Tokens available for the round
     */
    event NewRound(uint256 indexed roundId, uint256 startTime, uint256 endTime, uint256 tokensPerRound);

    /**
     * @notice Event emitted when a user claims tokens in a round
     * @param user Address of the user claiming tokens
     * @param roundId ID of the round
     * @param amount Tokens claimed by the user
     */
    event TokensClaimed(address indexed user, uint256 indexed roundId, uint256 amount);

    /**
     * @notice Struct representing a round
     * @param startTime Start time of the round
     * @param endTime End time of the round
     * @param tokensPerRound Tokens available for the round
     * @param tokensClaimed Tokens claimed so far in the round
     */
    struct Round {
        uint256 startTime;
        uint256 endTime;
        uint256 tokensPerRound;
        uint256 tokensClaimed;
    }

    /**
     * @notice Constructor
     * @param _tokenAddress Address of the TAO Inu token
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = ERC20(_tokenAddress);
    }

    /**
     * @notice Create a new round
     * @param _startTime Start time of the round
     * @param _endTime End time of the round
     * @param _tokensPerRound Tokens available for the round
     */
    function createRound(uint256 _startTime, uint256 _endTime, uint256 _tokensPerRound) public {
        require(_startTime > block.timestamp, "Start time must be in the future");
        require(_endTime > _startTime, "End time must be after start time");
        require(_tokensPerRound > 0, "Tokens per round must be greater than 0");

        totalRounds++;
        currentRoundId = totalRounds;

        rounds[currentRoundId] = Round({
            startTime: _startTime,
            endTime: _endTime,
            tokensPerRound: _tokensPerRound,
            tokensClaimed: 0
        });

        emit NewRound(currentRoundId, _startTime, _endTime, _tokensPerRound);
    }

    /**
     * @notice Claim tokens in a round
     * @param _roundId ID of the round
     * @param _amount Tokens to claim
     */
    function claimTokens(uint256 _roundId, uint256 _amount) public nonReentrant {
        require(_roundId > 0 && _roundId <= totalRounds, "Invalid round ID");
        require(rounds[_roundId].startTime <= block.timestamp && block.timestamp <= rounds[_roundId].endTime, "Round not active");
        require(_amount > 0, "Claim amount must be greater than 0");
        require(token.balanceOf(address(this)) >= _amount, "Insufficient tokens in contract");

        uint256 userClaimed = userClaims[msg.sender][_roundId];
        uint256 remainingTokens = rounds[_roundId].tokensPerRound.sub(rounds[_roundId].tokensClaimed);
        uint256 claimAmount = _amount > remainingTokens ? remainingTokens : _amount;

        require(claimAmount > 0, "Nothing to claim");

        userClaims[msg.sender][_roundId] = userClaimed.add(claimAmount);
        rounds[_roundId].tokensClaimed = rounds[_roundId].tokensClaimed.add(claimAmount);

        token.transfer(msg.sender, claimAmount);

        emit TokensClaimed(msg.sender, _roundId, claimAmount);
    }

    /**
     * @notice Get the number of tokens claimable by a user in a round
     * @param _user Address of the user
     * @param _roundId ID of the round
     * @return claimable tokens
     */
    function getClaimableTokens(address _user, uint256 _roundId) public view returns (uint256) {
        uint256 userClaimed = userClaims[_user][_roundId];
        uint256 remainingTokens = rounds[_roundId].tokensPerRound.sub(rounds[_roundId].tokensClaimed);

        return remainingTokens > 0 ? remainingTokens : 0;
    }
}
```
