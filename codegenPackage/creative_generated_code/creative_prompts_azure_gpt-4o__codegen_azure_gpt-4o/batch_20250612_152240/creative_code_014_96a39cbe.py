"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earthmeta-ai.pages.dev
Prompt: Write a Solidity smart contract for managing token allocation based on the structure outlined on the EarthMeta website, including presale, staking pools, and liquidity pools.
Generated: DETERMINISTIC_96a39cbe0af92b69
Batch ID: 20250612_152240
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

/**
 * @title TokenAllocation
 * @dev A smart contract for managing token allocation for presale, staking pools, and liquidity pools.
 */
contract TokenAllocation {
    // ERC20 token interface
    IERC20 public token;

    // Allocation structures
    struct Allocation {
        uint256 amount;
        bool allocated;
    }

    // Mapping for presale allocations (address => Allocation)
    mapping(address => Allocation) public presaleAllocations;

    // Staking pool allocation
    uint256 public stakingPoolAllocation;

    // Liquidity pool allocation
    uint256 public liquidityPoolAllocation;

    // Total allocated tokens
    uint256 public totalAllocated;

    // Maximum allocation cap
    uint256 public constant MAX_ALLOCATION = 1_000_000 * (10 ** 18); // Assuming 1M tokens with 18 decimals

    // Owner of the contract
    address public owner;

    // Events
    event PresaleAllocationSet(address indexed user, uint256 amount);
    event TokenWithdrawn(address indexed user, uint256 amount);
    event PoolAllocationSet(string poolType, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function.");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _token Address of the ERC20 token contract.
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero.");
        token = IERC20(_token);
        owner = msg.sender;
    }

    /**
     * @dev Set presale allocation for a user.
     * @param _user Address of the user.
     * @param _amount Allocation amount.
     */
    function setPresaleAllocation(address _user, uint256 _amount) external onlyOwner {
        require(_user != address(0), "User address cannot be zero.");
        require(_amount > 0, "Allocation amount must be greater than zero.");
        require(totalAllocated + _amount <= MAX_ALLOCATION, "Total allocation exceeds maximum cap.");

        presaleAllocations[_user] = Allocation(_amount, true);
        totalAllocated += _amount;

        emit PresaleAllocationSet(_user, _amount);
    }

    /**
     * @dev Set allocation for staking pool.
     * @param _amount Allocation amount.
     */
    function setStakingPoolAllocation(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Allocation amount must be greater than zero.");
        require(totalAllocated + _amount <= MAX_ALLOCATION, "Total allocation exceeds maximum cap.");

        stakingPoolAllocation = _amount;
        totalAllocated += _amount;

        emit PoolAllocationSet("Staking Pool", _amount);
    }

    /**
     * @dev Set allocation for liquidity pool.
     * @param _amount Allocation amount.
     */
    function setLiquidityPoolAllocation(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Allocation amount must be greater than zero.");
        require(totalAllocated + _amount <= MAX_ALLOCATION, "Total allocation exceeds maximum cap.");

        liquidityPoolAllocation = _amount;
        totalAllocated += _amount;

        emit PoolAllocationSet("Liquidity Pool", _amount);
    }

    /**
     * @dev Withdraw tokens for presale users.
     */
    function withdrawTokens() external {
        Allocation storage allocation = presaleAllocations[msg.sender];
        require(allocation.allocated, "No allocation found.");
        require(allocation.amount > 0, "Allocation amount must be greater than zero.");

        uint256 amount = allocation.amount;
        allocation.amount = 0; // Prevent re-entrancy
        allocation.allocated = false;

        bool success = token.transfer(msg.sender, amount);
        require(success, "Token transfer failed.");

        emit TokenWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Recover any ERC20 token sent to this contract by accident.
     * @param _token Address of the ERC20 token.
     * @param _amount Amount to recover.
     */
    function recoverTokens(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(0), "Token address cannot be zero.");
        require(_amount > 0, "Amount must be greater than zero.");

        bool success = IERC20(_token).transfer(owner, _amount);
        require(success, "Token recovery failed.");
    }
}

// Minimal ERC20 interface for token interactions
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
