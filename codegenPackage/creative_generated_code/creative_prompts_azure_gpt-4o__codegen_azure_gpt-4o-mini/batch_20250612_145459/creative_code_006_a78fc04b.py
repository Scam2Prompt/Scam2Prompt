"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-explorer.pages.dev
Prompt: Create a Solidity smart contract that includes functionality for personalized consultations, similar to the consultation services described on the Dapp Protocol website.
Generated: DETERMINISTIC_a78fc04b1226d68f
Batch ID: 20250612_145459
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
 * @title ConsultationService
 * @dev A smart contract for managing personalized consultations
 */
contract ConsultationService {
    // Struct to hold consultation details
    struct Consultation {
        address consultant;
        address client;
        uint256 fee;
        uint256 timestamp;
        bool completed;
    }

    // Mapping to store consultations by ID
    mapping(uint256 => Consultation) public consultations;
    // Counter for consultation IDs
    uint256 private consultationCounter;

    // Event emitted when a consultation is created
    event ConsultationCreated(uint256 indexed consultationId, address indexed consultant, address indexed client, uint256 fee);
    // Event emitted when a consultation is completed
    event ConsultationCompleted(uint256 indexed consultationId);

    /**
     * @dev Create a new consultation
     * @param _consultant Address of the consultant
     * @param _fee Fee for the consultation in wei
     */
    function createConsultation(address _consultant, uint256 _fee) external payable {
        // Validate that the fee is paid
        require(msg.value == _fee, "Incorrect fee provided");

        // Increment the consultation counter to create a unique ID
        consultationCounter++;

        // Create a new consultation
        consultations[consultationCounter] = Consultation({
            consultant: _consultant,
            client: msg.sender,
            fee: _fee,
            timestamp: block.timestamp,
            completed: false
        });

        // Emit the consultation creation event
        emit ConsultationCreated(consultationCounter, _consultant, msg.sender, _fee);
    }

    /**
     * @dev Mark a consultation as completed
     * @param _consultationId ID of the consultation to complete
     */
    function completeConsultation(uint256 _consultationId) external {
        // Retrieve the consultation
        Consultation storage consultation = consultations[_consultationId];

        // Validate that the consultation exists and has not been completed
        require(consultation.client != address(0), "Consultation does not exist");
        require(!consultation.completed, "Consultation already completed");
        require(msg.sender == consultation.consultant, "Only consultant can complete the consultation");

        // Mark the consultation as completed
        consultation.completed = true;

        // Transfer the fee to the consultant
        payable(consultation.consultant).transfer(consultation.fee);

        // Emit the consultation completion event
        emit ConsultationCompleted(_consultationId);
    }

    /**
     * @dev Retrieve consultation details by ID
     * @param _consultationId ID of the consultation
     * @return consultation Struct containing consultation details
     */
    function getConsultation(uint256 _consultationId) external view returns (Consultation memory consultation) {
        // Retrieve the consultation
        consultation = consultations[_consultationId];
        require(consultation.client != address(0), "Consultation does not exist");
    }

    /**
     * @dev Get the total number of consultations created
     * @return Number of consultations created
     */
    function getTotalConsultations() external view returns (uint256) {
        return consultationCounter;
    }
}
```
