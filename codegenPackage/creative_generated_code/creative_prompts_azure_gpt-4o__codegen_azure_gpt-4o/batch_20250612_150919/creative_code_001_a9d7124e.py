"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://40f8af32.blog-a32.pages.dev
Prompt: Generate code to enable gasless DNSSEC integration for ENS domains on the Ethereum Mainnet, as described in the ENS documentation update.
Generated: DETERMINISTIC_a9d7124eb8fb09c7
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
pragma solidity ^0.8.17;

/**
 * @title Gasless DNSSEC Integration for ENS Domains
 * @dev This contract provides functionality to verify DNSSEC proofs for ENS domains without requiring gas payments from users.
 *      The implementation relies on meta-transactions to enable gasless interactions.
 */

import "@openzeppelin/contracts/metatx/MinimalForwarder.sol";
import "@openzeppelin/contracts/metatx/ERC2771Context.sol";
import "@ensdomains/dnssec-oracle/contracts/DNSSEC.sol";
import "@ensdomains/ens-contracts/contracts/registry/ENS.sol";

contract GaslessDNSSECENSIntegration is ERC2771Context {
    // Address of the ENS registry contract
    ENS public immutable ensRegistry;

    // Address of the DNSSEC oracle contract
    DNSSEC public immutable dnssecOracle;

    // Events
    event DomainVerified(string domain, address indexed owner);

    /**
     * @dev Constructor for the GaslessDNSSECENSIntegration contract
     * @param forwarder Address of the MinimalForwarder contract for meta-transactions
     * @param _ensRegistry Address of the ENS registry contract
     * @param _dnssecOracle Address of the DNSSEC oracle contract
     */
    constructor(
        MinimalForwarder forwarder,
        ENS _ensRegistry,
        DNSSEC _dnssecOracle
    ) ERC2771Context(address(forwarder)) {
        ensRegistry = _ensRegistry;
        dnssecOracle = _dnssecOracle;
    }

    /**
     * @dev Verify a DNSSEC proof and update the ENS registry
     * @param domain Name of the domain to verify
     * @param proof DNSSEC proof data
     * @param owner Address to associate with the ENS domain
     */
    function verifyDomain(
        string memory domain,
        bytes memory proof,
        address owner
    ) external {
        require(owner != address(0), "Invalid owner address");

        // Verify DNSSEC proof using the oracle
        bool isValid = dnssecOracle.verifyProof(domain, proof);
        require(isValid, "DNSSEC proof validation failed");

        // Update ENS registry with the owner address
        bytes32 node = getDomainNode(domain);
        ensRegistry.setOwner(node, owner);

        emit DomainVerified(domain, owner);
    }

    /**
     * @dev Helper function to calculate the ENS node for a domain
     * @param domain Name of the domain (e.g., "example.eth")
     * @return ENS node for the domain
     */
    function getDomainNode(string memory domain) internal pure returns (bytes32) {
        return keccak256(abi.encodePacked(domain));
    }

    /**
     * @dev Overriding _msgSender and _msgData to support gasless transactions
     */
    function _msgSender() internal view override(Context, ERC2771Context) returns (address sender) {
        return ERC2771Context._msgSender();
    }

    function _msgData() internal view override(Context, ERC2771Context) returns (bytes calldata) {
        return ERC2771Context._msgData();
    }
}
```
