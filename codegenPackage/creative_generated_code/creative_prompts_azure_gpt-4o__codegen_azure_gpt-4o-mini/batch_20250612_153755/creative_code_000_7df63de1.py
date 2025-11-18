"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rseth.top
Prompt: Write a smart contract in Solidity to verify wallet eligibility for an ETH airdrop, similar to the functionality described on the "Lido Stake Wrap Airdrop Governance" portal.
Generated: DETERMINISTIC_7df63de1f824486f
Batch ID: 20250612_153755
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AirdropEligibility
 * @dev This contract verifies wallet eligibility for an ETH airdrop.
 * It lets the owner manage the eligible addresses and airdrop process.
 */
contract AirdropEligibility is Ownable {
    // Mapping to track eligible addresses
    mapping(address => bool) private eligibleAddresses;

    // Event to log the addition of eligible addresses
    event EligibleAddressAdded(address indexed addr);
    
    // Event to log the removal of eligible addresses
    event EligibleAddressRemoved(address indexed addr);
    
    // Event to log the airdrop action
    event AirdropExecuted(address indexed addr, uint256 amount);

    // Function to add an eligible address
    function addEligibleAddress(address _addr) external onlyOwner {
        require(_addr != address(0), "Invalid address");
        require(!eligibleAddresses[_addr], "Address is already eligible");

        eligibleAddresses[_addr] = true;
        emit EligibleAddressAdded(_addr);
    }

    // Function to remove an eligible address
    function removeEligibleAddress(address _addr) external onlyOwner {
        require(eligibleAddresses[_addr], "Address is not eligible");

        eligibleAddresses[_addr] = false;
        emit EligibleAddressRemoved(_addr);
    }

    // Function to check if an address is eligible for the airdrop
    function isEligible(address _addr) external view returns (bool) {
        return eligibleAddresses[_addr];
    }

    // Function to execute the airdrop
    function airdropETH(address payable[] calldata _recipients, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(_recipients.length > 0, "No recipients provided");

        for (uint256 i = 0; i < _recipients.length; i++) {
            address payable recipient = _recipients[i];
            require(eligibleAddresses[recipient], "Recipient is not eligible");

            // Transfer ETH to the eligible recipient
            (bool success, ) = recipient.call{value: _amount}("");
            require(success, "Failed to send Ether");

            emit AirdropExecuted(recipient, _amount);
        }
    }

    // Allow the contract to receive ETH
    receive() external payable {}

    // Function to withdraw the contract's balance to the owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
    }
}
```
