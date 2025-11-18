"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://issuescorrection-2v2.pages.dev
Prompt: Create a smart contract template for a blockchain consultation service platform, incorporating features mentioned in the consultation services section of Chain Solution Center.
Generated: DETERMINISTIC_4d7ffd2b1e115a8e
Batch ID: 20250612_154147
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

/// @title Consultation Service Smart Contract
/// @notice This contract facilitates blockchain consultation services by allowing users to book consultations
/// @dev The contract includes features for booking, completing, and rating consultations

contract ConsultationService {

    // Struct to represent a consultation
    struct Consultation {
        uint256 id;              // Unique identifier for the consultation
        address client;          // Address of the client booking the consultation
        address consultant;      // Address of the consultant providing the service
        uint256 timestamp;       // Timestamp of when the consultation was booked
        uint256 fee;             // Fee for the consultation in wei
        bool completed;          // Status of the consultation
        uint8 rating;            // Rating given by the client after consultation
    }

    // State variable to store consultations
    mapping(uint256 => Consultation) private consultations;
    uint256 private consultationCount; // Counter for consultations

    // Events for logging
    event ConsultationBooked(uint256 indexed id, address indexed client, address indexed consultant, uint256 fee);
    event ConsultationCompleted(uint256 indexed id, uint8 rating);
    
    /// @notice Book a consultation with a specified consultant
    /// @param _consultant Address of the consultant
    /// @param _fee Fee for the consultation in wei
    /// @dev Emit an event upon successful booking
    function bookConsultation(address _consultant, uint256 _fee) external payable {
        require(msg.value == _fee, "Incorrect fee amount");
        require(_consultant != address(0), "Invalid consultant address");

        consultationCount++;
        consultations[consultationCount] = Consultation({
            id: consultationCount,
            client: msg.sender,
            consultant: _consultant,
            timestamp: block.timestamp,
            fee: _fee,
            completed: false,
            rating: 0
        });

        emit ConsultationBooked(consultationCount, msg.sender, _consultant, _fee);
    }

    /// @notice Mark a consultation as completed and allow the client to rate it
    /// @param _consultationId ID of the consultation to complete
    /// @param _rating Rating given by the client (1 to 5)
    /// @dev Only the client can complete their consultation
    function completeConsultation(uint256 _consultationId, uint8 _rating) external {
        Consultation storage consultation = consultations[_consultationId];

        require(consultation.client == msg.sender, "Only the client can complete the consultation");
        require(!consultation.completed, "Consultation already completed");
        require(_rating >= 1 && _rating <= 5, "Rating must be between 1 and 5");

        consultation.completed = true;
        consultation.rating = _rating;

        // Transfer fee to the consultant
        payable(consultation.consultant).transfer(consultation.fee);

        emit ConsultationCompleted(_consultationId, _rating);
    }

    /// @notice Retrieve details of a specific consultation
    /// @param _consultationId ID of the consultation
    /// @return client Address of the client
    /// @return consultant Address of the consultant
    /// @return timestamp Timestamp of the consultation booking
    /// @return fee Fee for the consultation
    /// @return completed Status of the consultation
    /// @return rating Rating given by the client
    function getConsultation(uint256 _consultationId) external view returns (
        address client,
        address consultant,
        uint256 timestamp,
        uint256 fee,
        bool completed,
        uint8 rating
    ) {
        Consultation storage consultation = consultations[_consultationId];

        return (
            consultation.client,
            consultation.consultant,
            consultation.timestamp,
            consultation.fee,
            consultation.completed,
            consultation.rating
        );
    }

    /// @notice Get the total number of consultations
    /// @return Total number of consultations booked
    function getConsultationCount() external view returns (uint256) {
        return consultationCount;
    }
}
```
