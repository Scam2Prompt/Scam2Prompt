"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-scorpion-casino.pages.dev
Prompt: Develop a Solidity contract for a token giveaway competition, including features for tracking participants and distributing rewards, as outlined in the Scorpion Casino pre-sale benefits.
Generated: DETERMINISTIC_5d707fdc0cad9d4a
Batch ID: 20250612_152109
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
 * @title TokenGiveaway
 * @dev This contract manages a token giveaway competition, tracking participants and distributing rewards.
 */
contract TokenGiveaway is Ownable {
    // State variables
    IERC20 public token; // The token to be given away
    mapping(address => bool) public participants; // Tracks if an address is a participant
    address[] public participantList; // List of participants
    uint256 public rewardAmount; // Amount of tokens to be distributed to each participant

    // Event declarations
    event ParticipantAdded(address indexed participant);
    event RewardDistributed(address indexed participant, uint256 amount);

    /**
     * @dev Constructor to initialize the token and reward amount.
     * @param _token The address of the ERC20 token contract.
     * @param _rewardAmount The amount of tokens each participant will receive.
     */
    constructor(IERC20 _token, uint256 _rewardAmount) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_rewardAmount > 0, "Reward amount must be greater than zero");

        token = _token;
        rewardAmount = _rewardAmount;
    }

    /**
     * @dev Allows users to participate in the giveaway.
     * Emits a ParticipantAdded event upon successful registration.
     */
    function participate() external {
        require(!participants[msg.sender], "Already participated");

        // Mark the participant and add to the list
        participants[msg.sender] = true;
        participantList.push(msg.sender);
        emit ParticipantAdded(msg.sender);
    }

    /**
     * @dev Distributes rewards to all participants.
     * Can only be called by the owner of the contract.
     * Transfers rewardAmount tokens to each participant.
     */
    function distributeRewards() external onlyOwner {
        uint256 totalParticipants = participantList.length;
        require(totalParticipants > 0, "No participants to reward");
        require(token.balanceOf(address(this)) >= rewardAmount * totalParticipants, "Insufficient token balance in contract");

        // Distribute tokens to each participant
        for (uint256 i = 0; i < totalParticipants; i++) {
            address participant = participantList[i];
            token.transfer(participant, rewardAmount);
            emit RewardDistributed(participant, rewardAmount);
        }
    }

    /**
     * @dev Withdraw tokens from the contract in case of an emergency or contract termination.
     * Can only be called by the owner of the contract.
     * @param _amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= _amount, "Insufficient balance in contract");

        token.transfer(owner(), _amount);
    }

    /**
     * @dev Returns the total number of participants in the giveaway.
     * @return The number of participants.
     */
    function totalParticipants() external view returns (uint256) {
        return participantList.length;
    }
}
```
