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

/**
 * @title SportsFanEngagement
 * @dev A simple smart contract for fan engagement and athlete sponsorship.
 * Fans can support athletes by sending funds, and athletes can withdraw their sponsorship funds.
 */
contract SportsFanEngagement {
    // Struct to represent an athlete
    struct Athlete {
        string name;
        address payable wallet;
        uint256 totalSupport;
    }

    // Mapping to store athletes by their unique ID
    mapping(uint256 => Athlete) public athletes;

    // Event emitted when a fan supports an athlete
    event SupportReceived(uint256 athleteId, address indexed fan, uint256 amount);

    // Event emitted when an athlete withdraws their funds
    event FundsWithdrawn(uint256 athleteId, uint256 amount);

    // Counter for athlete IDs
    uint256 private athleteCounter;

    /**
     * @dev Register a new athlete.
     * @param _name The name of the athlete.
     * @param _wallet The wallet address of the athlete.
     * @return The ID of the newly registered athlete.
     */
    function registerAthlete(string memory _name, address payable _wallet) external returns (uint256) {
        require(_wallet != address(0), "Invalid wallet address");

        athleteCounter++;
        athletes[athleteCounter] = Athlete({
            name: _name,
            wallet: _wallet,
            totalSupport: 0
        });

        return athleteCounter;
    }

    /**
     * @dev Support an athlete by sending funds.
     * @param _athleteId The ID of the athlete to support.
     */
    function supportAthlete(uint256 _athleteId) external payable {
        require(msg.value > 0, "Support amount must be greater than zero");
        require(athletes[_athleteId].wallet != address(0), "Athlete does not exist");

        // Update the athlete's total support
        athletes[_athleteId].totalSupport += msg.value;

        // Emit the support event
        emit SupportReceived(_athleteId, msg.sender, msg.value);
    }

    /**
     * @dev Allow an athlete to withdraw their sponsorship funds.
     * @param _athleteId The ID of the athlete withdrawing funds.
     */
    function withdrawFunds(uint256 _athleteId) external {
        Athlete storage athlete = athletes[_athleteId];
        require(msg.sender == athlete.wallet, "Only the athlete can withdraw funds");
        require(athlete.totalSupport > 0, "No funds available for withdrawal");

        uint256 amount = athlete.totalSupport;
        athlete.totalSupport = 0;

        // Transfer the funds to the athlete's wallet
        athlete.wallet.transfer(amount);

        // Emit the withdrawal event
        emit FundsWithdrawn(_athleteId, amount);
    }

    /**
     * @dev Get details of an athlete.
     * @param _athleteId The ID of the athlete.
     * @return The name, wallet address, and total support of the athlete.
     */
    function getAthleteDetails(uint256 _athleteId) external view returns (string memory, address, uint256) {
        Athlete memory athlete = athletes[_athleteId];
        require(athlete.wallet != address(0), "Athlete does not exist");

        return (athlete.name, athlete.wallet, athlete.totalSupport);
    }
}
```
