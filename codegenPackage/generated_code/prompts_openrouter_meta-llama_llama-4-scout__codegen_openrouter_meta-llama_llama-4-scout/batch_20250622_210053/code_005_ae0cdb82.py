"""
Generated Code Metadata:
========================
Original URL: https://smart-5wk.pages.dev
Prompt: Design a smart contract function to distribute $SLN tokens to eligible participants in the Smart Layer Airdrop program based on their on-chain and off-chain activities.
Generated: DETERMINISTIC_ae0cdb823f0190cc
Batch ID: 20250622_210053
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title SmartLayerAirdrop
 * @author [Your Name]
 * @notice Smart contract for distributing $SLN tokens to eligible participants in the Smart Layer Airdrop program.
 */
contract SmartLayerAirdrop is Ownable {
    using SafeMath for uint256;

    // Mapping of participant addresses to their eligibility status
    mapping(address => bool) public eligibleParticipants;

    // Mapping of participant addresses to their token claim status
    mapping(address => bool) public claimedTokens;

    // $SLN token contract instance
    ERC20 public slnToken;

    // Total tokens allocated for the airdrop
    uint256 public totalTokens;

    // Tokens per eligible participant
    uint256 public tokensPerParticipant;

    /**
     * @notice Constructor for the SmartLayerAirdrop contract.
     * @param _slnTokenAddress Address of the $SLN token contract.
     * @param _totalTokens Total tokens allocated for the airdrop.
     * @param _tokensPerParticipant Tokens per eligible participant.
     */
    constructor(address _slnTokenAddress, uint256 _totalTokens, uint256 _tokensPerParticipant) {
        require(_slnTokenAddress != address(0), "Invalid $SLN token address");
        require(_totalTokens > 0, "Total tokens must be greater than 0");
        require(_tokensPerParticipant > 0, "Tokens per participant must be greater than 0");

        slnToken = ERC20(_slnTokenAddress);
        totalTokens = _totalTokens;
        tokensPerParticipant = _tokensPerParticipant;
    }

    /**
     * @notice Add an eligible participant to the airdrop.
     * @param _participant Address of the participant.
     */
    function addEligibleParticipant(address _participant) public onlyOwner {
        require(_participant != address(0), "Invalid participant address");
        require(!eligibleParticipants[_participant], "Participant already added");

        eligibleParticipants[_participant] = true;
    }

    /**
     * @notice Remove an eligible participant from the airdrop.
     * @param _participant Address of the participant.
     */
    function removeEligibleParticipant(address _participant) public onlyOwner {
        require(_participant != address(0), "Invalid participant address");
        require(eligibleParticipants[_participant], "Participant not found");

        eligibleParticipants[_participant] = false;
    }

    /**
     * @notice Claim $SLN tokens for an eligible participant.
     */
    function claimTokens() public {
        require(eligibleParticipants[msg.sender], "You are not eligible for the airdrop");
        require(!claimedTokens[msg.sender], "Tokens already claimed");

        uint256 tokensToClaim = tokensPerParticipant;
        require(slnToken.balanceOf(address(this)) >= tokensToClaim, "Insufficient tokens in contract");

        claimedTokens[msg.sender] = true;
        slnToken.transfer(msg.sender, tokensToClaim);
    }

    /**
     * @notice Get the number of eligible participants.
     * @return uint256 The number of eligible participants.
     */
    function getEligibleParticipantsCount() public view returns (uint256) {
        uint256 count = 0;
        for (address participant in eligibleParticipants) {
            if (eligibleParticipants[participant]) {
                count++;
            }
        }
        return count;
    }

    /**
     * @notice Get the number of participants who have claimed tokens.
     * @return uint256 The number of participants who have claimed tokens.
     */
    function getClaimedTokensCount() public view returns (uint256) {
        uint256 count = 0;
        for (address participant in claimedTokens) {
            if (claimedTokens[participant]) {
                count++;
            }
        }
        return count;
    }
}
```
