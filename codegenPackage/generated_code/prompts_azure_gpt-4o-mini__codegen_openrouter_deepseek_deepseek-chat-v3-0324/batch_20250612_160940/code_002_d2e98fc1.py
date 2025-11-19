"""
Generated Code Metadata:
========================
Original URL: https://bonk-net.pages.dev
Prompt: Create a Solidity smart contract that mimics the BONKMILLON airdrop mechanism, ensuring a first-come, first-served distribution of tokens.
Generated: DETERMINISTIC_d2e98fc129bb722a
Batch ID: 20250612_160940
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

/**
 * @title BONKMILLONAirdrop
 * @dev A smart contract for first-come, first-served token airdrops with anti-sybil measures
 */
contract BONKMILLONAirdrop is Ownable, ReentrancyGuard {
    IERC20 public token;
    uint256 public airdropAmount;
    uint256 public maxParticipants;
    uint256 public participantCount;
    uint256 public startTime;
    uint256 public endTime;
    bool public isAirdropActive;

    mapping(address => bool) public hasParticipated;

    event AirdropClaimed(address indexed participant, uint256 amount);
    event AirdropStarted(uint256 startTime, uint256 endTime);
    event AirdropEnded(uint256 endTime);
    event TokensWithdrawn(address indexed owner, uint256 amount);

    /**
     * @dev Constructor initializes the airdrop contract
     * @param _token Address of the ERC20 token to be airdropped
     * @param _airdropAmount Amount of tokens each participant receives
     * @param _maxParticipants Maximum number of participants allowed
     */
    constructor(
        address _token,
        uint256 _airdropAmount,
        uint256 _maxParticipants
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_airdropAmount > 0, "Airdrop amount must be greater than zero");
        require(_maxParticipants > 0, "Max participants must be greater than zero");

        token = IERC20(_token);
        airdropAmount = _airdropAmount;
        maxParticipants = _maxParticipants;
        isAirdropActive = false;
    }

    /**
     * @dev Start the airdrop with specified duration
     * @param _duration Duration of the airdrop in seconds
     */
    function startAirdrop(uint256 _duration) external onlyOwner {
        require(!isAirdropActive, "Airdrop is already active");
        require(_duration > 0, "Duration must be greater than zero");

        startTime = block.timestamp;
        endTime = startTime + _duration;
        isAirdropActive = true;
        participantCount = 0;

        emit AirdropStarted(startTime, endTime);
    }

    /**
     * @dev End the airdrop manually before scheduled end time
     */
    function endAirdrop() external onlyOwner {
        require(isAirdropActive, "Airdrop is not active");

        isAirdropActive = false;
        endTime = block.timestamp;

        emit AirdropEnded(endTime);
    }

    /**
     * @dev Claim airdrop tokens (first-come, first-served)
     */
    function claimAirdrop() external nonReentrant {
        require(isAirdropActive, "Airdrop is not active");
        require(block.timestamp >= startTime, "Airdrop has not started yet");
        require(block.timestamp <= endTime, "Airdrop has ended");
        require(!hasParticipated[msg.sender], "Address has already participated");
        require(participantCount < maxParticipants, "Airdrop capacity reached");

        uint256 contractBalance = token.balanceOf(address(this));
        require(contractBalance >= airdropAmount, "Insufficient tokens in contract");

        hasParticipated[msg.sender] = true;
        participantCount++;

        bool success = token.transfer(msg.sender, airdropAmount);
        require(success, "Token transfer failed");

        emit AirdropClaimed(msg.sender, airdropAmount);
    }

    /**
     * @dev Withdraw remaining tokens after airdrop ends
     */
    function withdrawRemainingTokens() external onlyOwner {
        require(!isAirdropActive, "Airdrop must be ended first");

        uint256 remainingBalance = token.balanceOf(address(this));
        require(remainingBalance > 0, "No tokens to withdraw");

        bool success = token.transfer(owner(), remainingBalance);
        require(success, "Token transfer failed");

        emit TokensWithdrawn(owner(), remainingBalance);
    }

    /**
     * @dev Check if airdrop is still ongoing
     * @return True if airdrop is active and not expired
     */
    function isAirdropOngoing() external view returns (bool) {
        return isAirdropActive && block.timestamp >= startTime && block.timestamp <= endTime;
    }

    /**
     * @dev Check remaining participant slots
     * @return Number of remaining participant slots
     */
    function remainingSlots() external view returns (uint256) {
        if (maxParticipants > participantCount) {
            return maxParticipants - participantCount;
        }
        return 0;
    }
}
```
