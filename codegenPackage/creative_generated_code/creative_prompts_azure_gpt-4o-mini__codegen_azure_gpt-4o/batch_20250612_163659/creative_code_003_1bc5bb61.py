"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iqratechpoint.pages.dev
Prompt: Generate a sample smart contract for managing scholarships and grants using IQRA Token on the Binance Smart Chain.
Generated: DETERMINISTIC_1bc5bb618d3296a1
Batch ID: 20250612_163659
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
 * @title ScholarshipManager
 * @dev A smart contract to manage scholarships and grants using IQRA Token on Binance Smart Chain
 */
contract ScholarshipManager {
    // State variables
    address public admin; // Contract administrator address
    address public iqraToken; // IQRA Token contract address
    uint256 public totalScholarships; // Total scholarships created

    struct Scholarship {
        string name; // Scholarship name
        uint256 amount; // Scholarship amount in IQRA Token
        address recipient; // Recipient address
        bool isClaimed; // Whether the scholarship has been claimed
    }

    // Mapping to store scholarships by their ID
    mapping(uint256 => Scholarship) public scholarships;

    // Events
    event ScholarshipCreated(uint256 indexed scholarshipId, string name, uint256 amount, address indexed recipient);
    event ScholarshipClaimed(uint256 indexed scholarshipId, address indexed recipient);

    // Modifiers
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    modifier validScholarship(uint256 scholarshipId) {
        require(scholarshipId < totalScholarships, "Invalid scholarship ID");
        _;
    }

    constructor(address _iqraToken) {
        require(_iqraToken != address(0), "IQRA Token address cannot be zero");
        admin = msg.sender; // Set contract deployer as admin
        iqraToken = _iqraToken; // Set IQRA Token contract address
    }

    /**
     * @dev Creates a new scholarship.
     * @param _name Name of the scholarship
     * @param _amount Amount in IQRA Token
     * @param _recipient Recipient address
     */
    function createScholarship(string memory _name, uint256 _amount, address _recipient)
        external
        onlyAdmin
    {
        require(_amount > 0, "Scholarship amount must be greater than zero");
        require(_recipient != address(0), "Recipient address cannot be zero");

        // Create a new scholarship
        scholarships[totalScholarships] = Scholarship({
            name: _name,
            amount: _amount,
            recipient: _recipient,
            isClaimed: false
        });

        emit ScholarshipCreated(totalScholarships, _name, _amount, _recipient);

        // Increment the total scholarships counter
        totalScholarships++;
    }

    /**
     * @dev Allows the recipient to claim their scholarship.
     * @param scholarshipId ID of the scholarship to claim
     */
    function claimScholarship(uint256 scholarshipId) external validScholarship(scholarshipId) {
        Scholarship storage scholarship = scholarships[scholarshipId];

        require(!scholarship.isClaimed, "Scholarship already claimed");
        require(msg.sender == scholarship.recipient, "Only the recipient can claim this scholarship");

        // Transfer IQRA Token to the recipient
        bool success = IERC20(iqraToken).transfer(scholarship.recipient, scholarship.amount);
        require(success, "Token transfer failed");

        // Mark the scholarship as claimed
        scholarship.isClaimed = true;

        emit ScholarshipClaimed(scholarshipId, scholarship.recipient);
    }

    /**
     * @dev Updates the admin address.
     * @param newAdmin New admin address
     */
    function updateAdmin(address newAdmin) external onlyAdmin {
        require(newAdmin != address(0), "New admin address cannot be zero");
        admin = newAdmin;
    }

    /**
     * @dev Interface for interacting with IQRA Token (ERC20).
     */
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
    }
}
```
