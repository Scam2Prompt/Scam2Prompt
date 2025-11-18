"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodeclaim.pages.dev
Prompt: Using Solidity, write a smart contract to interact with the ENS DAO and retrieve Ethereum Name Service details, as mentioned on the webpage.
Generated: DETERMINISTIC_be04d482f595bdea
Batch ID: 20250612_153648
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

// Importing required interfaces for ENS
import "@ensdomains/ens-contracts/contracts/ENS.sol";
import "@ensdomains/ens-contracts/contracts/interfaces/IENS.sol";
import "@ensdomains/ens-contracts/contracts/interfaces/IResolver.sol";

contract EnsDaoInteraction {
    // Instance of ENS contract
    IENS public ens;

    // Event to emit when ENS details are retrieved
    event EnsDetailsRetrieved(bytes32 indexed node, address resolverAddress, string name);

    // Constructor to initialize the ENS contract
    constructor(address ensAddress) {
        require(ensAddress != address(0), "ENS address cannot be zero");
        ens = IENS(ensAddress);
    }

    /**
     * @dev Retrieves ENS details based on the provided node
     * @param node The node to retrieve details for (keccak256 of domain name)
     * @return resolverAddress The address of the resolver associated with the node
     * @return name The human-readable name corresponding to the node
     */
    function getEnsDetails(bytes32 node) external returns (address resolverAddress, string memory name) {
        // Retrieve resolver address from ENS
        resolverAddress = ens.resolver(node);
        require(resolverAddress != address(0), "Resolver does not exist for this node");

        // Create an instance of the resolver
        IResolver resolver = IResolver(resolverAddress);

        // Retrieve the name associated with the node
        name = resolver.name(node);
        require(bytes(name).length > 0, "No name registered for this node");

        // Emit an event for logging purposes
        emit EnsDetailsRetrieved(node, resolverAddress, name);
    }
}
```
