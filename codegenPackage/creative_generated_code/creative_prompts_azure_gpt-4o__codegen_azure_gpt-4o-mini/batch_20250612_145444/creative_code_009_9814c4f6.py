"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flockerz-claim.web.app
Prompt: Create a Solidity contract that implements tokenomics similar to Flockerz, including allocations for presale, staking, DAO vault, exchanges, and marketing.
Generated: DETERMINISTIC_9814c4f6a68990a8
Batch ID: 20250612_145444
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

// Importing OpenZeppelin contracts for ERC20 standard implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FlockToken
 * @dev This contract implements a token with specific allocations for presale, staking, DAO vault, exchanges, and marketing.
 */
contract FlockToken is ERC20, Ownable {
    // Allocation percentages (in basis points, 10000 = 100%)
    uint256 public constant PRESALE_ALLOCATION = 2000; // 20%
    uint256 public constant STAKING_ALLOCATION = 3000; // 30%
    uint256 public constant DAO_VAULT_ALLOCATION = 2500; // 25%
    uint256 public constant EXCHANGE_ALLOCATION = 2000; // 20%
    uint256 public constant MARKETING_ALLOCATION = 1500; // 15%

    uint256 public constant TOTAL_ALLOCATION = 10000; // 100%

    // Variables to hold allocated tokens
    uint256 public presaleTokens;
    uint256 public stakingTokens;
    uint256 public daoVaultTokens;
    uint256 public exchangeTokens;
    uint256 public marketingTokens;

    // Event to log token allocations
    event TokensAllocated(uint256 presale, uint256 staking, uint256 daoVault, uint256 exchange, uint256 marketing);

    // Constructor to initialize token and allocate tokens
    constructor(uint256 totalSupply) ERC20("FlockToken", "FLOCK") {
        // Ensure total supply is greater than zero
        require(totalSupply > 0, "Total supply must be greater than zero");
        
        // Calculate token allocations based on total supply
        presaleTokens = (totalSupply * PRESALE_ALLOCATION) / TOTAL_ALLOCATION;
        stakingTokens = (totalSupply * STAKING_ALLOCATION) / TOTAL_ALLOCATION;
        daoVaultTokens = (totalSupply * DAO_VAULT_ALLOCATION) / TOTAL_ALLOCATION;
        exchangeTokens = (totalSupply * EXCHANGE_ALLOCATION) / TOTAL_ALLOCATION;
        marketingTokens = (totalSupply * MARKETING_ALLOCATION) / TOTAL_ALLOCATION;

        // Minting the total supply of tokens to the contract owner
        _mint(msg.sender, totalSupply);

        // Emitting the allocation event
        emit TokensAllocated(presaleTokens, stakingTokens, daoVaultTokens, exchangeTokens, marketingTokens);
    }

    /**
     * @dev Function to withdraw tokens for a specific purpose by the owner.
     * @param to The address to receive the tokens.
     * @param amount The amount of tokens to withdraw.
     * @param allocationType The type of allocation to withdraw from.
     */
    function withdrawTokens(address to, uint256 amount, string memory allocationType) external onlyOwner {
        require(to != address(0), "Can't send to the zero address");
        require(amount > 0, "Amount must be greater than zero");

        if (keccak256(abi.encodePacked(allocationType)) == keccak256("presale")) {
            require(presaleTokens >= amount, "Insufficient presale tokens");
            presaleTokens -= amount;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256("staking")) {
            require(stakingTokens >= amount, "Insufficient staking tokens");
            stakingTokens -= amount;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256("daoVault")) {
            require(daoVaultTokens >= amount, "Insufficient DAO vault tokens");
            daoVaultTokens -= amount;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256("exchange")) {
            require(exchangeTokens >= amount, "Insufficient exchange tokens");
            exchangeTokens -= amount;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256("marketing")) {
            require(marketingTokens >= amount, "Insufficient marketing tokens");
            marketingTokens -= amount;
        } else {
            revert("Invalid allocation type");
        }

        // Transfer the tokens to the specified address
        _transfer(msg.sender, to, amount);
    }

    /**
     * @dev Function to get the total allocated tokens for review.
     * @return totalAllocated Tokens allocated based on the allocations.
     */
    function getTotalAllocated() external view returns (uint256 totalAllocated) {
        totalAllocated = presaleTokens + stakingTokens + daoVaultTokens + exchangeTokens + marketingTokens;
    }
}
```
