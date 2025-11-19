"""
Generated Code Metadata:
========================
Original URL: https://scrollnetwork-dashboard.pages.dev
Prompt: Describe the process of migrating an Ethereum app to Scroll while maintaining bytecode-level compatibility.
Generated: DETERMINISTIC_a2f22a787ad420cb
Batch ID: 20250612_161035
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
 * @title Scroll Migration Helper
 * @dev Provides utilities for migrating Ethereum contracts to Scroll while maintaining bytecode compatibility
 */
contract ScrollMigrationHelper {
    // Address of the Scroll L2 bridge contract
    address public immutable scrollBridge;

    // Mapping to track migrated contracts (Ethereum address => Scroll address)
    mapping(address => address) public migratedContracts;

    event ContractMigrated(address indexed ethAddress, address indexed scrollAddress);

    /**
     * @dev Constructor sets the Scroll bridge address
     * @param _scrollBridge Address of the Scroll bridge contract
     */
    constructor(address _scrollBridge) {
        require(_scrollBridge != address(0), "Invalid bridge address");
        scrollBridge = _scrollBridge;
    }

    /**
     * @dev Verifies bytecode compatibility between Ethereum and Scroll contracts
     * @param ethAddress Address of the Ethereum contract
     * @param scrollAddress Address of the Scroll contract
     * @return isCompatible True if bytecode is compatible
     */
    function verifyBytecodeCompatibility(
        address ethAddress,
        address scrollAddress
    ) public view returns (bool isCompatible) {
        bytes memory ethCode = _getCode(ethAddress);
        bytes memory scrollCode = _getCode(scrollAddress);
        
        // Compare bytecode (excluding metadata which may differ)
        uint256 minLength = ethCode.length < scrollCode.length ? ethCode.length : scrollCode.length;
        for (uint256 i = 0; i < minLength; i++) {
            // Skip metadata comparison (last 2 bytes of length)
            if (i >= minLength - 2) continue;
            if (ethCode[i] != scrollCode[i]) {
                return false;
            }
        }
        return true;
    }

    /**
     * @dev Registers a migrated contract after verifying bytecode compatibility
     * @param ethAddress Address of the Ethereum contract
     * @param scrollAddress Address of the Scroll contract
     */
    function registerMigratedContract(
        address ethAddress,
        address scrollAddress
    ) external {
        require(msg.sender == scrollBridge, "Only bridge can register");
        require(verifyBytecodeCompatibility(ethAddress, scrollAddress), "Bytecode mismatch");
        
        migratedContracts[ethAddress] = scrollAddress;
        emit ContractMigrated(ethAddress, scrollAddress);
    }

    /**
     * @dev Internal helper to get contract code
     * @param addr Address to get code from
     * @return code The contract bytecode
     */
    function _getCode(address addr) internal view returns (bytes memory code) {
        assembly {
            // Retrieve the size of the code
            let size := extcodesize(addr)
            // Allocate output byte array
            code := mload(0x40)
            // New "memory end" including padding
            mstore(0x40, add(code, and(add(add(size, 0x20), 0x1f), not(0x1f))))
            // Store length in memory
            mstore(code, size)
            // Copy the code
            extcodecopy(addr, add(code, 0x20), 0, size)
        }
    }

    /**
     * @dev Gets the Scroll address for a migrated Ethereum contract
     * @param ethAddress Address of the Ethereum contract
     * @return scrollAddress Corresponding Scroll address if migrated
     */
    function getScrollAddress(address ethAddress) external view returns (address scrollAddress) {
        scrollAddress = migratedContracts[ethAddress];
        require(scrollAddress != address(0), "Contract not migrated");
    }
}

/**
 * @title Scroll-Compatible Contract Template
 * @dev Base contract for Scroll migration with L1/L2 awareness
 */
abstract contract ScrollCompatible {
    address public immutable l1Address;
    bool public isL2;

    constructor(address _l1Address) {
        l1Address = _l1Address;
        // Detect if we're on L2 by checking if L1 address is 0 (or other chain-specific check)
        isL2 = _l1Address == address(0);
    }

    /**
     * @dev Modifier to restrict function to L1 only
     */
    modifier onlyL1() {
        require(!isL2, "L2 only");
        _;
    }

    /**
     * @dev Modifier to restrict function to L2 only
     */
    modifier onlyL2() {
        require(isL2, "L1 only");
        _;
    }
}
```
