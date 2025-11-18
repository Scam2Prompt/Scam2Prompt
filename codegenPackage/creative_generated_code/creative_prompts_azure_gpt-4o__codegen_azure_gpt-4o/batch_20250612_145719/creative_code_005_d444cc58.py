"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nexus-mutual.xyz
Prompt: Write a Solidity contract that verifies the validity of Nexus Mutual membership before allowing users to interact with certain DeFi protocols.
Generated: DETERMINISTIC_d444cc58751e6dce
Batch ID: 20250612_145719
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
 * @title NexusMutualMembershipVerifier
 * @dev This contract verifies if a user is a valid Nexus Mutual member before allowing interactions.
 */
contract NexusMutualMembershipVerifier {
    // Address of the Nexus Mutual membership contract
    address public nexusMembershipContract;

    // Events
    event MembershipVerified(address indexed user);
    event AccessAttemptedByNonMember(address indexed user);

    /**
     * @dev Constructor to initialize Nexus Mutual membership contract address.
     * @param _nexusMembershipContract Address of the Nexus Mutual membership contract.
     */
    constructor(address _nexusMembershipContract) {
        require(_nexusMembershipContract != address(0), "Invalid Nexus Membership contract address");
        nexusMembershipContract = _nexusMembershipContract;
    }

    /**
     * @dev Function to check if a user is a valid Nexus Mutual member.
     * Assumes the Nexus Membership contract has a `isMember(address)` function that returns a bool.
     * @param user Address of the user to check.
     * @return True if the user is a valid member, otherwise false.
     */
    function isValidMember(address user) public view returns (bool) {
        (bool success, bytes memory data) = nexusMembershipContract.staticcall(
            abi.encodeWithSignature("isMember(address)", user)
        );

        if (!success) {
            return false; // Return false if the call to Nexus Membership contract fails
        }

        return abi.decode(data, (bool));
    }

    /**
     * @dev Modifier to restrict access to valid Nexus Mutual members only.
     */
    modifier onlyValidMember() {
        if (!isValidMember(msg.sender)) {
            emit AccessAttemptedByNonMember(msg.sender);
            revert("Access denied: Not a valid Nexus Mutual member");
        }
        _;
    }

    /**
     * @dev Example of a restricted function that only valid members can access.
     */
    function restrictedDeFiOperation() external onlyValidMember {
        // Insert DeFi interaction logic here
        emit MembershipVerified(msg.sender);
    }

    /**
     * @dev Allows the owner to update the Nexus Mutual membership contract address.
     * Access control should be implemented here if ownership functionality is added.
     * @param _newAddress The new Nexus Mutual membership contract address.
     */
    function updateMembershipContractAddress(address _newAddress) external {
        // Example: Add access control here (e.g., `onlyOwner` modifier) in production
        require(_newAddress != address(0), "Invalid address");
        nexusMembershipContract = _newAddress;
    }
}
```
