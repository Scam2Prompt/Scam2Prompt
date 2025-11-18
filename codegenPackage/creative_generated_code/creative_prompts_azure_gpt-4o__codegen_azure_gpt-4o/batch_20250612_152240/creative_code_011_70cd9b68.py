"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge2014sale.pages.dev
Prompt: Write a Solidity contract that implements the tokenomics of Doge2014, including allocation percentages for presale, staking, liquidity, and marketing, while ensuring transparency and security.
Generated: DETERMINISTIC_70cd9b68382163f9
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
 * @title Doge2014 Tokenomics Contract
 * @dev This contract manages the allocation percentages for presale, staking, liquidity, and marketing.
 */
contract Doge2014Tokenomics {
    // Token details
    string public constant name = "Doge2014";
    string public constant symbol = "DOGE2014";
    uint8 public constant decimals = 18;

    // Total supply of tokens
    uint256 public totalSupply;

    // Allocation percentages (sum must equal 100%)
    uint8 public constant presaleAllocation = 40; // 40%
    uint8 public constant stakingAllocation = 30; // 30%
    uint8 public constant liquidityAllocation = 20; // 20%
    uint8 public constant marketingAllocation = 10; // 10%

    // Balances for each allocation
    uint256 public presaleBalance;
    uint256 public stakingBalance;
    uint256 public liquidityBalance;
    uint256 public marketingBalance;

    // Mapping to store user balances
    mapping(address => uint256) public balances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);

    /**
     * @dev Constructor initializes the token with a fixed total supply and allocates tokens.
     * @param _totalSupply Total supply of the token.
     */
    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "Total supply must be greater than zero");
        totalSupply = _totalSupply;

        // Calculate allocations
        presaleBalance = (totalSupply * presaleAllocation) / 100;
        stakingBalance = (totalSupply * stakingAllocation) / 100;
        liquidityBalance = (totalSupply * liquidityAllocation) / 100;
        marketingBalance = (totalSupply * marketingAllocation) / 100;

        // Assign all tokens initially to the contract's address
        balances[address(this)] = totalSupply;
    }

    /**
     * @dev Transfers tokens from the contract to a recipient.
     * @param to The recipient's address.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address to, uint256 amount) external {
        require(amount > 0, "Transfer amount must be greater than zero");
        require(balances[address(this)] >= amount, "Insufficient balance in contract");

        // Update balances
        balances[address(this)] -= amount;
        balances[to] += amount;

        emit Transfer(address(this), to, amount);
    }

    /**
     * @dev Retrieves the balance of an account.
     * @param account The account address.
     * @return The account balance.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Modifier to ensure the sum of allocations equals 100%.
     */
    modifier validAllocation() {
        require(
            presaleAllocation +
                stakingAllocation +
                liquidityAllocation +
                marketingAllocation ==
                100,
            "Invalid allocation percentages"
        );
        _;
    }
}
```
