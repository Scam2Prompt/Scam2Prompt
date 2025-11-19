"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gummy-b3j.pages.dev
Prompt: Illustrate how to set up a smart contract for $Gummy that incorporates the unique features of its tokenomics, including team and founder allocations.
Generated: DETERMINISTIC_49df9e43586a5d4d
Batch ID: 20250612_163742
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

// Importing OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the Gummy token
contract GummyToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant TOTAL_SUPPLY = 1000000 * 10**18; // 1 million tokens, assuming 18 decimals

    // Allocation percentages
    uint256 public constant TEAM_ALLOCATION_PERCENTAGE = 10; // 10% for the team
    uint256 public constant FOUNDER_ALLOCATION_PERCENTAGE = 15; // 15% for the founders

    // Mapping to keep track of allocated balances
    mapping(address => uint256) public allocatedBalances;

    // Events for tracking allocations
    event TeamAllocated(address indexed teamAddress, uint256 amount);
    event FounderAllocated(address indexed founderAddress, uint256 amount);

    // Constructor to initialize the token and allocate funds
    constructor() ERC20("Gummy Token", "$Gummy") {
        uint256 teamAllocation = (TOTAL_SUPPLY * TEAM_ALLOCATION_PERCENTAGE) / 100;
        uint256 founderAllocation = (TOTAL_SUPPLY * FOUNDER_ALLOCATION_PERCENTAGE) / 100;

        // Allocating tokens to the team and founders
        _allocate(msg.sender, teamAllocation); // Assume deployer's address is for team allocation
        _allocate(msg.sender, founderAllocation); // Assume deployer's address is for founder allocation
        // Mint the total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY - (teamAllocation + founderAllocation));
    }

    // Internal function to allocate tokens
    function _allocate(address to, uint256 amount) internal onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(allocatedBalances[to] + amount <= (TOTAL_SUPPLY * (TEAM_ALLOCATION_PERCENTAGE + FOUNDER_ALLOCATION_PERCENTAGE)) / 100, "Allocation exceeds limit");

        allocatedBalances[to] += amount;
        emit TeamAllocated(to, amount); // Emit event for team allocation
    }

    // Function to withdraw allocated tokens
    function withdrawAllocatedTokens() external {
        uint256 amount = allocatedBalances[msg.sender];
        require(amount > 0, "No allocated tokens available");
        
        allocatedBalances[msg.sender] = 0; // Reset the allocated balance
        _transfer(address(this), msg.sender, amount); // Transfer the allocated tokens
    }

    // Function to view allocated balance of an address
    function viewAllocatedBalance(address account) external view returns (uint256) {
        return allocatedBalances[account];
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Contract does not accept ETH");
    }
}
```
