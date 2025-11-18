"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophpon.pages.dev
Prompt: Generate a Solidity contract to implement the tokenomics of $SOPH, including cliffs, vesting schedules, and lock-up periods for various allocation categories.
Generated: DETERMINISTIC_cee7ab7b87e2b991
Batch ID: 20250612_152235
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
 * @title SOPHTokenomics
 * @dev This contract manages token allocations with cliffs, vesting schedules, and lock-up periods for $SOPH token.
 */
contract SOPHTokenomics {
    // Token allocation structure
    struct Allocation {
        uint256 totalAmount; // Total allocated tokens
        uint256 vestedAmount; // Vested tokens
        uint256 cliffDate; // Cliff date (timestamp)
        uint256 vestingEndDate; // Vesting end date (timestamp)
        uint256 lockupEndDate; // Lock-up period end date (timestamp)
    }

    // Mapping for token allocations by address
    mapping(address => Allocation) public allocations;

    // Address of the admin
    address public admin;

    // Events
    event AllocationCreated(
        address indexed beneficiary,
        uint256 totalAmount,
        uint256 cliffDate,
        uint256 vestingEndDate,
        uint256 lockupEndDate
    );
    event TokensClaimed(address indexed beneficiary, uint256 amount);

    // Modifiers
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    modifier validAddress(address _addr) {
        require(_addr != address(0), "Invalid address");
        _;
    }

    constructor() {
        admin = msg.sender;
    }

    /**
     * @dev Initialize a new allocation for a beneficiary.
     * @param _beneficiary Address of the beneficiary.
     * @param _totalAmount Total token allocation for the beneficiary.
     * @param _cliffDate Cliff date (timestamp).
     * @param _vestingEndDate Vesting end date (timestamp).
     * @param _lockupEndDate Lock-up end date (timestamp).
     */
    function createAllocation(
        address _beneficiary,
        uint256 _totalAmount,
        uint256 _cliffDate,
        uint256 _vestingEndDate,
        uint256 _lockupEndDate
    )
        external
        onlyAdmin
        validAddress(_beneficiary)
    {
        require(_totalAmount > 0, "Allocation amount must be greater than zero");
        require(_cliffDate >= block.timestamp, "Cliff date must be in the future");
        require(_vestingEndDate > _cliffDate, "Vesting end date must be after cliff date");
        require(_lockupEndDate >= _vestingEndDate, "Lock-up end date must be after vesting end date");

        allocations[_beneficiary] = Allocation({
            totalAmount: _totalAmount,
            vestedAmount: 0,
            cliffDate: _cliffDate,
            vestingEndDate: _vestingEndDate,
            lockupEndDate: _lockupEndDate
        });

        emit AllocationCreated(_beneficiary, _totalAmount, _cliffDate, _vestingEndDate, _lockupEndDate);
    }

    /**
     * @dev Claim vested tokens after the cliff date.
     */
    function claimTokens() external {
        Allocation storage allocation = allocations[msg.sender];
        require(allocation.totalAmount > 0, "No allocation found for this address");
        require(block.timestamp >= allocation.cliffDate, "Cliff period not reached");
        require(block.timestamp < allocation.lockupEndDate, "Lock-up period active");

        uint256 vestedAmount = _calculateVestedAmount(allocation);
        require(vestedAmount > allocation.vestedAmount, "No new tokens available to claim");

        uint256 claimableAmount = vestedAmount - allocation.vestedAmount;
        allocation.vestedAmount = vestedAmount;

        emit TokensClaimed(msg.sender, claimableAmount);

        // Transfer tokens (replace with actual token transfer logic)
        // Example: token.transfer(msg.sender, claimableAmount);
        // Ensure that token contract is integrated before deployment
    }

    /**
     * @dev Internal function to calculate vested amount based on time passed.
     * @param allocation Allocation structure of the beneficiary.
     * @return The vested amount of tokens.
     */
    function _calculateVestedAmount(Allocation memory allocation) internal view returns (uint256) {
        if (block.timestamp >= allocation.vestingEndDate) {
            return allocation.totalAmount;
        }
        uint256 vestingDuration = allocation.vestingEndDate - allocation.cliffDate;
        uint256 timeElapsed = block.timestamp - allocation.cliffDate;
        return (allocation.totalAmount * timeElapsed) / vestingDuration;
    }

    /**
     * @dev Update the admin of the contract.
     * @param _newAdmin Address of the new admin.
     */
    function updateAdmin(address _newAdmin) external onlyAdmin validAddress(_newAdmin) {
        admin = _newAdmin;
    }
}
```
