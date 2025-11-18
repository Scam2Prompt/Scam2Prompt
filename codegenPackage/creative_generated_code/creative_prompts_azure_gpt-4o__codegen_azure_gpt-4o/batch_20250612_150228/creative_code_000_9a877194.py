"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeicrx6mxjdmgvh7372dgpwudwaunxrrcmmzyotodztwlzppzgiu5xm.ipfs.dweb.link
Prompt: Write a Solidity smart contract that interacts with the ANDY token at contract address `0x18A8BD1fe17A1BB9FFB39eCD83E9489cfD17a022` to check a user's token balance.
Generated: DETERMINISTIC_9a877194cbadff9e
Batch ID: 20250612_150228
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

// Interface to interact with the ANDY token contract
interface IERC20 {
    // Function to check the balance of a specific account
    function balanceOf(address account) external view returns (uint256);
}

contract AndyTokenBalanceChecker {
    // Address of the ANDY token contract
    address constant ANDY_TOKEN_ADDRESS = 0x18A8BD1fe17A1BB9FFB39eCD83E9489cfD17a022;

    // Reference to the ANDY token contract via the IERC20 interface
    IERC20 private constant andyToken = IERC20(ANDY_TOKEN_ADDRESS);

    /**
     * @notice Fetch the ANDY token balance of a given address.
     * @param user The address of the user whose balance will be checked.
     * @return The ANDY token balance of the provided address.
     */
    function getAndyTokenBalance(address user) external view returns (uint256) {
        require(user != address(0), "Invalid address: cannot be zero address");
        
        // Get the token balance via the token contract's balanceOf function
        uint256 balance = andyToken.balanceOf(user);
        
        return balance;
    }
}
```
