"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mammoth-cxk.pages.dev
Prompt: Develop a smart contract snippet that integrates with the MammothAI token ($MAMAI) to support conservation donations directly from users' wallets.
Generated: DETERMINISTIC_1a708396ce20d43b
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

/**
 * @title ConservationDonation
 * @dev A smart contract to facilitate donations in $MAMAI tokens for conservation efforts.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract ConservationDonation {
    // Address of the $MAMAI token contract
    address public immutable mamaiToken;

    // Address where donations are sent (e.g., conservation fund wallet)
    address public immutable conservationWallet;

    // Event emitted when a donation is made
    event DonationMade(address indexed donor, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with token and conservation wallet addresses.
     * @param _mamaiToken Address of the $MAMAI token contract.
     * @param _conservationWallet Address of the conservation fund wallet.
     */
    constructor(address _mamaiToken, address _conservationWallet) {
        require(_mamaiToken != address(0), "Invalid token address");
        require(_conservationWallet != address(0), "Invalid wallet address");

        mamaiToken = _mamaiToken;
        conservationWallet = _conservationWallet;
    }

    /**
     * @dev Allows a user to donate $MAMAI tokens directly from their wallet.
     * @param amount Amount of $MAMAI tokens to donate.
     *
     * Requirements:
     * - `amount` must be greater than zero.
     * - The user must have approved this contract to spend their $MAMAI tokens beforehand.
     */
    function donate(uint256 amount) external {
        require(amount > 0, "Donation amount must be greater than zero");

        // Check donor's balance
        uint256 donorBalance = IERC20(mamaiToken).balanceOf(msg.sender);
        require(donorBalance >= amount, "Insufficient token balance");

        // Transfer tokens from donor to conservation wallet
        bool success = IERC20(mamaiToken).transferFrom(msg.sender, conservationWallet, amount);
        require(success, "Token transfer failed");

        emit DonationMade(msg.sender, amount);
    }
}
```
