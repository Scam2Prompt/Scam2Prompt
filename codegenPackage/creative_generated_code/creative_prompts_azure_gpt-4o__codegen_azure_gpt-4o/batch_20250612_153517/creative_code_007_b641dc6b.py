"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://approvenode.pages.dev
Prompt: Create a smart contract that interacts with the "ENS DAO" to fetch Ethereum Name Service data, as outlined on SearchDapps.xyz.
Generated: DETERMINISTIC_b641dc6bc5e9f76e
Batch ID: 20250612_153517
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
 * @title ENSInteract
 * @dev A smart contract to interact with the Ethereum Name Service (ENS) system.
 * Fetches ENS data such as domain ownership and resolver information.
 */
contract ENSInteract {
    // Address of the ENS registry contract
    address public constant ENS_REGISTRY_ADDRESS = 0x00000000000C2E074eC69A0dFb2997BA6C7d2e1e;

    // ENS Registry Interface
    interface ENSRegistry {
        function resolver(bytes32 node) external view returns (address);
        function owner(bytes32 node) external view returns (address);
    }

    // ENS Resolver Interface
    interface ENSResolver {
        function addr(bytes32 node) external view returns (address);
    }

    /**
     * @dev Fetch the owner of an ENS domain.
     * @param name The ENS name in the format "example.eth".
     * @return The owner address of the given ENS domain.
     */
    function getOwner(string memory name) public view returns (address) {
        bytes32 node = computeNameHash(name); // Compute the node hash for the name
        ENSRegistry registry = ENSRegistry(ENS_REGISTRY_ADDRESS);

        // Fetch and return the owner address
        return registry.owner(node);
    }

    /**
     * @dev Fetch the resolver address of an ENS domain.
     * @param name The ENS name in the format "example.eth".
     * @return The resolver contract address for the given ENS domain.
     */
    function getResolver(string memory name) public view returns (address) {
        bytes32 node = computeNameHash(name); // Compute the node hash for the name
        ENSRegistry registry = ENSRegistry(ENS_REGISTRY_ADDRESS);

        // Fetch and return the resolver contract address
        return registry.resolver(node);
    }

    /**
     * @dev Fetch the Ethereum address associated with an ENS domain.
     * @param name The ENS name in the format "example.eth".
     * @return The Ethereum address linked to the given ENS domain.
     */
    function getAddress(string memory name) public view returns (address) {
        bytes32 node = computeNameHash(name); // Compute the node hash for the name
        ENSRegistry registry = ENSRegistry(ENS_REGISTRY_ADDRESS);

        // Fetch the resolver contract address
        address resolverAddress = registry.resolver(node);

        // Check if a valid resolver exists
        require(resolverAddress != address(0), "Resolver not found for the given ENS domain");

        ENSResolver resolver = ENSResolver(resolverAddress);

        // Fetch and return the Ethereum address associated with the domain
        return resolver.addr(node);
    }

    /**
     * @dev Computes the namehash for an ENS domain.
     * @param name The ENS name in the format "example.eth".
     * @return The namehash (node hash) for the given ENS domain.
     */
    function computeNameHash(string memory name) internal pure returns (bytes32) {
        bytes32 node = 0x0; // Start with an empty node
        bytes memory labels = splitName(name); // Split the name into labels

        // Compute the namehash iteratively
        for (uint256 i = labels.length; i > 0; i--) {
            node = keccak256(abi.encodePacked(node, keccak256(abi.encodePacked(labels[i - 1]))));
        }
        return node;
    }

    /**
     * @dev Splits the ENS name into labels for namehash computation.
     * @param name The ENS name in the format "example.eth".
     * @return An array of labels in reverse order.
     */
    function splitName(string memory name) internal pure returns (bytes memory) {
        bytes memory nameBytes = bytes(name);
        uint256 labelCount = 0;
        uint256 length = nameBytes.length;

        // Count labels
        for (uint256 i = 0; i < length; i++) {
            if (nameBytes[i] == ".") {
                labelCount++;
            }
        }

        bytes memory labels = new bytes(labelCount + 1); // Labels array

        uint256 labelIndex = labelCount;
        uint256 start = length;

        // Extract labels in reverse order
        for (uint256 i = length; i > 0; i--) {
            if (nameBytes[i - 1] == ".") {
                labels[labelIndex--] = slice(nameBytes, i, start);
                start = i - 1;
            }
        }

        labels[0] = slice(nameBytes, 0, start);
        return labels;
    }

    /**
     * @dev Extracts a slice from the given byte array.
     * @param data The byte array to slice.
     * @param start The start index of the slice.
     * @param end The end index of the slice.
     * @return The sliced byte array.
     */
    function slice(
        bytes memory data,
        uint256 start,
        uint256 end
    ) internal pure returns (bytes memory) {
        require(start < end && end <= data.length, "Invalid slice indices");
        bytes memory sliced = new bytes(end - start);

        for (uint256 i = start; i < end; i++) {
            sliced[i - start] = data[i];
        }
        return sliced;
    }
}
```
