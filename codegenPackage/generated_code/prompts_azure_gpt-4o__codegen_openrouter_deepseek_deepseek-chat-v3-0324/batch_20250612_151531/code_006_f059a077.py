"""
Generated Code Metadata:
========================
Original URL: https://ziber.io
Prompt: Write a smart contract in Solidity that redirects VOIP calls from mobile phones to a blockchain-based system, as described in Ziber's decentralized masternode system.
Generated: DETERMINISTIC_f059a077f31db6b7
Batch ID: 20250612_151531
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
 * @title VoIP Call Redirector
 * @dev Smart contract for redirecting VoIP calls to a blockchain-based system
 */
contract VoIPCallRedirector {
    // Struct to store call routing information
    struct CallRoute {
        address caller;
        address callee;
        uint256 timestamp;
        string sipAddress;
        bool isActive;
    }

    // Mapping from call ID to CallRoute
    mapping(bytes32 => CallRoute) public callRoutes;

    // Mapping from user address to SIP address
    mapping(address => string) public userSipAddresses;

    // Events
    event CallInitiated(
        bytes32 indexed callId,
        address indexed caller,
        address indexed callee,
        string sipAddress,
        uint256 timestamp
    );
    event CallRedirected(
        bytes32 indexed callId,
        address indexed caller,
        address indexed callee,
        string sipAddress,
        uint256 timestamp
    );
    event CallEnded(bytes32 indexed callId, uint256 timestamp);
    event SipAddressRegistered(address indexed user, string sipAddress);

    // Modifiers
    modifier onlyRegisteredUser(address user) {
        require(
            bytes(userSipAddresses[user]).length > 0,
            "User not registered with SIP address"
        );
        _;
    }

    /**
     * @dev Register a SIP address for the caller
     * @param sipAddress The SIP address to register
     */
    function registerSipAddress(string memory sipAddress) external {
        require(bytes(sipAddress).length > 0, "SIP address cannot be empty");
        userSipAddresses[msg.sender] = sipAddress;
        emit SipAddressRegistered(msg.sender, sipAddress);
    }

    /**
     * @dev Initiate a call and create a call route
     * @param callee The address of the callee
     * @return callId The unique identifier for this call
     */
    function initiateCall(address callee)
        external
        onlyRegisteredUser(msg.sender)
        onlyRegisteredUser(callee)
        returns (bytes32 callId)
    {
        callId = keccak256(
            abi.encodePacked(msg.sender, callee, block.timestamp)
        );

        require(
            callRoutes[callId].caller == address(0),
            "Call with this ID already exists"
        );

        callRoutes[callId] = CallRoute({
            caller: msg.sender,
            callee: callee,
            timestamp: block.timestamp,
            sipAddress: userSipAddresses[callee],
            isActive: true
        });

        emit CallInitiated(
            callId,
            msg.sender,
            callee,
            userSipAddresses[callee],
            block.timestamp
        );
    }

    /**
     * @dev Redirect an existing call
     * @param callId The ID of the call to redirect
     * @param newSipAddress The new SIP address to redirect to
     */
    function redirectCall(bytes32 callId, string memory newSipAddress)
        external
        onlyRegisteredUser(msg.sender)
    {
        CallRoute storage route = callRoutes[callId];
        require(route.isActive, "Call is not active");
        require(
            route.callee == msg.sender,
            "Only callee can redirect the call"
        );
        require(bytes(newSipAddress).length > 0, "SIP address cannot be empty");

        route.sipAddress = newSipAddress;
        emit CallRedirected(
            callId,
            route.caller,
            route.callee,
            newSipAddress,
            block.timestamp
        );
    }

    /**
     * @dev End an active call
     * @param callId The ID of the call to end
     */
    function endCall(bytes32 callId) external {
        CallRoute storage route = callRoutes[callId];
        require(route.isActive, "Call is not active");
        require(
            route.caller == msg.sender || route.callee == msg.sender,
            "Only call participants can end the call"
        );

        route.isActive = false;
        emit CallEnded(callId, block.timestamp);
    }

    /**
     * @dev Get call routing information
     * @param callId The ID of the call
     * @return CallRoute The call routing information
     */
    function getCallRoute(bytes32 callId)
        external
        view
        returns (CallRoute memory)
    {
        return callRoutes[callId];
    }
}
```
