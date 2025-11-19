"""
Generated Code Metadata:
========================
Original URL: https://oeth-route.pages.dev
Prompt: Write a Solidity contract to implement the bug bounty mechanism for OUSD, offering rewards for identifying vulnerabilities, as described in the documentation.
Generated: DETERMINISTIC_e3d7ddb2b276d583
Batch ID: 20250612_150622
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
 * @title OUSDBugBounty
 * @dev A contract for managing bug bounty rewards for OUSD vulnerabilities.
 */
contract OUSDBugBounty is Ownable, ReentrancyGuard {
    // OUSD token contract
    IERC20 public immutable ousdToken;

    // Bounty tiers in OUSD tokens
    uint256 public constant CRITICAL_TIER = 50000 ether; // 50,000 OUSD
    uint256 public constant HIGH_TIER = 25000 ether;    // 25,000 OUSD
    uint256 public constant MEDIUM_TIER = 10000 ether;  // 10,000 OUSD
    uint256 public constant LOW_TIER = 5000 ether;      // 5,000 OUSD

    // Bounty status
    enum BountyStatus { PENDING, APPROVED, REJECTED, PAID }

    // Bounty submission
    struct BountySubmission {
        address submitter;
        string description;
        uint256 tier;
        BountyStatus status;
    }

    // Mapping of bounty IDs to submissions
    mapping(uint256 => BountySubmission) public bountySubmissions;
    uint256 public nextBountyId;

    // Events
    event BountySubmitted(
        uint256 indexed bountyId,
        address indexed submitter,
        string description,
        uint256 tier
    );
    event BountyReviewed(
        uint256 indexed bountyId,
        BountyStatus status,
        address reviewer
    );
    event BountyPaid(
        uint256 indexed bountyId,
        address indexed submitter,
        uint256 amount
    );
    event FundsWithdrawn(address indexed owner, uint256 amount);

    /**
     * @dev Constructor initializes the OUSD token contract.
     * @param _ousdToken Address of the OUSD token contract.
     */
    constructor(address _ousdToken) {
        require(_ousdToken != address(0), "Invalid OUSD token address");
        ousdToken = IERC20(_ousdToken);
    }

    /**
     * @dev Submit a bug bounty report.
     * @param _description Description of the vulnerability.
     * @param _tier The severity tier of the vulnerability.
     */
    function submitBounty(
        string calldata _description,
        uint256 _tier
    ) external {
        require(bytes(_description).length > 0, "Description cannot be empty");
        require(
            _tier == CRITICAL_TIER ||
                _tier == HIGH_TIER ||
                _tier == MEDIUM_TIER ||
                _tier == LOW_TIER,
            "Invalid bounty tier"
        );

        uint256 bountyId = nextBountyId++;
        bountySubmissions[bountyId] = BountySubmission({
            submitter: msg.sender,
            description: _description,
            tier: _tier,
            status: BountyStatus.PENDING
        });

        emit BountySubmitted(bountyId, msg.sender, _description, _tier);
    }

    /**
     * @dev Review a bounty submission (only owner).
     * @param _bountyId ID of the bounty submission.
     * @param _approved Whether the bounty is approved.
     */
    function reviewBounty(
        uint256 _bountyId,
        bool _approved
    ) external onlyOwner {
        require(_bountyId < nextBountyId, "Invalid bounty ID");
        BountySubmission storage submission = bountySubmissions[_bountyId];
        require(
            submission.status == BountyStatus.PENDING,
            "Bounty already reviewed"
        );

        submission.status = _approved ? BountyStatus.APPROVED : BountyStatus.REJECTED;

        emit BountyReviewed(
            _bountyId,
            submission.status,
            msg.sender
        );
    }

    /**
     * @dev Pay out an approved bounty (only owner).
     * @param _bountyId ID of the bounty submission.
     */
    function payBounty(uint256 _bountyId) external onlyOwner nonReentrant {
        require(_bountyId < nextBountyId, "Invalid bounty ID");
        BountySubmission storage submission = bountySubmissions[_bountyId];
        require(
            submission.status == BountyStatus.APPROVED,
            "Bounty not approved"
        );
        require(submission.status != BountyStatus.PAID, "Bounty already paid");

        uint256 amount = submission.tier;
        uint256 contractBalance = ousdToken.balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient contract balance");

        submission.status = BountyStatus.PAID;
        ousdToken.transfer(submission.submitter, amount);

        emit BountyPaid(_bountyId, submission.submitter, amount);
    }

    /**
     * @dev Withdraw remaining OUSD tokens from the contract (only owner).
     * @param _amount Amount to withdraw.
     */
    function withdrawFunds(uint256 _amount) external onlyOwner nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        uint256 contractBalance = ousdToken.balanceOf(address(this));
        require(contractBalance >= _amount, "Insufficient contract balance");

        ousdToken.transfer(owner(), _amount);
        emit FundsWithdrawn(owner(), _amount);
    }

    /**
     * @dev Get the current contract balance in OUSD tokens.
     * @return The contract balance.
     */
    function getContractBalance() external view returns (uint256) {
        return ousdToken.balanceOf(address(this));
    }
}
```
