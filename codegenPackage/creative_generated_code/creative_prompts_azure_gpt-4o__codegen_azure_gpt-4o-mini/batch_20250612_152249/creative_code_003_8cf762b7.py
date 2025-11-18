"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeie3nw7cyq2q2jw5zaaxhqznmxmr6ano4kkfjked4sebtl2biznzfy.ipfs.dweb.link
Prompt: Create a smart contract in Solidity that manages a whitelist for a public pre-sale, allowing users to register using their Web3 wallet addresses.
Generated: DETERMINISTIC_8cf762b784ccf42e
Batch ID: 20250612_152249
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

/**
 * @title WhitelistManager
 * @dev This contract manages a whitelist for a public pre-sale.
 */
contract WhitelistManager {
    // State variable to store the owner of the contract
    address public owner;

    // Mapping to track whitelisted addresses
    mapping(address => bool) public whitelisted;

    // Event emitted when an address is whitelisted
    event AddressWhitelisted(address indexed user);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to set the contract deployer as the owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows the owner to add an address to the whitelist
     * @param user The address to be whitelisted
     */
    function whitelistAddress(address user) external onlyOwner {
        require(user != address(0), "Invalid address");
        require(!whitelisted[user], "Address already whitelisted");

        whitelisted[user] = true;
        emit AddressWhitelisted(user);
    }

    /**
     * @dev Allows the owner to remove an address from the whitelist
     * @param user The address to be removed from the whitelist
     */
    function removeAddressFromWhitelist(address user) external onlyOwner {
        require(user != address(0), "Invalid address");
        require(whitelisted[user], "Address not whitelisted");

        whitelisted[user] = false;
    }

    /**
     * @dev Checks if an address is whitelisted
     * @param user The address to check
     * @return bool indicating if the address is whitelisted
     */
    function isWhitelisted(address user) external view returns (bool) {
        return whitelisted[user];
    }

    /**
     * @dev Allows the owner to withdraw any Ether that may be sent to the contract
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Transfer failed");
    }

    // Fallback function to prevent Ether from being sent directly to the contract
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```
