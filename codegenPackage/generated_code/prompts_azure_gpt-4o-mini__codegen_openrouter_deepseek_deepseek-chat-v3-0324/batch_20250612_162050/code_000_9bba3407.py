"""
Generated Code Metadata:
========================
Original URL: https://powag.ch
Prompt: Write a smart contract using Solidity that demonstrates a proof-of-concept (PoC) for a blockchain solution, as described by Proof of Work AG.
Generated: DETERMINISTIC_9bba34076f6e9109
Batch ID: 20250612_162050
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
 * @title ProofOfWorkAG
 * @dev A smart contract demonstrating a Proof-of-Concept (PoC) for a blockchain solution
 * as described by Proof of Work AG. This contract includes basic functionality for
 * registering participants, submitting work, and verifying proof of work.
 */
contract ProofOfWorkAG {
    // Struct to store participant information
    struct Participant {
        address participantAddress;
        string participantName;
        uint256 workCount;
        bool isRegistered;
    }

    // Struct to store work submission details
    struct WorkSubmission {
        address submitter;
        string workData;
        uint256 timestamp;
        bool verified;
    }

    // Contract owner
    address public owner;

    // Mapping of participant addresses to Participant struct
    mapping(address => Participant) public participants;

    // Array to store all work submissions
    WorkSubmission[] public workSubmissions;

    // Events
    event ParticipantRegistered(address indexed participant, string name);
    event WorkSubmitted(address indexed submitter, string workData, uint256 submissionId);
    event WorkVerified(uint256 submissionId, address indexed verifier);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Modifier to ensure only registered participants can perform certain actions
    modifier onlyRegistered() {
        require(participants[msg.sender].isRegistered, "Only registered participants can perform this action");
        _;
    }

    /**
     * @dev Constructor sets the contract deployer as the owner
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Register a new participant
     * @param _name Name of the participant
     */
    function registerParticipant(string memory _name) external {
        require(!participants[msg.sender].isRegistered, "Participant already registered");
        require(bytes(_name).length > 0, "Name cannot be empty");

        participants[msg.sender] = Participant({
            participantAddress: msg.sender,
            participantName: _name,
            workCount: 0,
            isRegistered: true
        });

        emit ParticipantRegistered(msg.sender, _name);
    }

    /**
     * @dev Submit work to the contract
     * @param _workData Data representing the work done
     */
    function submitWork(string memory _workData) external onlyRegistered {
        require(bytes(_workData).length > 0, "Work data cannot be empty");

        workSubmissions.push(WorkSubmission({
            submitter: msg.sender,
            workData: _workData,
            timestamp: block.timestamp,
            verified: false
        }));

        participants[msg.sender].workCount++;

        emit WorkSubmitted(msg.sender, _workData, workSubmissions.length - 1);
    }

    /**
     * @dev Verify a work submission (simplified PoC verification)
     * @param _submissionId ID of the submission to verify
     */
    function verifyWork(uint256 _submissionId) external onlyOwner {
        require(_submissionId < workSubmissions.length, "Invalid submission ID");
        require(!workSubmissions[_submissionId].verified, "Work already verified");

        // Simplified verification - in a real implementation, this would involve
        // checking the actual proof of work
        workSubmissions[_submissionId].verified = true;

        emit WorkVerified(_submissionId, msg.sender);
    }

    /**
     * @dev Get the total number of work submissions
     * @return uint256 Count of all work submissions
     */
    function getTotalSubmissions() external view returns (uint256) {
        return workSubmissions.length;
    }

    /**
     * @dev Get details of a specific work submission
     * @param _submissionId ID of the submission to retrieve
     * @return WorkSubmission The requested work submission
     */
    function getSubmission(uint256 _submissionId) external view returns (WorkSubmission memory) {
        require(_submissionId < workSubmissions.length, "Invalid submission ID");
        return workSubmissions[_submissionId];
    }

    /**
     * @dev Get participant information
     * @param _participant Address of the participant
     * @return Participant The participant's information
     */
    function getParticipant(address _participant) external view returns (Participant memory) {
        require(participants[_participant].isRegistered, "Participant not registered");
        return participants[_participant];
    }
}
```
