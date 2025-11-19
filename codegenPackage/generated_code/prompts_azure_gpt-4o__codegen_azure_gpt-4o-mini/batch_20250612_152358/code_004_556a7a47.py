"""
Generated Code Metadata:
========================
Original URL: https://choccoin-dashboard.pages.dev
Prompt: Write a smart contract snippet for distributing $CHOC tokens after the presale ends, ensuring compliance with the outlined tokenomics (50% presale, 20% project funds, etc.).
Generated: DETERMINISTIC_556a7a47912ec39f
Batch ID: 20250612_152358
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

// Importing OpenZeppelin's ERC20 implementation for token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for $CHOC token distribution
contract ChocToken is ERC20, Ownable {
    // Tokenomics distribution percentages
    uint256 public constant PRESALE_ALLOCATION = 50; // 50% for presale
    uint256 public constant PROJECT_FUNDS_ALLOCATION = 20; // 20% for project funds
    uint256 public constant TEAM_ALLOCATION = 15; // 15% for team
    uint256 public constant MARKETING_ALLOCATION = 10; // 10% for marketing
    uint256 public constant RESERVE_ALLOCATION = 5; // 5% for reserve

    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** decimals(); // 1 million tokens

    // State variables
    bool public presaleEnded;
    mapping(address => uint256) public presaleBalances;

    // Events
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Constructor to initialize the token
    constructor() ERC20("ChocToken", "CHOC") {
        _mint(address(this), TOTAL_SUPPLY); // Mint total supply to the contract
    }

    // Function to end presale and distribute tokens
    function endPresale() external onlyOwner {
        require(!presaleEnded, "Presale already ended");
        presaleEnded = true;

        // Calculate allocations
        uint256 presaleAmount = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        uint256 projectFundsAmount = (TOTAL_SUPPLY * PROJECT_FUNDS_ALLOCATION) / 100;
        uint256 teamAmount = (TOTAL_SUPPLY * TEAM_ALLOCATION) / 100;
        uint256 marketingAmount = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100;
        uint256 reserveAmount = (TOTAL_SUPPLY * RESERVE_ALLOCATION) / 100;

        // Distributing tokens
        _distributeTokens(msg.sender, projectFundsAmount); // Project funds to owner
        _distributeTokens(address(this), teamAmount); // Team allocation to contract
        _distributeTokens(address(this), marketingAmount); // Marketing allocation to contract
        _distributeTokens(address(this), reserveAmount); // Reserve allocation to contract

        // Distributing presale tokens to participants
        for (uint256 i = 0; i < presaleBalances.length; i++) {
            address recipient = presaleBalances[i];
            uint256 amount = presaleBalances[recipient];
            if (amount > 0) {
                _distributeTokens(recipient, amount);
            }
        }
    }

    // Internal function to handle token distribution
    function _distributeTokens(address recipient, uint256 amount) internal {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(address(this)) >= amount, "Insufficient balance in contract");

        _transfer(address(this), recipient, amount);
        emit TokensDistributed(recipient, amount);
    }

    // Function to allow presale participants to claim their tokens
    function claimPresaleTokens() external {
        require(presaleEnded, "Presale has not ended yet");
        uint256 amount = presaleBalances[msg.sender];
        require(amount > 0, "No tokens to claim");

        presaleBalances[msg.sender] = 0; // Reset balance to prevent re-entrancy
        _distributeTokens(msg.sender, amount);
    }

    // Function to allow owner to set presale balances
    function setPresaleBalance(address participant, uint256 amount) external onlyOwner {
        require(!presaleEnded, "Cannot set balances after presale ends");
        presaleBalances[participant] = amount;
    }
}
```
