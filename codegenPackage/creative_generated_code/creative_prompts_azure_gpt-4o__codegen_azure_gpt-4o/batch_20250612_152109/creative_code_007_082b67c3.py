"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scotty-theai-io.web.app
Prompt: Write a Solidity smart contract to implement the tokenomics structure of $SCOTTY, including allocations for staking, development, exchange listings, and marketing.
Generated: DETERMINISTIC_082b67c31ef0db17
Batch ID: 20250612_152109
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
 * @title SCOTTY Tokenomics Smart Contract
 * @dev Implements token distribution and allocation for staking, development, exchange listings, and marketing.
 */
contract ScottyToken {
    // Token details
    string public name = "$SCOTTY";
    string public symbol = "SCOTTY";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Allocation percentages
    uint256 public stakingAllocationPercentage = 40; // 40%
    uint256 public developmentAllocationPercentage = 25; // 25%
    uint256 public exchangeListingAllocationPercentage = 20; // 20%
    uint256 public marketingAllocationPercentage = 15; // 15%

    // Allocation balances
    uint256 public stakingAllocation;
    uint256 public developmentAllocation;
    uint256 public exchangeListingAllocation;
    uint256 public marketingAllocation;

    // Address balances
    mapping(address => uint256) public balances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event AllocationSet(
        uint256 stakingAllocation,
        uint256 developmentAllocation,
        uint256 exchangeListingAllocation,
        uint256 marketingAllocation
    );

    // Constructor
    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "Total supply must be greater than zero");

        totalSupply = _totalSupply;

        // Set allocations based on percentages
        stakingAllocation = (totalSupply * stakingAllocationPercentage) / 100;
        developmentAllocation = (totalSupply * developmentAllocationPercentage) / 100;
        exchangeListingAllocation = (totalSupply * exchangeListingAllocationPercentage) / 100;
        marketingAllocation = (totalSupply * marketingAllocationPercentage) / 100;

        // Allocate tokens to contract owner
        balances[msg.sender] = totalSupply;

        // Emit allocation event
        emit AllocationSet(
            stakingAllocation,
            developmentAllocation,
            exchangeListingAllocation,
            marketingAllocation
        );
    }

    /**
     * @dev Transfers tokens from the sender to the recipient.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(amount > 0, "Transfer amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Perform the transfer
        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        // Emit transfer event
        emit Transfer(msg.sender, recipient, amount);

        return true;
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account Address to query the balance of.
     * @return uint256 Balance of the address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev View function to get allocation details.
     * @return Allocations for staking, development, exchange listings, and marketing.
     */
    function getAllocations()
        external
        view
        returns (
            uint256 staking,
            uint256 development,
            uint256 exchangeListing,
            uint256 marketing
        )
    {
        return (stakingAllocation, developmentAllocation, exchangeListingAllocation, marketingAllocation);
    }
}
```
