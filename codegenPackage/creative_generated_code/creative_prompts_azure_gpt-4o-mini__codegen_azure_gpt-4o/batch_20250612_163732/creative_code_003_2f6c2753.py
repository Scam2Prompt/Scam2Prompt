"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kaicat-claims.pages.dev
Prompt: Develop a smart contract for an ERC20 token that mimics the tokenomics of $KAI, including liquidity, staking, and presale allocations.
Generated: DETERMINISTIC_2f6c2753b9d9662a
Batch ID: 20250612_163732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for an ERC20 token smart contract written in Solidity. It is clean, well-commented, and follows best practices. Note that due to complexity, advanced features like staking are only outlined; you would need to implement additional staking contracts for production use.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import the OpenZeppelin ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract KAIToken is ERC20, Ownable {
    // Token details
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public presaleAllocation = 300_000_000 * 10**18; // 30% for presale
    uint256 public liquidityAllocation = 500_000_000 * 10**18; // 50% for liquidity
    uint256 public stakingAllocation = 200_000_000 * 10**18; // 20% for staking

    // Track allocations
    uint256 public presaleDistributed;
    uint256 public liquidityDistributed;
    uint256 public stakingDistributed;

    // Events
    event TokensDistributed(address indexed to, uint256 amount, string allocationType);

    constructor() ERC20("KAI Token", "KAI") {
        // Mint total supply to the contract owner (typically the deployer)
        _mint(owner(), MAX_SUPPLY);
    }

    /**
     * @dev Distribute tokens for presale.
     * @param recipient Address to receive the presale tokens.
     * @param amount Amount of tokens to distribute.
     */
    function distributePresale(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(presaleDistributed + amount <= presaleAllocation, "Exceeds presale allocation");

        presaleDistributed += amount;
        _transfer(owner(), recipient, amount);

        emit TokensDistributed(recipient, amount, "Presale");
    }

    /**
     * @dev Distribute tokens for liquidity.
     * @param recipient Address to receive the liquidity tokens.
     * @param amount Amount of tokens to distribute.
     */
    function distributeLiquidity(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(liquidityDistributed + amount <= liquidityAllocation, "Exceeds liquidity allocation");

        liquidityDistributed += amount;
        _transfer(owner(), recipient, amount);

        emit TokensDistributed(recipient, amount, "Liquidity");
    }

    /**
     * @dev Allocate tokens for staking rewards (handled separately in a staking contract).
     * @param stakingContract Address of the staking contract.
     * @param amount Amount of tokens to allocate for staking rewards.
     */
    function allocateStaking(address stakingContract, uint256 amount) external onlyOwner {
        require(stakingContract != address(0), "Invalid staking contract address");
        require(stakingDistributed + amount <= stakingAllocation, "Exceeds staking allocation");

        stakingDistributed += amount;
        _transfer(owner(), stakingContract, amount);

        emit TokensDistributed(stakingContract, amount, "Staking");
    }

    /**
     * @dev Emergency function to reclaim any leftover tokens (only by the owner).
     */
    function reclaimTokens() external onlyOwner {
        uint256 reclaimableTokens = MAX_SUPPLY - (presaleDistributed + liquidityDistributed + stakingDistributed);
        require(reclaimableTokens > 0, "No tokens to reclaim");

        _transfer(owner(), owner(), reclaimableTokens);
    }
}
```

### Notes:
- This contract uses OpenZeppelin's `ERC20` and `Ownable` implementations for security and maintainability.
- Staking functionality is delegated to another contract, and the script only allocates staking tokens.
- Proper error handling is included with require statements.
- Events are emitted for transparency in token distribution.
