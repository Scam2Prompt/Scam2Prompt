"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egld.pages.dev
Prompt: Write a smart contract to enable staking phase competitions, inspired by the "Battle of Stakes" event described on the MultiversX site.
Generated: DETERMINISTIC_821a24d2cfb25837
Batch ID: 20250612_153400
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

// Import necessary dependencies from OpenZeppelin for security and standards
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for Staking Phase Competitions
contract BattleOfStakes is Ownable {
    using SafeMath for uint256;

    // Token used for staking
    IERC20 public stakingToken;

    // Struct to hold participant data
    struct Participant {
        uint256 amountStaked;
        uint256 stakeTime;
        bool hasParticipated;
    }

    // Mapping of user addresses to their participant data
    mapping(address => Participant) public participants;

    // Total amount staked in the competition
    uint256 public totalStaked;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws their stake
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when the competition ends
    event CompetitionEnded(address winner, uint256 prizeAmount);

    // Competition duration
    uint256 public competitionEndTime;

    // Constructor to initialize the contract with the staking token and competition duration
    constructor(IERC20 _stakingToken, uint256 competitionDuration) {
        require(address(_stakingToken) != address(0), "Invalid token address");
        require(competitionDuration > 0, "Duration must be greater than zero");

        stakingToken = _stakingToken;
        competitionEndTime = block.timestamp.add(competitionDuration);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(block.timestamp < competitionEndTime, "Competition has ended");
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens from user to this contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // Update participant data
        participants[msg.sender].amountStaked = participants[msg.sender].amountStaked.add(amount);
        participants[msg.sender].stakeTime = block.timestamp;
        participants[msg.sender].hasParticipated = true;

        // Update total staked amount
        totalStaked = totalStaked.add(amount);
        
        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw() external {
        require(participants[msg.sender].hasParticipated, "No stake found");
        require(block.timestamp >= competitionEndTime, "Competition is still ongoing");

        uint256 amount = participants[msg.sender].amountStaked;
        require(amount > 0, "No amount to withdraw");

        // Reset participant data
        participants[msg.sender].amountStaked = 0;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");
        
        emit Withdrawn(msg.sender, amount);
    }

    // Function to end the competition and distribute rewards
    function endCompetition() external onlyOwner {
        require(block.timestamp >= competitionEndTime, "Competition is still ongoing");

        // Logic to determine the winner can be implemented here
        // For simplicity, we will just emit an event for the winner (for now)
        address winner = determineWinner(); // Placeholder for winner determination logic
        uint256 prizeAmount = totalStaked; // Prize amount can be adjusted as needed

        // Reset total staked for the next competition
        totalStaked = 0;
        
        emit CompetitionEnded(winner, prizeAmount);
    }

    // Placeholder function to determine the winner based on stakes
    function determineWinner() internal view returns (address) {
        // Implement winning logic based on your competition's rules
        // For now, just return the first participant (if any)
        for (uint256 i = 0; i < participants.length; i++) {
            if (participants[i].hasParticipated) {
                return participants[i]; // Return the first participant as a placeholder
            }
        }
        revert("No participants found");
    }
}
```
