"""
Generated Code Metadata:
========================
Original URL: https://d-510.pages.dev
Prompt: Create a smart contract in Solidity for a utility token like Lingo, ensuring it includes functionality for interacting with a Community DAO to select RWA investments.
Generated: DETERMINISTIC_29f0d314d29e4daa
Batch ID: 20250612_151003
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

// Importing OpenZeppelin's ERC20 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// CommunityDAO interface to interact with the DAO for investment proposals
interface ICommunityDAO {
    function proposeInvestment(string memory proposal) external;
    function voteOnProposal(uint256 proposalId, bool support) external;
    function getProposalStatus(uint256 proposalId) external view returns (bool);
}

// UtilityToken contract that extends ERC20 and Ownable
contract UtilityToken is ERC20, Ownable {
    // Address of the Community DAO contract
    ICommunityDAO public communityDAO;

    // Event emitted when a new investment proposal is made
    event InvestmentProposed(string proposal);
    
    // Event emitted when a vote is cast on a proposal
    event VoteCast(uint256 proposalId, bool support);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol, address daoAddress) 
        ERC20(name, symbol) 
    {
        // Set the Community DAO address
        communityDAO = ICommunityDAO(daoAddress);
    }

    // Function to propose an investment to the Community DAO
    function proposeInvestment(string memory proposal) external onlyOwner {
        communityDAO.proposeInvestment(proposal);
        emit InvestmentProposed(proposal);
    }

    // Function to vote on a proposal in the Community DAO
    function voteOnProposal(uint256 proposalId, bool support) external onlyOwner {
        communityDAO.voteOnProposal(proposalId, support);
        emit VoteCast(proposalId, support);
    }

    // Function to mint new tokens to a specified address
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        _mint(to, amount);
    }

    // Function to burn tokens from a specified address
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }

    // Function to set a new Community DAO address
    function setCommunityDAO(address daoAddress) external onlyOwner {
        require(daoAddress != address(0), "Invalid DAO address");
        communityDAO = ICommunityDAO(daoAddress);
    }

    // Function to retrieve the current Community DAO address
    function getCommunityDAO() external view returns (address) {
        return address(communityDAO);
    }
}
```
