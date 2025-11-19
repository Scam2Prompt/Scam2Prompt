"""
Generated Code Metadata:
========================
Original URL: https://ethberlin.org
Prompt: Suggest tools and frameworks for organizing a blockchain-based hackathon similar to ETHBerlin04, and include example code for managing participant contributions on-chain.
Generated: DETERMINISTIC_65d8741effd92fa9
Batch ID: 20250612_150554
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

/// @title Hackathon Contribution Manager
/// @notice This contract manages participant contributions for a blockchain-based hackathon
contract HackathonContributionManager {
    // Struct to hold participant information
    struct Participant {
        address participantAddress; // Address of the participant
        uint256 contributionAmount;  // Amount contributed by the participant
        bool hasContributed;         // Flag to check if the participant has contributed
    }

    // Mapping to store participant contributions
    mapping(address => Participant) public participants;

    // Event to log contributions
    event ContributionReceived(address indexed participant, uint256 amount);

    /// @notice Allows a participant to contribute to the hackathon
    /// @dev Only allows contributions greater than zero
    /// @param _amount The amount contributed by the participant
    function contribute(uint256 _amount) external payable {
        require(_amount > 0, "Contribution must be greater than zero");
        require(msg.value == _amount, "Sent value must match contribution amount");

        // Check if the participant has already contributed
        if (!participants[msg.sender].hasContributed) {
            participants[msg.sender] = Participant({
                participantAddress: msg.sender,
                contributionAmount: _amount,
                hasContributed: true
            });
        } else {
            // Update the existing contribution amount
            participants[msg.sender].contributionAmount += _amount;
        }

        // Emit the contribution event
        emit ContributionReceived(msg.sender, _amount);
    }

    /// @notice Allows the hackathon organizer to withdraw funds
    /// @dev Only the organizer can call this function
    /// @param _to The address to withdraw funds to
    /// @param _amount The amount to withdraw
    function withdraw(address payable _to, uint256 _amount) external {
        // Only the contract owner should be able to withdraw
        require(msg.sender == address(this), "Only the organizer can withdraw");
        require(address(this).balance >= _amount, "Insufficient balance");

        // Transfer the specified amount to the organizer
        _to.transfer(_amount);
    }

    /// @notice Get the contribution details of a participant
    /// @param _participant The address of the participant
    /// @return The contribution amount and status
    function getParticipantContribution(address _participant) external view returns (uint256, bool) {
        return (participants[_participant].contributionAmount, participants[_participant].hasContributed);
    }
}
```

### Suggested Tools and Frameworks for Organizing a Blockchain-Based Hackathon:
1. **Ethereum**: The primary blockchain platform for deploying smart contracts.
2. **Truffle Suite**: A development environment and asset pipeline for Ethereum.
3. **Hardhat**: A development environment to compile, deploy, test, and debug Ethereum software.
4. **IPFS**: For decentralized storage of hackathon projects and submissions.
5. **MetaMask**: A browser extension for managing Ethereum wallets and interacting with dApps.
6. **Discord**: For community engagement and communication during the hackathon.
7. **GitHub**: For version control and collaboration on project code.
8. **DApp Frameworks**: Such as React.js or Vue.js for building the frontend of the hackathon applications.
