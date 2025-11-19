"""
Generated Code Metadata:
========================
Original URL: https://safergf.pages.dev
Prompt: Develop a guide for using Safe CORE Protocol Kit to create customizable smart contract accounts with transaction batching and battle-tested security.
Generated: DETERMINISTIC_c1a35a918e24012d
Batch ID: 20250622_210806
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

import "@safe-global/safe-contracts/contracts/Safe.sol";
import "@safe-global/safe-contracts/contracts/proxies/SafeProxyFactory.sol";
import "@safe-global/safe-contracts/contracts/libraries/MultiSend.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

/**
 * @title SafeCOREProtocolKit
 * @dev A utility contract for creating and managing Safe smart contract accounts
 * with transaction batching capabilities and enhanced security features.
 */
contract SafeCOREProtocolKit {
    using ECDSA for bytes32;

    SafeProxyFactory public immutable proxyFactory;
    address public immutable safeSingleton;
    MultiSend public immutable multiSend;

    /**
     * @dev Initializes the Protocol Kit with required Safe contracts
     * @param _proxyFactory Address of SafeProxyFactory contract
     * @param _safeSingleton Address of Safe master copy contract
     * @param _multiSend Address of MultiSend contract
     */
    constructor(
        address _proxyFactory,
        address _safeSingleton,
        address _multiSend
    ) {
        require(_proxyFactory != address(0), "Invalid proxy factory address");
        require(_safeSingleton != address(0), "Invalid singleton address");
        require(_multiSend != address(0), "Invalid multi-send address");

        proxyFactory = SafeProxyFactory(_proxyFactory);
        safeSingleton = _safeSingleton;
        multiSend = MultiSend(_multiSend);
    }

    /**
     * @dev Creates a new Safe account with specified owners and threshold
     * @param owners List of owner addresses
     * @param threshold Number of required confirmations
     * @param saltNonce Nonce for create2 salt
     * @return Address of the created Safe proxy
     */
    function createSafe(
        address[] memory owners,
        uint256 threshold,
        uint256 saltNonce
    ) external returns (address) {
        require(owners.length > 0, "At least one owner required");
        require(threshold > 0 && threshold <= owners.length, "Invalid threshold");

        bytes memory initializer = abi.encodeWithSignature(
            "setup(address[],uint256,address,bytes,address,address,uint256,address)",
            owners,
            threshold,
            address(0),
            "",
            address(0),
            address(0),
            0,
            address(0)
        );

        SafeProxy safe = proxyFactory.createProxyWithNonce(
            safeSingleton,
            initializer,
            saltNonce
        );

        return address(safe);
    }

    /**
     * @dev Creates a batched transaction for execution by a Safe
     * @param to List of target addresses
     * @param value List of ETH values to send
     * @param data List of calldata
     * @param operation List of operation types (0 for call, 1 for delegatecall)
     * @return Packed transaction data for MultiSend
     */
    function createBatchTransaction(
        address[] memory to,
        uint256[] memory value,
        bytes[] memory data,
        uint8[] memory operation
    ) external pure returns (bytes memory) {
        require(
            to.length == value.length &&
                value.length == data.length &&
                data.length == operation.length,
            "Array length mismatch"
        );

        bytes memory transactions;
        for (uint256 i = 0; i < to.length; i++) {
            transactions = abi.encodePacked(
                transactions,
                operation[i],
                to[i],
                value[i],
                data[i].length,
                data[i]
            );
        }

        return abi.encodeWithSignature("multiSend(bytes)", transactions);
    }

    /**
     * @dev Executes a batched transaction via Safe
     * @param safe Address of the Safe contract
     * @param transactions Packed transaction data from createBatchTransaction
     * @param signatures Signatures from Safe owners
     */
    function executeBatchTransaction(
        address safe,
        bytes memory transactions,
        bytes memory signatures
    ) external {
        require(safe != address(0), "Invalid Safe address");
        require(transactions.length > 0, "No transactions provided");

        Safe(payable(safe)).execTransaction(
            address(multiSend),
            0,
            transactions,
            Enum.Operation.DelegateCall,
            0,
            0,
            0,
            address(0),
            payable(address(0)),
            signatures
        );
    }

    /**
     * @dev Verifies signatures for a Safe transaction
     * @param safe Address of the Safe contract
     * @param txHash Transaction hash
     * @param signatures Concatenated signatures
     * @return Whether the signatures are valid
     */
    function verifySignatures(
        address safe,
        bytes32 txHash,
        bytes memory signatures
    ) external view returns (bool) {
        require(safe != address(0), "Invalid Safe address");
        require(signatures.length > 0, "No signatures provided");

        uint256 threshold = Safe(payable(safe)).getThreshold();
        address[] memory owners = Safe(payable(safe)).getOwners();

        address currentOwner;
        uint8 v;
        bytes32 r;
        bytes32 s;
        address lastOwner = address(0);
        uint256 validSignatures = 0;

        for (uint256 i = 0; i < threshold; i++) {
            (v, r, s) = signatureSplit(signatures, i);
            currentOwner = ecrecover(txHash, v, r, s);

            if (currentOwner <= lastOwner || !isOwner(owners, currentOwner)) {
                return false;
            }
            lastOwner = currentOwner;
            validSignatures++;
        }

        return validSignatures >= threshold;
    }

    /**
     * @dev Internal helper to check if address is an owner
     * @param owners List of owners
     * @param addr Address to check
     * @return Whether the address is an owner
     */
    function isOwner(address[] memory owners, address addr) internal pure returns (bool) {
        for (uint256 i = 0; i < owners.length; i++) {
            if (owners[i] == addr) {
                return true;
            }
        }
        return false;
    }

    /**
     * @dev Internal helper to split signature bytes
     * @param signatures Concatenated signatures
     * @param pos Position to split
     * @return v, r, s Signature components
     */
    function signatureSplit(bytes memory signatures, uint256 pos)
        internal
        pure
        returns (
            uint8 v,
            bytes32 r,
            bytes32 s
        )
    {
        assembly {
            let signaturePos := mul(0x41, pos)
            r := mload(add(signatures, add(signaturePos, 0x20)))
            s := mload(add(signatures, add(signaturePos, 0x40)))
            v := byte(0, mload(add(signatures, add(signaturePos, 0x60))))
        }
    }
}
```
