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
pragma solidity ^0.8.0;

import "@ensdomains/ens-contracts/contracts/ENS.sol";
import "@ensdomains/ens-contracts/contracts/ETHRegistrarController.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

contract ENSManager {
    ENS public ens; // Instance of the ENS contract
    ETHRegistrarController public registrar; // Instance of the registrar for managing domains

    // Event emitted when a domain is registered
    event DomainRegistered(string domain, address owner);
    // Event emitted when a domain is renewed
    event DomainRenewed(string domain, uint256 duration);
    // Event emitted when a domain is transferred
    event DomainTransferred(string domain, address newOwner);

    constructor(ENS _ens, ETHRegistrarController _registrar) {
        ens = _ens; // Set the ENS contract
        registrar = _registrar; // Set the registrar contract
    }

    /**
     * @dev Registers a new domain name
     * @param domain The domain name to register (e.g., "example.eth")
     * @param owner The address of the domain owner
     * @param duration The duration for which the domain is registered
     * @param value The value in ETH to pay for registering the domain
     */
    function registerDomain(string memory domain, address owner, uint256 duration, uint256 value) public payable {
        require(msg.value == value, "Incorrect ETH value sent");
        
        // Register the domain using the registrar contract
        registrar.register(domain, owner, duration);

        emit DomainRegistered(domain, owner);
    }

    /**
     * @dev Renews a registered domain
     * @param domain The domain name to renew
     * @param duration The duration for which to renew the domain
     */
    function renewDomain(string memory domain, uint256 duration) public {
        // Renew the domain using the registrar contract
        registrar.renew(domain, duration);
        
        emit DomainRenewed(domain, duration);
    }

    /**
     * @dev Transfers a domain to a new owner
     * @param domain The domain name to transfer
     * @param newOwner The address of the new domain owner
     */
    function transferDomain(string memory domain, address newOwner) public {
        require(msg.sender == registrar.owner(domain), "Only the domain owner can transfer");

        // Transfer the domain ownership
        registrar.safeTransferFrom(msg.sender, newOwner, domain);

        emit DomainTransferred(domain, newOwner);
    }

    /**
     * @dev Fallback function to accept Ether
     */
    receive() external payable {}

    /**
     * @dev Withdraws the contract's balance to the owner's address
     * @param to The address to withdraw the funds to
     */
    function withdraw(address payable to) public {
        require(msg.sender == address(this), "Only the contract can withdraw"); // Change to proper access control
        require(address(this).balance > 0, "No funds to withdraw");

        (bool success, ) = to.call{value: address(this).balance}("");
        require(success, "Transfer failed");
    }
}
```
