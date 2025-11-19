"""
Generated Code Metadata:
========================
Original URL: https://bull-dogito-com.pages.dev
Prompt: Create a Solidity smart contract that allows community voting on which companies should join the BDOGITO ecosystem.
Generated: DETERMINISTIC_e31d8d634381f3e7
Batch ID: 20250612_155855
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
import "@openzeppelin/contracts/utils/Counters.sol";

// @title BDOGITO Voting Contract
// @notice This contract allows community voting on which companies should join the BDOGITO ecosystem.
contract BDOGITOVoting is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a company
    struct Company {
        string name; // Name of the company
        uint256 voteCount; // Number of votes received
        bool exists; // Check if the company exists
    }

    // Mapping to store companies by their ID
    mapping(uint256 => Company) public companies;
    // Counter to track the number of companies
    Counters.Counter private companyIdCounter;

    // Mapping to track if an address has voted
    mapping(address => bool) public hasVoted;

    // Event emitted when a new company is added
    event CompanyAdded(uint256 indexed companyId, string name);
    // Event emitted when a vote is cast
    event VoteCast(uint256 indexed companyId, address indexed voter);

    // @notice Add a new company to the voting list
    // @param _name The name of the company to be added
    function addCompany(string memory _name) external onlyOwner {
        require(bytes(_name).length > 0, "Company name cannot be empty");

        // Increment the company ID counter
        uint256 newCompanyId = companyIdCounter.current();
        companyIdCounter.increment();

        // Create a new company and store it
        companies[newCompanyId] = Company({
            name: _name,
            voteCount: 0,
            exists: true
        });

        emit CompanyAdded(newCompanyId, _name);
    }

    // @notice Cast a vote for a company
    // @param _companyId The ID of the company to vote for
    function vote(uint256 _companyId) external {
        require(!hasVoted[msg.sender], "You have already voted");
        require(companies[_companyId].exists, "Company does not exist");

        // Record the vote
        companies[_companyId].voteCount += 1;
        hasVoted[msg.sender] = true;

        emit VoteCast(_companyId, msg.sender);
    }

    // @notice Get the details of a company
    // @param _companyId The ID of the company
    // @return name The name of the company
    // @return voteCount The number of votes received by the company
    function getCompany(uint256 _companyId) external view returns (string memory name, uint256 voteCount) {
        require(companies[_companyId].exists, "Company does not exist");
        Company memory company = companies[_companyId];
        return (company.name, company.voteCount);
    }

    // @notice Reset the voting status for all addresses (only owner)
    function resetVoting() external onlyOwner {
        for (uint256 i = 0; i < companyIdCounter.current(); i++) {
            if (companies[i].exists) {
                companies[i].voteCount = 0; // Reset vote count
            }
        }
        // Reset hasVoted mapping
        for (uint256 i = 0; i < companyIdCounter.current(); i++) {
            hasVoted[msg.sender] = false; // Reset voting status for all addresses
        }
    }
}
```
