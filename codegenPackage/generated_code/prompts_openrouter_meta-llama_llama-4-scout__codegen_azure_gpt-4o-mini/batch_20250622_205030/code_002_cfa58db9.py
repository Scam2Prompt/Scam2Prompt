"""
Generated Code Metadata:
========================
Original URL: https://tesneiro-5281.vercel.app
Prompt: Generate a code snippet in Solidity to create a simple airdrop contract similar to Neiro's 10,000,000 token giveaway, with a limited number of participants.
Generated: DETERMINISTIC_cfa58db955d7bf81
Batch ID: 20250622_205030
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Airdrop contract for distributing tokens to a limited number of participants
contract Airdrop is Ownable {
    // Token to be distributed
    IERC20 public token;

    // Maximum number of participants allowed
    uint256 public maxParticipants;

    // Mapping to track participants
    mapping(address => bool) public hasClaimed;

    // Event to log successful claims
    event TokensClaimed(address indexed participant, uint256 amount);

    // Constructor to initialize the token and max participants
    constructor(IERC20 _token, uint256 _maxParticipants) {
        token = _token;
        maxParticipants = _maxParticipants;
    }

    // Function to claim tokens
    function claimTokens(uint256 amount) external {
        // Check if the participant has already claimed
        require(!hasClaimed[msg.sender], "You have already claimed tokens.");
        
        // Check if the maximum number of participants has been reached
        require(getParticipantCount() < maxParticipants, "Maximum participants reached.");

        // Transfer tokens to the participant
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance.");
        hasClaimed[msg.sender] = true;
        token.transfer(msg.sender, amount);

        // Emit event for successful claim
        emit TokensClaimed(msg.sender, amount);
    }

    // Function to get the current number of participants who have claimed
    function getParticipantCount() public view returns (uint256 count) {
        for (uint256 i = 0; i < maxParticipants; i++) {
            if (hasClaimed[address(i)]) {
                count++;
            }
        }
    }

    // Function for the owner to withdraw remaining tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance.");
        token.transfer(msg.sender, amount);
    }
}
```
