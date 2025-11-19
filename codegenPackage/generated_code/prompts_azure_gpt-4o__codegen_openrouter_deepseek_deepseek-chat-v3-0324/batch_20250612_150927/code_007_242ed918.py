"""
Generated Code Metadata:
========================
Original URL: https://9aa9e9cd.dapp-a9y.pages.dev
Prompt: Generate a smart contract template that integrates HatsFinance's bug bounty features for securing a DeFi protocol.
Generated: DETERMINISTIC_242ed918d0f004e1
Batch ID: 20250612_150927
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
 * @title HatsFinanceBugBountyIntegration
 * @dev A smart contract template for integrating HatsFinance's bug bounty features
 * to secure a DeFi protocol with proper reward mechanisms and vulnerability reporting.
 */
contract HatsFinanceBugBountyIntegration is Ownable, ReentrancyGuard {
    // Struct to store bounty details
    struct Bounty {
        uint256 amount;
        address token;
        bool isActive;
        uint256 severityLevel; // 1-5 scale (1=low, 5=critical)
        string description;
    }

    // Struct to store reported vulnerabilities
    struct VulnerabilityReport {
        address reporter;
        string description;
        uint256 bountyId;
        uint256 timestamp;
        bool isVerified;
        bool isPaid;
    }

    // Mapping of bounty IDs to Bounty structs
    mapping(uint256 => Bounty) public bounties;

    // Mapping of report IDs to VulnerabilityReport structs
    mapping(uint256 => VulnerabilityReport) public vulnerabilityReports;

    // Counter for bounty IDs
    uint256 public nextBountyId;

    // Counter for report IDs
    uint256 public nextReportId;

    // Address of HatsFinance contract (to be set by owner)
    address public hatsFinanceAddress;

    // Events
    event BountyCreated(
        uint256 indexed bountyId,
        uint256 amount,
        address token,
        uint256 severityLevel,
        string description
    );
    event BountyUpdated(uint256 indexed bountyId, bool isActive);
    event VulnerabilityReported(
        uint256 indexed reportId,
        address indexed reporter,
        uint256 indexed bountyId,
        string description
    );
    event VulnerabilityVerified(uint256 indexed reportId, bool isVerified);
    event RewardPaid(
        uint256 indexed reportId,
        address indexed reporter,
        uint256 amount,
        address token
    );

    /**
     * @dev Constructor to initialize the contract
     * @param _hatsFinanceAddress Address of HatsFinance contract
     */
    constructor(address _hatsFinanceAddress) {
        require(
            _hatsFinanceAddress != address(0),
            "Invalid HatsFinance address"
        );
        hatsFinanceAddress = _hatsFinanceAddress;
    }

    /**
     * @dev Create a new bug bounty
     * @param amount Reward amount for the bounty
     * @param token Token address for the reward (address(0) for native token)
     * @param severityLevel Severity level (1-5)
     * @param description Description of the bounty
     */
    function createBounty(
        uint256 amount,
        address token,
        uint256 severityLevel,
        string memory description
    ) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(severityLevel >= 1 && severityLevel <= 5, "Invalid severity level");

        uint256 bountyId = nextBountyId++;
        bounties[bountyId] = Bounty({
            amount: amount,
            token: token,
            isActive: true,
            severityLevel: severityLevel,
            description: description
        });

        emit BountyCreated(bountyId, amount, token, severityLevel, description);
    }

    /**
     * @dev Update bounty status (active/inactive)
     * @param bountyId ID of the bounty to update
     * @param isActive New status of the bounty
     */
    function updateBountyStatus(uint256 bountyId, bool isActive) external onlyOwner {
        require(bountyId < nextBountyId, "Invalid bounty ID");
        bounties[bountyId].isActive = isActive;
        emit BountyUpdated(bountyId, isActive);
    }

    /**
     * @dev Report a vulnerability
     * @param bountyId ID of the related bounty
     * @param description Description of the vulnerability
     */
    function reportVulnerability(
        uint256 bountyId,
        string memory description
    ) external nonReentrant {
        require(bountyId < nextBountyId, "Invalid bounty ID");
        require(bounties[bountyId].isActive, "Bounty is not active");
        require(bytes(description).length > 0, "Description cannot be empty");

        uint256 reportId = nextReportId++;
        vulnerabilityReports[reportId] = VulnerabilityReport({
            reporter: msg.sender,
            description: description,
            bountyId: bountyId,
            timestamp: block.timestamp,
            isVerified: false,
            isPaid: false
        });

        emit VulnerabilityReported(reportId, msg.sender, bountyId, description);
    }

    /**
     * @dev Verify a vulnerability report (only owner or HatsFinance can call)
     * @param reportId ID of the report to verify
     * @param isVerified Verification status
     */
    function verifyVulnerability(
        uint256 reportId,
        bool isVerified
    ) external {
        require(reportId < nextReportId, "Invalid report ID");
        require(
            msg.sender == owner() || msg.sender == hatsFinanceAddress,
            "Not authorized"
        );

        vulnerabilityReports[reportId].isVerified = isVerified;
        emit VulnerabilityVerified(reportId, isVerified);
    }

    /**
     * @dev Pay reward for a verified vulnerability report
     * @param reportId ID of the verified report
     */
    function payReward(uint256 reportId) external nonReentrant {
        require(reportId < nextReportId, "Invalid report ID");
        VulnerabilityReport storage report = vulnerabilityReports[reportId];
        require(report.isVerified, "Report not verified");
        require(!report.isPaid, "Reward already paid");

        Bounty storage bounty = bounties[report.bountyId];
        require(bounty.amount > 0, "Bounty amount is zero");

        report.isPaid = true;

        if (bounty.token == address(0)) {
            // Native token transfer
            (bool success, ) = report.reporter.call{value: bounty.amount}("");
            require(success, "Transfer failed");
        } else {
            // ERC20 token transfer
            IERC20 token = IERC20(bounty.token);
            require(
                token.transfer(report.reporter, bounty.amount),
                "Token transfer failed"
            );
        }

        emit RewardPaid(
            reportId,
            report.reporter,
            bounty.amount,
            bounty.token
        );
    }

    /**
     * @dev Update HatsFinance address (only owner)
     * @param _hatsFinanceAddress New HatsFinance address
     */
    function updateHatsFinanceAddress(address _hatsFinanceAddress) external onlyOwner {
        require(
            _hatsFinanceAddress != address(0),
            "Invalid HatsFinance address"
        );
        hatsFinanceAddress = _hatsFinanceAddress;
    }

    /**
     * @dev Withdraw funds from contract (only owner)
     * @param token Token address to withdraw (address(0) for native token)
     * @param amount Amount to withdraw
     */
    function withdrawFunds(address token, uint256 amount) external onlyOwner {
        if (token == address(0)) {
            (bool success, ) = owner().call{value: amount}("");
            require(success, "Transfer failed");
        } else {
            IERC20(token).transfer(owner(), amount);
        }
    }

    // Receive function to accept native token deposits
    receive() external payable {}
}
```
