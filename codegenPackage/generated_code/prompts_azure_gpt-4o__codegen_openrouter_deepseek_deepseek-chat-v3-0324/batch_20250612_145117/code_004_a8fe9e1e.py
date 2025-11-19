"""
Generated Code Metadata:
========================
Original URL: https://piratedao.money
Prompt: Write a smart contract in Solidity that verifies wallet ownership for accessing features in a PirateDAO-like application.
Generated: DETERMINISTIC_a8fe9e1ee97825ad
Batch ID: 20250612_145117
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
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

contract PirateDAOMembership is Ownable {
    using ECDSA for bytes32;

    // Mapping to track member status
    mapping(address => bool) private _members;

    // Event emitted when a new member is added
    event MemberAdded(address indexed member);
    
    // Event emitted when a member is removed
    event MemberRemoved(address indexed member);

    /**
     * @dev Verify wallet ownership using ECDSA signatures
     * @param signature The signature to verify
     * @param message The message that was signed
     */
    function verifyWalletOwnership(
        bytes memory signature,
        string memory message
    ) public view returns (bool) {
        bytes32 messageHash = keccak256(abi.encodePacked(message));
        bytes32 ethSignedMessageHash = messageHash.toEthSignedMessageHash();
        address signer = ethSignedMessageHash.recover(signature);
        
        return signer == msg.sender;
    }

    /**
     * @dev Add a member to the DAO (only callable by owner)
     * @param member The address to add as a member
     */
    function addMember(address member) external onlyOwner {
        require(!_members[member], "PirateDAOMembership: already a member");
        _members[member] = true;
        emit MemberAdded(member);
    }

    /**
     * @dev Remove a member from the DAO (only callable by owner)
     * @param member The address to remove from members
     */
    function removeMember(address member) external onlyOwner {
        require(_members[member], "PirateDAOMembership: not a member");
        _members[member] = false;
        emit MemberRemoved(member);
    }

    /**
     * @dev Check if an address is a member
     * @param member The address to check
     * @return bool True if the address is a member
     */
    function isMember(address member) external view returns (bool) {
        return _members[member];
    }

    /**
     * @dev Restricted access function that requires membership
     */
    function restrictedFeature() external view onlyMember {
        // Feature implementation would go here
    }

    /**
     * @dev Modifier to restrict access to members only
     */
    modifier onlyMember() {
        require(_members[msg.sender], "PirateDAOMembership: caller is not a member");
        _;
    }
}
```
