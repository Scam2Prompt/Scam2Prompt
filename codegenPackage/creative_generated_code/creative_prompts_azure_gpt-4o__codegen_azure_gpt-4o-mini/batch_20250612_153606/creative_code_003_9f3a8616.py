"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularitydaoai-launchpad.pages.dev
Prompt: Create a smart contract in Solidity that implements a vesting schedule for WSDM tokens as described on the SingularityDAO Launchpad page, including cliff and linear per block vesting.
Generated: DETERMINISTIC_9f3a86162ca5cb76
Batch ID: 20250612_153606
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

// Importing OpenZeppelin's Ownable and ERC20 interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title VestingContract
 * @dev This contract allows for the vesting of WSDM tokens with a cliff and linear release.
 */
contract VestingContract is Ownable {
    // The token to be vested
    IERC20 public token;

    // Beneficiary of tokens after they are released
    address public beneficiary;

    // Vesting parameters
    uint256 public start; // Start time of the vesting
    uint256 public cliff; // Duration of the cliff in seconds
    uint256 public duration; // Total duration of the vesting period in seconds

    // Amount of tokens to be released
    uint256 public totalAmount;

    // Amount of tokens released so far
    uint256 public released;

    /**
     * @dev Emitted when tokens are released.
     */
    event TokensReleased(uint256 amount);

    /**
     * @param _token The address of the token being vested
     * @param _beneficiary The address that will receive the vested tokens
     * @param _start The start time of the vesting (in timestamp)
     * @param _cliff The duration of the cliff (in seconds)
     * @param _duration The total duration of the vesting period (in seconds)
     * @param _totalAmount The total amount of tokens to be vested
     */
    constructor(
        IERC20 _token,
        address _beneficiary,
        uint256 _start,
        uint256 _cliff,
        uint256 _duration,
        uint256 _totalAmount
    ) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_beneficiary != address(0), "Beneficiary address cannot be zero");
        require(_cliff <= _duration, "Cliff must be less than or equal to duration");
        require(_totalAmount > 0, "Total amount must be greater than zero");

        token = _token;
        beneficiary = _beneficiary;
        start = _start;
        cliff = _cliff;
        duration = _duration;
        totalAmount = _totalAmount;
    }

    /**
     * @dev Allows the beneficiary to release vested tokens.
     */
    function release() public {
        // Calculate the releasable amount of tokens
        uint256 unreleased = _releasableAmount();

        require(unreleased > 0, "No tokens are due for release");

        // Update the released amount
        released += unreleased;

        // Transfer the tokens to the beneficiary
        require(token.transfer(beneficiary, unreleased), "Transfer failed");

        emit TokensReleased(unreleased);
    }

    /**
     * @dev Calculates the amount of tokens that can be released.
     * @return The amount of tokens that are releasable
     */
    function _releasableAmount() private view returns (uint256) {
        uint256 vestedAmount = _vestedAmount();
        return vestedAmount - released;
    }

    /**
     * @dev Calculates the total amount of vested tokens up to the current block.
     * @return The total vested amount
     */
    function _vestedAmount() private view returns (uint256) {
        if (block.timestamp < start + cliff) {
            return 0; // No tokens are vested during the cliff
        } else if (block.timestamp >= start + duration) {
            return totalAmount; // All tokens are vested after the duration ends
        } else {
            // Linear vesting calculation
            return (totalAmount * (block.timestamp - start)) / duration;
        }
    }

    /**
     * @dev Returns the amount of tokens that have been released.
     * @return The total amount of released tokens
     */
    function releasedAmount() public view returns (uint256) {
        return released;
    }
    
    /**
     * @dev Returns the amount of tokens that can still be released.
     * @return The amount of tokens that are still releasable
     */
    function releasableAmount() public view returns (uint256) {
        return _releasableAmount();
    }
}
```
