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

/**
 * @title ReferralBountySystem
 * @dev A smart contract for managing referral bounties in a Web3 job platform.
 * Recruiters earn rewards for successfully referring candidates to job openings.
 */
contract ReferralBountySystem {
    // Struct to store referral details
    struct Referral {
        address recruiter; // Address of the recruiter
        address candidate; // Address of the candidate
        uint256 jobId;     // ID of the job opening
        bool rewarded;     // Whether the recruiter has been rewarded
    }

    // Mapping to store referrals by ID
    mapping(uint256 => Referral) public referrals;

    // Mapping to store job rewards
    mapping(uint256 => uint256) public jobRewards;

    // Counter for referral IDs
    uint256 private referralCounter;

    // Address of the platform owner
    address public owner;

    // Event emitted when a referral is created
    event ReferralCreated(uint256 referralId, address recruiter, address candidate, uint256 jobId);

    // Event emitted when a reward is distributed
    event RewardDistributed(uint256 referralId, address recruiter, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Modifier to ensure the job has a reward set
    modifier jobHasReward(uint256 jobId) {
        require(jobRewards[jobId] > 0, "Job does not have a reward set");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Set the reward for a specific job.
     * @param jobId The ID of the job opening.
     * @param reward The reward amount in wei.
     */
    function setJobReward(uint256 jobId, uint256 reward) external onlyOwner {
        require(reward > 0, "Reward must be greater than zero");
        jobRewards[jobId] = reward;
    }

    /**
     * @dev Create a referral for a job opening.
     * @param recruiter The address of the recruiter.
     * @param candidate The address of the candidate.
     * @param jobId The ID of the job opening.
     */
    function createReferral(address recruiter, address candidate, uint256 jobId)
        external
        jobHasReward(jobId)
    {
        require(recruiter != address(0), "Recruiter address cannot be zero");
        require(candidate != address(0), "Candidate address cannot be zero");
        require(recruiter != candidate, "Recruiter and candidate cannot be the same");

        referralCounter++;
        referrals[referralCounter] = Referral({
            recruiter: recruiter,
            candidate: candidate,
            jobId: jobId,
            rewarded: false
        });

        emit ReferralCreated(referralCounter, recruiter, candidate, jobId);
    }

    /**
     * @dev Distribute the reward to the recruiter for a successful referral.
     * @param referralId The ID of the referral.
     */
    function distributeReward(uint256 referralId) external onlyOwner {
        Referral storage referral = referrals[referralId];
        require(!referral.rewarded, "Reward has already been distributed");
        require(referral.recruiter != address(0), "Invalid referral");

        uint256 reward = jobRewards[referral.jobId];
        require(address(this).balance >= reward, "Insufficient contract balance");

        referral.rewarded = true;
        payable(referral.recruiter).transfer(reward);

        emit RewardDistributed(referralId, referral.recruiter, reward);
    }

    /**
     * @dev Deposit funds into the contract to cover rewards.
     */
    function depositFunds() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
    }

    /**
     * @dev Withdraw funds from the contract (only owner).
     * @param amount The amount to withdraw in wei.
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");
        payable(owner).transfer(amount);
    }

    /**
     * @dev Get the balance of the contract.
     * @return The balance of the contract in wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
