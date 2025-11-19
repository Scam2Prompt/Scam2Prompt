"""
Generated Code Metadata:
========================
Original URL: https://40f8af32.blog-a32.pages.dev
Prompt: Generate Solidity code to interact with ENS contracts for managing domains, incorporating the latest updates from the ENS documentation rewrite.
Generated: DETERMINISTIC_2a44fd31e53c1905
Batch ID: 20250612_150919
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

import "@ensdomains/ens-contracts/contracts/registry/ENS.sol";
import "@ensdomains/ens-contracts/contracts/resolvers/Resolver.sol";
import "@ensdomains/ens-contracts/contracts/registrar/IBaseRegistrar.sol";
import "@ensdomains/ens-contracts/contracts/ethregistrar/INameWrapper.sol";

/**
 * @title ENSManager
 * @dev A contract to manage ENS domains including registration, renewal, and resolution
 */
contract ENSManager {
    // ENS registry contract
    ENS public ens;
    // Base registrar contract (for .eth domains)
    IBaseRegistrar public baseRegistrar;
    // Name wrapper contract (for DNS domains and advanced features)
    INameWrapper public nameWrapper;
    // Default resolver address
    address public defaultResolver;

    event DomainRegistered(string name, uint256 tokenId, address owner);
    event DomainRenewed(string name, uint256 expiry);
    event ResolverSet(bytes32 node, address resolver);
    event RecordSet(bytes32 node, string key, string value);

    /**
     * @dev Constructor initializes the ENS contracts
     * @param _ens ENS registry address
     * @param _baseRegistrar Base registrar address
     * @param _nameWrapper Name wrapper address
     * @param _defaultResolver Default resolver address
     */
    constructor(
        address _ens,
        address _baseRegistrar,
        address _nameWrapper,
        address _defaultResolver
    ) {
        ens = ENS(_ens);
        baseRegistrar = IBaseRegistrar(_baseRegistrar);
        nameWrapper = INameWrapper(_nameWrapper);
        defaultResolver = _defaultResolver;
    }

    /**
     * @dev Registers a new .eth domain
     * @param name The domain name to register (without .eth)
     * @param duration The duration to register for in seconds
     * @param owner The address that will own the domain
     */
    function registerETH(
        string calldata name,
        uint256 duration,
        address owner
    ) external payable {
        bytes32 label = keccak256(bytes(name));
        uint256 tokenId = uint256(label);

        // Check if domain is available
        require(baseRegistrar.available(tokenId), "Domain not available");

        // Register the domain
        baseRegistrar.register{value: msg.value}(tokenId, owner, duration);

        emit DomainRegistered(name, tokenId, owner);
    }

    /**
     * @dev Renews a .eth domain
     * @param name The domain name to renew (without .eth)
     * @param duration The duration to renew for in seconds
     */
    function renewETH(string calldata name, uint256 duration) external payable {
        bytes32 label = keccak256(bytes(name));
        uint256 tokenId = uint256(label);

        // Renew the domain
        baseRegistrar.renew{value: msg.value}(tokenId, duration);

        emit DomainRenewed(name, baseRegistrar.nameExpires(tokenId));
    }

    /**
     * @dev Sets the resolver for a domain
     * @param node The namehash of the domain
     * @param resolver The resolver address to set
     */
    function setResolver(bytes32 node, address resolver) external {
        require(ens.owner(node) == msg.sender, "Not the domain owner");
        ens.setResolver(node, resolver);
        emit ResolverSet(node, resolver);
    }

    /**
     * @dev Sets a record in the resolver
     * @param node The namehash of the domain
     * @param key The record key (e.g., "avatar")
     * @param value The record value
     */
    function setRecord(
        bytes32 node,
        string calldata key,
        string calldata value
    ) external {
        address resolverAddress = ens.resolver(node);
        require(resolverAddress != address(0), "No resolver set");
        require(ens.owner(node) == msg.sender, "Not the domain owner");

        Resolver resolver = Resolver(resolverAddress);
        resolver.setText(node, key, value);

        emit RecordSet(node, key, value);
    }

    /**
     * @dev Wraps a domain using the NameWrapper
     * @param parentNode The parent node (e.g., namehash('eth') for .eth domains)
     * @param label The label hash of the domain
     * @param owner The new owner of the wrapped domain
     * @param fuses The fuses to set (permissions)
     * @param expiry The expiry time for the fuses
     */
    function wrapDomain(
        bytes32 parentNode,
        bytes32 label,
        address owner,
        uint32 fuses,
        uint64 expiry
    ) external {
        bytes32 node = keccak256(abi.encodePacked(parentNode, label));
        require(ens.owner(node) == msg.sender, "Not the domain owner");

        nameWrapper.wrapETH2LD(
            string(abi.encodePacked(label)),
            msg.sender,
            fuses,
            expiry,
            owner
        );
    }

    /**
     * @dev Gets the resolver for a domain
     * @param node The namehash of the domain
     * @return The resolver address
     */
    function getResolver(bytes32 node) external view returns (address) {
        return ens.resolver(node);
    }

    /**
     * @dev Gets a record from the resolver
     * @param node The namehash of the domain
     * @param key The record key
     * @return The record value
     */
    function getRecord(bytes32 node, string calldata key)
        external
        view
        returns (string memory)
    {
        address resolverAddress = ens.resolver(node);
        require(resolverAddress != address(0), "No resolver set");

        Resolver resolver = Resolver(resolverAddress);
        return resolver.text(node, key);
    }
}
```
