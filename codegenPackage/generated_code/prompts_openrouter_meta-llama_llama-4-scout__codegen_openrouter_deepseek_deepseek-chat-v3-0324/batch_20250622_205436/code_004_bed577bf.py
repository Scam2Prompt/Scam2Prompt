"""
Generated Code Metadata:
========================
Original URL: https://upgrading-ethereum.info
Prompt: Develop a donation system for supporting Ethereum developers, using the provided Ethereum address and referencing the Protocol Guild.
Generated: DETERMINISTIC_bed577bfec0e9cd6
Batch ID: 20250622_205436
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

/**
 * @title ProtocolGuildDonation
 * @dev A smart contract for donating ETH to Ethereum developers via Protocol Guild
 * @notice This contract allows users to donate ETH which will be forwarded to a specified Protocol Guild address
 */
contract ProtocolGuildDonation {
    // Protocol Guild's Ethereum address
    address public constant PROTOCOL_GUILD_ADDRESS = 0xF29Ff96aaEa6C9A1fBa851f74737f3c069d4f1a9;

    /**
     * @dev Emitted when a donation is made
     * @param donor Address of the donor
     * @param amount Amount donated in wei
     */
    event DonationReceived(address indexed donor, uint256 amount);

    /**
     * @dev Receive function to accept ETH donations
     */
    receive() external payable {
        require(msg.value > 0, "Donation amount must be greater than 0");
        emit DonationReceived(msg.sender, msg.value);
    }

    /**
     * @dev Fallback function to accept ETH donations
     */
    fallback() external payable {
        require(msg.value > 0, "Donation amount must be greater than 0");
        emit DonationReceived(msg.sender, msg.value);
    }

    /**
     * @dev Allows the contract to forward the donated ETH to Protocol Guild
     * @notice This function can be called by anyone to transfer the contract's balance
     */
    function forwardDonations() external {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available to forward");

        (bool success, ) = PROTOCOL_GUILD_ADDRESS.call{value: balance}("");
        require(success, "ETH transfer failed");
    }

    /**
     * @dev Returns the current balance of the contract
     * @return The balance in wei
     */
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
