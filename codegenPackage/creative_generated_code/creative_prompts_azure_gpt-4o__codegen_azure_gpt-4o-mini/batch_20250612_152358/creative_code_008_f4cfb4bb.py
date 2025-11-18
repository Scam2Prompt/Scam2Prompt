"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalmiracle.online
Prompt: Provide an example of a scholarship funding program in Solidity that uses GMC tokens for educational initiatives, as described in the use cases section of the Global Miracle Coin site.
Generated: DETERMINISTIC_f4cfb4bbd421e86d
Batch ID: 20250612_152358
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

// Importing OpenZeppelin's ERC20 interface for token transfers
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract ScholarshipFunding {

    // Struct to represent a scholarship
    struct Scholarship {
        uint256 id;
        address recipient;
        uint256 amount;
        bool funded;
    }

    // State variables
    IERC20 public gmcToken; // Instance of the GMC token
    uint256 public scholarshipCount; // Counter to track scholarship IDs
    mapping(uint256 => Scholarship) public scholarships; // Mapping to store scholarships
    address public admin; // Admin address for managing scholarships

    // Events
    event ScholarshipCreated(uint256 indexed id, address indexed recipient, uint256 amount);
    event ScholarshipFunded(uint256 indexed id, address indexed recipient, uint256 amount);

    // Modifier to restrict access to admin functions
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    // Constructor to initialize the contract with the GMC token address
    constructor(address _gmcToken) {
        gmcToken = IERC20(_gmcToken);
        admin = msg.sender; // Set the contract creator as admin
    }

    // Function to create a new scholarship
    function createScholarship(address recipient, uint256 amount) external onlyAdmin {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        scholarshipCount++;
        scholarships[scholarshipCount] = Scholarship(scholarshipCount, recipient, amount, false);
        
        emit ScholarshipCreated(scholarshipCount, recipient, amount);
    }

    // Function to fund a scholarship with GMC tokens
    function fundScholarship(uint256 scholarshipId) external onlyAdmin {
        Scholarship storage scholarship = scholarships[scholarshipId];
        
        require(scholarship.id == scholarshipId, "Scholarship does not exist");
        require(!scholarship.funded, "Scholarship has already been funded");

        // Transfer GMC tokens from the admin to the recipient
        require(gmcToken.transfer(scholarship.recipient, scholarship.amount), "Token transfer failed");

        scholarship.funded = true; // Mark scholarship as funded

        emit ScholarshipFunded(scholarshipId, scholarship.recipient, scholarship.amount);
    }

    // Function to retrieve scholarship details
    function getScholarship(uint256 scholarshipId) external view returns (Scholarship memory) {
        require(scholarshipId > 0 && scholarshipId <= scholarshipCount, "Invalid scholarship ID");
        return scholarships[scholarshipId];
    }

    // Function to withdraw tokens in case of emergency (only for admin)
    function withdrawTokens(address to, uint256 amount) external onlyAdmin {
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        uint256 balance = gmcToken.balanceOf(address(this));
        require(amount <= balance, "Insufficient contract balance");

        require(gmcToken.transfer(to, amount), "Token transfer failed");
    }

    // Fallback function to receive ETH (if needed)
    receive() external payable {}
}
```
