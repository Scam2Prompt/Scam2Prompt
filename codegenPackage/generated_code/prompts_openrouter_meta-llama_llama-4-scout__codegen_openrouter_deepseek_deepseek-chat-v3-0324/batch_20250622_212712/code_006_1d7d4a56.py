"""
Generated Code Metadata:
========================
Original URL: https://claires.pages.dev
Prompt: How does Symbiotic's permissionless and immutable core contract enable builders to have choice and control over shared security agreements, and what are the implications for decentralized network architecture?
Generated: DETERMINISTIC_1d7d4a56500a1df4
Batch ID: 20250622_212712
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
 * @title SymbioticCoreContract
 * @dev A permissionless and immutable core contract enabling builders to create and manage
 * shared security agreements with full control and choice.
 */
contract SymbioticCoreContract {
    // Struct representing a shared security agreement
    struct SecurityAgreement {
        address builder;
        address securityProvider;
        uint256 stakeAmount;
        uint256 duration;
        bool isActive;
        uint256 createdAt;
    }

    // Mapping of agreement IDs to SecurityAgreement
    mapping(bytes32 => SecurityAgreement) public agreements;

    // Event emitted when a new agreement is created
    event AgreementCreated(
        bytes32 indexed agreementId,
        address indexed builder,
        address indexed securityProvider,
        uint256 stakeAmount,
        uint256 duration
    );

    // Event emitted when an agreement is terminated
    event AgreementTerminated(bytes32 indexed agreementId);

    /**
     * @dev Creates a new shared security agreement
     * @param securityProvider The address providing security
     * @param stakeAmount The amount staked for security
     * @param duration The duration of the agreement in seconds
     * @return agreementId The ID of the created agreement
     */
    function createAgreement(
        address securityProvider,
        uint256 stakeAmount,
        uint256 duration
    ) external returns (bytes32 agreementId) {
        require(securityProvider != address(0), "Invalid security provider");
        require(stakeAmount > 0, "Stake amount must be positive");
        require(duration > 0, "Duration must be positive");

        agreementId = keccak256(
            abi.encodePacked(
                msg.sender,
                securityProvider,
                stakeAmount,
                duration,
                block.timestamp
            )
        );

        agreements[agreementId] = SecurityAgreement({
            builder: msg.sender,
            securityProvider: securityProvider,
            stakeAmount: stakeAmount,
            duration: duration,
            isActive: true,
            createdAt: block.timestamp
        });

        emit AgreementCreated(
            agreementId,
            msg.sender,
            securityProvider,
            stakeAmount,
            duration
        );

        return agreementId;
    }

    /**
     * @dev Terminates an existing agreement
     * @param agreementId The ID of the agreement to terminate
     */
    function terminateAgreement(bytes32 agreementId) external {
        SecurityAgreement storage agreement = agreements[agreementId];
        require(agreement.isActive, "Agreement not active");
        require(
            msg.sender == agreement.builder ||
                msg.sender == agreement.securityProvider,
            "Only builder or security provider can terminate"
        );

        agreement.isActive = false;
        emit AgreementTerminated(agreementId);
    }

    /**
     * @dev Checks if an agreement is valid and active
     * @param agreementId The ID of the agreement to check
     * @return isValid True if the agreement is valid and active
     */
    function isAgreementValid(bytes32 agreementId) external view returns (bool isValid) {
        SecurityAgreement storage agreement = agreements[agreementId];
        isValid =
            agreement.isActive &&
            block.timestamp < (agreement.createdAt + agreement.duration);
        return isValid;
    }

    /**
     * @dev Gets agreement details
     * @param agreementId The ID of the agreement
     * @return agreement The SecurityAgreement struct
     */
    function getAgreement(bytes32 agreementId)
        external
        view
        returns (SecurityAgreement memory agreement)
    {
        return agreements[agreementId];
    }
}
```
