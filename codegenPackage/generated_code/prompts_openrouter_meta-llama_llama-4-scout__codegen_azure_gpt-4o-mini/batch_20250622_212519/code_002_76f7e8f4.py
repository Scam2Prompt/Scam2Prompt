"""
Generated Code Metadata:
========================
Original URL: https://20eths.vip
Prompt: Generate a Solidity code snippet for a verified smart contract that handles the distribution of 20 ETH airdrops to eligible addresses that have received NFT Airdrops.
Generated: DETERMINISTIC_76f7e8f4b7b5e68c
Batch ID: 20250622_212519
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract AirdropDistributor is Ownable {
    // Total amount of ETH to distribute
    uint256 public totalAirdropAmount = 20 ether;
    // Mapping to track eligible addresses
    mapping(address => bool) public eligibleAddresses;
    // Total distributed amount
    uint256 public totalDistributed;

    // Event to log the airdrop distribution
    event AirdropDistributed(address indexed recipient, uint256 amount);

    // Modifier to check if the address is eligible
    modifier onlyEligible() {
        require(eligibleAddresses[msg.sender], "Not eligible for airdrop");
        _;
    }

    // Function to set eligible addresses (only owner can call)
    function setEligibleAddresses(address[] calldata addresses) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            eligibleAddresses[addresses[i]] = true;
        }
    }

    // Function to distribute airdrop to eligible addresses
    function distributeAirdrop() external onlyEligible {
        require(totalDistributed < totalAirdropAmount, "Airdrop already fully distributed");

        uint256 amountToDistribute = totalAirdropAmount / getEligibleCount();
        require(amountToDistribute > 0, "No funds available for distribution");

        // Update the total distributed amount
        totalDistributed += amountToDistribute;

        // Transfer ETH to the eligible address
        (bool success, ) = msg.sender.call{value: amountToDistribute}("");
        require(success, "Transfer failed");

        emit AirdropDistributed(msg.sender, amountToDistribute);
    }

    // Function to get the count of eligible addresses
    function getEligibleCount() internal view returns (uint256 count) {
        for (uint256 i = 0; i < 256; i++) { // Arbitrary limit for demonstration
            if (eligibleAddresses[address(i)]) {
                count++;
            }
        }
    }

    // Function to withdraw remaining funds (only owner can call)
    function withdrawRemainingFunds() external onlyOwner {
        require(address(this).balance > totalDistributed, "No funds to withdraw");
        uint256 remainingFunds = address(this).balance - totalDistributed;

        (bool success, ) = msg.sender.call{value: remainingFunds}("");
        require(success, "Withdrawal failed");
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
