"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.pages.dev
Prompt: Write a Solidity function to manage liquidity allocation for CEX and DEX listings, ensuring 10% of the total token supply is reserved as per $FROP tokenomics.
Generated: DETERMINISTIC_70dd0deb113553d7
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title LiquidityManager
 * @dev This contract manages the allocation of liquidity for CEX and DEX listings,
 * ensuring that 10% of the total token supply is reserved as per $FROP tokenomics.
 */
contract LiquidityManager {
    address public owner; // Address of the contract owner
    uint256 public totalTokenSupply; // Total supply of the tokens
    uint256 public reservedLiquidity; // Amount reserved for liquidity (10% of total supply)
    uint256 public allocatedToCEX; // Amount allocated for CEX listings
    uint256 public allocatedToDEX; // Amount allocated for DEX listings

    event LiquidityAllocated(
        string allocationType,
        uint256 amount,
        uint256 timestamp
    );
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor sets the total token supply and calculates reserved liquidity.
     * @param _totalTokenSupply Total supply of the tokens.
     */
    constructor(uint256 _totalTokenSupply) {
        require(_totalTokenSupply > 0, "Total token supply must be greater than zero");
        owner = msg.sender;
        totalTokenSupply = _totalTokenSupply;
        reservedLiquidity = (totalTokenSupply * 10) / 100; // Calculate 10% of total supply
    }

    /**
     * @dev Function to allocate liquidity to CEX.
     * @param amount Amount of tokens to allocate to CEX.
     */
    function allocateToCEX(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(
            allocatedToCEX + allocatedToDEX + amount <= reservedLiquidity,
            "Allocation exceeds reserved liquidity"
        );

        allocatedToCEX += amount;
        emit LiquidityAllocated("CEX", amount, block.timestamp);
    }

    /**
     * @dev Function to allocate liquidity to DEX.
     * @param amount Amount of tokens to allocate to DEX.
     */
    function allocateToDEX(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(
            allocatedToCEX + allocatedToDEX + amount <= reservedLiquidity,
            "Allocation exceeds reserved liquidity"
        );

        allocatedToDEX += amount;
        emit LiquidityAllocated("DEX", amount, block.timestamp);
    }

    /**
     * @dev Function to update the total token supply (onlyOwner).
     * This recalculates the reserved liquidity (10% of the new total supply).
     * @param _newTotalTokenSupply The new total token supply.
     */
    function updateTotalTokenSupply(uint256 _newTotalTokenSupply) external onlyOwner {
        require(_newTotalTokenSupply > 0, "Total token supply must be greater than zero");
        totalTokenSupply = _newTotalTokenSupply;
        reservedLiquidity = (totalTokenSupply * 10) / 100; // Recalculate reserved liquidity
    }

    /**
     * @dev Transfer ownership of the contract to a new address.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Ether transfers not supported");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Ether transfers not supported");
    }
}
```
