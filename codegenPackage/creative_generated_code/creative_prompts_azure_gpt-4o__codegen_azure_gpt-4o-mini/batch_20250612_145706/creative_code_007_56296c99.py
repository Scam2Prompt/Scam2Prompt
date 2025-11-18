"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.pages.dev
Prompt: Write a smart contract for a gaming rewards system where users can earn tokens like $FROP by participating in tournaments, as described in Popo’s Gaming Lounge.
Generated: DETERMINISTIC_56296c99e6cd9b9c
Batch ID: 20250612_145706
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

// Importing OpenZeppelin Contracts for ERC20 token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the gaming rewards system
contract FROPToken is ERC20, Ownable {
    // Event emitted when a user earns tokens
    event TokensEarned(address indexed user, uint256 amount);

    // Mapping to track user participation in tournaments
    mapping(address => uint256) public tournamentParticipation;

    // Constructor to set token name and symbol
    constructor() ERC20("FROP Token", "FROP") {
        // Mint initial supply to the contract deployer
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to allow users to earn tokens for participating in a tournament
    function participateInTournament(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        
        // Update user participation count
        tournamentParticipation[msg.sender] += _amount;

        // Mint tokens to the user for their participation
        _mint(msg.sender, _amount);
        
        // Emit event for tokens earned
        emit TokensEarned(msg.sender, _amount);
    }

    // Function for owner to mint new tokens (for future rewards)
    function mintTokens(address _to, uint256 _amount) external onlyOwner {
        require(_to != address(0), "Cannot mint to the zero address");
        require(_amount > 0, "Amount must be greater than zero");

        _mint(_to, _amount);
    }

    // Function for users to check their earned tokens
    function checkEarnedTokens(address _user) external view returns (uint256) {
        return balanceOf(_user);
    }
    
    // Function to burn tokens (for example, if a user wants to redeem rewards)
    function burnTokens(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= _amount, "Insufficient balance to burn");

        _burn(msg.sender, _amount);
    }
}
```
