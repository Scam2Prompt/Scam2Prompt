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
pragma solidity ^0.8.17;

/**
 * @title ShrineWalletRegistry
 * @dev A smart contract to manage wallet registration and participant tracking for a shrine-based blockchain system.
 */
contract ShrineWalletRegistry {
    // Event emitted when a wallet is successfully registered.
    event WalletRegistered(address indexed wallet, string participantName);

    // Event emitted when a participant is updated.
    event ParticipantUpdated(address indexed wallet, string oldName, string newName);

    // Struct to store participant information.
    struct Participant {
        string name;  // Name of the participant
        bool isRegistered;  // Registration status
    }

    // Mapping to track wallet addresses to participant details.
    mapping(address => Participant) private participants;

    // Address of the contract owner.
    address public owner;

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to register a new wallet and participant in the shrine system.
     * @param participantName Name of the participant to register.
     */
    function registerWallet(string memory participantName) external {
        require(!participants[msg.sender].isRegistered, "Wallet is already registered");
        require(bytes(participantName).length > 0, "Participant name cannot be empty");

        participants[msg.sender] = Participant({
            name: participantName,
            isRegistered: true
        });

        emit WalletRegistered(msg.sender, participantName);
    }

    /**
     * @dev Function to update the participant name associated with a registered wallet.
     * @param newName New name for the participant.
     */
    function updateParticipantName(string memory newName) external {
        require(participants[msg.sender].isRegistered, "Wallet is not registered");
        require(bytes(newName).length > 0, "New name cannot be empty");

        string memory oldName = participants[msg.sender].name;
        participants[msg.sender].name = newName;

        emit ParticipantUpdated(msg.sender, oldName, newName);
    }

    /**
     * @dev Function to check if a wallet is registered.
     * @param wallet Address of the wallet to check.
     * @return bool indicating whether the wallet is registered.
     */
    function isWalletRegistered(address wallet) external view returns (bool) {
        return participants[wallet].isRegistered;
    }

    /**
     * @dev Function to get participant details for a given wallet.
     * @param wallet Address of the wallet to query.
     * @return name of the participant and registration status.
     */
    function getParticipantDetails(address wallet)
        external
        view
        returns (string memory name, bool isRegistered)
    {
        Participant memory participant = participants[wallet];
        return (participant.name, participant.isRegistered);
    }

    /**
     * @dev Function to transfer ownership of the contract to a new owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        owner = newOwner;
    }
}
```
