"""
Generated Code Metadata:
========================
Original URL: https://swanchain4.pages.dev
Prompt: Write a smart contract using Swan Chain's Layer 2 blockchain to automate payments for AI computing services, leveraging its decentralized payment system and reduced gas fees.
Generated: DETERMINISTIC_82cf2a09a8913f46
Batch ID: 20250612_152511
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title AIComputePayment
 * @dev Smart contract for automated payments for AI computing services on Swan Chain L2
 */
contract AIComputePayment is Ownable, ReentrancyGuard {
    // Struct to represent a computing job
    struct Job {
        address client;
        address provider;
        uint256 amount;
        uint256 duration;
        uint256 startTime;
        bool isCompleted;
        bool isPaid;
    }

    // Swan Chain's native token interface
    IERC20 public paymentToken;

    // Mapping of job IDs to Job structs
    mapping(bytes32 => Job) public jobs;

    // Service fee percentage (1 = 0.1%, 100 = 10%)
    uint256 public serviceFeePercentage = 10; // Default 1%

    // Events
    event JobCreated(
        bytes32 indexed jobId,
        address indexed client,
        address indexed provider,
        uint256 amount,
        uint256 duration
    );
    event JobCompleted(bytes32 indexed jobId);
    event PaymentReleased(bytes32 indexed jobId, uint256 amount);
    event ServiceFeeUpdated(uint256 newFeePercentage);

    /**
     * @dev Constructor
     * @param _paymentToken Address of the ERC20 token used for payments
     */
    constructor(address _paymentToken) {
        require(_paymentToken != address(0), "Invalid token address");
        paymentToken = IERC20(_paymentToken);
    }

    /**
     * @dev Create a new computing job
     * @param _jobId Unique identifier for the job
     * @param _provider Address of the service provider
     * @param _amount Payment amount in tokens
     * @param _duration Duration of the job in seconds
     */
    function createJob(
        bytes32 _jobId,
        address _provider,
        uint256 _amount,
        uint256 _duration
    ) external nonReentrant {
        require(_provider != address(0), "Invalid provider address");
        require(_amount > 0, "Amount must be greater than 0");
        require(jobs[_jobId].client == address(0), "Job ID already exists");

        // Transfer tokens from client to contract
        require(
            paymentToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        jobs[_jobId] = Job({
            client: msg.sender,
            provider: _provider,
            amount: _amount,
            duration: _duration,
            startTime: block.timestamp,
            isCompleted: false,
            isPaid: false
        });

        emit JobCreated(_jobId, msg.sender, _provider, _amount, _duration);
    }

    /**
     * @dev Mark a job as completed
     * @param _jobId ID of the job to complete
     */
    function completeJob(bytes32 _jobId) external {
        Job storage job = jobs[_jobId];
        require(job.provider == msg.sender, "Only provider can complete job");
        require(!job.isCompleted, "Job already completed");
        require(block.timestamp <= job.startTime + job.duration, "Job duration exceeded");

        job.isCompleted = true;
        emit JobCompleted(_jobId);
    }

    /**
     * @dev Release payment to the provider
     * @param _jobId ID of the job to release payment for
     */
    function releasePayment(bytes32 _jobId) external nonReentrant {
        Job storage job = jobs[_jobId];
        require(job.client == msg.sender || msg.sender == owner(), "Unauthorized");
        require(job.isCompleted, "Job not completed");
        require(!job.isPaid, "Payment already released");

        uint256 serviceFee = (job.amount * serviceFeePercentage) / 1000;
        uint256 providerAmount = job.amount - serviceFee;

        // Transfer payment to provider
        require(
            paymentToken.transfer(job.provider, providerAmount),
            "Provider transfer failed"
        );

        // Transfer service fee to owner
        if (serviceFee > 0) {
            require(
                paymentToken.transfer(owner(), serviceFee),
                "Fee transfer failed"
            );
        }

        job.isPaid = true;
        emit PaymentReleased(_jobId, providerAmount);
    }

    /**
     * @dev Update the service fee percentage
     * @param _newFeePercentage New fee percentage (1 = 0.1%, 100 = 10%)
     */
    function updateServiceFee(uint256 _newFeePercentage) external onlyOwner {
        require(_newFeePercentage <= 100, "Fee cannot exceed 10%");
        serviceFeePercentage = _newFeePercentage;
        emit ServiceFeeUpdated(_newFeePercentage);
    }

    /**
     * @dev Get job details
     * @param _jobId ID of the job to query
     * @return Job details
     */
    function getJob(bytes32 _jobId) external view returns (Job memory) {
        return jobs[_jobId];
    }
}
```
