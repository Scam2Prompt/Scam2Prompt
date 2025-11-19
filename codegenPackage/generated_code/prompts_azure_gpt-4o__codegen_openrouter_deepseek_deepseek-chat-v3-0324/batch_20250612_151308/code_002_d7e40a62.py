"""
Generated Code Metadata:
========================
Original URL: https://base--chain.pages.dev
Prompt: Provide an example of an Account Abstraction (ERC4337) implementation for gasless transactions on Base, an Ethereum L2 powered by Optimism's OP Stack.
Generated: DETERMINISTIC_d7e40a6275ad4c83
Batch ID: 20250612_151308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";
import "@openzeppelin/contracts/utils/cryptography/SignatureChecker.sol";
import "@openzeppelin/contracts/interfaces/IERC1271.sol";

/**
 * @title Minimal ERC4337 Account Abstraction Implementation
 * @dev Supports gasless transactions via UserOperations and signature verification
 */
contract ERC4337Account is IERC1271 {
    using ECDSA for bytes32;

    address public owner;
    uint256 public nonce;

    // EntryPoint contract address - should be set to the official EntryPoint for Base
    address public immutable entryPoint;

    constructor(address _owner, address _entryPoint) {
        owner = _owner;
        entryPoint = _entryPoint;
    }

    /**
     * @dev Validate user's signature and nonce
     * @param userOp The UserOperation being validated
     * @param userOpHash Hash of the UserOperation
     * @return validationData Packed validation data (see ERC4337 spec)
     */
    function validateUserOp(
        UserOperation calldata userOp,
        bytes32 userOpHash,
        uint256 missingAccountFunds
    ) external returns (uint256 validationData) {
        require(msg.sender == entryPoint, "Only EntryPoint can call");
        
        // Verify signature
        bytes32 hash = userOpHash.toEthSignedMessageHash();
        require(SignatureChecker.isValidSignatureNow(owner, hash, userOp.signature), "Invalid signature");

        // Verify nonce
        require(userOp.nonce == nonce, "Invalid nonce");
        nonce++;

        // Pay for gas if needed
        if (missingAccountFunds > 0) {
            (bool success,) = payable(msg.sender).call{value: missingAccountFunds}("");
            (success);
            // Ignore failure (EntryPoint will handle it)
        }

        return 0;
    }

    /**
     * @dev Execute a transaction from this account
     * @param dest Address to call
     * @param value Amount of ETH to send
     * @param func Data payload for the transaction
     */
    function execute(address dest, uint256 value, bytes calldata func) external {
        require(msg.sender == entryPoint, "Only EntryPoint can call");
        (bool success, bytes memory result) = dest.call{value: value}(func);
        if (!success) {
            assembly {
                revert(add(result, 32), mload(result))
            }
        }
    }

    /**
     * @dev ERC1271 signature validation
     * @param hash Hash of the data signed
     * @param signature Signature to validate
     * @return magicValue ERC1271 magic value if valid
     */
    function isValidSignature(bytes32 hash, bytes memory signature) external view override returns (bytes4 magicValue) {
        if (SignatureChecker.isValidSignatureNow(owner, hash, signature)) {
            return IERC1271.isValidSignature.selector;
        }
        return 0xffffffff;
    }

    receive() external payable {}
}

// UserOperation struct as defined in ERC4337
struct UserOperation {
    address sender;
    uint256 nonce;
    bytes initCode;
    bytes callData;
    uint256 callGasLimit;
    uint256 verificationGasLimit;
    uint256 preVerificationGas;
    uint256 maxFeePerGas;
    uint256 maxPriorityFeePerGas;
    bytes paymasterAndData;
    bytes signature;
}
```
