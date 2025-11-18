"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimplena.vercel.app
Prompt: Generate a smart contract that manages token distribution for the $PLENA Quest participants, ensuring compliance with campaign rules.
Generated: DETERMINISTIC_145b8160536bee1d
Batch ID: 20250612_153225
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

// Importing OpenZeppelin's ERC20 implementation for token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for managing $PLENA token distribution for Quest participants
contract PlenaQuestTokenDistribution is ERC20, Ownable {
    // Mapping to track the tokens distributed to each participant
    mapping(address => uint256) private _distributions;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed participant, uint256 amount);

    // Maximum tokens that can be distributed
    uint256 public constant MAX_TOKENS = 1000000 * 10 ** decimals();

    // Total tokens distributed
    uint256 private _totalDistributed;

    // Constructor to set the token details and initial supply
    constructor() ERC20("PLENA", "$PLENA") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, MAX_TOKENS);
    }

    // Function to distribute tokens to participants
    // Only callable by the contract owner
    function distributeTokens(address participant, uint256 amount) external onlyOwner {
        require(participant != address(0), "Cannot distribute tokens to the zero address");
        require(amount > 0, "Distribution amount must be greater than zero");
        require(_totalDistributed + amount <= MAX_TOKENS, "Exceeds maximum token distribution limit");

        // Update distributions
        _distributions[participant] += amount;
        _totalDistributed += amount;

        // Transfer tokens to the participant
        _transfer(msg.sender, participant, amount);

        // Emit the event for tracking purposes
        emit TokensDistributed(participant, amount);
    }

    // Function to check the distribution of tokens to a specific participant
    function getDistribution(address participant) external view returns (uint256) {
        return _distributions[participant];
    }

    // Function to check the total distributed tokens
    function totalDistributed() external view returns (uint256) {
        return _totalDistributed;
    }

    // Function to withdraw leftover tokens (if any) from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient contract balance");
        _transfer(address(this), msg.sender, amount);
    }
}
```
