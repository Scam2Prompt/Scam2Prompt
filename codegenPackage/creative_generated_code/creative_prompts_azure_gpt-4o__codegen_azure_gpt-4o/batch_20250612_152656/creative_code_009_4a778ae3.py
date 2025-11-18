"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scotty-theai-def.web.app
Prompt: Generate a Solidity contract for presale token distribution, ensuring compliance with Scotty AI's tokenomics structure (e.g., 30% public sale, 70% staking, dev, exchange, marketing).
Generated: DETERMINISTIC_4a778ae3f552826e
Batch ID: 20250612_152656
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
 * @title PresaleTokenDistribution
 * @dev This contract is designed for Scotty AI's tokenomics structure, ensuring compliance with allocations:
 *      - 30% for public sale
 *      - 70% for staking, dev, exchange, and marketing
 */
contract PresaleTokenDistribution {
    // Tokenomics percentages
    uint256 public constant PUBLIC_SALE_PERCENTAGE = 30;
    uint256 public constant OTHER_ALLOCATIONS_PERCENTAGE = 70;

    // Total token supply
    uint256 public totalSupply;

    // Allocation mapping
    uint256 public publicSaleAllocation;
    uint256 public stakingAllocation;
    uint256 public devAllocation;
    uint256 public exchangeAllocation;
    uint256 public marketingAllocation;

    // Owner address
    address public owner;

    // Modifier to restrict access to owner-only functionality
    modifier onlyOwner() {
        require(msg.sender == owner, "PresaleTokenDistribution: Caller is not the owner");
        _;
    }

    // Events
    event TokensDistributed(address indexed recipient, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Constructor to initialize total supply and set allocations based on tokenomics structure.
     * @param _totalSupply The total token supply for the contract.
     */
    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "PresaleTokenDistribution: Total supply must be greater than zero");
        
        owner = msg.sender;
        totalSupply = _totalSupply;

        // Calculate allocations based on percentages
        publicSaleAllocation = (totalSupply * PUBLIC_SALE_PERCENTAGE) / 100;
        stakingAllocation = (totalSupply * OTHER_ALLOCATIONS_PERCENTAGE) / 100 / 4;
        devAllocation = (totalSupply * OTHER_ALLOCATIONS_PERCENTAGE) / 100 / 4;
        exchangeAllocation = (totalSupply * OTHER_ALLOCATIONS_PERCENTAGE) / 100 / 4;
        marketingAllocation = (totalSupply * OTHER_ALLOCATIONS_PERCENTAGE) / 100 / 4;
    }

    /**
     * @dev Allows the owner to distribute tokens for the public sale.
     * @param recipient Address of the token recipient.
     * @param amount Amount of tokens to distribute.
     */
    function distributePublicSale(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "PresaleTokenDistribution: Invalid recipient address");
        require(amount <= publicSaleAllocation, "PresaleTokenDistribution: Insufficient public sale allocation");

        publicSaleAllocation -= amount;
        emit TokensDistributed(recipient, amount);
    }

    /**
     * @dev Allows the owner to distribute tokens for staking, development, exchange, or marketing purposes.
     * @param recipient Address of the token recipient.
     * @param amount Amount of tokens to distribute.
     * @param allocationType The type of allocation (staking = 0, dev = 1, exchange = 2, marketing = 3).
     */
    function distributeOtherAllocations(
        address recipient,
        uint256 amount,
        uint8 allocationType
    ) external onlyOwner {
        require(recipient != address(0), "PresaleTokenDistribution: Invalid recipient address");
        require(allocationType >= 0 && allocationType <= 3, "PresaleTokenDistribution: Invalid allocation type");

        if (allocationType == 0) {
            require(amount <= stakingAllocation, "PresaleTokenDistribution: Insufficient staking allocation");
            stakingAllocation -= amount;
        } else if (allocationType == 1) {
            require(amount <= devAllocation, "PresaleTokenDistribution: Insufficient dev allocation");
            devAllocation -= amount;
        } else if (allocationType == 2) {
            require(amount <= exchangeAllocation, "PresaleTokenDistribution: Insufficient exchange allocation");
            exchangeAllocation -= amount;
        } else if (allocationType == 3) {
            require(amount <= marketingAllocation, "PresaleTokenDistribution: Insufficient marketing allocation");
            marketingAllocation -= amount;
        }

        emit TokensDistributed(recipient, amount);
    }

    /**
     * @dev Allows the current owner to transfer ownership to a new owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "PresaleTokenDistribution: New owner cannot be zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}
```
