"""
Generated Code Metadata:
========================
Original URL: https://sportnode.nl
Prompt: Generate a smart contract for a sports organization using web3 principles as described by Sportnode.
Generated: DETERMINISTIC_5d9fda36e59e8f32
Batch ID: 20250612_162504
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
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

/**
 * @title SportNode Organization Contract
 * @dev A smart contract for managing sports organizations, teams, and memberships
 */
contract SportNodeOrganization is ERC721, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to represent a sports organization
    struct Organization {
        string name;
        string description;
        string logoURI;
        address owner;
        uint256 createdAt;
    }

    // Struct to represent a team within an organization
    struct Team {
        string name;
        string description;
        uint256 organizationId;
        address manager;
        uint256 createdAt;
    }

    // Struct to represent a membership (player/coach/staff)
    struct Membership {
        uint256 organizationId;
        uint256 teamId;
        string role;
        uint256 joinedAt;
        bool isActive;
    }

    // Mappings for storing data
    mapping(uint256 => Organization) public organizations;
    mapping(uint256 => Team) public teams;
    mapping(address => mapping(uint256 => Membership)) public memberships;
    mapping(uint256 => address[]) public organizationMembers;
    mapping(uint256 => address[]) public teamMembers;

    // Events
    event OrganizationCreated(uint256 indexed id, string name, address owner);
    event TeamCreated(uint256 indexed id, string name, uint256 organizationId, address manager);
    event MembershipGranted(address indexed member, uint256 organizationId, uint256 teamId, string role);
    event MembershipRevoked(address indexed member, uint256 organizationId);
    event TeamChanged(address indexed member, uint256 organizationId, uint256 newTeamId);

    constructor() ERC721("SportNodeMembership", "SNM") {}

    /**
     * @dev Creates a new sports organization
     * @param name Name of the organization
     * @param description Description of the organization
     * @param logoURI URI of the organization's logo
     */
    function createOrganization(
        string memory name,
        string memory description,
        string memory logoURI
    ) external {
        _tokenIdCounter.increment();
        uint256 newOrgId = _tokenIdCounter.current();

        organizations[newOrgId] = Organization({
            name: name,
            description: description,
            logoURI: logoURI,
            owner: msg.sender,
            createdAt: block.timestamp
        });

        _safeMint(msg.sender, newOrgId);
        _setTokenURI(newOrgId, logoURI);

        emit OrganizationCreated(newOrgId, name, msg.sender);
    }

    /**
     * @dev Creates a new team within an organization
     * @param organizationId ID of the parent organization
     * @param name Name of the team
     * @param description Description of the team
     */
    function createTeam(
        uint256 organizationId,
        string memory name,
        string memory description
    ) external {
        require(_exists(organizationId), "Organization does not exist");
        require(ownerOf(organizationId) == msg.sender, "Only organization owner can create teams");

        _tokenIdCounter.increment();
        uint256 newTeamId = _tokenIdCounter.current();

        teams[newTeamId] = Team({
            name: name,
            description: description,
            organizationId: organizationId,
            manager: msg.sender,
            createdAt: block.timestamp
        });

        emit TeamCreated(newTeamId, name, organizationId, msg.sender);
    }

    /**
     * @dev Grants membership to an address in an organization/team
     * @param member Address to grant membership to
     * @param organizationId ID of the organization
     * @param teamId ID of the team (0 for organization-level membership)
     * @param role Role of the member (player, coach, staff, etc.)
     */
    function grantMembership(
        address member,
        uint256 organizationId,
        uint256 teamId,
        string memory role
    ) external {
        require(_exists(organizationId), "Organization does not exist");
        require(
            ownerOf(organizationId) == msg.sender || 
            (teamId != 0 && teams[teamId].manager == msg.sender),
            "Not authorized to grant membership"
        );

        if (teamId != 0) {
            require(teams[teamId].organizationId == organizationId, "Team not in organization");
        }

        memberships[member][organizationId] = Membership({
            organizationId: organizationId,
            teamId: teamId,
            role: role,
            joinedAt: block.timestamp,
            isActive: true
        });

        organizationMembers[organizationId].push(member);
        if (teamId != 0) {
            teamMembers[teamId].push(member);
        }

        emit MembershipGranted(member, organizationId, teamId, role);
    }

    /**
     * @dev Revokes membership from an address in an organization
     * @param member Address to revoke membership from
     * @param organizationId ID of the organization
     */
    function revokeMembership(address member, uint256 organizationId) external {
        require(_exists(organizationId), "Organization does not exist");
        require(
            ownerOf(organizationId) == msg.sender,
            "Only organization owner can revoke memberships"
        );
        require(memberships[member][organizationId].isActive, "Membership not active");

        memberships[member][organizationId].isActive = false;
        emit MembershipRevoked(member, organizationId);
    }

    /**
     * @dev Changes a member's team within an organization
     * @param member Address of the member
     * @param organizationId ID of the organization
     * @param newTeamId ID of the new team (0 for organization-level)
     */
    function changeTeam(
        address member,
        uint256 organizationId,
        uint256 newTeamId
    ) external {
        require(_exists(organizationId), "Organization does not exist");
        require(
            ownerOf(organizationId) == msg.sender || 
            (newTeamId != 0 && teams[newTeamId].manager == msg.sender),
            "Not authorized to change team"
        );
        require(memberships[member][organizationId].isActive, "Membership not active");

        if (newTeamId != 0) {
            require(teams[newTeamId].organizationId == organizationId, "Team not in organization");
        }

        uint256 oldTeamId = memberships[member][organizationId].teamId;
        memberships[member][organizationId].teamId = newTeamId;

        // Update team members lists
        if (oldTeamId != 0) {
            _removeFromTeam(member, oldTeamId);
        }
        if (newTeamId != 0) {
            teamMembers[newTeamId].push(member);
        }

        emit TeamChanged(member, organizationId, newTeamId);
    }

    /**
     * @dev Internal function to remove a member from a team's member list
     * @param member Address of the member to remove
     * @param teamId ID of the team
     */
    function _removeFromTeam(address member, uint256 teamId) internal {
        address[] storage members = teamMembers[teamId];
        for (uint256 i = 0; i < members.length; i++) {
            if (members[i] == member) {
                members[i] = members[members.length - 1];
                members.pop();
                break;
            }
        }
    }

    /**
     * @dev Returns all members of an organization
     * @param organizationId ID of the organization
     * @return Array of member addresses
     */
    function getOrganizationMembers(uint256 organizationId) external view returns (address[] memory) {
        return organizationMembers[organizationId];
    }

    /**
     * @dev Returns all members of a team
     * @param teamId ID of the team
     * @return Array of member addresses
     */
    function getTeamMembers(uint256 teamId) external view returns (address[] memory) {
        return teamMembers[teamId];
    }

    /**
     * @dev Returns membership details for a member in an organization
     * @param member Address of the member
     * @param organizationId ID of the organization
     * @return Membership details
     */
    function getMembership(address member, uint256 organizationId) external view returns (Membership memory) {
        return memberships[member][organizationId];
    }

    // Override functions for ERC721URIStorage
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId) public view override(ERC721, ERC721URIStorage) returns (string memory) {
        return super.tokenURI(tokenId);
