"""
Generated Code Metadata:
========================
Original URL: https://website1-beo.pages.dev
Prompt: Generate a smart contract that supports long-term relationships and transparency in crypto projects, reflecting the values of Innodapter ApS.
Generated: DETERMINISTIC_684c0e0b1d087e55
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
 * @title InnodapterRelationshipContract
 * @dev A smart contract to establish long-term relationships and transparency in crypto projects
 * @notice Implements commitment tracking, milestone verification, and transparent fund management
 */
contract InnodapterRelationshipContract {
    // Struct to represent a project milestone
    struct Milestone {
        string description;
        uint256 deadline;
        uint256 fundsAllocated;
        bool isCompleted;
        bool isVerified;
    }

    // Struct to represent a project relationship
    struct Relationship {
        address client;
        address provider;
        uint256 totalFunds;
        uint256 fundsReleased;
        uint256 startDate;
        uint256 duration;
        bool isActive;
        Milestone[] milestones;
    }

    // Mapping from relationship ID to Relationship
    mapping(bytes32 => Relationship) public relationships;

    // Mapping to track commitments (address => relationship IDs)
    mapping(address => bytes32[]) public commitments;

    // Events for transparency
    event RelationshipCreated(
        bytes32 indexed relationshipId,
        address indexed client,
        address indexed provider,
        uint256 totalFunds,
        uint256 duration
    );
    event MilestoneAdded(
        bytes32 indexed relationshipId,
        uint256 milestoneIndex,
        string description,
        uint256 deadline,
        uint256 fundsAllocated
    );
    event FundsDeposited(bytes32 indexed relationshipId, uint256 amount);
    event MilestoneCompleted(bytes32 indexed relationshipId, uint256 milestoneIndex);
    event MilestoneVerified(bytes32 indexed relationshipId, uint256 milestoneIndex);
    event FundsReleased(bytes32 indexed relationshipId, uint256 amount);
    event RelationshipTerminated(bytes32 indexed relationshipId);

    // Modifier to check if relationship exists
    modifier relationshipExists(bytes32 relationshipId) {
        require(
            relationships[relationshipId].client != address(0),
            "Relationship does not exist"
        );
        _;
    }

    // Modifier to check if caller is client
    modifier onlyClient(bytes32 relationshipId) {
        require(
            msg.sender == relationships[relationshipId].client,
            "Only client can perform this action"
        );
        _;
    }

    // Modifier to check if caller is provider
    modifier onlyProvider(bytes32 relationshipId) {
        require(
            msg.sender == relationships[relationshipId].provider,
            "Only provider can perform this action"
        );
        _;
    }

    // Modifier to check if relationship is active
    modifier isActive(bytes32 relationshipId) {
        require(
            relationships[relationshipId].isActive,
            "Relationship is not active"
        );
        _;
    }

    /**
     * @dev Create a new relationship
     * @param provider The address of the service provider
     * @param totalFunds The total funds allocated for the relationship
     * @param duration The duration of the relationship in seconds
     * @return relationshipId The ID of the newly created relationship
     */
    function createRelationship(
        address provider,
        uint256 totalFunds,
        uint256 duration
    ) external returns (bytes32) {
        require(provider != address(0), "Invalid provider address");
        require(totalFunds > 0, "Total funds must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        bytes32 relationshipId = keccak256(
            abi.encodePacked(msg.sender, provider, block.timestamp)
        );

        Relationship storage newRelationship = relationships[relationshipId];
        newRelationship.client = msg.sender;
        newRelationship.provider = provider;
        newRelationship.totalFunds = totalFunds;
        newRelationship.startDate = block.timestamp;
        newRelationship.duration = duration;
        newRelationship.isActive = true;

        commitments[msg.sender].push(relationshipId);
        commitments[provider].push(relationshipId);

        emit RelationshipCreated(
            relationshipId,
            msg.sender,
            provider,
            totalFunds,
            duration
        );

        return relationshipId;
    }

    /**
     * @dev Add a milestone to a relationship
     * @param relationshipId The ID of the relationship
     * @param description Description of the milestone
     * @param deadline Deadline for the milestone (timestamp)
     * @param fundsAllocated Funds allocated for this milestone
     */
    function addMilestone(
        bytes32 relationshipId,
        string memory description,
        uint256 deadline,
        uint256 fundsAllocated
    ) external relationshipExists(relationshipId) onlyClient(relationshipId) isActive(relationshipId) {
        Relationship storage relationship = relationships[relationshipId];

        require(
            deadline > block.timestamp,
            "Deadline must be in the future"
        );
        require(
            fundsAllocated > 0,
            "Funds allocated must be greater than zero"
        );
        require(
            relationship.fundsReleased + fundsAllocated <= relationship.totalFunds,
            "Total funds allocation exceeded"
        );

        relationship.milestones.push(
            Milestone({
                description: description,
                deadline: deadline,
                fundsAllocated: fundsAllocated,
                isCompleted: false,
                isVerified: false
            })
        );

        emit MilestoneAdded(
            relationshipId,
            relationship.milestones.length - 1,
            description,
            deadline,
            fundsAllocated
        );
    }

    /**
     * @dev Deposit funds into the relationship contract
     * @param relationshipId The ID of the relationship
     */
    function depositFunds(bytes32 relationshipId)
        external
        payable
        relationshipExists(relationshipId)
        onlyClient(relationshipId)
        isActive(relationshipId)
    {
        Relationship storage relationship = relationships[relationshipId];
        require(
            relationship.fundsReleased + msg.value <= relationship.totalFunds,
            "Cannot exceed total funds commitment"
        );

        emit FundsDeposited(relationshipId, msg.value);
    }

    /**
     * @dev Mark a milestone as completed (called by provider)
     * @param relationshipId The ID of the relationship
     * @param milestoneIndex Index of the milestone
     */
    function completeMilestone(bytes32 relationshipId, uint256 milestoneIndex)
        external
        relationshipExists(relationshipId)
        onlyProvider(relationshipId)
        isActive(relationshipId)
    {
        Relationship storage relationship = relationships[relationshipId];
        require(
            milestoneIndex < relationship.milestones.length,
            "Invalid milestone index"
        );

        Milestone storage milestone = relationship.milestones[milestoneIndex];
        require(!milestone.isCompleted, "Milestone already completed");
        require(
            block.timestamp <= milestone.deadline,
            "Milestone deadline has passed"
        );

        milestone.isCompleted = true;
        emit MilestoneCompleted(relationshipId, milestoneIndex);
    }

    /**
     * @dev Verify a completed milestone (called by client)
     * @param relationshipId The ID of the relationship
     * @param milestoneIndex Index of the milestone
     */
    function verifyMilestone(bytes32 relationshipId, uint256 milestoneIndex)
        external
        relationshipExists(relationshipId)
        onlyClient(relationshipId)
        isActive(relationshipId)
    {
        Relationship storage relationship = relationships[relationshipId];
        require(
            milestoneIndex < relationship.milestones.length,
            "Invalid milestone index"
        );

        Milestone storage milestone = relationship.milestones[milestoneIndex];
        require(milestone.isCompleted, "Milestone not completed");
        require(!milestone.isVerified, "Milestone already verified");

        milestone.isVerified = true;
        relationship.fundsReleased += milestone.fundsAllocated;

        // Transfer funds to provider
        payable(relationship.provider).transfer(milestone.fundsAllocated);

        emit MilestoneVerified(relationshipId, milestoneIndex);
        emit FundsReleased(relationshipId, milestone.fundsAllocated);
    }

    /**
     * @dev Terminate a relationship (can be called by either party)
     * @param relationshipId The ID of the relationship
     */
    function terminateRelationship(bytes32 relationshipId)
        external
        relationshipExists(relationshipId)
        isActive(relationshipId)
    {
        Relationship storage relationship = relationships[relationshipId];
        require(
            msg.sender == relationship.client || msg.sender == relationship.provider,
            "Only client or provider can terminate"
        );

        relationship.isActive = false;

        // Return remaining funds to client
        uint256 remainingBalance = address(this).balance;
        if (remainingBalance > 0) {
            payable(relationship.client).transfer(remainingBalance);
        }

        emit RelationshipTerminated(relationshipId);
    }

    /**
     * @dev Get relationship details
     * @param relationshipId The ID of the relationship
     * @return client The client address
     * @return provider The provider address
     * @return totalFunds Total funds allocated
     * @return fundsReleased Funds already released
     * @return startDate Relationship start date
     * @return duration Relationship duration
     * @return isActive Relationship status
     * @return milestoneCount Number of milestones
     */
    function getRelationshipDetails(bytes32 relationshipId)
        external
        view
        relationshipExists(relationshipId)
        returns (
            address client,
            address provider,
            uint256 totalFunds,
            uint256 fundsReleased,
            uint256 startDate,
            uint256 duration,
            bool isActive,
            uint256 milestoneCount
