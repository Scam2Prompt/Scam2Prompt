"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrogclaim.pages.dev
Prompt: Write a script in Solidity to implement a fixed token supply of 111,111,111,111 $FROP tokens, with allocations for presale, staking, marketing, rewards, and liquidity as outlined in the tokenomics section of the Popo The Frog webpage.
Generated: DETERMINISTIC_78623ea128dd13bc
Batch ID: 20250612_151648
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
 * @title FROPToken
 * @notice Implementation of a fixed supply ERC20 token with predefined allocations.
 * @dev Allocations are distributed for presale, staking, marketing, rewards, and liquidity.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract FROPToken is ERC20, Ownable {
    // Fixed token supply
    uint256 public constant TOTAL_SUPPLY = 111_111_111_111 * (10 ** 18);

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 25; // 25%
    uint256 public constant STAKING_ALLOCATION = 20; // 20%
    uint256 public constant MARKETING_ALLOCATION = 15; // 15%
    uint256 public constant REWARDS_ALLOCATION = 25; // 25%
    uint256 public constant LIQUIDITY_ALLOCATION = 15; // 15%

    // Addresses for respective allocations
    address public presaleWallet;
    address public stakingWallet;
    address public marketingWallet;
    address public rewardsWallet;
    address public liquidityWallet;

    /**
     * @dev Constructor for FROPToken contract.
     * @param _presaleWallet Address for the presale allocation.
     * @param _stakingWallet Address for the staking allocation.
     * @param _marketingWallet Address for the marketing allocation.
     * @param _rewardsWallet Address for the rewards allocation.
     * @param _liquidityWallet Address for the liquidity allocation.
     */
    constructor(
        address _presaleWallet,
        address _stakingWallet,
        address _marketingWallet,
        address _rewardsWallet,
        address _liquidityWallet
    ) ERC20("$FROP", "FROP") {
        require(
            _presaleWallet != address(0) &&
            _stakingWallet != address(0) &&
            _marketingWallet != address(0) &&
            _rewardsWallet != address(0) &&
            _liquidityWallet != address(0),
            "Wallet addresses cannot be zero."
        );

        // Assigning wallet addresses
        presaleWallet = _presaleWallet;
        stakingWallet = _stakingWallet;
        marketingWallet = _marketingWallet;
        rewardsWallet = _rewardsWallet;
        liquidityWallet = _liquidityWallet;

        // Minting token allocations
        _mint(presaleWallet, (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100);
        _mint(stakingWallet, (TOTAL_SUPPLY * STAKING_ALLOCATION) / 100);
        _mint(marketingWallet, (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100);
        _mint(rewardsWallet, (TOTAL_SUPPLY * REWARDS_ALLOCATION) / 100);
        _mint(liquidityWallet, (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100);
    }

    /**
     * @dev Update wallet addresses for allocations, callable only by the owner.
     * @param _presaleWallet New address for presale allocation.
     * @param _stakingWallet New address for staking allocation.
     * @param _marketingWallet New address for marketing allocation.
     * @param _rewardsWallet New address for rewards allocation.
     * @param _liquidityWallet New address for liquidity allocation.
     */
    function updateWallets(
        address _presaleWallet,
        address _stakingWallet,
        address _marketingWallet,
        address _rewardsWallet,
        address _liquidityWallet
    ) external onlyOwner {
        require(
            _presaleWallet != address(0) &&
            _stakingWallet != address(0) &&
            _marketingWallet != address(0) &&
            _rewardsWallet != address(0) &&
            _liquidityWallet != address(0),
            "Wallet addresses cannot be zero."
        );

        presaleWallet = _presaleWallet;
        stakingWallet = _stakingWallet;
        marketingWallet = _marketingWallet;
        rewardsWallet = _rewardsWallet;
        liquidityWallet = _liquidityWallet;
    }
}
```
