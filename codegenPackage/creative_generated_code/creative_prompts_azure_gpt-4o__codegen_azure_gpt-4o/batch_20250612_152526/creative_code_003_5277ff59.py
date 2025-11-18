"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artyfact-gaming.pages.dev
Prompt: Create a smart contract on Binance Smart Chain (BSC) that mirrors the vesting functionality described on the Artyfact website, including allocation tracking and multi-round claiming.
Generated: DETERMINISTIC_5277ff59b87d1287
Batch ID: 20250612_152526
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
 * @title VestingContract
 * @dev A smart contract that enables token vesting with allocation tracking and multi-round claiming.
 *      Designed for Binance Smart Chain (BSC).
 */
contract VestingContract {
    // Token interface for interacting with BEP-20 tokens
    interface IBEP20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // Struct to represent a single vesting allocation
    struct Allocation {
        uint256 totalAmount;       // Total allocated tokens
        uint256 claimedAmount;     // Amount of tokens already claimed
        uint256[] claimRounds;     // Timestamps for claimable rounds
        uint256[] roundAmounts;    // Amounts for each claimable round
    }

    // Mapping of user addresses to their allocation data
    mapping(address => Allocation) public allocations;

    // Address of the admin who manages allocations
    address public admin;

    // Address of the token being vested
    IBEP20 public token;

    // Event emitted when an allocation is created or updated
    event AllocationUpdated(address indexed beneficiary, uint256 totalAmount);

    // Event emitted when a beneficiary claims tokens
    event TokensClaimed(address indexed beneficiary, uint256 amount);

    // Modifier to restrict access to admin functions
    modifier onlyAdmin() {
        require(msg.sender == admin, "Caller is not the admin");
        _;
    }

    /**
     * @dev Constructor to set the admin and token addresses.
     * @param _token Address of the BEP-20 token being vested.
     */
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        admin = msg.sender;
        token = IBEP20(_token);
    }

    /**
     * @dev Function to create or update a beneficiary's vesting allocation.
     * @param _beneficiary Address of the beneficiary.
     * @param _totalAmount Total amount allocated to the beneficiary.
     * @param _claimRounds Timestamps for claimable rounds.
     * @param _roundAmounts Amounts available to claim in each round.
     */
    function setAllocation(
        address _beneficiary,
        uint256 _totalAmount,
        uint256[] memory _claimRounds,
        uint256[] memory _roundAmounts
    ) external onlyAdmin {
        require(_beneficiary != address(0), "Invalid beneficiary address");
        require(_totalAmount > 0, "Total amount must be greater than zero");
        require(
            _claimRounds.length == _roundAmounts.length,
            "Claim rounds and amounts length mismatch"
        );

        // Create or update the allocation
        Allocation storage allocation = allocations[_beneficiary];
        allocation.totalAmount = _totalAmount;
        allocation.claimRounds = _claimRounds;
        allocation.roundAmounts = _roundAmounts;

        emit AllocationUpdated(_beneficiary, _totalAmount);
    }

    /**
     * @dev Function for a beneficiary to claim vested tokens for a specific round.
     * @param _roundIndex Index of the claimable round.
     */
    function claim(uint256 _roundIndex) external {
        Allocation storage allocation = allocations[msg.sender];

        require(allocation.totalAmount > 0, "No allocation found for beneficiary");
        require(_roundIndex < allocation.claimRounds.length, "Invalid round index");
        require(block.timestamp >= allocation.claimRounds[_roundIndex], "Claim round not yet available");
        require(allocation.claimedAmount + allocation.roundAmounts[_roundIndex] <= allocation.totalAmount, "Exceeds allocated amount");

        uint256 claimAmount = allocation.roundAmounts[_roundIndex];
        require(claimAmount > 0, "No tokens available for this round");

        allocation.claimedAmount += claimAmount;

        // Transfer the tokens to the beneficiary
        require(token.transfer(msg.sender, claimAmount), "Token transfer failed");

        emit TokensClaimed(msg.sender, claimAmount);
    }

    /**
     * @dev Function to retrieve the unclaimed token balance for a beneficiary.
     * @param _beneficiary Address of the beneficiary.
     * @return The unclaimed token balance.
     */
    function getUnclaimedBalance(address _beneficiary) external view returns (uint256) {
        Allocation storage allocation = allocations[_beneficiary];
        return allocation.totalAmount - allocation.claimedAmount;
    }

    /**
     * @dev Function to transfer admin rights to a new address.
     * @param _newAdmin Address of the new admin.
     */
    function transferAdmin(address _newAdmin) external onlyAdmin {
        require(_newAdmin != address(0), "Invalid new admin address");
        admin = _newAdmin;
    }
}
```
