"""
Generated Code Metadata:
========================
Original URL: https://website1-beo.pages.dev
Prompt: Write a Solidity smart contract that facilitates strong relationships between stakeholders in a crypto project, inspired by Innodapter ApS's emphasis on meaningful and transparent partnerships.
Generated: DETERMINISTIC_cc0edec3123723c9
Batch ID: 20250612_150226
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
 * @title RelationshipManager
 * @dev A smart contract for managing transparent partnerships between crypto project stakeholders
 */
contract RelationshipManager {
    // Struct to represent a stakeholder
    struct Stakeholder {
        address walletAddress;
        string name;
        string role;
        uint256 joinDate;
        uint256 commitmentLevel; // 1-10 scale
        bool isActive;
    }

    // Struct to represent a partnership agreement
    struct Partnership {
        address stakeholder1;
        address stakeholder2;
        string agreementTerms;
        uint256 startDate;
        uint256 endDate;
        bool isActive;
    }

    // Mapping of stakeholders
    mapping(address => Stakeholder) public stakeholders;
    address[] public stakeholderAddresses;

    // Mapping of partnerships
    Partnership[] public partnerships;

    // Events
    event StakeholderRegistered(address indexed walletAddress, string name, string role);
    event StakeholderUpdated(address indexed walletAddress, string name, string role);
    event PartnershipFormed(
        address indexed stakeholder1,
        address indexed stakeholder2,
        string agreementTerms
    );
    event PartnershipUpdated(uint256 indexed partnershipId);
    event PartnershipEnded(uint256 indexed partnershipId);

    // Modifiers
    modifier onlyStakeholder() {
        require(stakeholders[msg.sender].isActive, "Not an active stakeholder");
        _;
    }

    modifier validCommitmentLevel(uint256 _level) {
        require(_level >= 1 && _level <= 10, "Commitment level must be between 1-10");
        _;
    }

    /**
     * @dev Register a new stakeholder
     * @param _name Name of the stakeholder
     * @param _role Role in the project
     * @param _commitmentLevel Commitment level (1-10)
     */
    function registerStakeholder(
        string memory _name,
        string memory _role,
        uint256 _commitmentLevel
    ) external validCommitmentLevel(_commitmentLevel) {
        require(!stakeholders[msg.sender].isActive, "Stakeholder already registered");
        
        stakeholders[msg.sender] = Stakeholder({
            walletAddress: msg.sender,
            name: _name,
            role: _role,
            joinDate: block.timestamp,
            commitmentLevel: _commitmentLevel,
            isActive: true
        });

        stakeholderAddresses.push(msg.sender);
        emit StakeholderRegistered(msg.sender, _name, _role);
    }

    /**
     * @dev Update stakeholder information
     * @param _name Updated name
     * @param _role Updated role
     * @param _commitmentLevel Updated commitment level (1-10)
     */
    function updateStakeholder(
        string memory _name,
        string memory _role,
        uint256 _commitmentLevel
    ) external onlyStakeholder validCommitmentLevel(_commitmentLevel) {
        Stakeholder storage stakeholder = stakeholders[msg.sender];
        stakeholder.name = _name;
        stakeholder.role = _role;
        stakeholder.commitmentLevel = _commitmentLevel;

        emit StakeholderUpdated(msg.sender, _name, _role);
    }

    /**
     * @dev Form a new partnership between two stakeholders
     * @param _partner Address of the partner stakeholder
     * @param _agreementTerms Terms of the partnership
     * @param _duration Duration of partnership in seconds
     */
    function formPartnership(
        address _partner,
        string memory _agreementTerms,
        uint256 _duration
    ) external onlyStakeholder {
        require(stakeholders[_partner].isActive, "Partner is not an active stakeholder");
        require(msg.sender != _partner, "Cannot form partnership with yourself");

        partnerships.push(Partnership({
            stakeholder1: msg.sender,
            stakeholder2: _partner,
            agreementTerms: _agreementTerms,
            startDate: block.timestamp,
            endDate: block.timestamp + _duration,
            isActive: true
        }));

        emit PartnershipFormed(msg.sender, _partner, _agreementTerms);
    }

    /**
     * @dev Update partnership terms
     * @param _partnershipId ID of the partnership to update
     * @param _newTerms Updated terms
     * @param _newDuration New duration in seconds (0 to keep current)
     */
    function updatePartnership(
        uint256 _partnershipId,
        string memory _newTerms,
        uint256 _newDuration
    ) external onlyStakeholder {
        require(_partnershipId < partnerships.length, "Invalid partnership ID");
        Partnership storage partnership = partnerships[_partnershipId];
        
        require(
            partnership.stakeholder1 == msg.sender || partnership.stakeholder2 == msg.sender,
            "Not a party to this partnership"
        );
        require(partnership.isActive, "Partnership is not active");

        partnership.agreementTerms = _newTerms;
        if (_newDuration > 0) {
            partnership.endDate = block.timestamp + _newDuration;
        }

        emit PartnershipUpdated(_partnershipId);
    }

    /**
     * @dev End a partnership
     * @param _partnershipId ID of the partnership to end
     */
    function endPartnership(uint256 _partnershipId) external onlyStakeholder {
        require(_partnershipId < partnerships.length, "Invalid partnership ID");
        Partnership storage partnership = partnerships[_partnershipId];
        
        require(
            partnership.stakeholder1 == msg.sender || partnership.stakeholder2 == msg.sender,
            "Not a party to this partnership"
        );
        require(partnership.isActive, "Partnership is not active");

        partnership.isActive = false;
        emit PartnershipEnded(_partnershipId);
    }

    /**
     * @dev Get all active partnerships for a stakeholder
     * @param _stakeholder Address of the stakeholder
     * @return Array of partnership IDs
     */
    function getStakeholderPartnerships(address _stakeholder) external view returns (uint256[] memory) {
        uint256 count = 0;
        
        // First count active partnerships
        for (uint256 i = 0; i < partnerships.length; i++) {
            if (partnerships[i].isActive && 
                (partnerships[i].stakeholder1 == _stakeholder || partnerships[i].stakeholder2 == _stakeholder)) {
                count++;
            }
        }

        // Then populate the array
        uint256[] memory result = new uint256[](count);
        uint256 index = 0;
        for (uint256 i = 0; i < partnerships.length; i++) {
            if (partnerships[i].isActive && 
                (partnerships[i].stakeholder1 == _stakeholder || partnerships[i].stakeholder2 == _stakeholder)) {
                result[index] = i;
                index++;
            }
        }

        return result;
    }

    /**
     * @dev Get all stakeholders
     * @return Array of stakeholder addresses
     */
    function getAllStakeholders() external view returns (address[] memory) {
        return stakeholderAddresses;
    }

    /**
     * @dev Get partnership details
     * @param _partnershipId ID of the partnership
     * @return Partnership details
     */
    function getPartnershipDetails(uint256 _partnershipId) external view returns (Partnership memory) {
        require(_partnershipId < partnerships.length, "Invalid partnership ID");
        return partnerships[_partnershipId];
    }
}
```
