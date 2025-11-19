"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dop-io.web.app
Prompt: Generate an example of a smart contract that utilizes the Data Ownership Protocol's features for customized data disclosure permissions.
Generated: DETERMINISTIC_e66b57ac57883865
Batch ID: 20250612_140250
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
 * @title DataOwnershipProtocol
 * @dev A smart contract to manage data disclosure permissions.
 */
contract DataOwnershipProtocol {
    // Struct to represent a data access request
    struct AccessRequest {
        address requester; // Address requesting data access
        string purpose;    // Purpose of the data request
        bool approved;     // Approval status of the request
    }

    // Owner of the data
    address public dataOwner;

    // Mapping to store permissions for each requester
    mapping(address => AccessRequest) public accessRequests;

    // Event emitted when a new access request is submitted
    event AccessRequested(address indexed requester, string purpose);

    // Event emitted when an access request is approved
    event AccessApproved(address indexed requester);

    // Event emitted when an access request is revoked
    event AccessRevoked(address indexed requester);

    /**
     * @dev Modifier to restrict certain functions to the data owner.
     */
    modifier onlyDataOwner() {
        require(msg.sender == dataOwner, "Only the data owner can perform this action.");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the data owner.
     */
    constructor() {
        dataOwner = msg.sender; // Set the deployer as the data owner
    }

    /**
     * @dev Function for a user to request access to the data.
     * @param _purpose Purpose of the data request.
     */
    function requestAccess(string memory _purpose) external {
        require(bytes(_purpose).length > 0, "Purpose cannot be empty.");
        require(accessRequests[msg.sender].requester == address(0), "You have already submitted a request.");

        // Create a new access request
        accessRequests[msg.sender] = AccessRequest({
            requester: msg.sender,
            purpose: _purpose,
            approved: false
        });

        emit AccessRequested(msg.sender, _purpose);
    }

    /**
     * @dev Function for the data owner to approve a data access request.
     * @param _requester Address of the requester.
     */
    function approveAccess(address _requester) external onlyDataOwner {
        AccessRequest storage request = accessRequests[_requester];
        require(request.requester != address(0), "No access request found for this address.");
        require(!request.approved, "Access request is already approved.");

        // Approve the access request
        request.approved = true;
        emit AccessApproved(_requester);
    }

    /**
     * @dev Function for the data owner to revoke access from a requester.
     * @param _requester Address of the requester.
     */
    function revokeAccess(address _requester) external onlyDataOwner {
        AccessRequest storage request = accessRequests[_requester];
        require(request.requester != address(0), "No access request found for this address.");
        require(request.approved, "Access has not been granted to this requester.");

        // Remove the access approval
        request.approved = false;
        emit AccessRevoked(_requester);
    }

    /**
     * @dev Function for a requester to check if their access has been approved.
     * @return bool Returns true if access is approved, false otherwise.
     */
    function hasAccess() external view returns (bool) {
        AccessRequest memory request = accessRequests[msg.sender];
        return request.approved;
    }

    /**
     * @dev Function for the data owner to transfer ownership of the data to another address.
     * @param _newOwner Address of the new data owner.
     */
    function transferOwnership(address _newOwner) external onlyDataOwner {
        require(_newOwner != address(0), "New owner address cannot be zero.");
        dataOwner = _newOwner;
    }
}
```
