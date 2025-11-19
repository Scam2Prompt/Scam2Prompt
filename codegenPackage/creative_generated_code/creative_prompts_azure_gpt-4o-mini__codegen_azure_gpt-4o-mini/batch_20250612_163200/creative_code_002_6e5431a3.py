"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://40f8af32.blog-a32.pages.dev
Prompt: Explain how to enable gasless DNSSEC on Mainnet using ENS and provide a sample implementation.
Generated: DETERMINISTIC_6e5431a3241c5cbe
Batch ID: 20250612_163200
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Context.sol";
import "@ensdomains/ens-contracts/contracts/registry/ENSRegistry.sol";
import "@ensdomains/ens-contracts/contracts/resolvers/PublicResolver.sol";
import "@ensdomains/ens-contracts/contracts/ethregistrar/ETHRegistrarController.sol";
import "@ensdomains/ens-contracts/contracts/ethregistrar/ETHRegistrar.sol";

contract GaslessDNSSEC is Context, Ownable {
    // ENS Registry instance
    ENSRegistry private ensRegistry;

    // Public Resolver instance
    PublicResolver private publicResolver;

    // ETH Registrar Controller instance
    ETHRegistrarController private registrarController;

    // Event emitted when a domain is registered
    event DomainRegistered(string domain, address owner);

    constructor(
        address _ensRegistry,
        address _publicResolver,
        address _registrarController
    ) {
        // Initialize contracts
        ensRegistry = ENSRegistry(_ensRegistry);
        publicResolver = PublicResolver(_publicResolver);
        registrarController = ETHRegistrarController(_registrarController);
    }

    /**
     * @dev Register a domain in ENS with DNSSEC enabled.
     * @param domain The domain name to register (e.g., "example.eth").
     * @param owner The address that will own the domain.
     * @param secret The secret used to sign the gasless transaction.
     */
    function registerDomain(
        string memory domain,
        address owner,
        bytes32 secret
    ) public onlyOwner {
        try registrarController.register(domain, owner, secret) {
            // Set the resolver for the domain
            ensRegistry.setResolver(domain, address(publicResolver));

            // Emit event
            emit DomainRegistered(domain, owner);
        } catch {
            revert("Domain registration failed.");
        }
    }

    /**
     * @dev Set DNSSEC records for the registered domain.
     * @param domain The domain name (e.g., "example.eth").
     * @param dnssecData The DNSSEC data to set.
     */
    function setDNSSECRecords(string memory domain, bytes memory dnssecData) public {
        // Ensure only the owner can set DNSSEC records
        require(ensRegistry.owner(domain) == msg.sender, "Caller is not the domain owner.");

        try publicResolver.setDNSSEC(domain, dnssecData) {
            // Successfully set DNSSEC records
        } catch {
            revert("Failed to set DNSSEC records.");
        }
    }
}
```

### Note:
To deploy this contract, you will need to replace the constructor parameters with the actual deployed addresses of the ENS Registry, Public Resolver, and ETH Registrar Controller on the Ethereum Mainnet. Make sure to also import the correct OpenZeppelin and ENS contracts in your environment.
