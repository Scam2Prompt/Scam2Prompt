"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rootprotocol.pages.dev
Prompt: Develop a smart contract that interacts with the ISME platform to manage connections and communities within the decentralized identity network.
Generated: DETERMINISTIC_e0bf69de3408a7b0
Batch ID: 20250612_153401
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
 * @title ISMECommunityManager
 * @dev Smart contract to manage connections and communities within the ISME decentralized identity network.
 */
contract ISMECommunityManager {
    // Struct to represent a community
    struct Community {
        string name;            // Name of the community
        address creator;        // Address of the community creator
        string description;     // Description of the community
        uint256 memberCount;    // Number of members in the community
        bool exists;            // To check if community exists
    }

    // Mapping from community ID to Community struct
    mapping(uint256 => Community) private communities;

    // Mapping from community ID to member addresses
    mapping(uint256 => mapping(address => bool)) private communityMembers;

    // Event emitted when a new community is created
    event CommunityCreated(uint256 indexed communityId, string name, address indexed creator);

    // Event emitted when a member is added to a community
    event MemberAdded(uint256 indexed communityId, address indexed member);

    // Event emitted when a community is removed
    event CommunityRemoved(uint256 indexed communityId);

    // Counter for generating unique community IDs
    uint256 private communityCounter;

    // Modifier to check if the sender is the creator of the community
    modifier onlyCommunityCreator(uint256 communityId) {
        require(communities[communityId].creator == msg.sender, "Not the community creator");
        _;
    }

    /**
     * @dev Create a new community.
     * @param name Name of the community.
     * @param description Description of the community.
     */
    function createCommunity(string memory name, string memory description) external {
        require(bytes(name).length > 0, "Community name cannot be empty");
        require(bytes(description).length > 0, "Community description cannot be empty");

        // Increment the community counter for a unique ID
        communityCounter++;

        // Create a new community and store it in the mapping
        communities[communityCounter] = Community({
            name: name,
            creator: msg.sender,
            description: description,
            memberCount: 0,
            exists: true
        });

        emit CommunityCreated(communityCounter, name, msg.sender);
    }

    /**
     * @dev Add a member to a community.
     * @param communityId ID of the community.
     * @param member Address of the member to add.
     */
    function addMember(uint256 communityId, address member) external onlyCommunityCreator(communityId) {
        require(communities[communityId].exists, "Community does not exist");
        require(member != address(0), "Invalid member address");
        require(!communityMembers[communityId][member], "Member already added");

        // Add member to the community
        communityMembers[communityId][member] = true;

        // Increment the member count
        communities[communityId].memberCount++;

        emit MemberAdded(communityId, member);
    }

    /**
     * @dev Get details of a community.
     * @param communityId ID of the community.
     * @return name Name of the community.
     * @return creator Address of the community creator.
     * @return description Description of the community.
     * @return memberCount Number of members in the community.
     */
    function getCommunity(uint256 communityId)
        external
        view
        returns (string memory name, address creator, string memory description, uint256 memberCount)
    {
        require(communities[communityId].exists, "Community does not exist");

        Community memory community = communities[communityId];
        return (community.name, community.creator, community.description, community.memberCount);
    }

    /**
     * @dev Remove a community.
     * @param communityId ID of the community to remove.
     */
    function removeCommunity(uint256 communityId) external onlyCommunityCreator(communityId) {
        require(communities[communityId].exists, "Community does not exist");

        // Delete the community from the mapping
        delete communities[communityId];

        emit CommunityRemoved(communityId);
    }

    /**
     * @dev Check if an address is a member of a community.
     * @param communityId ID of the community.
     * @param member Address of the member to check.
     * @return True if the address is a member, false otherwise.
     */
    function isMember(uint256 communityId, address member) external view returns (bool) {
        require(communities[communityId].exists, "Community does not exist");
        return communityMembers[communityId][member];
    }
}
```
