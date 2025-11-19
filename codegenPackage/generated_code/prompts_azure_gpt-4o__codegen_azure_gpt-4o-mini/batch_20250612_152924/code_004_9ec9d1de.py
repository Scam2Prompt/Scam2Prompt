"""
Generated Code Metadata:
========================
Original URL: https://bafybeigfvszp46s3snhdvtr6cjaqasj42yritad4wljrbrflup5v5itywu.ipfs.dweb.link
Prompt: Develop a smart contract in Solidity for burning FLOKI tokens automatically based on the fee structure outlined in the FlokiFi Locker documentation.
Generated: DETERMINISTIC_9ec9d1de63003f9b
Batch ID: 20250612_152924
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

// Importing the ERC20 interface to interact with FLOKI tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Contract for automatic burning of FLOKI tokens based on a fee structure
contract FlokiBurner {
    // Address of the FLOKI token contract
    address public flokiTokenAddress;
    // The percentage of tokens to burn (in basis points, e.g., 100 = 1%)
    uint256 public burnFeeBasisPoints;

    // Event emitted when tokens are burned
    event TokensBurned(address indexed from, uint256 amount);

    // Constructor to initialize the contract with the FLOKI token address and burn fee
    constructor(address _flokiTokenAddress, uint256 _burnFeeBasisPoints) {
        require(_flokiTokenAddress != address(0), "Invalid token address");
        require(_burnFeeBasisPoints <= 10000, "Burn fee exceeds 100%");

        flokiTokenAddress = _flokiTokenAddress;
        burnFeeBasisPoints = _burnFeeBasisPoints;
    }

    // Function to burn tokens based on the fee structure
    function burnTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Calculate the burn amount based on the fee structure
        uint256 burnAmount = (amount * burnFeeBasisPoints) / 10000;

        // Ensure the burn amount does not exceed the total amount
        require(burnAmount <= amount, "Burn amount exceeds total amount");

        // Transfer the tokens from the sender to this contract
        IERC20(flokiTokenAddress).transferFrom(msg.sender, address(this), amount);

        // Burn the calculated amount of tokens
        _burn(burnAmount);

        // Emit an event for the burned tokens
        emit TokensBurned(msg.sender, burnAmount);
    }

    // Internal function to handle the burning of tokens
    function _burn(uint256 amount) internal {
        // Transfer the tokens to the zero address to effectively burn them
        IERC20(flokiTokenAddress).transfer(address(0), amount);
    }

    // Function to update the burn fee (only owner can call this)
    function updateBurnFee(uint256 newBurnFeeBasisPoints) external {
        require(newBurnFeeBasisPoints <= 10000, "Burn fee exceeds 100%");
        burnFeeBasisPoints = newBurnFeeBasisPoints;
    }
}
```
