"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://base--chain.pages.dev
Prompt: Provide an example of an Account Abstraction (ERC4337) implementation for gasless transactions on Base, an Ethereum L2 powered by Optimism's OP Stack.
Generated: DETERMINISTIC_d7e40a6275ad4c83
Batch ID: 20250612_151308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title SimpleAccount
 * @dev An example implementation of an ERC-4337 Account abstraction for gasless transactions.
 * This contract is designed to be compatible with Base, an Ethereum L2 powered by Optimism's OP Stack.
 * For simplicity, this implementation assumes a single signer (owner) model.
 */

import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/interfaces/IERC1271.sol";

interface IEntryPoint {
    function handleOps(bytes calldata userOp, address payable beneficiary) external;
}

contract SimpleAccount is Ownable, IERC1271 {
    using ECDSA for bytes32;

    // Address of the EntryPoint contract (the central point for handling operations)
    IEntryPoint public immutable entryPoint;

    /**
     * @dev Constructor to initialize the contract with the EntryPoint address.
     * @param _entryPoint Address of the EntryPoint contract.
     * @param _owner Address of the owner of the account.
     */
    constructor(IEntryPoint _entryPoint, address _owner) {
        entryPoint = _entryPoint;
        transferOwnership(_owner);
    }

    /**
     * @dev Execute a transaction called by the EntryPoint.
     * This allows the EntryPoint to call user-defined logic from this account.
     * Note: This function will typically execute operations requested in the UserOperation struct sent by EntryPoint.
     * @param to Address to call.
     * @param value Value (ETH) to send.
     * @param data Call data to send.
     */
    function executeTransaction(
        address to,
        uint256 value,
        bytes calldata data
    ) external onlyEntryPoint {
        require(to != address(0), "Invalid target address");

        // Execute the call and revert if it fails
        (bool success,) = to.call{value: value}(data);
        require(success, "Transaction failed");
    }

    /**
     * @dev Verify that a given signature belongs to the owner of this account.
     * This is part of the ERC-1271 standard and is used by the EntryPoint to verify UserOperation signatures.
     * @param hash The hashed message to verify.
     * @param signature The signature to verify.
     * @return Magic value indicating whether the signature is valid.
     */
    function isValidSignature(bytes32 hash, bytes memory signature) external view override returns (bytes4) {
        address signer = hash.recover(signature);
        return (signer == owner()) ? IERC1271.isValidSignature.selector : bytes4(0);
    }

    /**
     * @notice Modifier to restrict function calls to the EntryPoint.
     */
    modifier onlyEntryPoint() {
        require(msg.sender == address(entryPoint), "Caller is not EntryPoint");
        _;
    }

    /**
     * @dev Allow the contract to receive ETH (for funding purposes).
     */
    receive() external payable {}
}
```

Note: Deploy the `SimpleAccount` contract with a valid EntryPoint contract address on Base (Optimism L2) and ensure the contract's owner is correctly set.
