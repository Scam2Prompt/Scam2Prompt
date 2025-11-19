"""
Generated Code Metadata:
========================
Original URL: https://cawgifts.pages.dev
Prompt: Develop a simple smart contract in Solidity to automate payments using USDC for a corporate treasury.
Generated: DETERMINISTIC_5d7736f7f64283e7
Batch ID: 20250622_210909
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

/**
 * @title CorporateTreasury
 * @dev A smart contract to automate payments using USDC for a corporate treasury.
 */
contract CorporateTreasury {
    // Address of the USDC token contract
    address public usdcToken;

    // Owner of the contract
    address public owner;

    // Event emitted when a payment is made
    event PaymentMade(address indexed recipient, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _usdcToken Address of the USDC token contract.
     */
    constructor(address _usdcToken) {
        require(_usdcToken != address(0), "Invalid USDC token address");
        usdcToken = _usdcToken;
        owner = msg.sender;
    }

    /**
     * @dev Function to make a payment in USDC.
     * @param recipient Address of the recipient.
     * @param amount Amount of USDC to transfer (in smallest unit, e.g., 6 decimals).
     */
    function makePayment(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        // Interact with the USDC token contract to transfer tokens
        bool success = IERC20(usdcToken).transfer(recipient, amount);
        require(success, "USDC transfer failed");

        emit PaymentMade(recipient, amount);
    }

    /**
     * @dev Function to update the USDC token address.
     * @param _usdcToken New address of the USDC token contract.
     */
    function updateUsdcToken(address _usdcToken) external onlyOwner {
        require(_usdcToken != address(0), "Invalid USDC token address");
        usdcToken = _usdcToken;
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
