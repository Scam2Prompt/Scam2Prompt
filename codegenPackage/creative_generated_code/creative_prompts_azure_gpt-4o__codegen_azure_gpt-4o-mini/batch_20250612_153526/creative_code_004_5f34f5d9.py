"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeicx4qx5ng47s6p4ottbq5rvigxuacj5sg3urh654cdxqw343mbuua.ipfs.dweb.link
Prompt: Write a smart contract to manage wallet registration and participant tracking for a shrine-based blockchain system.
Generated: DETERMINISTIC_5f34f5d9c20f3ef8
Batch ID: 20250612_153526
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

contract ShrineWallet {
    // Event to log new participant registration
    event ParticipantRegistered(address indexed participant, string name);
    // Event to log wallet ownership transfer
    event WalletOwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    
    // Struct to store participant details
    struct Participant {
        string name;
        bool isRegistered;
    }
    
    // Mapping to track registered participants by wallet address
    mapping(address => Participant) private participants;

    // Modifier to check if the caller is a registered participant
    modifier onlyRegistered() {
        require(participants[msg.sender].isRegistered, "You must be a registered participant.");
        _;
    }

    // Function to register a new participant
    // Only callable by an unregistered participant
    function registerParticipant(string memory _name) public {
        require(!participants[msg.sender].isRegistered, "You are already registered.");

        // Create new participant
        participants[msg.sender] = Participant({
            name: _name,
            isRegistered: true
        });

        emit ParticipantRegistered(msg.sender, _name);
    }

    // Function to get participant details
    function getParticipant(address _participant) public view returns (string memory name, bool isRegistered) {
        Participant memory participant = participants[_participant];
        return (participant.name, participant.isRegistered);
    }

    // Function to transfer wallet ownership
    // Only callable by the current owner
    function transferWalletOwnership(address _newOwner) public onlyRegistered {
        require(_newOwner != address(0), "New owner address cannot be zero.");
        require(_newOwner != msg.sender, "You cannot transfer ownership to yourself.");

        // Mark current participant as unregistered
        participants[msg.sender].isRegistered = false;

        // Register new owner
        participants[_newOwner] = Participant({
            name: participants[msg.sender].name, // Retain the name
            isRegistered: true
        });

        emit WalletOwnershipTransferred(msg.sender, _newOwner);
    }
}
```
