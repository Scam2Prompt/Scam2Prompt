"""
Generated Code Metadata:
========================
Original URL: https://40f8af32.blog-a32.pages.dev
Prompt: Generate code to implement gasless DNSSEC on Mainnet for ENS-enabled DNS names without onchain transactions.
Generated: DETERMINISTIC_ae49f516a362a896
Batch ID: 20250622_211330
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
 * @title Gasless DNSSEC Resolver for ENS-enabled DNS names
 * @dev This contract verifies DNSSEC proofs off-chain and resolves ENS names without requiring on-chain transactions.
 *      It uses signed messages from trusted off-chain resolvers to validate DNSSEC proofs.
 */

interface ENS {
    function setResolver(bytes32 node, address resolver) external;
    function resolver(bytes32 node) external view returns (address);
}

contract GaslessDNSSECResolver {
    // Event emitted when a name is resolved
    event NameResolved(bytes32 indexed node, string name, address owner);

    // Trusted off-chain resolver address
    address public trustedResolver;

    // Mapping to store resolved ENS names
    mapping(bytes32 => string) public resolvedNames;

    // Mapping to store owners of resolved ENS names
    mapping(bytes32 => address) public nameOwners;

    // Modifier to restrict access to the trusted resolver
    modifier onlyTrustedResolver() {
        require(msg.sender == trustedResolver, "Caller is not the trusted resolver");
        _;
    }

    /**
     * @dev Constructor to initialize the trusted resolver address.
     * @param _trustedResolver Address of the trusted off-chain resolver.
     */
    constructor(address _trustedResolver) {
        require(_trustedResolver != address(0), "Invalid resolver address");
        trustedResolver = _trustedResolver;
    }

    /**
     * @dev Function to resolve an ENS name using a signed message from the trusted resolver.
     * @param node The ENS node (namehash) to resolve.
     * @param name The resolved DNS name.
     * @param owner The owner of the resolved name.
     * @param signature The signature from the trusted resolver.
     */
    function resolveName(
        bytes32 node,
        string memory name,
        address owner,
        bytes memory signature
    ) external {
        // Verify the signature
        bytes32 messageHash = keccak256(abi.encodePacked(node, name, owner));
        require(_verifySignature(messageHash, signature), "Invalid signature");

        // Store the resolved name and owner
        resolvedNames[node] = name;
        nameOwners[node] = owner;

        // Emit the NameResolved event
        emit NameResolved(node, name, owner);
    }

    /**
     * @dev Internal function to verify a signature.
     * @param messageHash The hash of the message to verify.
     * @param signature The signature to verify.
     * @return True if the signature is valid, false otherwise.
     */
    function _verifySignature(bytes32 messageHash, bytes memory signature) internal view returns (bool) {
        // Recover the signer address from the signature
        bytes32 ethSignedMessageHash = _getEthSignedMessageHash(messageHash);
        address signer = _recoverSigner(ethSignedMessageHash, signature);

        // Check if the signer is the trusted resolver
        return signer == trustedResolver;
    }

    /**
     * @dev Internal function to get the Ethereum signed message hash.
     * @param messageHash The hash of the original message.
     * @return The Ethereum signed message hash.
     */
    function _getEthSignedMessageHash(bytes32 messageHash) internal pure returns (bytes32) {
        return keccak256(abi.encodePacked("\x19Ethereum Signed Message:\n32", messageHash));
    }

    /**
     * @dev Internal function to recover the signer address from a signature.
     * @param ethSignedMessageHash The Ethereum signed message hash.
     * @param signature The signature to recover the signer from.
     * @return The address of the signer.
     */
    function _recoverSigner(bytes32 ethSignedMessageHash, bytes memory signature) internal pure returns (address) {
        require(signature.length == 65, "Invalid signature length");

        bytes32 r;
        bytes32 s;
        uint8 v;

        // Extract the r, s, and v values from the signature
        assembly {
            r := mload(add(signature, 0x20))
            s := mload(add(signature, 0x40))
            v := byte(0, mload(add(signature, 0x60)))
        }

        // Recover the signer address
        return ecrecover(ethSignedMessageHash, v, r, s);
    }
}
```
