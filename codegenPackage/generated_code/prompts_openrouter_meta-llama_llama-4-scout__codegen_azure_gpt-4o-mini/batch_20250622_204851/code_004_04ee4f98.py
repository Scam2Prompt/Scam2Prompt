"""
Generated Code Metadata:
========================
Original URL: https://bondex-app.pages.dev
Prompt: Develop a smart contract for a referral bounty system, enabling recruiters to earn rewards for referring candidates to Web3 job openings on a platform like Bondex.
Generated: DETERMINISTIC_04ee4f98122ea0d7
Batch ID: 20250622_204851
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

contract ReferralBounty {
    // Struct to hold information about each referral
    struct Referral {
        address recruiter; // Address of the recruiter
        address candidate; // Address of the candidate referred
        uint256 bountyAmount; // Amount of bounty for the referral
        bool isClaimed; // Status of the bounty claim
    }

    // Mapping to store referrals by their unique ID
    mapping(uint256 => Referral) public referrals;
    // Counter for unique referral IDs
    uint256 public referralCount;
    // Address of the contract owner
    address public owner;

    // Event emitted when a new referral is created
    event ReferralCreated(uint256 indexed referralId, address indexed recruiter, address indexed candidate, uint256 bountyAmount);
    // Event emitted when a bounty is claimed
    event BountyClaimed(uint256 indexed referralId, address indexed recruiter);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    // Function to create a new referral
    function createReferral(address _candidate, uint256 _bountyAmount) external {
        require(_candidate != address(0), "Invalid candidate address");
        require(_bountyAmount > 0, "Bounty amount must be greater than zero");

        // Increment the referral count to create a unique ID
        referralCount++;
        // Create a new referral
        referrals[referralCount] = Referral(msg.sender, _candidate, _bountyAmount, false);

        // Emit the ReferralCreated event
        emit ReferralCreated(referralCount, msg.sender, _candidate, _bountyAmount);
    }

    // Function to claim the bounty for a referral
    function claimBounty(uint256 _referralId) external {
        Referral storage referral = referrals[_referralId];

        // Ensure the referral exists and is not already claimed
        require(referral.recruiter != address(0), "Referral does not exist");
        require(!referral.isClaimed, "Bounty already claimed");
        require(msg.sender == referral.recruiter, "Only the recruiter can claim the bounty");

        // Mark the bounty as claimed
        referral.isClaimed = true;

        // Transfer the bounty amount to the recruiter
        payable(referral.recruiter).transfer(referral.bountyAmount);

        // Emit the BountyClaimed event
        emit BountyClaimed(_referralId, referral.recruiter);
    }

    // Function to withdraw funds from the contract (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    // Fallback function to accept ETH deposits
    receive() external payable {}
}
```
