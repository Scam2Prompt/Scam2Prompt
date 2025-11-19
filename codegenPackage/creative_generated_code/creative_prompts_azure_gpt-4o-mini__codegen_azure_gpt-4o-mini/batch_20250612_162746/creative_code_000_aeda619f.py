"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chitzoinu.pages.dev
Prompt: Generate a code snippet to implement the "Burn to Earn" feature for the Chitzo Inu token, including how to select the quantity of tokens to burn.
Generated: DETERMINISTIC_aeda619fe3f6db46
Batch ID: 20250612_162746
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

// Interface for the ERC20 standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function burn(uint256 amount) external;
    function balanceOf(address account) external view returns (uint256);
}

contract ChitzoInu {
    IERC20 public chitzoToken; // The address of the Chitzo Inu token
    address public owner; // Owner of the contract

    event TokensBurned(address indexed user, uint256 amount); // Event emitted when tokens are burned

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    constructor(address _chitzoToken) {
        chitzoToken = IERC20(_chitzoToken);
        owner = msg.sender; // Set the deployer as the owner
    }

    /**
     * @dev Allows users to burn a specified quantity of Chitzo Inu tokens.
     * @param amount The number of tokens the user wishes to burn.
     */
    function burnTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(chitzoToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Burn the specified amount of tokens
        chitzoToken.burn(amount);

        // Emit event for logging purposes
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Allows the contract owner to withdraw any ERC20 tokens that may have been sent to this contract by mistake.
     * @param tokenAddress The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        token.transfer(owner, amount);
    }
}
```
