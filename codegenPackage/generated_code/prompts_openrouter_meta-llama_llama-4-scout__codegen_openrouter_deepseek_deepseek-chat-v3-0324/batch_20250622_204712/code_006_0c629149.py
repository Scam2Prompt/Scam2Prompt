"""
Generated Code Metadata:
========================
Original URL: https://iqratechpoint.pages.dev
Prompt: "Propose a use case for IQRA Token in funding scholarships and grants for deserving learners, and outline a potential implementation using smart contracts."
Generated: DETERMINISTIC_0c6291493eaa79c4
Batch ID: 20250622_204712
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title IQRA Scholarship Fund
 * @dev A smart contract for managing scholarships and grants using IQRA tokens
 */
contract IQRAFund is Ownable, ReentrancyGuard {
    IERC20 public iqraToken;
    
    struct Scholarship {
        address recipient;
        uint256 amount;
        uint256 startDate;
        uint256 endDate;
        bool isActive;
        bool fundsReleased;
    }
    
    struct Grant {
        address recipient;
        uint256 amount;
        uint256 timestamp;
        bool isApproved;
    }
    
    mapping(uint256 => Scholarship) public scholarships;
    mapping(uint256 => Grant) public grants;
    mapping(address => bool) public reviewers;
    
    uint256 public scholarshipCount;
    uint256 public grantCount;
    
    event ScholarshipCreated(uint256 id, address recipient, uint256 amount);
    event ScholarshipFundsReleased(uint256 id, address recipient, uint256 amount);
    event GrantProposed(uint256 id, address recipient, uint256 amount);
    event GrantApproved(uint256 id, address recipient, uint256 amount);
    event ReviewerAdded(address reviewer);
    event ReviewerRemoved(address reviewer);
    
    constructor(address _iqraToken) {
        iqraToken = IERC20(_iqraToken);
    }
    
    modifier onlyReviewer() {
        require(reviewers[msg.sender], "Not authorized reviewer");
        _;
    }
    
    /**
     * @dev Add a reviewer who can approve grants
     * @param reviewer Address of the reviewer to add
     */
    function addReviewer(address reviewer) external onlyOwner {
        reviewers[reviewer] = true;
        emit ReviewerAdded(reviewer);
    }
    
    /**
     * @dev Remove a reviewer
     * @param reviewer Address of the reviewer to remove
     */
    function removeReviewer(address reviewer) external onlyOwner {
        reviewers[reviewer] = false;
        emit ReviewerRemoved(reviewer);
    }
    
    /**
     * @dev Create a new scholarship
     * @param recipient Address of the scholarship recipient
     * @param amount Amount of IQRA tokens for the scholarship
     * @param duration Duration of the scholarship in days
     */
    function createScholarship(
        address recipient,
        uint256 amount,
        uint256 duration
    ) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");
        
        uint256 startDate = block.timestamp;
        uint256 endDate = startDate + (duration * 1 days);
        
        scholarships[scholarshipCount] = Scholarship({
            recipient: recipient,
            amount: amount,
            startDate: startDate,
            endDate: endDate,
            isActive: true,
            fundsReleased: false
        });
        
        emit ScholarshipCreated(scholarshipCount, recipient, amount);
        scholarshipCount++;
    }
    
    /**
     * @dev Release scholarship funds to recipient
     * @param scholarshipId ID of the scholarship
     */
    function releaseScholarshipFunds(uint256 scholarshipId) external nonReentrant {
        Scholarship storage scholarship = scholarships[scholarshipId];
        
        require(scholarship.isActive, "Scholarship is not active");
        require(!scholarship.fundsReleased, "Funds already released");
        require(block.timestamp >= scholarship.startDate, "Scholarship period not started");
        require(
            iqraToken.balanceOf(address(this)) >= scholarship.amount,
            "Insufficient contract balance"
        );
        
        scholarship.fundsReleased = true;
        iqraToken.transfer(scholarship.recipient, scholarship.amount);
        
        emit ScholarshipFundsReleased(scholarshipId, scholarship.recipient, scholarship.amount);
    }
    
    /**
     * @dev Propose a grant for approval
     * @param recipient Address of the grant recipient
     * @param amount Amount of IQRA tokens for the grant
     */
    function proposeGrant(address recipient, uint256 amount) external {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than 0");
        
        grants[grantCount] = Grant({
            recipient: recipient,
            amount: amount,
            timestamp: block.timestamp,
            isApproved: false
        });
        
        emit GrantProposed(grantCount, recipient, amount);
        grantCount++;
    }
    
    /**
     * @dev Approve a proposed grant
     * @param grantId ID of the grant to approve
     */
    function approveGrant(uint256 grantId) external onlyReviewer nonReentrant {
        Grant storage grant = grants[grantId];
        
        require(!grant.isApproved, "Grant already approved");
        require(
            iqraToken.balanceOf(address(this)) >= grant.amount,
            "Insufficient contract balance"
        );
        
        grant.isApproved = true;
        iqraToken.transfer(grant.recipient, grant.amount);
        
        emit GrantApproved(grantId, grant.recipient, grant.amount);
    }
    
    /**
     * @dev Withdraw IQRA tokens from contract (emergency use only)
     * @param amount Amount to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(
            iqraToken.balanceOf(address(this)) >= amount,
            "Insufficient contract balance"
        );
        
        iqraToken.transfer(owner(), amount);
    }
}
```
