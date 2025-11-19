"""
Generated Code Metadata:
========================
Original URL: https://toto1m.pages.dev
Prompt: Develop a smart contract that integrates with the POON ecosystem, highlighting the partnerships and community aspects discussed on the site.
Generated: DETERMINISTIC_41ab7e95981f020f
Batch ID: 20250612_162207
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
 * @title POON Ecosystem Smart Contract
 * @dev This contract integrates with the POON ecosystem, highlighting partnerships and community aspects.
 */
contract POONEcosystem {
    // Address of the contract owner
    address public owner;

    // Struct to represent a partnership
    struct Partnership {
        string name; // Name of the partner
        string description; // Description of the partnership
        string website; // Website of the partner
        bool active; // Status of the partnership
    }

    // Array to store all partnerships
    Partnership[] public partnerships;

    // Mapping to track community members
    mapping(address => bool) public communityMembers;

    // Event emitted when a new partnership is added
    event PartnershipAdded(string name, string description, string website);

    // Event emitted when a community member is added
    event CommunityMemberAdded(address member);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to add a new partnership to the ecosystem.
     * @param _name Name of the partner.
     * @param _description Description of the partnership.
     * @param _website Website of the partner.
     */
    function addPartnership(
        string memory _name,
        string memory _description,
        string memory _website
    ) public onlyOwner {
        partnerships.push(Partnership(_name, _description, _website, true));
        emit PartnershipAdded(_name, _description, _website);
    }

    /**
     * @dev Function to deactivate a partnership.
     * @param _index Index of the partnership in the array.
     */
    function deactivatePartnership(uint256 _index) public onlyOwner {
        require(_index < partnerships.length, "Invalid partnership index");
        partnerships[_index].active = false;
    }

    /**
     * @dev Function to add a community member to the ecosystem.
     * @param _member Address of the community member.
     */
    function addCommunityMember(address _member) public onlyOwner {
        require(!communityMembers[_member], "Member is already part of the community");
        communityMembers[_member] = true;
        emit CommunityMemberAdded(_member);
    }

    /**
     * @dev Function to check if an address is a community member.
     * @param _member Address to check.
     * @return bool True if the address is a community member, false otherwise.
     */
    function isCommunityMember(address _member) public view returns (bool) {
        return communityMembers[_member];
    }

    /**
     * @dev Function to get the total number of partnerships.
     * @return uint256 Total number of partnerships.
     */
    function getPartnershipCount() public view returns (uint256) {
        return partnerships.length;
    }

    /**
     * @dev Function to retrieve partnership details by index.
     * @param _index Index of the partnership in the array.
     * @return Partnership Struct containing partnership details.
     */
    function getPartnership(uint256 _index) public view returns (Partnership memory) {
        require(_index < partnerships.length, "Invalid partnership index");
        return partnerships[_index];
    }
}
```
