"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zora-air-spring.nfts2.me
Prompt: Write a smart contract that tracks referrals and calculates earnings based on mints, inspired by the Zora Air Spring model.
Generated: DETERMINISTIC_3f415c8691e3d289
Batch ID: 20250612_162811
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

contract ReferralEarnings {

    // Struct to store referral information
    struct Referral {
        address referrer;
        uint256 earnings;
        uint256 mintsCount;
    }

    // Mapping to track referrals by address
    mapping(address => Referral) public referrals;

    // Event to emit when a new referral is recorded
    event NewReferral(address indexed referrer, address indexed referred);

    // Event to emit when earnings are calculated for a referral
    event EarningsCalculated(address indexed referrer, uint256 earnings);

    // Allows users to refer others and track their earnings
    function refer(address _referred) external {
        // Ensure that the referred address is valid
        require(_referred != address(0), "Invalid address");
        require(referrals[_referred].referrer == address(0), "Already referred");

        // Record the referrer and the referred address
        referrals[_referred].referrer = msg.sender;

        // Emit the event for new referral
        emit NewReferral(msg.sender, _referred);
    }

    // Function to mint an NFT and calculate earnings for the referrer
    function mint() external {
        // Ensure that the caller has a referrer
        require(referrals[msg.sender].referrer != address(0), "No referrer found");

        // Increment the count of mints for the referrer
        address referrer = referrals[msg.sender].referrer;
        referrals[referrer].mintsCount += 1;

        // Calculate earnings (e.g., 10% of a hypothetical minting fee)
        uint256 earnings = calculateEarnings(1 ether); // Assume minting costs 1 ether
        referrals[referrer].earnings += earnings;

        // Emit event for earnings calculation
        emit EarningsCalculated(referrer, earnings);
    }

    // Function to calculate earnings based on mint cost
    function calculateEarnings(uint256 mintCost) internal pure returns (uint256) {
        // Here we assume a 10% commission for the referrer
        return (mintCost * 10) / 100;
    }

    // Function to withdraw earnings for a referrer
    function withdrawEarnings() external {
        uint256 earnings = referrals[msg.sender].earnings;
        
        // Ensure that the caller has earnings to withdraw
        require(earnings > 0, "No earnings to withdraw");

        // Reset the earnings to zero before transferring
        referrals[msg.sender].earnings = 0;

        // Transfer earnings to the referrer
        (bool success, ) = msg.sender.call{value: earnings}("");
        require(success, "Transfer failed");

        // Emit event for earnings withdrawal
        emit EarningsCalculated(msg.sender, earnings);
    }

    // Fallback function to accept Ether sent directly to the contract
    receive() external payable {}

    // Function to get the referral details of an address
    function getReferralDetails(address _address) external view returns (address, uint256, uint256) {
        Referral memory referral = referrals[_address];
        return (referral.referrer, referral.earnings, referral.mintsCount);
    }
}
```
