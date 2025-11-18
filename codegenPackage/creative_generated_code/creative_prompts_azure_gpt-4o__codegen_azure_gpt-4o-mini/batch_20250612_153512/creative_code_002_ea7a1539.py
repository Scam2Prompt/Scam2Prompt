"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-floki-airdrop.pages.dev
Prompt: Generate code in Solidity to interact with the Floki contract (e.g., `0xcf0c...2b6a2e`) for querying token balances related to the $MONKY airdrop eligibility.
Generated: DETERMINISTIC_ea7a15399a9cc12f
Batch ID: 20250612_153512
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

// Importing the IERC20 interface to interact with ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract AirdropEligibility {
    // Address of the Floki token contract
    address public flokiTokenAddress = 0xcf0c...2b6a2e; // Replace with actual contract address
    IERC20 private flokiToken;

    // Mapping to keep track of addresses that have been checked for eligibility
    mapping(address => bool) public eligibilityChecked;

    // Event to emit when eligibility is checked
    event EligibilityChecked(address indexed user, uint256 balance, bool eligible);

    // Constructor to initialize the Floki token contract instance
    constructor() {
        flokiToken = IERC20(flokiTokenAddress);
    }

    /**
     * @dev Checks the token balance of a specific address for airdrop eligibility.
     * Emits an event with the balance and eligibility status.
     * @param user The address to check eligibility for.
     */
    function checkEligibility(address user) external {
        require(user != address(0), "Invalid address");

        // Query the token balance
        uint256 balance = flokiToken.balanceOf(user);

        // Determine eligibility based on the balance (example criteria: > 100 tokens)
        bool isEligible = balance > 100 * 10 ** 18;

        // Mark the address as checked
        eligibilityChecked[user] = true;

        // Emit the eligibility checked event
        emit EligibilityChecked(user, balance, isEligible);
    }

    /**
     * @dev Returns the Floki token balance of a user.
     * @param user The address of the user to query.
     * @return balance The token balance of the user.
     */
    function getFlokiBalance(address user) external view returns (uint256) {
        require(user != address(0), "Invalid address");
        return flokiToken.balanceOf(user);
    }
}
```
