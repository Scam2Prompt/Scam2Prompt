"""
Generated Code Metadata:
========================
Original URL: https://nexus-mutual.xyz
Prompt: Write a Solidity contract that verifies the validity of Nexus Mutual membership before allowing users to interact with certain DeFi protocols.
Generated: DETERMINISTIC_d444cc58751e6dce
Batch ID: 20250612_145719
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

// Interface for Nexus Mutual Membership contract
interface INexusMutual {
    function isMember(address _user) external view returns (bool);
}

/**
 * @title DeFi Protocol with Nexus Mutual Membership Verification
 * @dev Contract that restricts certain functions to Nexus Mutual members only
 */
contract NexusMutualProtectedProtocol {
    INexusMutual public immutable nexusMutual;
    address public admin;

    // Mapping to track allowed protocols
    mapping(address => bool) public allowedProtocols;

    // Events
    event ProtocolAdded(address indexed protocol);
    event ProtocolRemoved(address indexed protocol);
    event AdminChanged(address indexed newAdmin);

    // Errors
    error NotNexusMutualMember();
    error NotAdmin();
    error ProtocolAlreadyExists();
    error ProtocolDoesNotExist();

    /**
     * @dev Constructor sets the Nexus Mutual contract address and initial admin
     * @param _nexusMutualAddress Address of the Nexus Mutual membership contract
     */
    constructor(address _nexusMutualAddress) {
        require(_nexusMutualAddress != address(0), "Invalid Nexus Mutual address");
        nexusMutual = INexusMutual(_nexusMutualAddress);
        admin = msg.sender;
    }

    modifier onlyAdmin() {
        if (msg.sender != admin) revert NotAdmin();
        _;
    }

    modifier onlyNexusMutualMember() {
        if (!nexusMutual.isMember(msg.sender)) revert NotNexusMutualMember();
        _;
    }

    modifier onlyAllowedProtocol(address _protocol) {
        require(allowedProtocols[_protocol], "Protocol not allowed");
        _;
    }

    /**
     * @dev Change the admin of the contract
     * @param _newAdmin Address of the new admin
     */
    function changeAdmin(address _newAdmin) external onlyAdmin {
        require(_newAdmin != address(0), "Invalid admin address");
        admin = _newAdmin;
        emit AdminChanged(_newAdmin);
    }

    /**
     * @dev Add a new protocol to the allowed list
     * @param _protocol Address of the protocol to add
     */
    function addProtocol(address _protocol) external onlyAdmin {
        if (allowedProtocols[_protocol]) revert ProtocolAlreadyExists();
        allowedProtocols[_protocol] = true;
        emit ProtocolAdded(_protocol);
    }

    /**
     * @dev Remove a protocol from the allowed list
     * @param _protocol Address of the protocol to remove
     */
    function removeProtocol(address _protocol) external onlyAdmin {
        if (!allowedProtocols[_protocol]) revert ProtocolDoesNotExist();
        allowedProtocols[_protocol] = false;
        emit ProtocolRemoved(_protocol);
    }

    /**
     * @dev Protected function that can only be called by Nexus Mutual members
     * @param _protocol Address of the protocol being interacted with
     */
    function interactWithProtocol(address _protocol) 
        external 
        onlyNexusMutualMember 
        onlyAllowedProtocol(_protocol) 
    {
        // Implementation of protocol interaction would go here
        // This is a placeholder for the actual interaction logic
    }

    /**
     * @dev Check if a user is a Nexus Mutual member
     * @param _user Address of the user to check
     * @return bool True if user is a member, false otherwise
     */
    function isNexusMutualMember(address _user) external view returns (bool) {
        return nexusMutual.isMember(_user);
    }
}
```
