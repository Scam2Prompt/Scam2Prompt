"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinuairdrop.pages.dev
Prompt: Generate a smart contract in Solidity that implements tokenomics for $POODL, including allocations for presale (50%), staking (30%), DEX liquidity (10%), and marketing (10%).
Generated: DETERMINISTIC_5b0b19a107782a83
Batch ID: 20250612_153400
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
 * @title POODL Token Contract
 * @dev Implements tokenomics for $POODL including allocations for presale, staking, DEX liquidity, and marketing.
 */
contract POODLToken {
    // Basic token information
    string public name = "$POODL";
    string public symbol = "POODL";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION_PERCENT = 50; // 50%
    uint256 public constant STAKING_ALLOCATION_PERCENT = 30; // 30%
    uint256 public constant DEX_LIQUIDITY_ALLOCATION_PERCENT = 10; // 10%
    uint256 public constant MARKETING_ALLOCATION_PERCENT = 10; // 10%

    // Allocation balances
    uint256 public presaleAllocation;
    uint256 public stakingAllocation;
    uint256 public dexLiquidityAllocation;
    uint256 public marketingAllocation;

    // Balances mapping
    mapping(address => uint256) public balances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);

    /**
     * @dev Constructor to initialize the token and allocate balances.
     * @param _totalSupply The total supply of the token.
     * @param presaleAddress The address for presale allocation.
     * @param stakingAddress The address for staking allocation.
     * @param dexLiquidityAddress The address for DEX liquidity allocation.
     * @param marketingAddress The address for marketing allocation.
     */
    constructor(
        uint256 _totalSupply,
        address presaleAddress,
        address stakingAddress,
        address dexLiquidityAddress,
        address marketingAddress
    ) {
        require(presaleAddress != address(0), "Invalid presale address");
        require(stakingAddress != address(0), "Invalid staking address");
        require(dexLiquidityAddress != address(0), "Invalid DEX liquidity address");
        require(marketingAddress != address(0), "Invalid marketing address");

        totalSupply = _totalSupply;

        // Allocate tokens based on percentages
        presaleAllocation = (_totalSupply * PRESALE_ALLOCATION_PERCENT) / 100;
        stakingAllocation = (_totalSupply * STAKING_ALLOCATION_PERCENT) / 100;
        dexLiquidityAllocation = (_totalSupply * DEX_LIQUIDITY_ALLOCATION_PERCENT) / 100;
        marketingAllocation = (_totalSupply * MARKETING_ALLOCATION_PERCENT) / 100;

        // Assign initial balances
        balances[presaleAddress] = presaleAllocation;
        balances[stakingAddress] = stakingAllocation;
        balances[dexLiquidityAddress] = dexLiquidityAllocation;
        balances[marketingAddress] = marketingAllocation;

        // Emit transfer events for transparency
        emit Transfer(address(0), presaleAddress, presaleAllocation);
        emit Transfer(address(0), stakingAddress, stakingAllocation);
        emit Transfer(address(0), dexLiquidityAddress, dexLiquidityAllocation);
        emit Transfer(address(0), marketingAddress, marketingAllocation);
    }

    /**
     * @dev Transfer tokens from the sender to a recipient.
     * @param recipient The address of the recipient.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Deduct from sender and add to recipient
        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        // Emit transfer event
        emit Transfer(msg.sender, recipient, amount);

        return true;
    }

    /**
     * @dev Get the balance of a specific address.
     * @param account The address to query the balance.
     * @return The balance of the queried account.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }
}
```
