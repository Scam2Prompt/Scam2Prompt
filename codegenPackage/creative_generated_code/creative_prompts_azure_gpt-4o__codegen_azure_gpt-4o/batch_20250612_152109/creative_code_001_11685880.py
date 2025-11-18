"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ronin-cyberkongz.pages.dev
Prompt: Generate code for an on-chain two-factor authentication system similar to the Guardian Contract used in the CyberKongz ecosystem.
Generated: DETERMINISTIC_11685880fcce020d
Batch ID: 20250612_152109
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
 * @title TwoFactorAuth
 * @dev Implements an on-chain two-factor authentication system similar to Guardian Contract
 * used in the CyberKongz ecosystem.
 */
contract TwoFactorAuth {
    // State variables
    address public owner; // The primary owner of the contract
    address public guardian; // The secondary guardian address for two-factor authentication

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    /**
     * @dev Modifier to restrict access to the guardian.
     */
    modifier onlyGuardian() {
        require(msg.sender == guardian, "Only guardian can perform this action");
        _;
    }

    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    event GuardianChanged(address indexed previousGuardian, address indexed newGuardian);

    /**
     * @dev Constructor to initialize the contract with the owner and guardian.
     * @param _owner The address of the owner.
     * @param _guardian The address of the guardian.
     */
    constructor(address _owner, address _guardian) {
        require(_owner != address(0), "Owner address cannot be zero");
        require(_guardian != address(0), "Guardian address cannot be zero");

        owner = _owner;
        guardian = _guardian;
    }

    /**
     * @dev Function to change the owner with guardian confirmation.
     * @param _newOwner The address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyGuardian {
        require(_newOwner != address(0), "New owner address cannot be zero");
        require(_newOwner != owner, "New owner must be different to the current owner");

        address previousOwner = owner;
        owner = _newOwner;

        emit OwnershipTransferred(previousOwner, _newOwner);
    }

    /**
     * @dev Function to change the guardian address.
     * @param _newGuardian The address of the new guardian.
     */
    function changeGuardian(address _newGuardian) external onlyOwner {
        require(_newGuardian != address(0), "New guardian address cannot be zero");
        require(_newGuardian != guardian, "New guardian must be different to the current guardian");

        address previousGuardian = guardian;
        guardian = _newGuardian;

        emit GuardianChanged(previousGuardian, _newGuardian);
    }

    /**
     * @dev Function to recover ownership in case the owner is compromised (guardian can perform this action).
     * @param _recoveryOwner The address to transfer ownership to during recovery.
     */
    function recoverOwnership(address _recoveryOwner) external onlyGuardian {
        require(_recoveryOwner != address(0), "Recovery owner address cannot be zero");

        address previousOwner = owner;
        owner = _recoveryOwner;

        emit OwnershipTransferred(previousOwner, _recoveryOwner);
    }

    /**
     * @dev Function to check the current owner and guardian addresses.
     * @return The owner and guardian addresses.
     */
    function getStatus() external view returns (address, address) {
        return (owner, guardian);
    }
}
```
