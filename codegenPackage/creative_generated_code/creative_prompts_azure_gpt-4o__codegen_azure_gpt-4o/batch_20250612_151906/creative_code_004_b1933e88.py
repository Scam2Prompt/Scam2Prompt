"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ens.gifts
Prompt: Write a smart contract that automates the process of gifting ENS domains, including domain registration and transfer.
Generated: DETERMINISTIC_b1933e88d9cd1423
Batch ID: 20250612_151906
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

// Import OpenZeppelin's SafeMath for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Import the ENS Registry interface
interface IENSRegistry {
    function setOwner(bytes32 node, address owner) external;
    function owner(bytes32 node) external view returns (address);
    function setResolver(bytes32 node, address resolver) external;
    function setTTL(bytes32 node, uint64 ttl) external;
}

// Import the ENS Registrar interface for domain registration
interface IENSRegistrar {
    function register(uint256 id, address owner) external;
    function available(uint256 id) external view returns (bool);
}

contract ENSGiftContract {
    using SafeMath for uint256;

    // Address of the ENS Registry
    IENSRegistry private ensRegistry;
    // Address of the ENS Registrar
    IENSRegistrar private ensRegistrar;

    // Event emitted after a domain is gifted
    event DomainGifted(string domainName, address recipient);

    // Constructor to initialize ENS Registry and Registrar addresses
    constructor(address _ensRegistry, address _ensRegistrar) {
        require(_ensRegistry != address(0), "Invalid ENS Registry address");
        require(_ensRegistrar != address(0), "Invalid ENS Registrar address");

        ensRegistry = IENSRegistry(_ensRegistry);
        ensRegistrar = IENSRegistrar(_ensRegistrar);
    }

    /**
     * @notice Register and transfer an ENS domain to a recipient.
     * @param domainName The name of the domain to be gifted (e.g., "example.eth").
     * @param recipient The address of the recipient who will receive the domain.
     */
    function giftENSDomain(string memory domainName, address recipient) external payable {
        require(bytes(domainName).length > 0, "Domain name cannot be empty");
        require(recipient != address(0), "Recipient address cannot be zero");

        // Calculate the namehash and labelhash of the domain
        bytes32 namehash = _getNamehash(domainName);
        bytes32 labelhash = keccak256(abi.encodePacked(domainName));

        // Check if the domain is available for registration
        uint256 id = uint256(labelhash);
        require(ensRegistrar.available(id), "Domain is already registered");

        // Register the domain to the sender (temporary ownership)
        ensRegistrar.register(id, msg.sender);

        // Transfer domain ownership to the recipient
        ensRegistry.setOwner(namehash, recipient);

        // Emit the gifting event
        emit DomainGifted(domainName, recipient);
    }

    /**
     * @notice Helper function to compute the namehash of a domain.
     * @param domainName The domain name (e.g., "example.eth").
     * @return The computed namehash.
     */
    function _getNamehash(string memory domainName) private pure returns (bytes32) {
        bytes32 node = 0x0;
        string memory label = domainName;
        node = keccak256(abi.encodePacked(node, keccak256(abi.encodePacked(label))));
        return node;
    }
}
```
