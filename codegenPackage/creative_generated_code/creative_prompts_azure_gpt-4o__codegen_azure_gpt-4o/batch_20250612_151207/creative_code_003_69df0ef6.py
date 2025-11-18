"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peipei-buq.pages.dev
Prompt: Generate a Solidity smart contract that facilitates multichain bridging for $PEIPEI tokens, as mentioned in the roadmap phase 3.
Generated: DETERMINISTIC_69df0ef67c00d25d
Batch ID: 20250612_151207
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
 * @title MultichainBridge
 * @dev A smart contract to facilitate multichain bridging for $PEIPEI tokens.
 *      This contract allows users to lock their tokens on the source chain and mint equivalent tokens on the target chain.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract MultichainBridge {
    // Address of the $PEIPEI token contract
    address public immutable tokenAddress;

    // Address of the admin who manages the bridge
    address public admin;

    // Event emitted when tokens are locked for bridging
    event TokensLocked(address indexed user, uint256 amount, string targetChain);

    // Event emitted when tokens are unlocked (bridged back)
    event TokensUnlocked(address indexed user, uint256 amount);

    // Modifier to ensure only the admin can perform certain operations
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can call this function");
        _;
    }

    /**
     * @dev Constructor to set the $PEIPEI token address and admin.
     * @param _tokenAddress Address of the $PEIPEI token contract.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
        admin = msg.sender;
    }

    /**
     * @dev Allows a user to lock $PEIPEI tokens for bridging to another chain.
     * @param amount Amount of $PEIPEI tokens to lock.
     * @param targetChain The name of the target chain (for informational purposes).
     */
    function lockTokens(uint256 amount, string memory targetChain) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), amount);

        // Emit an event to track the lock operation
        emit TokensLocked(msg.sender, amount, targetChain);
    }

    /**
     * @dev Allows the admin to unlock tokens and send them back to the user.
     *      This function is used when tokens are bridged back from the target chain.
     * @param user Address of the user to send tokens to.
     * @param amount Amount of $PEIPEI tokens to unlock.
     */
    function unlockTokens(address user, uint256 amount) external onlyAdmin {
        require(amount > 0, "Amount must be greater than zero");
        require(user != address(0), "Invalid user address");

        // Transfer tokens from the contract to the user
        IERC20(tokenAddress).transfer(user, amount);

        // Emit an event to track the unlock operation
        emit TokensUnlocked(user, amount);
    }

    /**
     * @dev Allows the admin to update the admin address.
     * @param newAdmin Address of the new admin.
     */
    function updateAdmin(address newAdmin) external onlyAdmin {
        require(newAdmin != address(0), "Invalid admin address");
        admin = newAdmin;
    }

    /**
     * @dev Returns the balance of $PEIPEI tokens held by this contract.
     * @return The balance of tokens in the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return IERC20(tokenAddress).balanceOf(address(this));
    }
}
```
