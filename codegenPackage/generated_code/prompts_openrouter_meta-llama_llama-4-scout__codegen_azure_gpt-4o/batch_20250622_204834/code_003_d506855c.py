"""
Generated Code Metadata:
========================
Original URL: https://agora-next-guh1xmcsb-voteagora.vercel.app
Prompt: What is the quorum requirement for Optimism Agora proposals, and how can it be implemented in a smart contract?
Generated: DETERMINISTIC_d506855cc75e2e3c
Batch ID: 20250622_204834
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
 * @title OptimismAgoraQuorum
 * @dev A smart contract to determine quorum requirements for Optimism Agora proposals.
 * Quorum is calculated as a percentage of total voting power.
 */
contract OptimismAgoraQuorum {
    // State variables
    uint256 public totalVotingPower; // Total voting power in the system
    uint256 public quorumPercentage; // Quorum percentage required (e.g., 20 for 20%)

    // Events
    event QuorumUpdated(uint256 oldQuorumPercentage, uint256 newQuorumPercentage);
    event TotalVotingPowerUpdated(uint256 oldTotalVotingPower, uint256 newTotalVotingPower);

    /**
     * @dev Constructor to initialize the contract with total voting power and quorum percentage.
     * @param _totalVotingPower Initial total voting power in the system.
     * @param _quorumPercentage Initial quorum percentage required.
     */
    constructor(uint256 _totalVotingPower, uint256 _quorumPercentage) {
        require(_quorumPercentage > 0 && _quorumPercentage <= 100, "Invalid quorum percentage");
        totalVotingPower = _totalVotingPower;
        quorumPercentage = _quorumPercentage;
    }

    /**
     * @dev Function to update the quorum percentage.
     * @param _newQuorumPercentage New quorum percentage to be set.
     */
    function updateQuorumPercentage(uint256 _newQuorumPercentage) external {
        require(_newQuorumPercentage > 0 && _newQuorumPercentage <= 100, "Invalid quorum percentage");
        uint256 oldQuorumPercentage = quorumPercentage;
        quorumPercentage = _newQuorumPercentage;
        emit QuorumUpdated(oldQuorumPercentage, _newQuorumPercentage);
    }

    /**
     * @dev Function to update the total voting power.
     * @param _newTotalVotingPower New total voting power to be set.
     */
    function updateTotalVotingPower(uint256 _newTotalVotingPower) external {
        require(_newTotalVotingPower > 0, "Total voting power must be greater than zero");
        uint256 oldTotalVotingPower = totalVotingPower;
        totalVotingPower = _newTotalVotingPower;
        emit TotalVotingPowerUpdated(oldTotalVotingPower, _newTotalVotingPower);
    }

    /**
     * @dev Function to calculate the quorum requirement for a proposal.
     * @return The quorum requirement in terms of voting power.
     */
    function getQuorumRequirement() public view returns (uint256) {
        return (totalVotingPower * quorumPercentage) / 100;
    }

    /**
     * @dev Function to check if a proposal meets the quorum requirement.
     * @param votesReceived The number of votes received for the proposal.
     * @return True if the proposal meets the quorum requirement, false otherwise.
     */
    function isQuorumMet(uint256 votesReceived) public view returns (bool) {
        return votesReceived >= getQuorumRequirement();
    }
}
```
