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

/// @title ISME Community Management Smart Contract
/// @notice This contract manages connections and communities within the decentralized identity network of ISME.
/// @dev The contract allows users to create communities, join communities, and manage connections.
contract ISMECommunityManager {
    struct Community {
        string name;
        address[] members;
        address creator;
        bool exists;
    }

    // Mapping to store communities by ID
    mapping(uint256 => Community) private communities;
    // Counter for community IDs
    uint256 private communityIdCounter;

    // Events for logging actions
    event CommunityCreated(uint256 communityId, string name, address creator);
    event MemberJoined(uint256 communityId, address member);
    event MemberLeft(uint256 communityId, address member);

    /// @notice Create a new community
    /// @param _name The name of the community
    /// @return communityId The ID of the newly created community
    function createCommunity(string calldata _name) external returns (uint256 communityId) {
        require(bytes(_name).length > 0, "Community name cannot be empty");
        
        communityId = communityIdCounter++;
        communities[communityId] = Community({
            name: _name,
            members: new address[](0),
            creator: msg.sender,
            exists: true
        });

        emit CommunityCreated(communityId, _name, msg.sender);
    }

    /// @notice Join an existing community
    /// @param _communityId The ID of the community to join
    /// @dev Reverts if the community does not exist or if the caller is already a member
    function joinCommunity(uint256 _communityId) external {
        require(communities[_communityId].exists, "Community does not exist");
        require(!isMember(_communityId, msg.sender), "Already a member");

        communities[_communityId].members.push(msg.sender);
        emit MemberJoined(_communityId, msg.sender);
    }

    /// @notice Leave a community
    /// @param _communityId The ID of the community to leave
    /// @dev Reverts if the community does not exist or if the caller is not a member
    function leaveCommunity(uint256 _communityId) external {
        require(communities[_communityId].exists, "Community does not exist");
        require(isMember(_communityId, msg.sender), "Not a member");

        address[] storage members = communities[_communityId].members;
        for (uint256 i = 0; i < members.length; i++) {
            if (members[i] == msg.sender) {
                members[i] = members[members.length - 1]; // Move last member to the current position
                members.pop(); // Remove last member
                emit MemberLeft(_communityId, msg.sender);
                return;
            }
        }
    }

    /// @notice Check if an address is a member of a community
    /// @param _communityId The ID of the community
    /// @param _member The address to check
    /// @return isMember_ True if the address is a member, false otherwise
    function isMember(uint256 _communityId, address _member) public view returns (bool isMember_) {
        require(communities[_communityId].exists, "Community does not exist");

        address[] memory members = communities[_communityId].members;
        for (uint256 i = 0; i < members.length; i++) {
            if (members[i] == _member) {
                return true;
            }
        }
        return false;
    }

    /// @notice Get the details of a community
    /// @param _communityId The ID of the community
    /// @return name The name of the community
    /// @return members The list of members in the community
    function getCommunity(uint256 _communityId) external view returns (string memory name, address[] memory members) {
        require(communities[_communityId].exists, "Community does not exist");

        Community storage community = communities[_communityId];
        return (community.name, community.members);
    }
}
```
