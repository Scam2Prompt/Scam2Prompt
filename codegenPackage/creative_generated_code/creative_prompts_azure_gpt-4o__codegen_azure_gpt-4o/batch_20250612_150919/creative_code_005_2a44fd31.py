"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://40f8af32.blog-a32.pages.dev
Prompt: Generate Solidity code to interact with ENS contracts for managing domains, incorporating the latest updates from the ENS documentation rewrite.
Generated: DETERMINISTIC_2a44fd31e53c1905
Batch ID: 20250612_150919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title ENSManager
 * @dev A contract to interact with the Ethereum Name Service (ENS) contracts for managing domains.
 *      This contract is designed to handle domain resolution and registration updates using the ENS registry.
 */
interface ENSRegistry {
    function owner(bytes32 node) external view returns (address);
    function setOwner(bytes32 node, address owner) external;
    function setResolver(bytes32 node, address resolver) external;
    function resolver(bytes32 node) external view returns (address);
}

interface ENSResolver {
    function setAddr(bytes32 node, address addr) external;
    function addr(bytes32 node) external view returns (address);
}

contract ENSManager {
    ENSRegistry public ensRegistry;

    // Event for logging ownership updates
    event OwnershipTransferred(bytes32 indexed node, address indexed newOwner);

    // Event for logging resolver updates
    event ResolverUpdated(bytes32 indexed node, address indexed newResolver);

    // Event for logging address updates in resolver
    event AddressUpdated(bytes32 indexed node, address indexed newAddress);

    /**
     * @dev Constructor to initialize the ENS registry address.
     * @param _ensRegistry Address of the ENS registry contract.
     */
    constructor(address _ensRegistry) {
        require(_ensRegistry != address(0), "ENS registry address cannot be zero");
        ensRegistry = ENSRegistry(_ensRegistry);
    }

    /**
     * @dev Transfers ownership of a domain to a new owner.
     * @param node The namehash of the ENS domain.
     * @param newOwner Address of the new owner.
     */
    function transferDomainOwnership(bytes32 node, address newOwner) external {
        require(newOwner != address(0), "New owner cannot be zero address");
        require(ensRegistry.owner(node) == msg.sender, "Caller is not the owner of the domain");

        ensRegistry.setOwner(node, newOwner);

        emit OwnershipTransferred(node, newOwner);
    }

    /**
     * @dev Updates the resolver for a domain.
     * @param node The namehash of the ENS domain.
     * @param newResolver Address of the new resolver contract.
     */
    function updateResolver(bytes32 node, address newResolver) external {
        require(newResolver != address(0), "Resolver address cannot be zero");
        require(ensRegistry.owner(node) == msg.sender, "Caller is not the owner of the domain");

        ensRegistry.setResolver(node, newResolver);

        emit ResolverUpdated(node, newResolver);
    }

    /**
     * @dev Updates the address for a domain in the resolver contract.
     * @param node The namehash of the ENS domain.
     * @param newAddress The new address to associate with the domain.
     */
    function updateAddress(bytes32 node, address newAddress) external {
        require(newAddress != address(0), "Address cannot be zero");

        address resolverAddress = ensRegistry.resolver(node);
        require(resolverAddress != address(0), "Resolver not set for the domain");

        ENSResolver resolver = ENSResolver(resolverAddress);
        require(ensRegistry.owner(node) == msg.sender, "Caller is not the owner of the domain");

        resolver.setAddr(node, newAddress);

        emit AddressUpdated(node, newAddress);
    }

    /**
     * @dev Fetches the current owner of a domain.
     * @param node The namehash of the ENS domain.
     * @return The address of the owner.
     */
    function getDomainOwner(bytes32 node) external view returns (address) {
        return ensRegistry.owner(node);
    }

    /**
     * @dev Fetches the current resolver address for a domain.
     * @param node The namehash of the ENS domain.
     * @return The address of the resolver.
     */
    function getDomainResolver(bytes32 node) external view returns (address) {
        return ensRegistry.resolver(node);
    }

    /**
     * @dev Fetches the address associated with a domain in the resolver contract.
     * @param node The namehash of the ENS domain.
     * @return The associated address.
     */
    function getDomainAddress(bytes32 node) external view returns (address) {
        address resolverAddress = ensRegistry.resolver(node);
        require(resolverAddress != address(0), "Resolver not set for the domain");

        ENSResolver resolver = ENSResolver(resolverAddress);
        return resolver.addr(node);
    }
}
```
