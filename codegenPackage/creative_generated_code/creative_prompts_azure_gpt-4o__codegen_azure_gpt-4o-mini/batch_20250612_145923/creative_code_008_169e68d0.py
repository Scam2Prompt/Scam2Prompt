"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-claim.pages.dev
Prompt: Generate code for an airdrop system that distributes tokens to presale participants at the conclusion of the presale, ensuring no fees are required for claiming tokens.
Generated: DETERMINISTIC_169e68d0c3e666aa
Batch ID: 20250612_145923
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract Airdrop {
    using SafeMath for uint256;

    // Token contract address
    IERC20 public token;

    // Presale participant structure
    struct Participant {
        uint256 amount; // Amount of tokens allocated
        bool claimed; // Claim status
    }

    // Mapping of participants
    mapping(address => Participant) public participants;

    // Total tokens to be distributed
    uint256 public totalTokens;
    
    // Event for successful token claim
    event TokensClaimed(address indexed participant, uint256 amount);

    // Constructor to initialize the token address
    constructor(address _tokenAddress, uint256 _totalTokens) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_totalTokens > 0, "Total tokens must be greater than zero");

        token = IERC20(_tokenAddress);
        totalTokens = _totalTokens;
    }

    // Function to add participant to the presale
    function addParticipant(address _participant, uint256 _amount) external {
        require(_participant != address(0), "Invalid participant address");
        require(_amount > 0, "Amount must be greater than zero");
        require(participants[_participant].amount == 0, "Participant already added");

        participants[_participant] = Participant({
            amount: _amount,
            claimed: false
        });
    }

    // Function to claim tokens after presale
    function claimTokens() external {
        Participant storage participant = participants[msg.sender];

        // Verify that the participant exists and has not claimed their tokens
        require(participant.amount > 0, "No tokens allocated");
        require(!participant.claimed, "Tokens already claimed");

        // Update claim status
        participant.claimed = true;

        // Transfer tokens
        require(token.balanceOf(address(this)) >= participant.amount, "Insufficient contract token balance");
        token.transfer(msg.sender, participant.amount);

        // Emit event for successful claim
        emit TokensClaimed(msg.sender, participant.amount);
    }

    // Function to withdraw tokens in case of emergency
    function withdrawTokens(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= _amount, "Insufficient contract token balance");

        // Transfer tokens to the contract owner (or a designated address)
        token.transfer(msg.sender, _amount);
    }
}
```
