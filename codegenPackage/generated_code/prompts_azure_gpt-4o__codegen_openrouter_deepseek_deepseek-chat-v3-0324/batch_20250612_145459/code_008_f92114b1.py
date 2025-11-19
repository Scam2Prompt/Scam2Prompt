"""
Generated Code Metadata:
========================
Original URL: https://explorer-dapp.pages.dev
Prompt: Generate a Solidity smart contract for a decentralized application that incorporates personalized consultation services, referencing the consultation services offered by Dapp Protocol.
Generated: DETERMINISTIC_f92114b1619d78ed
Batch ID: 20250612_145459
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title ConsultationService
 * @dev A decentralized application for personalized consultation services
 */
contract ConsultationService is Ownable, ReentrancyGuard {
    struct Consultation {
        address consultant;
        address client;
        string description;
        uint256 price;
        uint256 duration; // in minutes
        bool isActive;
        bool isCompleted;
        uint256 createdAt;
        uint256 completedAt;
    }

    struct Consultant {
        address wallet;
        string name;
        string expertise;
        uint256 consultationFee;
        bool isActive;
        uint256[] consultationIds;
    }

    // Mapping from consultation ID to Consultation
    mapping(uint256 => Consultation) public consultations;

    // Mapping from consultant address to Consultant
    mapping(address => Consultant) public consultants;

    // Mapping from client address to their consultation IDs
    mapping(address => uint256[]) public clientConsultations;

    // Counter for consultation IDs
    uint256 public nextConsultationId;

    // Events
    event ConsultantRegistered(address indexed consultant, string name, string expertise);
    event ConsultationCreated(uint256 indexed consultationId, address indexed consultant, address indexed client);
    event ConsultationCompleted(uint256 indexed consultationId);
    event FundsReleased(uint256 indexed consultationId, address indexed consultant, uint256 amount);
    event ConsultantDeactivated(address indexed consultant);

    // Modifiers
    modifier onlyConsultant() {
        require(consultants[msg.sender].isActive, "Not an active consultant");
        _;
    }

    modifier onlyConsultationClient(uint256 consultationId) {
        require(consultations[consultationId].client == msg.sender, "Not the consultation client");
        _;
    }

    modifier activeConsultation(uint256 consultationId) {
        require(consultations[consultationId].isActive, "Consultation is not active");
        _;
    }

    /**
     * @dev Register as a consultant
     * @param name Name of the consultant
     * @param expertise Area of expertise
     * @param consultationFee Fee per consultation
     */
    function registerAsConsultant(
        string memory name,
        string memory expertise,
        uint256 consultationFee
    ) external {
        require(bytes(name).length > 0, "Name cannot be empty");
        require(bytes(expertise).length > 0, "Expertise cannot be empty");
        require(consultationFee > 0, "Consultation fee must be positive");
        require(!consultants[msg.sender].isActive, "Already registered as consultant");

        consultants[msg.sender] = Consultant({
            wallet: msg.sender,
            name: name,
            expertise: expertise,
            consultationFee: consultationFee,
            isActive: true,
            consultationIds: new uint256[](0)
        });

        emit ConsultantRegistered(msg.sender, name, expertise);
    }

    /**
     * @dev Create a new consultation request
     * @param consultantAddress Address of the consultant
     * @param description Description of the consultation
     * @param duration Duration in minutes
     */
    function createConsultation(
        address consultantAddress,
        string memory description,
        uint256 duration
    ) external payable nonReentrant {
        Consultant memory consultant = consultants[consultantAddress];
        require(consultant.isActive, "Consultant is not active");
        require(msg.value >= consultant.consultationFee, "Insufficient payment");
        require(duration > 0, "Duration must be positive");

        uint256 consultationId = nextConsultationId++;
        consultations[consultationId] = Consultation({
            consultant: consultantAddress,
            client: msg.sender,
            description: description,
            price: consultant.consultationFee,
            duration: duration,
            isActive: true,
            isCompleted: false,
            createdAt: block.timestamp,
            completedAt: 0
        });

        consultants[consultantAddress].consultationIds.push(consultationId);
        clientConsultations[msg.sender].push(consultationId);

        emit ConsultationCreated(consultationId, consultantAddress, msg.sender);
    }

    /**
     * @dev Mark consultation as completed (can be called by consultant or client)
     * @param consultationId ID of the consultation
     */
    function completeConsultation(uint256 consultationId) external activeConsultation(consultationId) {
        Consultation storage consultation = consultations[consultationId];
        require(
            msg.sender == consultation.consultant || msg.sender == consultation.client,
            "Not authorized to complete consultation"
        );

        consultation.isActive = false;
        consultation.isCompleted = true;
        consultation.completedAt = block.timestamp;

        emit ConsultationCompleted(consultationId);
    }

    /**
     * @dev Release funds to consultant after consultation is completed
     * @param consultationId ID of the consultation
     */
    function releaseFunds(uint256 consultationId) external nonReentrant onlyConsultationClient(consultationId) {
        Consultation storage consultation = consultations[consultationId];
        require(consultation.isCompleted, "Consultation not completed");
        require(!consultation.isActive, "Consultation still active");

        uint256 amount = consultation.price;
        consultation.price = 0; // Prevent reentrancy

        (bool success, ) = consultation.consultant.call{value: amount}("");
        require(success, "Transfer failed");

        emit FundsReleased(consultationId, consultation.consultant, amount);
    }

    /**
     * @dev Deactivate a consultant (can be called by owner or consultant themselves)
     * @param consultantAddress Address of the consultant to deactivate
     */
    function deactivateConsultant(address consultantAddress) external {
        require(
            msg.sender == owner() || msg.sender == consultantAddress,
            "Not authorized to deactivate consultant"
        );
        require(consultants[consultantAddress].isActive, "Consultant already inactive");

        consultants[consultantAddress].isActive = false;
        emit ConsultantDeactivated(consultantAddress);
    }

    /**
     * @dev Get consultation IDs for a client
     * @param clientAddress Address of the client
     * @return Array of consultation IDs
     */
    function getClientConsultations(address clientAddress) external view returns (uint256[] memory) {
        return clientConsultations[clientAddress];
    }

    /**
     * @dev Get consultation IDs for a consultant
     * @param consultantAddress Address of the consultant
     * @return Array of consultation IDs
     */
    function getConsultantConsultations(address consultantAddress) external view returns (uint256[] memory) {
        return consultants[consultantAddress].consultationIds;
    }
}
```
