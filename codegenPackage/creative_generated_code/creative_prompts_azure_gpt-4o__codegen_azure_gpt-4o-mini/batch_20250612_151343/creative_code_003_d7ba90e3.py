"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockdag-8bz.pages.dev
Prompt: Create a smart contract for BDAG tokenomics based on the presale allocation percentages provided in the website's tokenomics section.
Generated: DETERMINISTIC_d7ba90e3df7087b7
Batch ID: 20250612_151343
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

// Importing OpenZeppelin's SafeMath library for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BDAGToken
 * @dev ERC20 Token with specific tokenomics for presale allocation
 */
contract BDAGToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Presale allocation percentages (in basis points)
    uint256 public constant TEAM_ALLOCATION = 1500; // 15%
    uint256 public constant ADVISORS_ALLOCATION = 1000; // 10%
    uint256 public constant PARTNERSHIP_ALLOCATION = 1000; // 10%
    uint256 public constant LIQUIDITY_ALLOCATION = 2000; // 20%
    uint256 public constant COMMUNITY_ALLOCATION = 1500; // 15%
    uint256 public constant RESERVE_ALLOCATION = 2500; // 25%
    
    // Total Token Supply
    uint256 public constant TOTAL_SUPPLY = 1000000 * 10 ** decimals(); // 1,000,000 tokens

    // Mappings to keep track of allocations
    mapping(address => uint256) public allocations;
    
    // Events
    event TokensAllocated(address indexed recipient, uint256 amount);

    constructor() ERC20("BDAG Token", "BDAG") {
        // Mint total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
        
        // Allocate tokens based on the defined tokenomics
        allocateTokens();
    }

    /**
     * @dev Function to allocate tokens according to the presale distribution plan.
     * This function is called only once during the contract deployment.
     */
    function allocateTokens() private onlyOwner {
        // Example addresses for allocations (replace with actual addresses)
        address teamAddress = 0x1234567890123456789012345678901234567890;
        address advisorsAddress = 0x1234567890123456789012345678901234567891;
        address partnershipAddress = 0x1234567890123456789012345678901234567892;
        address liquidityAddress = 0x1234567890123456789012345678901234567893;
        address communityAddress = 0x1234567890123456789012345678901234567894;
        address reserveAddress = 0x1234567890123456789012345678901234567895;

        // Allocating tokens to respective addresses
        allocations[teamAddress] = TOTAL_SUPPLY.mul(TEAM_ALLOCATION).div(10000);
        allocations[advisorsAddress] = TOTAL_SUPPLY.mul(ADVISORS_ALLOCATION).div(10000);
        allocations[partnershipAddress] = TOTAL_SUPPLY.mul(PARTNERSHIP_ALLOCATION).div(10000);
        allocations[liquidityAddress] = TOTAL_SUPPLY.mul(LIQUIDITY_ALLOCATION).div(10000);
        allocations[communityAddress] = TOTAL_SUPPLY.mul(COMMUNITY_ALLOCATION).div(10000);
        allocations[reserveAddress] = TOTAL_SUPPLY.mul(RESERVE_ALLOCATION).div(10000);

        // Emit events for each allocation
        emit TokensAllocated(teamAddress, allocations[teamAddress]);
        emit TokensAllocated(advisorsAddress, allocations[advisorsAddress]);
        emit TokensAllocated(partnershipAddress, allocations[partnershipAddress]);
        emit TokensAllocated(liquidityAddress, allocations[liquidityAddress]);
        emit TokensAllocated(communityAddress, allocations[communityAddress]);
        emit TokensAllocated(reserveAddress, allocations[reserveAddress]);
    }

    /**
     * @dev Function to allow the owner to withdraw any accidentally sent tokens.
     * This is a safety measure in case tokens are sent to the contract mistakenly.
     * @param tokenAddress The address of the ERC20 token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        token.transfer(owner(), amount);
    }
}
```
