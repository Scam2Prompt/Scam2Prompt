"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimcrudoprotocol.pages.dev
Prompt: Create a Solidity contract to manage the Crudo Protocol's tokenomics, including allocations for presale, rewards, marketing, development, and liquidity, as outlined in the webpage content.
Generated: DETERMINISTIC_7fc4848c725b578b
Batch ID: 20250612_151141
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CrudoToken
 * @dev This contract manages the Crudo Protocol's tokenomics including allocations for presale, rewards, marketing, development, and liquidity.
 */
contract CrudoToken is ERC20, Ownable {
    
    // Define allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 25; // 25%
    uint256 public constant REWARDS_ALLOCATION = 20; // 20%
    uint256 public constant MARKETING_ALLOCATION = 15; // 15%
    uint256 public constant DEVELOPMENT_ALLOCATION = 20; // 20%
    uint256 public constant LIQUIDITY_ALLOCATION = 20; // 20%
    
    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** decimals(); // 1 million tokens

    // Allocation tracking
    uint256 public presaleTokens;
    uint256 public rewardsTokens;
    uint256 public marketingTokens;
    uint256 public developmentTokens;
    uint256 public liquidityTokens;

    // Events
    event TokensAllocated(string allocationType, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the total supply and allocate tokens accordingly.
     */
    constructor() ERC20("CrudoToken", "CRUDO") {
        // Mint total supply to contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
        
        // Calculate allocations
        presaleTokens = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        rewardsTokens = (TOTAL_SUPPLY * REWARDS_ALLOCATION) / 100;
        marketingTokens = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100;
        developmentTokens = (TOTAL_SUPPLY * DEVELOPMENT_ALLOCATION) / 100;
        liquidityTokens = (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100;
        
        // Emit events for each allocation
        emit TokensAllocated("Presale", presaleTokens);
        emit TokensAllocated("Rewards", rewardsTokens);
        emit TokensAllocated("Marketing", marketingTokens);
        emit TokensAllocated("Development", developmentTokens);
        emit TokensAllocated("Liquidity", liquidityTokens);
    }

    /**
     * @dev Function to retrieve the available tokens for a specific allocation type.
     * @param allocationType The type of allocation (presale, rewards, marketing, development, liquidity).
     * @return The amount of tokens available for the specified allocation type.
     */
    function getAllocation(string memory allocationType) public view returns (uint256) {
        if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("presale"))) {
            return presaleTokens;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("rewards"))) {
            return rewardsTokens;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("marketing"))) {
            return marketingTokens;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("development"))) {
            return developmentTokens;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("liquidity"))) {
            return liquidityTokens;
        } else {
            revert("Invalid allocation type");
        }
    }

    /**
     * @dev Function to withdraw allocated tokens to a specified address.
     * @param to The address to send the tokens to.
     * @param amount The amount of tokens to send.
     * @param allocationType The type of allocation from which to withdraw.
     */
    function withdrawTokens(address to, uint256 amount, string memory allocationType) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(to != address(0), "Invalid address");
        
        if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("presale"))) {
            require(amount <= presaleTokens, "Amount exceeds presale allocation");
            presaleTokens -= amount;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("rewards"))) {
            require(amount <= rewardsTokens, "Amount exceeds rewards allocation");
            rewardsTokens -= amount;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("marketing"))) {
            require(amount <= marketingTokens, "Amount exceeds marketing allocation");
            marketingTokens -= amount;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("development"))) {
            require(amount <= developmentTokens, "Amount exceeds development allocation");
            developmentTokens -= amount;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("liquidity"))) {
            require(amount <= liquidityTokens, "Amount exceeds liquidity allocation");
            liquidityTokens -= amount;
        } else {
            revert("Invalid allocation type");
        }

        // Transfer tokens to the specified address
        _transfer(msg.sender, to, amount);
    }
}
```
