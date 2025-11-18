"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meties.pages.dev
Prompt: Provide an example of deploying a governance token on Metis that supports decentralized decision-making as outlined in the CEG framework.
Generated: DETERMINISTIC_512e3ba80f37b405
Batch ID: 20250612_151636
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for token functionality and ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// GovernanceToken contract that extends ERC20 and Ownable
contract GovernanceToken is ERC20, Ownable {
    
    // Mapping to track addresses that have delegated their votes
    mapping(address => address) private _delegates;
    
    // Events to emit when votes are delegated
    event DelegateChanged(address indexed delegator, address indexed fromDelegate, address indexed toDelegate);

    // Constructor to initialize the token with name and symbol
    constructor() ERC20("Governance Token", "GOV") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to delegate votes to another address
    function delegate(address to) external {
        address from = _delegates[msg.sender];
        _delegates[msg.sender] = to;

        emit DelegateChanged(msg.sender, from, to);
    }

    // Function to get the delegate of a given address
    function getDelegate(address delegator) external view returns (address) {
        return _delegates[delegator];
    }

    // Function to allow the owner to mint new tokens (for governance proposals)
    function mint(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "GovernanceToken: mint to the zero address");
        require(amount > 0, "GovernanceToken: amount must be greater than zero");
        
        _mint(account, amount);
    }

    // Function to allow the owner to burn tokens (for governance proposals)
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "GovernanceToken: amount must be greater than zero");
        
        _burn(msg.sender, amount);
    }
}
```
