"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockbanki.pages.dev
Prompt: Write a Solidity contract to manage the allocation of $PEPU tokens based on the tokenomics breakdown (e.g., presale, staking, marketing, liquidity).
Generated: DETERMINISTIC_9dd29d23842e43d7
Batch ID: 20250612_151246
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
 * @title PEPU Token Allocation Contract
 * @dev This contract manages the allocation of $PEPU tokens based on tokenomics breakdown.
 */
contract PEPUTokenAllocation {
    // Define the owner of the contract
    address public owner;

    // Tokenomics allocations
    uint256 public presaleAllocation;
    uint256 public stakingAllocation;
    uint256 public marketingAllocation;
    uint256 public liquidityAllocation;

    // Total allocated tokens
    uint256 public totalAllocatedTokens;

    // Events
    event AllocationUpdated(string allocationType, uint256 oldValue, uint256 newValue);
    event TokensDistributed(string allocationType, address recipient, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to initialize the contract owner and tokenomics allocations
    constructor(
        uint256 _presaleAllocation,
        uint256 _stakingAllocation,
        uint256 _marketingAllocation,
        uint256 _liquidityAllocation
    ) {
        owner = msg.sender;

        // Initialize allocations
        presaleAllocation = _presaleAllocation;
        stakingAllocation = _stakingAllocation;
        marketingAllocation = _marketingAllocation;
        liquidityAllocation = _liquidityAllocation;

        // Update total allocated tokens
        totalAllocatedTokens =
            _presaleAllocation +
            _stakingAllocation +
            _marketingAllocation +
            _liquidityAllocation;
    }

    /**
     * @dev Update token allocation for a specific category (only owner).
     * @param allocationType The type of allocation (e.g., "presale", "staking", "marketing", "liquidity").
     * @param newAmount The new allocation amount.
     */
    function updateAllocation(string memory allocationType, uint256 newAmount)
        public
        onlyOwner
    {
        uint256 oldAmount;
        if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("presale"))) {
            oldAmount = presaleAllocation;
            presaleAllocation = newAmount;
        } else if (
            keccak256(abi.encodePacked(allocationType)) ==
            keccak256(abi.encodePacked("staking"))
        ) {
            oldAmount = stakingAllocation;
            stakingAllocation = newAmount;
        } else if (
            keccak256(abi.encodePacked(allocationType)) ==
            keccak256(abi.encodePacked("marketing"))
        ) {
            oldAmount = marketingAllocation;
            marketingAllocation = newAmount;
        } else if (
            keccak256(abi.encodePacked(allocationType)) ==
            keccak256(abi.encodePacked("liquidity"))
        ) {
            oldAmount = liquidityAllocation;
            liquidityAllocation = newAmount;
        } else {
            revert("Invalid allocation type");
        }

        // Update total allocated tokens
        totalAllocatedTokens =
            presaleAllocation +
            stakingAllocation +
            marketingAllocation +
            liquidityAllocation;

        emit AllocationUpdated(allocationType, oldAmount, newAmount);
    }

    /**
     * @dev Distribute tokens to a specific recipient from a specific allocation category.
     * @param allocationType The type of allocation (e.g., "presale", "staking", "marketing", "liquidity").
     * @param recipient The recipient address.
     * @param amount The amount of tokens to distribute.
     */
    function distributeTokens(
        string memory allocationType,
        address recipient,
        uint256 amount
    ) public onlyOwner {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");

        if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("presale"))) {
            require(amount <= presaleAllocation, "Insufficient presale allocation");
            presaleAllocation -= amount;
        } else if (
            keccak256(abi.encodePacked(allocationType)) ==
            keccak256(abi.encodePacked("staking"))
        ) {
            require(amount <= stakingAllocation, "Insufficient staking allocation");
            stakingAllocation -= amount;
        } else if (
            keccak256(abi.encodePacked(allocationType)) ==
            keccak256(abi.encodePacked("marketing"))
        ) {
            require(amount <= marketingAllocation, "Insufficient marketing allocation");
            marketingAllocation -= amount;
        } else if (
            keccak256(abi.encodePacked(allocationType)) ==
            keccak256(abi.encodePacked("liquidity"))
        ) {
            require(amount <= liquidityAllocation, "Insufficient liquidity allocation");
            liquidityAllocation -= amount;
        } else {
            revert("Invalid allocation type");
        }

        emit TokensDistributed(allocationType, recipient, amount);
    }

    /**
     * @dev Transfer ownership of the contract to a new owner.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        owner = newOwner;
    }
}
```
