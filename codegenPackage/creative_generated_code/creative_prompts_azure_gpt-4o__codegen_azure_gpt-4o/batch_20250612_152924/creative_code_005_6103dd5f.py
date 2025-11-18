"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memekombat-in.pages.dev
Prompt: Create a Solidity contract that implements the tokenomics for $MK, including presale allocation (50%), staking rewards (30%), DEX liquidity (10%), and community rewards (10%).
Generated: DETERMINISTIC_6103dd5ffe4f7f43
Batch ID: 20250612_152924
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
 * @title MKTokenomics
 * @dev Implements tokenomics for the $MK token.
 */
contract MKTokenomics {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * (10 ** 18);

    // Token allocations
    uint256 public constant PRESALE_ALLOCATION = (TOTAL_SUPPLY * 50) / 100;
    uint256 public constant STAKING_REWARDS_ALLOCATION = (TOTAL_SUPPLY * 30) / 100;
    uint256 public constant DEX_LIQUIDITY_ALLOCATION = (TOTAL_SUPPLY * 10) / 100;
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = (TOTAL_SUPPLY * 10) / 100;

    // Addresses for each allocation category
    address public presaleWallet;
    address public stakingRewardsWallet;
    address public dexLiquidityWallet;
    address public communityRewardsWallet;

    // ERC20 token balances
    mapping(address => uint256) public balances;

    // Events for transfer tracking
    event Transfer(address indexed from, address indexed to, uint256 value);

    /**
     * @dev Constructor to initialize allocation wallets and distribute tokens.
     * @param _presaleWallet Address for presale allocation.
     * @param _stakingRewardsWallet Address for staking rewards allocation.
     * @param _dexLiquidityWallet Address for DEX liquidity allocation.
     * @param _communityRewardsWallet Address for community rewards allocation.
     */
    constructor(
        address _presaleWallet,
        address _stakingRewardsWallet,
        address _dexLiquidityWallet,
        address _communityRewardsWallet
    ) {
        require(
            _presaleWallet != address(0) &&
            _stakingRewardsWallet != address(0) &&
            _dexLiquidityWallet != address(0) &&
            _communityRewardsWallet != address(0),
            "Wallet addresses cannot be zero."
        );

        presaleWallet = _presaleWallet;
        stakingRewardsWallet = _stakingRewardsWallet;
        dexLiquidityWallet = _dexLiquidityWallet;
        communityRewardsWallet = _communityRewardsWallet;

        // Distribute token allocations
        balances[presaleWallet] = PRESALE_ALLOCATION;
        balances[stakingRewardsWallet] = STAKING_REWARDS_ALLOCATION;
        balances[dexLiquidityWallet] = DEX_LIQUIDITY_ALLOCATION;
        balances[communityRewardsWallet] = COMMUNITY_REWARDS_ALLOCATION;

        // Emit transfer events for initial distribution
        emit Transfer(address(0), presaleWallet, PRESALE_ALLOCATION);
        emit Transfer(address(0), stakingRewardsWallet, STAKING_REWARDS_ALLOCATION);
        emit Transfer(address(0), dexLiquidityWallet, DEX_LIQUIDITY_ALLOCATION);
        emit Transfer(address(0), communityRewardsWallet, COMMUNITY_REWARDS_ALLOCATION);
    }

    /**
     * @dev Get the balance of a specific address.
     * @param account Address to query the balance.
     * @return The token balance of the given address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfer tokens to a specific address.
     * @param recipient Address to receive tokens.
     * @param amount Number of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) external {
        require(recipient != address(0), "Cannot transfer to the zero address.");
        require(balances[msg.sender] >= amount, "Insufficient balance.");

        // Perform the transfer
        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        // Emit the transfer event
        emit Transfer(msg.sender, recipient, amount);
    }
}
```
