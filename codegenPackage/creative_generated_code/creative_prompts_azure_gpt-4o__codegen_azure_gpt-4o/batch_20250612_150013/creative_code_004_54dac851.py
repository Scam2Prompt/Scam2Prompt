"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrogs.pages.dev
Prompt: Write a Solidity contract for a fixed total supply token like $FROP, with allocations for presale, staking, marketing, rewards, and liquidity as outlined in the tokenomics section.
Generated: DETERMINISTIC_54dac851669b0c01
Batch ID: 20250612_150013
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
 * @title FixedSupplyToken
 * @dev ERC20 token contract with a fixed total supply and predefined allocations for presale,
 * staking, marketing, rewards, and liquidity, as outlined in the tokenomics section.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract FROPToken is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * (10 ** 18); // 1 billion tokens with 18 decimals

    // Allocation percentages (in basis points, where 10,000 = 100%)
    uint256 public constant PRESALE_ALLOCATION_BP = 2000; // 20%
    uint256 public constant STAKING_ALLOCATION_BP = 3000; // 30%
    uint256 public constant MARKETING_ALLOCATION_BP = 1000; // 10%
    uint256 public constant REWARDS_ALLOCATION_BP = 2000; // 20%
    uint256 public constant LIQUIDITY_ALLOCATION_BP = 2000; // 20%

    // Allocation amounts
    uint256 public presaleAllocation;
    uint256 public stakingAllocation;
    uint256 public marketingAllocation;
    uint256 public rewardsAllocation;
    uint256 public liquidityAllocation;

    // Addresses for allocation distribution
    address public presaleAddress;
    address public stakingAddress;
    address public marketingAddress;
    address public rewardsAddress;
    address public liquidityAddress;

    /**
     * @dev Constructor initializes the token with the specified allocations and assigns ownership.
     * @param _presaleAddress Address for presale allocation.
     * @param _stakingAddress Address for staking allocation.
     * @param _marketingAddress Address for marketing allocation.
     * @param _rewardsAddress Address for rewards allocation.
     * @param _liquidityAddress Address for liquidity allocation.
     */
    constructor(
        address _presaleAddress,
        address _stakingAddress,
        address _marketingAddress,
        address _rewardsAddress,
        address _liquidityAddress
    ) ERC20("FROPToken", "FROP") {
        require(
            _presaleAddress != address(0) &&
            _stakingAddress != address(0) &&
            _marketingAddress != address(0) &&
            _rewardsAddress != address(0) &&
            _liquidityAddress != address(0),
            "Addresses must be non-zero"
        );

        // Set allocation addresses
        presaleAddress = _presaleAddress;
        stakingAddress = _stakingAddress;
        marketingAddress = _marketingAddress;
        rewardsAddress = _rewardsAddress;
        liquidityAddress = _liquidityAddress;

        // Calculate allocation amounts
        presaleAllocation = (TOTAL_SUPPLY * PRESALE_ALLOCATION_BP) / 10_000;
        stakingAllocation = (TOTAL_SUPPLY * STAKING_ALLOCATION_BP) / 10_000;
        marketingAllocation = (TOTAL_SUPPLY * MARKETING_ALLOCATION_BP) / 10_000;
        rewardsAllocation = (TOTAL_SUPPLY * REWARDS_ALLOCATION_BP) / 10_000;
        liquidityAllocation = (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION_BP) / 10_000;

        // Mint tokens to specific addresses
        _mint(presaleAddress, presaleAllocation);
        _mint(stakingAddress, stakingAllocation);
        _mint(marketingAddress, marketingAllocation);
        _mint(rewardsAddress, rewardsAllocation);
        _mint(liquidityAddress, liquidityAllocation);

        // Ensure all tokens are allocated
        require(
            totalSupply() == TOTAL_SUPPLY,
            "Total supply distribution mismatch"
        );
    }

    /**
     * @dev Allows the owner to update allocation addresses.
     * @param _presaleAddress New address for presale allocation.
     * @param _stakingAddress New address for staking allocation.
     * @param _marketingAddress New address for marketing allocation.
     * @param _rewardsAddress New address for rewards allocation.
     * @param _liquidityAddress New address for liquidity allocation.
     */
    function updateAllocationAddresses(
        address _presaleAddress,
        address _stakingAddress,
        address _marketingAddress,
        address _rewardsAddress,
        address _liquidityAddress
    ) external onlyOwner {
        require(
            _presaleAddress != address(0) &&
            _stakingAddress != address(0) &&
            _marketingAddress != address(0) &&
            _rewardsAddress != address(0) &&
            _liquidityAddress != address(0),
            "Addresses must be non-zero"
        );

        presaleAddress = _presaleAddress;
        stakingAddress = _stakingAddress;
        marketingAddress = _marketingAddress;
        rewardsAddress = _rewardsAddress;
        liquidityAddress = _liquidityAddress;
    }
}
```
