"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://explorer-dapp.pages.dev
Prompt: Generate a Solidity smart contract for a decentralized application that incorporates personalized consultation services, referencing the consultation services offered by Dapp Protocol.
Generated: DETERMINISTIC_f92114b1619d78ed
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
 * @title ConsultationServices
 * @dev A decentralized application (dApp) smart contract for booking personalized consultation services.
 */
contract ConsultationServices {
    // Owner of the contract
    address public owner;

    // Struct to represent a consultation session
    struct Consultation {
        uint256 id;
        address payable consultant;
        address user;
        string description;
        uint256 price;
        uint256 timestamp;
        bool isCompleted;
    }

    // Event to log consultation booking
    event ConsultationBooked(
        uint256 indexed id,
        address indexed consultant,
        address indexed user,
        uint256 price,
        string description
    );

    // Event to log completion of a consultation
    event ConsultationCompleted(uint256 indexed id, address indexed consultant);

    // Counter to generate unique consultation IDs
    uint256 private consultationCounter;

    // Mapping from consultation ID to Consultation struct
    mapping(uint256 => Consultation) public consultations;

    // Modifier to restrict access to the consultant
    modifier onlyConsultant(uint256 id) {
        require(
            msg.sender == consultations[id].consultant,
            "Only the consultant can perform this action"
        );
        _;
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor sets the contract deployer as the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to book a consultation with a consultant.
     * @param consultant The address of the consultant.
     * @param description A brief description of the consultation.
     * @param price The price of the consultation in wei.
     */
    function bookConsultation(
        address payable consultant,
        string memory description,
        uint256 price
    ) external payable {
        require(msg.value == price, "Incorrect payment amount");
        require(price > 0, "Price must be greater than zero");
        require(consultant != address(0), "Invalid consultant address");

        consultationCounter++;
        consultations[consultationCounter] = Consultation({
            id: consultationCounter,
            consultant: consultant,
            user: msg.sender,
            description: description,
            price: price,
            timestamp: block.timestamp,
            isCompleted: false
        });

        emit ConsultationBooked(
            consultationCounter,
            consultant,
            msg.sender,
            price,
            description
        );
    }

    /**
     * @dev Function for the consultant to mark a consultation as completed.
     * @param id The ID of the consultation to mark as completed.
     */
    function completeConsultation(uint256 id) external onlyConsultant(id) {
        Consultation storage consultation = consultations[id];
        require(!consultation.isCompleted, "Consultation already completed");

        consultation.isCompleted = true;

        // Transfer payment to consultant
        consultation.consultant.transfer(consultation.price);

        emit ConsultationCompleted(id, consultation.consultant);
    }

    /**
     * @dev Function for the contract owner to withdraw any remaining funds in the contract.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        payable(owner).transfer(balance);
    }
}
```
