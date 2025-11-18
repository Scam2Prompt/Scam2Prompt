"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pmkoookmpp.pages.dev
Prompt: Write a Solidity contract for the DOGEM tokenomics allocation, ensuring proper distribution of tokens across airdrop, liquidity pool, exchange listings, team, referral pool, and stake pool as specified.
Generated: DETERMINISTIC_30cb42453f6d9f7c
Batch ID: 20250612_151038
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

// Importing OpenZeppelin's ERC20 contract for standard implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DogemTokenomics is ERC20, Ownable {
    // Constants for token allocation percentages
    uint256 public constant AIRDROP_ALLOCATION = 1000000 ether; // Airdrop allocation
    uint256 public constant LIQUIDITY_POOL_ALLOCATION = 2000000 ether; // Liquidity Pool allocation
    uint256 public constant EXCHANGE_LISTINGS_ALLOCATION = 1500000 ether; // Exchange Listings allocation
    uint256 public constant TEAM_ALLOCATION = 500000 ether; // Team allocation
    uint256 public constant REFERRAL_POOL_ALLOCATION = 750000 ether; // Referral Pool allocation
    uint256 public constant STAKE_POOL_ALLOCATION = 1000000 ether; // Stake Pool allocation
    
    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = AIRDROP_ALLOCATION + LIQUIDITY_POOL_ALLOCATION + 
                                          EXCHANGE_LISTINGS_ALLOCATION + TEAM_ALLOCATION + 
                                          REFERRAL_POOL_ALLOCATION + STAKE_POOL_ALLOCATION;

    // Events for tracking allocations
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Mapping to track allocated addresses
    mapping(address => uint256) public allocations;

    // Constructor to mint tokens to the contract owner
    constructor() ERC20("DogemToken", "DOGEM") {
        // Mint total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Function to distribute tokens to a specific allocation category
    function distributeTokens(address _to, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(_to != address(0), "Invalid address");
        require(balanceOf(msg.sender) >= _amount, "Insufficient balance");

        // Transfer tokens from the owner to the recipient
        _transfer(msg.sender, _to, _amount);
        
        // Track the allocation
        allocations[_to] += _amount;

        emit TokensDistributed(_to, _amount);
    }

    // Function to retrieve the total supply of the token
    function totalSupply() public view override returns (uint256) {
        return TOTAL_SUPPLY;
    }

    // Function to retrieve the allocation for a specific address
    function getAllocation(address _address) external view returns (uint256) {
        return allocations[_address];
    }

    // Function to withdraw tokens from the contract (in case of emergency)
    function withdrawTokens(address _to, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(balanceOf(address(this)) >= _amount, "Insufficient contract balance");

        // Transfer tokens to the specified address
        _transfer(address(this), _to, _amount);
    }
}
```
