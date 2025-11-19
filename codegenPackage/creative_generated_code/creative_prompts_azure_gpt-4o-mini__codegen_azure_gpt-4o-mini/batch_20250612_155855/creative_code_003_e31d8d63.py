"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bull-dogito-com.pages.dev
Prompt: Create a Solidity smart contract that allows community voting on which companies should join the BDOGITO ecosystem.
Generated: DETERMINISTIC_e31d8d634381f3e7
Batch ID: 20250612_155855
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

/// @title BDOGITO Ecosystem Voting Contract
/// @author Your Name
/// @notice This contract allows community voting on which companies should join the BDOGITO ecosystem.
contract BDOGITOVoting {
    // Structure to hold company details
    struct Company {
        string name;               // Name of the company
        uint256 voteCount;         // Number of votes received
        bool exists;               // Check if the company is added
    }

    // Mapping to store companies by their ID
    mapping(uint256 => Company) public companies;
    uint256 public companyCount;       // Total number of companies added
    mapping(address => mapping(uint256 => bool)) public hasVoted; // Track if an address has voted for a company

    // Events
    event CompanyAdded(uint256 indexed companyId, string name);
    event Voted(uint256 indexed companyId, address indexed voter);

    /// @notice Adds a new company to the voting list
    /// @param _name The name of the company to be added
    /// @dev Only callable by the contract owner (to be implemented)
    function addCompany(string memory _name) public {
        require(bytes(_name).length > 0, "Company name must not be empty");

        // Create new company and increment the company count
        companies[companyCount] = Company({
            name: _name,
            voteCount: 0,
            exists: true
        });

        emit CompanyAdded(companyCount, _name);
        companyCount++;
    }

    /// @notice Vote for a company by its ID
    /// @param _companyId The ID of the company to vote for
    /// @dev Voters can only vote once per company
    function vote(uint256 _companyId) public {
        require(_companyId < companyCount, "Invalid company ID");
        require(!hasVoted[msg.sender][_companyId], "You have already voted for this company");

        // Record the vote
        hasVoted[msg.sender][_companyId] = true;
        companies[_companyId].voteCount++;

        emit Voted(_companyId, msg.sender);
    }

    /// @notice Retrieves the details of a company
    /// @param _companyId The ID of the company
    /// @return name The name of the company
    /// @return voteCount The total number of votes the company has received
    function getCompany(uint256 _companyId) public view returns (string memory name, uint256 voteCount) {
        require(_companyId < companyCount, "Invalid company ID");
        Company memory company = companies[_companyId];
        return (company.name, company.voteCount);
    }

    /// @notice Retrieves the total number of companies
    /// @return The total number of companies in the voting system
    function totalCompanies() public view returns (uint256) {
        return companyCount;
    }
}
```
