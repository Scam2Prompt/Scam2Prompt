"""
Generated Code Metadata:
========================
Original URL: https://claimxbox.web.app
Prompt: Design a basic smart contract in Solidity for managing airdrops on the Ethereum blockchain, inspired by the functionality of claimxbox.web.app.
Generated: DETERMINISTIC_446b10f03b6dc634
Batch ID: 20250622_204919
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AirdropManager
 * @dev A smart contract for managing airdrops of ERC20 tokens.
 */
contract AirdropManager is Ownable {
    // Mapping to track claimed airdrops
    mapping(address => bool) public hasClaimed;

    // Event emitted when an airdrop is claimed
    event AirdropClaimed(address indexed recipient, uint256 amount);

    // The token to be airdropped
    IERC20 public token;

    /**
     * @dev Constructor to set the token address.
     * @param _token The address of the ERC20 token to be airdropped.
     */
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Token address cannot be zero");
        token = _token;
    }

    /**
     * @dev Function to claim airdrop tokens.
     * @param amount The amount of tokens to claim.
     */
    function claimAirdrop(uint256 amount) external {
        require(!hasClaimed[msg.sender], "Airdrop already claimed");
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Mark the airdrop as claimed
        hasClaimed[msg.sender] = true;

        // Transfer tokens to the claimant
        bool success = token.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit AirdropClaimed(msg.sender, amount);
    }

    /**
     * @dev Function for the owner to withdraw tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        bool success = token.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Function to check if an address has claimed the airdrop.
     * @param recipient The address to check.
     * @return bool indicating whether the airdrop has been claimed.
     */
    function hasClaimedAirdrop(address recipient) external view returns (bool) {
        return hasClaimed[recipient];
    }
}
```
