"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerdogs.icu
Prompt: Provide code examples for implementing a referral contest mechanism in Solidity, where winners are determined by the number of active first-level referrals, as described in MinerDog's referral contest.
Generated: DETERMINISTIC_4f27c5624ade175d
Batch ID: 20250612_154111
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

/**
 * @title ReferralContest
 * @dev A contract to manage a referral contest where winners are determined
 *      by the number of active first-level referrals.
 */

contract ReferralContest {
    // Struct to represent a participant
    struct Participant {
        uint256 referralCount; // Number of active first-level referrals
        address referrer;      // Address of the referrer
    }

    // Mapping to store participant data
    mapping(address => Participant) public participants;

    // Mapping to store active referrals
    mapping(address => uint256) public activeReferrals;

    // Event emitted when a new referral is added
    event NewReferral(address indexed referrer, address indexed referral);

    // Event emitted when contest winners are determined
    event ContestWinners(address[] winners);

    // Array to store participants for iteration
    address[] private participantList;

    // Function to add a new referral
    function addReferral(address referrer, address referral) external {
        require(referrer != referral, "Referrer cannot be the same as the referral");
        require(participants[referral].referrer == address(0), "Referral already registered");

        // Register the referral
        participants[referral] = Participant(0, referrer);

        // Increment referral count for the referrer
        participants[referrer].referralCount++;

        // Track active referrals for referrer
        activeReferrals[referrer]++;

        // Add referral to participant list
        participantList.push(referral);

        emit NewReferral(referrer, referral);
    }

    // Function to determine contest winners based on referral count
    function determineWinners() external view returns (address[] memory) {
        // Temporary array to store winners
        address[] memory winners = new address[](participantList.length);
        uint256 maxReferrals = 0;
        uint256 winnerCount = 0;

        // Find the maximum referral count
        for (uint256 i = 0; i < participantList.length; i++) {
            address participant = participantList[i];
            uint256 count = participants[participant].referralCount;
            if (count > maxReferrals) {
                maxReferrals = count;
            }
        }

        // Collect winners with the maximum referral count
        for (uint256 i = 0; i < participantList.length; i++) {
            address participant = participantList[i];
            if (participants[participant].referralCount == maxReferrals) {
                winners[winnerCount] = participant;
                winnerCount++;
            }
        }

        // Resize the winners array to actual count
        assembly {
            mstore(winners, winnerCount)
        }

        return winners;
    }

    // Function to announce contest winners
    function announceWinners() external {
        address[] memory winners = determineWinners();
        emit ContestWinners(winners);
    }

    // Function to get participant data
    function getParticipantData(address participant) external view returns (uint256, address) {
        return (participants[participant].referralCount, participants[participant].referrer);
    }
}
```
