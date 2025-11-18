"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everlodge-claimv2.pages.dev
Prompt: Develop a smart contract that integrates a VIP membership tier system for token holders, inspired by Everlodge's private members club functionality.
Generated: DETERMINISTIC_38a63556bf8bb7ef
Batch ID: 20250612_145715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

// Smart Contract for a VIP Membership Tier System for Token Holders
contract VIPMembership {
    // Events to log activity
    event MembershipGranted(address indexed member, uint256 tier);
    event MembershipRevoked(address indexed member);
    event TierUpdated(address indexed member, uint256 newTier);

    // Struct to represent a member
    struct Member {
        uint256 tier; // VIP tier (e.g., 1 = Bronze, 2 = Silver, 3 = Gold, etc.)
        bool isActive; // Whether the membership is active
    }

    // Mapping to store members and their membership details
    mapping(address => Member) private members;

    // Owner of the contract
    address private owner;

    // Modifier to restrict access to contract owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    // Modifier to ensure the address is valid
    modifier validAddress(address _address) {
        require(_address != address(0), "Invalid address");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    // Function to grant a VIP membership to a user
    function grantMembership(address _member, uint256 _tier)
        external
        onlyOwner
        validAddress(_member)
    {
        require(_tier > 0, "Tier must be greater than zero");
        require(!members[_member].isActive, "Member already has an active membership");

        members[_member] = Member({
            tier: _tier,
            isActive: true
        });

        emit MembershipGranted(_member, _tier);
    }

    // Function to revoke a VIP membership from a user
    function revokeMembership(address _member)
        external
        onlyOwner
        validAddress(_member)
    {
        require(members[_member].isActive, "Member does not have an active membership");

        delete members[_member];
        emit MembershipRevoked(_member);
    }

    // Function to update the tier of an existing member
    function updateTier(address _member, uint256 _newTier)
        external
        onlyOwner
        validAddress(_member)
    {
        require(_newTier > 0, "Tier must be greater than zero");
        require(members[_member].isActive, "Member does not have an active membership");

        members[_member].tier = _newTier;
        emit TierUpdated(_member, _newTier);
    }

    // Public function to retrieve membership details for an address
    function getMembershipDetails(address _member)
        external
        view
        validAddress(_member)
        returns (uint256 tier, bool isActive)
    {
        Member memory member = members[_member];
        return (member.tier, member.isActive);
    }

    // Function to return the contract owner (useful for validation)
    function getOwner() external view returns (address) {
        return owner;
    }
}
```
