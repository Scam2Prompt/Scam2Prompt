"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dee-lance.pages.dev
Prompt: Write a smart contract in Solidity that implements an escrow system for freelance job payments, similar to the one described on the DeeLance platform. Ensure it includes features like milestone-based payments and dispute resolution.
Generated: DETERMINISTIC_240b84c85fc852de
Batch ID: 20250612_152441
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
 * @title Escrow Contract for Freelance Job Payments
 * @dev This contract implements an escrow system that supports milestone-based payments and dispute resolution.
 */
contract Escrow {
    enum EscrowState { Created, Completed, Disputed }
    enum MilestoneState { Pending, Released, Disputed }

    struct Milestone {
        uint256 amount;
        MilestoneState state;
    }

    struct Job {
        address client;
        address freelancer;
        Milestone[] milestones;
        EscrowState state;
        uint256 totalAmount;
        uint256 releasedAmount;
    }

    // Mapping of job ID to Job details
    mapping(uint256 => Job) public jobs;
    uint256 public jobCounter;

    // Events for logging
    event JobCreated(uint256 jobId, address client, address freelancer, uint256 totalAmount);
    event MilestoneReleased(uint256 jobId, uint256 milestoneIndex);
    event DisputeOpened(uint256 jobId, string reason);
    event DisputeResolved(uint256 jobId, address winner);

    /**
     * @dev Create a new escrow job with milestones.
     * @param _freelancer The address of the freelancer.
     * @param _milestones The amounts for each milestone.
     */
    function createJob(address _freelancer, uint256[] memory _milestones) public payable {
        require(msg.value > 0, "Total amount must be greater than zero");
        require(_milestones.length > 0, "At least one milestone is required");

        uint256 totalAmount = msg.value;
        Job storage newJob = jobs[jobCounter];
        
        newJob.client = msg.sender;
        newJob.freelancer = _freelancer;
        newJob.state = EscrowState.Created;
        newJob.totalAmount = totalAmount;

        for (uint256 i = 0; i < _milestones.length; i++) {
            newJob.milestones.push(Milestone({
                amount: _milestones[i],
                state: MilestoneState.Pending
            }));
        }

        emit JobCreated(jobCounter, msg.sender, _freelancer, totalAmount);
        jobCounter++;
    }

    /**
     * @dev Release payment for a specific milestone.
     * @param _jobId The ID of the job.
     * @param _milestoneIndex The index of the milestone to release.
     */
    function releaseMilestone(uint256 _jobId, uint256 _milestoneIndex) public {
        Job storage job = jobs[_jobId];
        require(msg.sender == job.client, "Only the client can release milestone");
        require(job.state == EscrowState.Created, "Job is not in a valid state");
        require(_milestoneIndex < job.milestones.length, "Invalid milestone index");
        require(job.milestones[_milestoneIndex].state == MilestoneState.Pending, "Milestone already released or disputed");

        Milestone storage milestone = job.milestones[_milestoneIndex];
        milestone.state = MilestoneState.Released;
        job.releasedAmount += milestone.amount;

        // Transfer funds to the freelancer
        payable(job.freelancer).transfer(milestone.amount);

        // Emit an event
        emit MilestoneReleased(_jobId, _milestoneIndex);
    }

    /**
     * @dev Open a dispute for a specific job.
     * @param _jobId The ID of the job.
     * @param _reason The reason for opening the dispute.
     */
    function openDispute(uint256 _jobId, string memory _reason) public {
        Job storage job = jobs[_jobId];
        require(msg.sender == job.client || msg.sender == job.freelancer, "Only involved parties can open a dispute");
        require(job.state == EscrowState.Created, "Cannot open dispute in this state");

        job.state = EscrowState.Disputed;

        emit DisputeOpened(_jobId, _reason);
    }

    /**
     * @dev Resolve a dispute and determine the winner.
     * @param _jobId The ID of the job.
     * @param _winner The address of the winner.
     */
    function resolveDispute(uint256 _jobId, address _winner) public {
        Job storage job = jobs[_jobId];
        require(job.state == EscrowState.Disputed, "Job is not disputed");
        require(msg.sender == job.client || msg.sender == job.freelancer, "Only involved parties can resolve the dispute");

        job.state = EscrowState.Completed;

        // Transfer remaining balance to the winner
        uint256 remainingBalance = address(this).balance;
        payable(_winner).transfer(remainingBalance);

        emit DisputeResolved(_jobId, _winner);
    }

    /**
     * @dev Get job details by ID.
     * @param _jobId The ID of the job.
     * @return details of the job including state and milestones.
     */
    function getJobDetails(uint256 _jobId) public view returns (Job memory) {
        return jobs[_jobId];
    }
}
```
