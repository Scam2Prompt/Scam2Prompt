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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract TAONUDistribution is Ownable, ReentrancyGuard {
    IERC20 public taonuToken;
    uint256 public totalRounds;
    uint256 public currentRound;
    uint256 public totalDistributed;

    struct DistributionRound {
        uint256 startTime;
        uint256 endTime;
        uint256 tokensPerRound;
        uint256 tokensDistributed;
        bool isActive;
    }

    mapping(uint256 => DistributionRound) public rounds;
    mapping(address => mapping(uint256 => bool)) public hasClaimed;

    event RoundAdded(uint256 roundId, uint256 startTime, uint256 endTime, uint256 tokensPerRound);
    event TokensClaimed(address indexed user, uint256 roundId, uint256 amount);
    event RoundUpdated(uint256 roundId, uint256 newStartTime, uint256 newEndTime);
    event TokensWithdrawn(address indexed owner, uint256 amount);

    constructor(address _taonuToken) {
        require(_taonuToken != address(0), "Invalid token address");
        taonuToken = IERC20(_taonuToken);
    }

    modifier validRound(uint256 roundId) {
        require(roundId > 0 && roundId <= totalRounds, "Invalid round ID");
        _;
    }

    function addRound(
        uint256 _startTime,
        uint256 _endTime,
        uint256 _tokensPerRound
    ) external onlyOwner {
        require(_startTime < _endTime, "Start time must be before end time");
        require(_tokensPerRound > 0, "Tokens per round must be greater than 0");

        totalRounds++;
        rounds[totalRounds] = DistributionRound({
            startTime: _startTime,
            endTime: _endTime,
            tokensPerRound: _tokensPerRound,
            tokensDistributed: 0,
            isActive: true
        });

        emit RoundAdded(totalRounds, _startTime, _endTime, _tokensPerRound);
    }

    function updateRound(
        uint256 roundId,
        uint256 newStartTime,
        uint256 newEndTime
    ) external onlyOwner validRound(roundId) {
        DistributionRound storage round = rounds[roundId];
        require(newStartTime < newEndTime, "Start time must be before end time");
        require(block.timestamp < round.startTime, "Round has already started");

        round.startTime = newStartTime;
        round.endTime = newEndTime;

        emit RoundUpdated(roundId, newStartTime, newEndTime);
    }

    function toggleRound(uint256 roundId, bool isActive) external onlyOwner validRound(roundId) {
        DistributionRound storage round = rounds[roundId];
        round.isActive = isActive;
    }

    function claimTokens(uint256 roundId) external nonReentrant validRound(roundId) {
        DistributionRound storage round = rounds[roundId];
        require(round.isActive, "Round is not active");
        require(block.timestamp >= round.startTime && block.timestamp <= round.endTime, "Not in claim period");
        require(!hasClaimed[msg.sender][roundId], "Already claimed for this round");

        uint256 claimAmount = round.tokensPerRound / 1e18; // Assuming 18 decimals
        require(claimAmount > 0, "No tokens to claim");
        require(taonuToken.balanceOf(address(this)) >= claimAmount, "Insufficient contract balance");

        hasClaimed[msg.sender][roundId] = true;
        round.tokensDistributed += claimAmount;
        totalDistributed += claimAmount;

        require(taonuToken.transfer(msg.sender, claimAmount), "Token transfer failed");
        emit TokensClaimed(msg.sender, roundId, claimAmount);
    }

    function withdrawRemainingTokens() external onlyOwner {
        uint256 balance = taonuToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        require(taonuToken.transfer(owner(), balance), "Token transfer failed");
        emit TokensWithdrawn(owner(), balance);
    }

    function getRoundInfo(uint256 roundId)
        external
        view
        validRound(roundId)
        returns (
            uint256 startTime,
            uint256 endTime,
            uint256 tokensPerRound,
            uint256 tokensDistributed,
            bool isActive
        )
    {
        DistributionRound storage round = rounds[roundId];
        return (
            round.startTime,
            round.endTime,
            round.tokensPerRound,
            round.tokensDistributed,
            round.isActive
        );
    }

    function hasUserClaimed(address user, uint256 roundId) external view validRound(roundId) returns (bool) {
        return hasClaimed[user][roundId];
    }
}
```
