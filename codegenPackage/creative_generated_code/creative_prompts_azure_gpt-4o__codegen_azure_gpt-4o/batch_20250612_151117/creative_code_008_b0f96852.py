"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdogai-en.pages.dev
Prompt: Generate a Solidity smart contract snippet to implement tokenomics similar to WienerAI's allocation percentages (e.g., presale, staking, rewards, liquidity, marketing).
Generated: DETERMINISTIC_b0f968524fee949a
Batch ID: 20250612_151117
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
 * @title TokenomicsContract
 * @dev Implements token allocation percentages for presale, staking, rewards, liquidity, and marketing
 */
contract TokenomicsContract {
    // ERC20 related state variables
    string public name = "TokenomicsToken";
    string public symbol = "TKN";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1_000_000 * (10 ** uint256(decimals));

    // Allocation percentages (in basis points: 1% = 100 basis points)
    uint256 public constant PRESALE_PERCENTAGE = 2000; // 20%
    uint256 public constant STAKING_PERCENTAGE = 3000; // 30%
    uint256 public constant REWARDS_PERCENTAGE = 2500; // 25%
    uint256 public constant LIQUIDITY_PERCENTAGE = 1500; // 15%
    uint256 public constant MARKETING_PERCENTAGE = 1000; // 10%

    // Token allocation state variables
    uint256 public presaleAllocation;
    uint256 public stakingAllocation;
    uint256 public rewardsAllocation;
    uint256 public liquidityAllocation;
    uint256 public marketingAllocation;

    // Balances mapping
    mapping(address => uint256) public balances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);

    /**
     * @dev Constructor that initializes token allocations and assigns tokens to the contract owner.
     */
    constructor() {
        // Calculate allocations based on percentages
        presaleAllocation = (totalSupply * PRESALE_PERCENTAGE) / 10000;
        stakingAllocation = (totalSupply * STAKING_PERCENTAGE) / 10000;
        rewardsAllocation = (totalSupply * REWARDS_PERCENTAGE) / 10000;
        liquidityAllocation = (totalSupply * LIQUIDITY_PERCENTAGE) / 10000;
        marketingAllocation = (totalSupply * MARKETING_PERCENTAGE) / 10000;

        // Assign 100% of tokens to the contract deployer initially
        balances[msg.sender] = totalSupply;

        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Transfers tokens from sender to recipient.
     * @param recipient The address of the recipient.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Perform the transfer
        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        // Emit transfer event
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Gets the balance of a specific account.
     * @param account The address of the account.
     * @return The balance of the account.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }
}
```
