"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dop-io.web.app
Prompt: Provide an example of how to use DOP for selective disclosure of ERC721 token ownership in an Ethereum-based marketplace.
Generated: DETERMINISTIC_4730755312de2624
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title ERC721 Ownership Disclosure Contract
 * @dev This contract enables selective disclosure of ERC721 token ownership
 *      using Delegated Ownership Proof (DOP) for use in an Ethereum-based marketplace.
 */

interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
}

contract OwnershipDisclosure {
    // Event emitted when a proof of ownership is created
    event OwnershipProofCreated(
        address indexed tokenContract,
        uint256 indexed tokenId,
        address indexed owner,
        uint256 nonce,
        bytes proof
    );

    // Mapping to store nonces per owner for uniqueness
    mapping(address => uint256) private nonces;

    /**
     * @notice Generates a proof of ownership for a specific ERC721 token.
     * @param tokenContract Address of the ERC721 contract.
     * @param tokenId ID of the token to disclose ownership of.
     * @return proof A signature proving ownership of the token.
     */
    function generateOwnershipProof(address tokenContract, uint256 tokenId)
        external
        returns (bytes memory proof)
    {
        // Ensure the tokenContract address is valid
        require(tokenContract != address(0), "Invalid token contract address");

        // Confirm ownership of the token
        address tokenOwner = IERC721(tokenContract).ownerOf(tokenId);
        require(tokenOwner == msg.sender, "Caller is not the owner of the token");

        // Increment nonce to ensure uniqueness of the proof
        uint256 nonce = getNonce(msg.sender);
        nonces[msg.sender]++;

        // Create the message hash for signing
        bytes32 messageHash = keccak256(abi.encodePacked(tokenContract, tokenId, tokenOwner, nonce));
        bytes32 ethSignedMessageHash = getEthSignedMessageHash(messageHash);

        // Generate the signature (proof)
        proof = signMessage(ethSignedMessageHash);

        // Emit the event for ownership disclosure
        emit OwnershipProofCreated(tokenContract, tokenId, tokenOwner, nonce, proof);

        return proof;
    }

    /**
     * @notice Verifies the ownership proof provided.
     * @param tokenContract Address of the ERC721 contract.
     * @param tokenId ID of the token for verification.
     * @param owner Claimed owner of the token.
     * @param nonce Nonce used in proof generation.
     * @param proof Signature proof to verify.
     * @return isValid True if the proof is valid, false otherwise.
     */
    function verifyOwnershipProof(
        address tokenContract,
        uint256 tokenId,
        address owner,
        uint256 nonce,
        bytes memory proof
    ) external pure returns (bool isValid) {
        // Ensure the tokenContract address is valid
        require(tokenContract != address(0), "Invalid token contract address");

        // Recreate the message hash
        bytes32 messageHash = keccak256(abi.encodePacked(tokenContract, tokenId, owner, nonce));
        bytes32 ethSignedMessageHash = getEthSignedMessageHash(messageHash);

        // Extract the signer from the provided proof
        address signer = recoverSigner(ethSignedMessageHash, proof);

        // Validate that the signer matches the claimed owner
        isValid = (signer == owner);
        return isValid;
    }

    /**
     * @notice Retrieves the nonce for a specific owner.
     * @param owner Address of the token owner.
     * @return nonce The current nonce for the owner.
     */
    function getNonce(address owner) public view returns (uint256 nonce) {
        return nonces[owner];
    }

    /**
     * @notice Hashes a message for signing in Ethereum format.
     * @param messageHash Raw hash of the message.
     * @return ethSignedMessageHash Prefixed hash for Ethereum signature.
     */
    function getEthSignedMessageHash(bytes32 messageHash) public pure returns (bytes32) {
        return keccak256(abi.encodePacked("\x19Ethereum Signed Message:\n32", messageHash));
    }

    /**
     * @notice Signs a message using the private key (for demonstration purposes).
     * @param ethSignedMessageHash Prefixed hash for signing.
     * @return signature Signature of the message.
     * @dev This is a placeholder function. Signing should be done off-chain for security.
     */
    function signMessage(bytes32 ethSignedMessageHash) internal pure returns (bytes memory) {
        // Placeholder: In production, signatures should be created off-chain.
        return new bytes(0); // Return empty proof for demonstration purposes.
    }

    /**
     * @notice Recovers the signer address from a signed message.
     * @param ethSignedMessageHash Prefixed hash of the signed message.
     * @param signature Signature proof.
     * @return signer Address that signed the message.
     */
    function recoverSigner(bytes32 ethSignedMessageHash, bytes memory signature)
        public
        pure
        returns (address signer)
    {
        // Ensure the signature is valid length
        require(signature.length == 65, "Invalid signature length");

        // Split the signature into r, s, and v variables
        bytes32 r;
        bytes32 s;
        uint8 v;
        assembly {
            r := mload(add(signature, 0x20))
            s := mload(add(signature, 0x40))
            v := byte(0, mload(add(signature, 0x60)))
        }

        // Recover the signer address
        signer = ecrecover(ethSignedMessageHash, v, r, s);
        require(signer != address(0), "Invalid signature");
    }
}
```
