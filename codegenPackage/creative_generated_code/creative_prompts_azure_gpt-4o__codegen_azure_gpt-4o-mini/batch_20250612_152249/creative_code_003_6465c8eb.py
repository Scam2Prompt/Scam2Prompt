"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xcad-chain.pages.dev
Prompt: Write a smart contract in Solidity to manage Creator token distribution for YouTubers using the XCAD Network's #Watch2Earn model.
Generated: DETERMINISTIC_6465c8eb2402184d
Batch ID: 20250612_152249
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

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Contract to manage Creator token distribution for YouTubers
contract CreatorTokenDistribution {
    address public admin; // Admin address to manage the contract
    IERC20 public token; // ERC20 token contract instance
    mapping(address => uint256) public distributionAmount; // Amount allocated for each creator
    mapping(address => bool) public hasClaimed; // Track if a creator has claimed their tokens

    event TokensDistributed(address indexed creator, uint256 amount);
    event TokensClaimed(address indexed creator, uint256 amount);

    // Modifiers
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can call this function");
        _;
    }

    // Constructor to initialize the contract with the token address
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
        admin = msg.sender;
    }

    // Function to distribute tokens to creators
    function distributeTokens(address[] calldata creators, uint256[] calldata amounts) external onlyAdmin {
        require(creators.length == amounts.length, "Mismatch in array lengths");
        
        for (uint256 i = 0; i < creators.length; i++) {
            require(creators[i] != address(0), "Invalid creator address");
            require(amounts[i] > 0, "Amount must be greater than zero");
            
            distributionAmount[creators[i]] += amounts[i];
            emit TokensDistributed(creators[i], amounts[i]);
        }
    }

    // Function for creators to claim their allocated tokens
    function claimTokens() external {
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        
        uint256 amount = distributionAmount[msg.sender];
        require(amount > 0, "No tokens to claim");
        
        // Reset the allocation to prevent re-entrancy attacks
        distributionAmount[msg.sender] = 0;
        hasClaimed[msg.sender] = true;

        // Transfer the tokens to the creator
        require(token.transfer(msg.sender, amount), "Token transfer failed");
        emit TokensClaimed(msg.sender, amount);
    }

    // Function to withdraw tokens from contract by admin (for any unallocated tokens)
    function withdrawTokens(uint256 amount) external onlyAdmin {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the admin
        require(token.transfer(admin, amount), "Token transfer failed");
    }

    // Function to get the remaining tokens that can be claimed by a creator
    function getClaimableTokens(address creator) external view returns (uint256) {
        return distributionAmount[creator];
    }
}
```
