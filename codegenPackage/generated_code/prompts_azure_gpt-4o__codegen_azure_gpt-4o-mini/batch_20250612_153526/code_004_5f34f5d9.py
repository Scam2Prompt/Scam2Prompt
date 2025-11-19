"""
Generated Code Metadata:
========================
Original URL: https://bafybeicx4qx5ng47s6p4ottbq5rvigxuacj5sg3urh654cdxqw343mbuua.ipfs.dweb.link
Prompt: Write a smart contract to manage wallet registration and participant tracking for a shrine-based blockchain system.
Generated: DETERMINISTIC_5f34f5d9c20f3ef8
Batch ID: 20250612_153526
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

contract ShrineWalletManager {
    // Struct to hold participant information
    struct Participant {
        address walletAddress; // Wallet address of the participant
        string name;          // Name of the participant
        bool isRegistered;    // Registration status
    }

    // Mapping to store participants by their wallet address
    mapping(address => Participant) private participants;

    // Event emitted when a participant is registered
    event ParticipantRegistered(address indexed walletAddress, string name);

    // Event emitted when a participant is unregistered
    event ParticipantUnregistered(address indexed walletAddress);

    // Modifier to check if the caller is already registered
    modifier onlyRegistered() {
        require(participants[msg.sender].isRegistered, "You are not registered.");
        _;
    }

    // Modifier to check if the caller is not registered
    modifier onlyNotRegistered() {
        require(!participants[msg.sender].isRegistered, "You are already registered.");
        _;
    }

    // Function to register a new participant
    function registerParticipant(string memory _name) public onlyNotRegistered {
        // Ensure the name is not empty
        require(bytes(_name).length > 0, "Name cannot be empty.");

        // Create a new participant and store it in the mapping
        participants[msg.sender] = Participant({
            walletAddress: msg.sender,
            name: _name,
            isRegistered: true
        });

        // Emit the registration event
        emit ParticipantRegistered(msg.sender, _name);
    }

    // Function to unregister a participant
    function unregisterParticipant() public onlyRegistered {
        // Remove the participant from the mapping
        delete participants[msg.sender];

        // Emit the unregistration event
        emit ParticipantUnregistered(msg.sender);
    }

    // Function to get participant details
    function getParticipant(address _walletAddress) public view returns (string memory name, bool isRegistered) {
        // Check if the participant exists
        require(participants[_walletAddress].isRegistered, "Participant not found.");

        // Return the participant's details
        Participant memory participant = participants[_walletAddress];
        return (participant.name, participant.isRegistered);
    }

    // Function to check if a wallet is registered
    function isParticipantRegistered(address _walletAddress) public view returns (bool) {
        return participants[_walletAddress].isRegistered;
    }
}
```
