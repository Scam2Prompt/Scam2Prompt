"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyanheroes-d2u.pages.dev
Prompt: Create a smart contract that mimics the token allocation system described on the Nyan Heroes platform, ensuring compatibility with $NYAN tokens.
Generated: DETERMINISTIC_bb6a81067ab2df46
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
// Smart Contract for Token Allocation - Compatible with $NYAN Tokens

pragma solidity ^0.8.0;

/**
 * @title TokenAllocation
 * @dev A smart contract to manage token allocations for $NYAN tokens.
 */
contract TokenAllocation {
    // Address of the $NYAN token contract
    IERC20 public nyanToken;

    // Struct to store allocation details
    struct Allocation {
        uint256 amount;       // Total allocated tokens
        uint256 claimed;      // Tokens already claimed
        uint256 startTime;    // Vesting start time
        uint256 cliff;        // Cliff duration in seconds
        uint256 duration;     // Vesting duration in seconds
    }

    // Mapping for token allocations by beneficiary
    mapping(address => Allocation) public allocations;

    // Owner of the contract
    address public owner;

    // Events
    event Allocated(address indexed beneficiary, uint256 amount);
    event Claimed(address indexed beneficiary, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set the $NYAN token address and initialize the contract owner.
     * @param _nyanToken Address of the $NYAN token contract.
     */
    constructor(address _nyanToken) {
        require(_nyanToken != address(0), "Invalid token address");
        nyanToken = IERC20(_nyanToken);
        owner = msg.sender;
    }

    /**
     * @dev Allocate tokens to a beneficiary with vesting details.
     * @param beneficiary Address of the beneficiary.
     * @param amount Total number of tokens allocated.
     * @param startTime Vesting start time.
     * @param cliff Cliff duration in seconds.
     * @param duration Vesting duration in seconds.
     */
    function allocate(
        address beneficiary,
        uint256 amount,
        uint256 startTime,
        uint256 cliff,
        uint256 duration
    ) external onlyOwner {
        require(beneficiary != address(0), "Invalid beneficiary address");
        require(amount > 0, "Invalid token amount");
        require(duration > cliff, "Duration must be longer than cliff");

        allocations[beneficiary] = Allocation({
            amount: amount,
            claimed: 0,
            startTime: startTime,
            cliff: cliff,
            duration: duration
        });

        emit Allocated(beneficiary, amount);
    }

    /**
     * @dev Claim vested tokens for the caller.
     */
    function claim() external {
        Allocation storage alloc = allocations[msg.sender];
        require(alloc.amount > 0, "No allocation found");

        uint256 vestedAmount = calculateVestedAmount(
            alloc.amount,
            alloc.startTime,
            alloc.cliff,
            alloc.duration
        );
        uint256 claimableAmount = vestedAmount - alloc.claimed;

        require(claimableAmount > 0, "No tokens available for claim");

        alloc.claimed += claimableAmount;
        require(nyanToken.transfer(msg.sender, claimableAmount), "Transfer failed");

        emit Claimed(msg.sender, claimableAmount);
    }

    /**
     * @dev Calculate the vested token amount based on the allocation details.
     * @param totalAmount Total allocated tokens.
     * @param startTime Vesting start time.
     * @param cliff Cliff duration in seconds.
     * @param duration Vesting duration in seconds.
     * @return uint256 Total vested token amount.
     */
    function calculateVestedAmount(
        uint256 totalAmount,
        uint256 startTime,
        uint256 cliff,
        uint256 duration
    ) public view returns (uint256) {
        if (block.timestamp < startTime + cliff) {
            return 0;
        } else if (block.timestamp >= startTime + duration) {
            return totalAmount;
        } else {
            uint256 timeElapsed = block.timestamp - startTime;
            return (totalAmount * timeElapsed) / duration;
        }
    }

    /**
     * @dev Emergency function for the owner to withdraw tokens from the contract.
     * @param amount Number of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(nyanToken.transfer(owner, amount), "Withdraw failed");
    }
}

// Interface for ERC20 token compatibility
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
