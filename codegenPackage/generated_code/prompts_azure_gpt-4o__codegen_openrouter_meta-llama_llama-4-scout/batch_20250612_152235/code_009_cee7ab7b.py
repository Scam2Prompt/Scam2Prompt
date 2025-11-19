"""
Generated Code Metadata:
========================
Original URL: https://sophpon.pages.dev
Prompt: Generate a Solidity contract to implement the tokenomics of $SOPH, including cliffs, vesting schedules, and lock-up periods for various allocation categories.
Generated: DETERMINISTIC_cee7ab7b87e2b991
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title SOPH Tokenomics Contract
 * @author [Your Name]
 * @notice This contract implements the tokenomics of $SOPH, including cliffs, vesting schedules, and lock-up periods for various allocation categories.
 */
contract SOPHTokenomics is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Allocation categories
    enum AllocationCategory {
        TEAM,
        ADVISORS,
        PRIVATE_SALE,
        PUBLIC_SALE,
        LIQUIDITY_PROVIDERS,
        RESERVE
    }

    // Vesting schedule structure
    struct VestingSchedule {
        uint256 cliff;
        uint256 vestingDuration;
        uint256 startTime;
    }

    // Mapping of allocation categories to their respective vesting schedules and lock-up periods
    mapping(AllocationCategory => VestingSchedule) public vestingSchedules;

    // Mapping of allocation categories to their respective token allocations
    mapping(AllocationCategory => uint256) public tokenAllocations;

    // Mapping of addresses to their respective allocation categories
    mapping(address => AllocationCategory) public allocationCategories;

    // Event emitted when tokens are vested
    event TokensVested(address indexed beneficiary, uint256 amount);

    /**
     * @notice Initializes the SOPH tokenomics contract.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Initialize vesting schedules and token allocations for each allocation category
        vestingSchedules[AllocationCategory.TEAM] = VestingSchedule(365 days, 730 days, block.timestamp);
        tokenAllocations[AllocationCategory.TEAM] = 10_000_000e18;

        vestingSchedules[AllocationCategory.ADVISORS] = VestingSchedule(180 days, 360 days, block.timestamp);
        tokenAllocations[AllocationCategory.ADVISORS] = 2_000_000e18;

        vestingSchedules[AllocationCategory.PRIVATE_SALE] = VestingSchedule(0 days, 0 days, block.timestamp);
        tokenAllocations[AllocationCategory.PRIVATE_SALE] = 5_000_000e18;

        vestingSchedules[AllocationCategory.PUBLIC_SALE] = VestingSchedule(0 days, 0 days, block.timestamp);
        tokenAllocations[AllocationCategory.PUBLIC_SALE] = 10_000_000e18;

        vestingSchedules[AllocationCategory.LIQUIDITY_PROVIDERS] = VestingSchedule(0 days, 0 days, block.timestamp);
        tokenAllocations[AllocationCategory.LIQUIDITY_PROVIDERS] = 5_000_000e18;

        vestingSchedules[AllocationCategory.RESERVE] = VestingSchedule(365 days, 730 days, block.timestamp);
        tokenAllocations[AllocationCategory.RESERVE] = 10_000_000e18;

        // Mint initial token supply
        _mint(msg.sender, 42_000_000e18);
    }

    /**
     * @notice Checks if tokens are vested for a given allocation category.
     * @param category The allocation category.
     * @param timestamp The timestamp to check.
     * @return bool True if tokens are vested, false otherwise.
     */
    function isVested(AllocationCategory category, uint256 timestamp) internal view returns (bool) {
        VestingSchedule memory schedule = vestingSchedules[category];
        return timestamp >= schedule.startTime + schedule.cliff && timestamp >= schedule.startTime + schedule.vestingDuration;
    }

    /**
     * @notice Vests tokens for a given allocation category.
     * @param category The allocation category.
     * @param beneficiary The address to vest tokens for.
     */
    function vestTokens(AllocationCategory category, address beneficiary) external nonReentrant {
        require(allocationCategories[beneficiary] == category, "Invalid allocation category");

        VestingSchedule memory schedule = vestingSchedules[category];
        uint256 vestedAmount = calculateVestedAmount(category, beneficiary);

        // Update token balance
        _mint(beneficiary, vestedAmount);

        // Emit event
        emit TokensVested(beneficiary, vestedAmount);
    }

    /**
     * @notice Calculates the vested amount for a given allocation category and beneficiary.
     * @param category The allocation category.
     * @param beneficiary The address to calculate vested amount for.
     * @return uint256 The vested amount.
     */
    function calculateVestedAmount(AllocationCategory category, address beneficiary) internal view returns (uint256) {
        VestingSchedule memory schedule = vestingSchedules[category];
        uint256 elapsedTime = block.timestamp - schedule.startTime;
        uint256 vestedPercentage = elapsedTime.mul(100).div(schedule.vestingDuration);

        // Apply cliff
        if (elapsedTime < schedule.cliff) {
            return 0;
        } else if (vestedPercentage > 100) {
            vestedPercentage = 100;
        }

        uint256 tokenAllocation = tokenAllocations[category];
        return tokenAllocation.mul(vestedPercentage).div(100);
    }

    /**
     * @notice Sets the allocation category for a given address.
     * @param beneficiary The address to set allocation category for.
     * @param category The allocation category.
     */
    function setAllocationCategory(address beneficiary, AllocationCategory category) external {
        allocationCategories[beneficiary] = category;
    }

    /**
     * @notice Burns tokens.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override {
        super.burn(amount);
    }
}
```
