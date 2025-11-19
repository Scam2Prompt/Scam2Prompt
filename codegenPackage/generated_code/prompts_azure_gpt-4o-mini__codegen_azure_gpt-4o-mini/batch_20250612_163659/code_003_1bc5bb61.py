"""
Generated Code Metadata:
========================
Original URL: https://iqratechpoint.pages.dev
Prompt: Generate a sample smart contract for managing scholarships and grants using IQRA Token on the Binance Smart Chain.
Generated: DETERMINISTIC_1bc5bb618d3296a1
Batch ID: 20250612_163659
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

// Importing the ERC20 interface for the IQRA Token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// ScholarshipManager contract to manage scholarships and grants using IQRA Token
contract ScholarshipManager is Ownable {
    // Struct to represent a scholarship
    struct Scholarship {
        string name;
        address recipient;
        uint256 amount;
        bool isActive;
    }

    // Mapping to store scholarships by their ID
    mapping(uint256 => Scholarship) public scholarships;
    // Counter for scholarship IDs
    uint256 public scholarshipCount;

    // The IQRA Token contract address
    IERC20 public iqraToken;

    // Event emitted when a scholarship is created
    event ScholarshipCreated(uint256 indexed scholarshipId, string name, address indexed recipient, uint256 amount);
    // Event emitted when a scholarship is funded
    event ScholarshipFunded(uint256 indexed scholarshipId, uint256 amount);
    // Event emitted when a scholarship is withdrawn
    event ScholarshipWithdrawn(uint256 indexed scholarshipId, address indexed recipient, uint256 amount);

    // Constructor to set the IQRA Token address
    constructor(address _iqraToken) {
        require(_iqraToken != address(0), "Invalid IQRA Token address");
        iqraToken = IERC20(_iqraToken);
    }

    // Function to create a new scholarship
    function createScholarship(string memory _name, address _recipient, uint256 _amount) external onlyOwner {
        require(_recipient != address(0), "Invalid recipient address");
        require(_amount > 0, "Amount must be greater than zero");

        scholarshipCount++;
        scholarships[scholarshipCount] = Scholarship({
            name: _name,
            recipient: _recipient,
            amount: _amount,
            isActive: true
        });

        emit ScholarshipCreated(scholarshipCount, _name, _recipient, _amount);
    }

    // Function to fund a scholarship
    function fundScholarship(uint256 _scholarshipId) external {
        Scholarship storage scholarship = scholarships[_scholarshipId];
        require(scholarship.isActive, "Scholarship is not active");
        require(scholarship.amount > 0, "Scholarship amount must be greater than zero");

        // Transfer IQRA tokens from the caller to the contract
        require(iqraToken.transferFrom(msg.sender, address(this), scholarship.amount), "Token transfer failed");

        emit ScholarshipFunded(_scholarshipId, scholarship.amount);
    }

    // Function to withdraw funds from a scholarship
    function withdrawScholarship(uint256 _scholarshipId) external {
        Scholarship storage scholarship = scholarships[_scholarshipId];
        require(scholarship.isActive, "Scholarship is not active");
        require(msg.sender == scholarship.recipient, "Only the recipient can withdraw");

        // Mark the scholarship as inactive
        scholarship.isActive = false;

        // Transfer the scholarship amount to the recipient
        require(iqraToken.transfer(scholarship.recipient, scholarship.amount), "Token transfer failed");

        emit ScholarshipWithdrawn(_scholarshipId, scholarship.recipient, scholarship.amount);
    }

    // Function to get scholarship details
    function getScholarship(uint256 _scholarshipId) external view returns (string memory, address, uint256, bool) {
        Scholarship storage scholarship = scholarships[_scholarshipId];
        return (scholarship.name, scholarship.recipient, scholarship.amount, scholarship.isActive);
    }
}
```
