"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnm-boxes.pages.dev
Prompt: Write a smart contract in Solidity that implements the vesting and distribution mechanics described in the $EARNM 'Fractal Box' protocol, ensuring a 12-month holding period and automatic redistribution of forfeited assets.
Generated: DETERMINISTIC_7c337ca1621ea956
Batch ID: 20250612_150130
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FractalBox
 * @dev A smart contract that implements the vesting and distribution mechanics for the $EARNM protocol.
 */
contract FractalBox is Ownable {
    // Struct to hold vesting information
    struct Vesting {
        uint256 amount;          // Amount of tokens to vest
        uint256 released;        // Amount of tokens released
        uint256 start;           // Start timestamp of the vesting period
        uint256 cliff;           // Cliff period in seconds
        uint256 duration;        // Total duration of the vesting period in seconds
        bool exists;             // Check if vesting exists
    }

    // Mapping of beneficiary addresses to their vesting information
    mapping(address => Vesting) private vestings;

    // ERC20 token being used for vesting
    IERC20 public token;

    // Event emitted when tokens are released
    event TokensReleased(address indexed beneficiary, uint256 amount);

    // Event emitted when vesting is created
    event VestingCreated(address indexed beneficiary, uint256 amount, uint256 start, uint256 cliff, uint256 duration);

    // Constructor to set the token address
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Creates a new vesting schedule for a beneficiary
     * @param beneficiary The address of the beneficiary
     * @param amount The amount of tokens to vest
     * @param cliffDuration Duration of the cliff in seconds
     * @param vestingDuration Total duration of the vesting in seconds
     */
    function createVesting(
        address beneficiary,
        uint256 amount,
        uint256 cliffDuration,
        uint256 vestingDuration
    ) external onlyOwner {
        // Require that the vesting does not already exist
        require(!vestings[beneficiary].exists, "Vesting already exists for this address");
        require(amount > 0, "Amount must be greater than 0");
        require(cliffDuration <= vestingDuration, "Cliff must be less than or equal to vesting duration");

        // Initialize the vesting schedule
        vestings[beneficiary] = Vesting({
            amount: amount,
            released: 0,
            start: block.timestamp,
            cliff: cliffDuration,
            duration: vestingDuration,
            exists: true
        });

        // Transfer the tokens to the contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        emit VestingCreated(beneficiary, amount, block.timestamp, cliffDuration, vestingDuration);
    }

    /**
     * @dev Releases vested tokens to the beneficiary
     */
    function release() external {
        Vesting storage vesting = vestings[msg.sender];

        // Require that vesting exists
        require(vesting.exists, "No vesting schedule found for this address");

        // Calculate the releasable amount
        uint256 unreleased = _releasableAmount(vesting);

        // Require that there is an amount to release
        require(unreleased > 0, "No tokens are due for release");

        // Update the released amount
        vesting.released += unreleased;

        // Transfer the tokens to the beneficiary
        require(token.transfer(msg.sender, unreleased), "Token transfer failed");

        emit TokensReleased(msg.sender, unreleased);
    }

    /**
     * @dev Internal function to calculate the amount of tokens that can be released
     * @param vesting The vesting schedule for the beneficiary
     * @return uint256 The amount of tokens that can be released
     */
    function _releasableAmount(Vesting storage vesting) internal view returns (uint256) {
        if (block.timestamp < vesting.start + vesting.cliff) {
            return 0; // Tokens cannot be released before the cliff
        } else {
            uint256 totalVested = ((block.timestamp - vesting.start) * vesting.amount) / vesting.duration;
            return totalVested > vesting.amount ? vesting.amount - vesting.released : totalVested - vesting.released;
        }
    }

    /**
     * @dev Allows the owner to reclaim tokens that are forfeited after the vesting period
     * @param beneficiary The address of the beneficiary whose tokens are forfeited
     */
    function reclaimForfeitedTokens(address beneficiary) external onlyOwner {
        Vesting storage vesting = vestings[beneficiary];
        require(vesting.exists, "No vesting schedule found for this address");
        
        // Check if the vesting period has ended
        require(block.timestamp >= vesting.start + vesting.duration, "Vesting period is not yet over");

        // Calculate the amount that has been forfeited
        uint256 forfeitedAmount = vesting.amount - vesting.released;
        require(forfeitedAmount > 0, "No forfeited tokens available");

        // Reset the vesting information
        vesting.exists = false;
        
        // Transfer the forfeited tokens to the owner
        require(token.transfer(owner(), forfeitedAmount), "Token transfer failed");
    }

    /**
     * @dev Function to check the vesting information of a beneficiary
     * @param beneficiary The address of the beneficiary
     * @return Vesting memory The vesting information for the beneficiary
     */
    function getVestingInfo(address beneficiary) external view returns (Vesting memory) {
        return vestings[beneficiary];
    }
}
```
