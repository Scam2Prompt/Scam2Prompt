"""
Generated Code Metadata:
========================
Original URL: https://vivalalibertadproject.com
Prompt: Generate a smart contract code for managing token distribution and funding applications on a blockchain platform, inspired by the $LIBRA token and the Viva La Libertad Project.
Generated: DETERMINISTIC_f437851b24a36497
Batch ID: 20250622_211853
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

// Importing OpenZeppelin's ERC20 implementation for token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for managing token distribution and funding applications
contract LibraToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping to track funding applications
    struct Application {
        address applicant;
        uint256 amountRequested;
        bool approved;
        bool funded;
    }

    // State variables
    uint256 public totalApplications;
    mapping(uint256 => Application) public applications;

    // Events for logging
    event ApplicationSubmitted(uint256 indexed applicationId, address indexed applicant, uint256 amountRequested);
    event ApplicationApproved(uint256 indexed applicationId);
    event ApplicationFunded(uint256 indexed applicationId, uint256 amount);

    // Constructor to initialize the token
    constructor() ERC20("LibraToken", "LIBRA") {
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint initial supply to the contract owner
    }

    // Function to submit a funding application
    function submitApplication(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        totalApplications = totalApplications.add(1);
        applications[totalApplications] = Application(msg.sender, amount, false, false);

        emit ApplicationSubmitted(totalApplications, msg.sender, amount);
    }

    // Function to approve a funding application
    function approveApplication(uint256 applicationId) external onlyOwner {
        Application storage application = applications[applicationId];
        require(application.applicant != address(0), "Application does not exist");
        require(!application.approved, "Application already approved");

        application.approved = true;
        emit ApplicationApproved(applicationId);
    }

    // Function to fund an approved application
    function fundApplication(uint256 applicationId) external onlyOwner {
        Application storage application = applications[applicationId];
        require(application.approved, "Application not approved");
        require(!application.funded, "Application already funded");
        require(balanceOf(msg.sender) >= application.amountRequested, "Insufficient token balance");

        // Transfer tokens to the applicant
        _transfer(msg.sender, application.applicant, application.amountRequested);
        application.funded = true;

        emit ApplicationFunded(applicationId, application.amountRequested);
    }

    // Function to get application details
    function getApplication(uint256 applicationId) external view returns (address, uint256, bool, bool) {
        Application storage application = applications[applicationId];
        require(application.applicant != address(0), "Application does not exist");

        return (application.applicant, application.amountRequested, application.approved, application.funded);
    }
}
```
