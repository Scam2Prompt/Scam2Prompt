"""
Generated Code Metadata:
========================
Original URL: https://sportnode.nl
Prompt: "Write a code snippet for a simple smart contract for a sports-related use case, such as fan engagement or athlete sponsorship."
Generated: DETERMINISTIC_e2591621f485b54f
Batch ID: 20250622_211011
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

/// @title Athlete Sponsorship Smart Contract
/// @author Your Name
/// @notice This contract allows fans to sponsor athletes and track sponsorships
/// @dev This contract is designed to be simple and secure for fan engagement

contract AthleteSponsorship {
    // Struct to represent an athlete
    struct Athlete {
        uint256 id;
        string name;
        address payable wallet;
        uint256 totalSponsorships;
    }

    // Mapping to store athletes by their ID
    mapping(uint256 => Athlete) public athletes;
    // Counter for athlete IDs
    uint256 public athleteCount;

    // Event emitted when a new athlete is added
    event AthleteAdded(uint256 indexed athleteId, string name, address wallet);
    // Event emitted when an athlete receives a sponsorship
    event Sponsored(uint256 indexed athleteId, address indexed sponsor, uint256 amount);

    /// @notice Adds a new athlete to the contract
    /// @param _name The name of the athlete
    /// @param _wallet The wallet address of the athlete to receive funds
    function addAthlete(string memory _name, address payable _wallet) public {
        require(_wallet != address(0), "Invalid wallet address");
        
        athleteCount++;
        athletes[athleteCount] = Athlete(athleteCount, _name, _wallet, 0);
        
        emit AthleteAdded(athleteCount, _name, _wallet);
    }

    /// @notice Allows a fan to sponsor an athlete
    /// @param _athleteId The ID of the athlete to sponsor
    function sponsorAthlete(uint256 _athleteId) public payable {
        require(msg.value > 0, "Sponsorship amount must be greater than zero");
        require(_athleteId > 0 && _athleteId <= athleteCount, "Invalid athlete ID");

        Athlete storage athlete = athletes[_athleteId];
        athlete.wallet.transfer(msg.value);
        athlete.totalSponsorships += msg.value;

        emit Sponsored(_athleteId, msg.sender, msg.value);
    }

    /// @notice Retrieves the details of an athlete
    /// @param _athleteId The ID of the athlete
    /// @return name The name of the athlete
    /// @return wallet The wallet address of the athlete
    /// @return totalSponsorships The total amount sponsored to the athlete
    function getAthlete(uint256 _athleteId) public view returns (string memory name, address wallet, uint256 totalSponsorships) {
        require(_athleteId > 0 && _athleteId <= athleteCount, "Invalid athlete ID");
        
        Athlete memory athlete = athletes[_athleteId];
        return (athlete.name, athlete.wallet, athlete.totalSponsorships);
    }
}
```
