"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://job3-threeprotocol.pages.dev
Prompt: Develop a smart contract to facilitate secure and instant crypto payments for job transactions, inspired by JOBS3's borderless payment system.
Generated: DETERMINISTIC_a3a54b8db7da9e3f
Batch ID: 20250612_150552
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
 * @title JobPayment
 * @dev A smart contract for secure and instant crypto payments for job transactions.
 */
contract JobPayment is Ownable {
    struct Job {
        address payable employer;
        address payable freelancer;
        uint256 amount;
        bool isPaid;
    }

    // Mapping to store job payments
    mapping(uint256 => Job) public jobs;
    uint256 public jobCounter;

    // Event emitted when a job payment is created
    event JobCreated(uint256 indexed jobId, address indexed employer, address indexed freelancer, uint256 amount);
    
    // Event emitted when a job payment is completed
    event JobPaid(uint256 indexed jobId, address indexed freelancer, uint256 amount);

    /**
     * @dev Create a new job payment
     * @param _freelancer The address of the freelancer
     * @param _amount The amount of payment in wei
     */
    function createJob(address payable _freelancer, uint256 _amount) external payable onlyOwner {
        require(msg.value == _amount, "Incorrect payment amount");
        
        jobCounter++;
        jobs[jobCounter] = Job({
            employer: payable(msg.sender),
            freelancer: _freelancer,
            amount: _amount,
            isPaid: false
        });

        emit JobCreated(jobCounter, msg.sender, _freelancer, _amount);
    }

    /**
     * @dev Complete the job payment
     * @param _jobId The ID of the job to pay
     */
    function payJob(uint256 _jobId) external {
        Job storage job = jobs[_jobId];

        // Ensure the job is valid and not already paid
        require(job.freelancer != address(0), "Job does not exist");
        require(!job.isPaid, "Job already paid");
        require(msg.sender == job.employer, "Only employer can pay");

        // Transfer the payment to the freelancer
        job.isPaid = true;
        (bool success, ) = job.freelancer.call{value: job.amount}("");
        require(success, "Transfer failed");

        emit JobPaid(_jobId, job.freelancer, job.amount);
    }

    /**
     * @dev Withdraw remaining funds if needed (for the owner)
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Withdraw failed");
    }

    /**
     * @dev Fallback function to receive Ether
     */
    receive() external payable {}
}
```
