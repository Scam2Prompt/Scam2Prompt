"""
Generated Code Metadata:
========================
Original URL: https://zora-air-spring.nfts2.me
Prompt: Write a smart contract that tracks referrals and calculates earnings based on mints, inspired by the Zora Air Spring model.
Generated: DETERMINISTIC_3f415c8691e3d289
Batch ID: 20250612_162811
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
 * @title ReferralMintTracker
 * @dev A smart contract to track referrals and calculate earnings based on mints.
 * Inspired by the Zora Air Spring model.
 */
contract ReferralMintTracker {
    // Struct to store referral information
    struct Referral {
        uint256 totalMints; // Total mints attributed to the referral
        uint256 totalEarnings; // Total earnings for the referral
    }

    // Mapping to track referrals and their data
    mapping(address => Referral) public referrals;

    // Mapping to track mint counts for users
    mapping(address => uint256) public userMintCount;

    // Address of the contract owner
    address public owner;

    // Event emitted when a mint occurs
    event Mint(address indexed minter, address indexed referrer, uint256 amount);

    // Event emitted when earnings are withdrawn
    event EarningsWithdrawn(address indexed referrer, uint256 amount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Mint function that tracks referrals and calculates earnings.
     * @param referrer The address of the referrer.
     * @param amount The amount of mints to perform.
     */
    function mint(address referrer, uint256 amount) external payable {
        require(amount > 0, "Mint amount must be greater than zero");
        require(msg.value >= amount * 0.01 ether, "Insufficient payment for minting");

        // Update the user's mint count
        userMintCount[msg.sender] += amount;

        // If a valid referrer is provided, update referral data
        if (referrer != address(0) && referrer != msg.sender) {
            referrals[referrer].totalMints += amount;
            referrals[referrer].totalEarnings += (msg.value * 10) / 100; // 10% referral earnings
        }

        emit Mint(msg.sender, referrer, amount);
    }

    /**
     * @dev Allows referrers to withdraw their earnings.
     */
    function withdrawEarnings() external {
        uint256 earnings = referrals[msg.sender].totalEarnings;
        require(earnings > 0, "No earnings available for withdrawal");

        // Reset the referrer's earnings before transferring to prevent reentrancy
        referrals[msg.sender].totalEarnings = 0;

        // Transfer the earnings to the referrer
        (bool success, ) = msg.sender.call{value: earnings}("");
        require(success, "Earnings withdrawal failed");

        emit EarningsWithdrawn(msg.sender, earnings);
    }

    /**
     * @dev Allows the owner to withdraw the contract's balance.
     */
    function withdrawContractBalance() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance available for withdrawal");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Contract balance withdrawal failed");
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {}

    /**
     * @dev Function to get referral data for a specific address.
     * @param referrer The address of the referrer.
     * @return totalMints The total mints attributed to the referrer.
     * @return totalEarnings The total earnings for the referrer.
     */
    function getReferralData(address referrer)
        external
        view
        returns (uint256 totalMints, uint256 totalEarnings)
    {
        Referral memory referral = referrals[referrer];
        return (referral.totalMints, referral.totalEarnings);
    }
}
```
