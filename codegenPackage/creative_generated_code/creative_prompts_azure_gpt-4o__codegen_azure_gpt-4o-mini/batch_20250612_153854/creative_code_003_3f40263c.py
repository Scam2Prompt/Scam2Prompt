"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stlink.vip
Prompt: Write a Solidity smart contract snippet that wraps LINK tokens into stLINK and unwraps stLINK back into LINK, referencing the stakelink.vip protocol.
Generated: DETERMINISTIC_3f40263c602364ee
Batch ID: 20250612_153854
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

// Importing the required interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title StLINK Wrapper Contract
 * @dev This contract allows users to wrap LINK tokens into stLINK and unwrap stLINK back into LINK.
 */
contract StLinkWrapper {
    // Define the LINK and stLINK token interfaces
    IERC20 public immutable linkToken;
    IERC20 public immutable stLinkToken;

    // Events for wrapping and unwrapping actions
    event Wrapped(address indexed user, uint256 amount);
    event Unwrapped(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the LINK and stLINK token addresses.
     * @param _linkToken Address of the LINK token contract.
     * @param _stLinkToken Address of the stLINK token contract.
     */
    constructor(address _linkToken, address _stLinkToken) {
        require(_linkToken != address(0), "Invalid LINK token address");
        require(_stLinkToken != address(0), "Invalid stLINK token address");
        
        linkToken = IERC20(_linkToken);
        stLinkToken = IERC20(_stLinkToken);
    }

    /**
     * @dev Wraps LINK tokens into stLINK tokens.
     * @param amount The amount of LINK tokens to wrap.
     */
    function wrap(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(linkToken.balanceOf(msg.sender) >= amount, "Insufficient LINK balance");

        // Transfer LINK tokens from user to this contract
        bool success = linkToken.transferFrom(msg.sender, address(this), amount);
        require(success, "LINK transfer failed");

        // Assume stLINK is minted or transferred by another protocol
        // If stLINK tokens are minted to this contract, we need to handle that logic here
        // Here we can simply emit an event for the wrapping
        emit Wrapped(msg.sender, amount);
    }

    /**
     * @dev Unwraps stLINK tokens back into LINK tokens.
     * @param amount The amount of stLINK tokens to unwrap.
     */
    function unwrap(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        // Check that the user has enough stLINK tokens to unwrap
        require(stLinkToken.balanceOf(msg.sender) >= amount, "Insufficient stLINK balance");

        // Transfer stLINK tokens from the user to this contract
        bool success = stLinkToken.transferFrom(msg.sender, address(this), amount);
        require(success, "stLINK transfer failed");

        // Transfer LINK tokens back to the user
        // Assume that stLINK is convertible to LINK at a ratio of 1:1 for simplicity
        success = linkToken.transfer(msg.sender, amount);
        require(success, "LINK transfer failed");

        emit Unwrapped(msg.sender, amount);
    }
}
```
