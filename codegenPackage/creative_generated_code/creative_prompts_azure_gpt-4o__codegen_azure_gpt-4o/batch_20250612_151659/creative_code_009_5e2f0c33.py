"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprimeapeplanetmint.pages.dev
Prompt: Create a donation tracking system in Solidity for an NFT project, where a portion of sales is allocated to charities, as described in Prime Ape Planet's roadmap.
Generated: DETERMINISTIC_5e2f0c33ab06a990
Batch ID: 20250612_151659
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
 * @title DonationTracker
 * @dev A contract to track and distribute donations to charities from NFT sales.
 */
contract DonationTracker {
    // Owner of the contract
    address public owner;

    // Total donations collected
    uint256 public totalDonations;

    // Mapping of charity addresses to their allocated donations
    mapping(address => uint256) public charityAllocations;

    // List of approved charities
    address[] public charities;

    // Event emitted when a donation is made
    event DonationMade(address indexed sender, uint256 amount);

    // Event emitted when funds are distributed to charities
    event FundsDistributed(uint256 totalAmount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor sets the contract deployer as the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows the owner to add a charity to the list of approved charities.
     * @param _charity Address of the charity to add.
     */
    function addCharity(address _charity) external onlyOwner {
        require(_charity != address(0), "Invalid charity address");
        charities.push(_charity);
    }

    /**
     * @dev Allows the owner to remove a charity from the list.
     * @param _charity Address of the charity to remove.
     */
    function removeCharity(address _charity) external onlyOwner {
        require(_charity != address(0), "Invalid charity address");
        for (uint256 i = 0; i < charities.length; i++) {
            if (charities[i] == _charity) {
                // Remove the charity by swapping it with the last element and resizing the array
                charities[i] = charities[charities.length - 1];
                charities.pop();
                break;
            }
        }
    }

    /**
     * @dev Allows users to make donations.
     */
    function donate() external payable {
        require(msg.value > 0, "Donation amount must be greater than zero");

        totalDonations += msg.value;
        emit DonationMade(msg.sender, msg.value);
    }

    /**
     * @dev Distributes collected donations evenly among approved charities.
     */
    function distributeFunds() external onlyOwner {
        require(charities.length > 0, "No charities available");
        require(totalDonations > 0, "No funds available for distribution");

        uint256 amountPerCharity = totalDonations / charities.length;
        require(amountPerCharity > 0, "Insufficient funds for distribution");

        for (uint256 i = 0; i < charities.length; i++) {
            charityAllocations[charities[i]] += amountPerCharity;
            (bool success, ) = charities[i].call{value: amountPerCharity}("");
            require(success, "Failed to send funds to charity");
        }

        // Reset totalDonations after distribution
        totalDonations = 0;

        emit FundsDistributed(amountPerCharity * charities.length);
    }

    /**
     * @dev Allows the owner to withdraw any remaining funds in the contract.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {
        totalDonations += msg.value;
        emit DonationMade(msg.sender, msg.value);
    }
}
```
