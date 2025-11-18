"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimflockerztoken.pages.dev
Prompt: Develop a Solidity contract that allocates $FLOCK tokens according to the tokenomics described (e.g., 20% for early birds, 25% for staking, 25% for the DAO vault).
Generated: DETERMINISTIC_c93e6b17dc492246
Batch ID: 20250612_154010
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
 * @title FLOCKToken
 * @dev ERC20 token with specific allocation for early birds, staking, and DAO vault
 */
contract FLOCKToken is ERC20, Ownable {
    // Constants for allocation percentages
    uint256 public constant EARLY_BIRD_ALLOCATION = 20;
    uint256 public constant STAKING_ALLOCATION = 25;
    uint256 public constant DAO_VAULT_ALLOCATION = 25;
    uint256 public constant TOTAL_ALLOCATION = EARLY_BIRD_ALLOCATION + STAKING_ALLOCATION + DAO_VAULT_ALLOCATION;

    // Total supply of the token (in wei)
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10**18; // 1 million tokens

    // Address for early birds allocation
    address public earlyBirdsAddress;
    // Address for staking allocation
    address public stakingAddress;
    // Address for DAO vault
    address public daoVaultAddress;

    // Struct to track whether allocations have been made
    struct AllocationStatus {
        bool earlyBirdsAllocated;
        bool stakingAllocated;
        bool daoVaultAllocated;
    }

    // Track allocation statuses
    AllocationStatus public allocationStatus;

    // Events for tracking allocation activities
    event AllocatedToEarlyBirds(address indexed to, uint256 amount);
    event AllocatedToStaking(address indexed to, uint256 amount);
    event AllocatedToDAOVault(address indexed to, uint256 amount);

    /**
     * @dev Constructor that initializes the token and sets allocation addresses
     * @param _earlyBirdsAddress Address to receive early birds allocation
     * @param _stakingAddress Address to receive staking allocation
     * @param _daoVaultAddress Address to receive DAO vault allocation
     */
    constructor(address _earlyBirdsAddress, address _stakingAddress, address _daoVaultAddress) 
        ERC20("FLOCK", "FLOCK") 
    {
        // Set allocation addresses
        earlyBirdsAddress = _earlyBirdsAddress;
        stakingAddress = _stakingAddress;
        daoVaultAddress = _daoVaultAddress;

        // Mint total supply to the contract deployer initially
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Allocates tokens according to the defined tokenomics.
     * Can only be called once by the contract owner.
     */
    function allocateTokens() external onlyOwner {
        require(!allocationStatus.earlyBirdsAllocated, "Tokens already allocated.");
        
        // Calculate allocations
        uint256 earlyBirdsAmount = TOTAL_SUPPLY * EARLY_BIRD_ALLOCATION / 100;
        uint256 stakingAmount = TOTAL_SUPPLY * STAKING_ALLOCATION / 100;
        uint256 daoVaultAmount = TOTAL_SUPPLY * DAO_VAULT_ALLOCATION / 100;

        // Transfer allocated tokens to respective addresses
        _transfer(msg.sender, earlyBirdsAddress, earlyBirdsAmount);
        _transfer(msg.sender, stakingAddress, stakingAmount);
        _transfer(msg.sender, daoVaultAddress, daoVaultAmount);

        // Update allocation statuses
        allocationStatus.earlyBirdsAllocated = true;
        allocationStatus.stakingAllocated = true;
        allocationStatus.daoVaultAllocated = true;

        // Emit events for tracking
        emit AllocatedToEarlyBirds(earlyBirdsAddress, earlyBirdsAmount);
        emit AllocatedToStaking(stakingAddress, stakingAmount);
        emit AllocatedToDAOVault(daoVaultAddress, daoVaultAmount);
    }

    /**
     * @dev Function to withdraw any tokens mistakenly sent to this contract.
     * @param tokenAddress The address of the token to withdraw
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw native tokens.");
        ERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
