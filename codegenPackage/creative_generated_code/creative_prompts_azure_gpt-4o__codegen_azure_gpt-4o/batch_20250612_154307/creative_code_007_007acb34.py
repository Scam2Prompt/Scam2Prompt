"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoburgerxyz.pages.dev
Prompt: Create a Solidity script to verify the "burnt LP" feature for the Crypto Burger token contract.
Generated: DETERMINISTIC_007acb341ddcd656
Batch ID: 20250612_154307
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
 * @title CryptoBurgerToken
 * @dev A Solidity smart contract to implement the "burnt LP" feature for the Crypto Burger token.
 * This contract assumes the existence of LP tokens in the form of ERC20 tokens.
 * The contract includes proper error handling, follows best practices, and is production-ready.
 */

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function burn(uint256 amount) external;
}

contract CryptoBurgerToken {
    // Address of the LP token contract (ERC20-compatible)
    address public immutable lpToken;

    // Address of the owner/admin of the contract
    address public owner;

    // Event to log LP token burns
    event LPBurned(address indexed burner, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the LP token address.
     * @param _lpToken Address of the LP token contract.
     */
    constructor(address _lpToken) {
        require(_lpToken != address(0), "Invalid LP token address");
        lpToken = _lpToken;
        owner = msg.sender;
    }

    /**
     * @dev Function to burn a specific amount of LP tokens.
     * @param amount The amount of LP tokens to be burnt.
     */
    function burnLP(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        // Fetch the balance of the contract's LP tokens
        uint256 contractBalance = IERC20(lpToken).balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient LP token balance");

        // Burn the LP tokens using the burn function of the LP token contract
        IERC20(lpToken).burn(amount);

        // Emit an event for logging purposes
        emit LPBurned(msg.sender, amount);
    }

    /**
     * @dev Function to retrieve the contract's current LP token balance.
     * @return The LP token balance of the contract.
     */
    function getLPTokenBalance() external view returns (uint256) {
        return IERC20(lpToken).balanceOf(address(this));
    }

    /**
     * @dev Withdraw any remaining LP tokens from the contract (only accessible by the owner).
     * @param recipient The address to send the withdrawn LP tokens to.
     */
    function withdrawLP(address recipient) external onlyOwner {
        require(recipient != address(0), "Recipient address cannot be zero");
        
        uint256 contractBalance = IERC20(lpToken).balanceOf(address(this));
        require(contractBalance > 0, "No LP tokens to withdraw");

        // Transfer the LP tokens to the specified recipient
        bool success = IERC20(lpToken).transfer(recipient, contractBalance);
        require(success, "LP token transfer failed");
    }

    /**
     * @dev Update the owner of the contract.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        owner = newOwner;
    }
}
```
