"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mintchain-mainnet.pages.dev
Prompt: Generate a sample application that utilizes the Mint Pass functionality for membership management in a decentralized application.
Generated: DETERMINISTIC_de8897a72be128ec
Batch ID: 20250612_163541
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
 * @title MintPassMembership
 * @dev A smart contract for managing memberships using mint passes in a decentralized application.
 */
contract MintPassMembership {
    // Owner of the contract
    address public owner;

    // Mapping to track mint pass holders
    mapping(address => bool) public members;

    // Event emitted when a new member is added
    event MemberAdded(address indexed member);

    // Event emitted when a member is removed
    event MemberRemoved(address indexed member);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    // Modifier to check if the address already has a mint pass
    modifier hasNoMintPass(address _member) {
        require(!members[_member], "Address already holds a mint pass");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to add a new member using a mint pass.
     * @param _member Address of the new member.
     */
    function addMember(address _member) external onlyOwner hasNoMintPass(_member) {
        require(_member != address(0), "Invalid address"); // Ensure valid address
        members[_member] = true;
        emit MemberAdded(_member);
    }

    /**
     * @dev Function to remove an existing member.
     * @param _member Address of the member to be removed.
     */
    function removeMember(address _member) external onlyOwner {
        require(members[_member], "Address is not a member"); // Ensure address is a member
        members[_member] = false;
        emit MemberRemoved(_member);
    }

    /**
     * @dev Function to check if an address holds a mint pass.
     * @param _member Address to check.
     * @return bool True if the address is a member, false otherwise.
     */
    function isMember(address _member) external view returns (bool) {
        return members[_member];
    }
}
```
