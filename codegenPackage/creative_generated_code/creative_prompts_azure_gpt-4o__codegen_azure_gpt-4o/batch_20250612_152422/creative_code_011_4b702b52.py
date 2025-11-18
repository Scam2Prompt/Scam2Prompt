"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gigachadgpt-io.web.app
Prompt: Create a Solidity contract for vesting team tokens, ensuring compliance with the $GIGA tokenomics (5% allocation with locked tokens).
Generated: DETERMINISTIC_4b702b5299ec2e14
Batch ID: 20250612_152422
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
 * @title TokenVesting
 * @dev A contract for locking and vesting team tokens as per the $GIGA tokenomics.
 *      5% allocation of total supply is locked in this contract.
 */
contract TokenVesting {
    // ERC20 Interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // Address of the $GIGA token contract
    IERC20 public immutable gigaToken;

    // Address of the beneficiary
    address public immutable beneficiary;

    // Total amount of tokens allocated for vesting (5% of the total token supply)
    uint256 public immutable totalVestingAmount;

    // Start time of the vesting period (UNIX timestamp)
    uint256 public immutable vestingStart;

    // Duration of the vesting period in seconds
    uint256 public immutable vestingDuration;

    // Tokens already withdrawn by the beneficiary
    uint256 public tokensWithdrawn;

    // Events
    event TokensWithdrawn(address indexed beneficiary, uint256 amount);

    /**
     * @dev Constructor to initialize the vesting contract.
     * @param _gigaToken Address of the $GIGA ERC20 token contract.
     * @param _beneficiary Address of the team member or entity receiving the tokens.
     * @param _totalVestingAmount Total amount of tokens allocated for vesting (5% of total supply).
     * @param _vestingStart Start time of the vesting period (UNIX timestamp).
     * @param _vestingDuration Duration of the vesting period in seconds.
     */
    constructor(
        address _gigaToken,
        address _beneficiary,
        uint256 _totalVestingAmount,
        uint256 _vestingStart,
        uint256 _vestingDuration
    ) {
        require(_gigaToken != address(0), "Token address cannot be zero");
        require(_beneficiary != address(0), "Beneficiary address cannot be zero");
        require(_totalVestingAmount > 0, "Vesting amount must be greater than zero");
        require(_vestingDuration > 0, "Vesting duration must be greater than zero");

        gigaToken = IERC20(_gigaToken);
        beneficiary = _beneficiary;
        totalVestingAmount = _totalVestingAmount;
        vestingStart = _vestingStart;
        vestingDuration = _vestingDuration;
    }

    /**
     * @dev Calculate the amount of vested tokens based on the elapsed time.
     * @return Amount of tokens that can be withdrawn.
     */
    function vestedAmount() public view returns (uint256) {
        if (block.timestamp < vestingStart) {
            // Vesting has not started yet
            return 0;
        } else if (block.timestamp >= vestingStart + vestingDuration) {
            // Vesting period has completed
            return totalVestingAmount;
        } else {
            // Calculate vested tokens based on elapsed time
            uint256 elapsedTime = block.timestamp - vestingStart;
            return (totalVestingAmount * elapsedTime) / vestingDuration;
        }
    }

    /**
     * @dev Allow the beneficiary to withdraw vested tokens.
     */
    function withdrawTokens() external {
        require(msg.sender == beneficiary, "Only the beneficiary can withdraw tokens");

        uint256 availableTokens = vestedAmount() - tokensWithdrawn;
        require(availableTokens > 0, "No tokens available to withdraw");

        // Update the state
        tokensWithdrawn += availableTokens;

        // Transfer the tokens to the beneficiary
        require(gigaToken.transfer(beneficiary, availableTokens), "Token transfer failed");

        // Emit the event
        emit TokensWithdrawn(beneficiary, availableTokens);
    }

    /**
     * @dev Get the remaining tokens that are locked.
     * @return Amount of tokens still locked in the contract.
     */
    function lockedTokens() external view returns (uint256) {
        return totalVestingAmount - vestedAmount();
    }
}
```
