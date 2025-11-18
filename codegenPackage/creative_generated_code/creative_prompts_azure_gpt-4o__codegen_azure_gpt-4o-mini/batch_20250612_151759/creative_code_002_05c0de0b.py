"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimehere.pages.dev
Prompt: Create a Solidity smart contract that integrates with the Verse Burn Engine to automate the burning of VERSE tokens.
Generated: DETERMINISTIC_05c0de0bf06f4d6b
Batch ID: 20250612_151759
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

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Interface for the Verse Burn Engine
interface IVerseBurnEngine {
    function burn(uint256 amount) external;
}

/**
 * @title VerseTokenBurner
 * @dev This contract allows users to burn VERSE tokens via the Verse Burn Engine.
 */
contract VerseTokenBurner {
    IERC20 public verseToken; // Instance of the VERSE token contract
    IVerseBurnEngine public burnEngine; // Instance of the Verse Burn Engine

    // Event emitted when tokens are burned
    event TokensBurned(address indexed user, uint256 amount);

    /**
     * @dev Sets the addresses for VERSE token and the Verse Burn Engine.
     * @param _verseToken Address of the VERSE token contract.
     * @param _burnEngine Address of the Verse Burn Engine contract.
     */
    constructor(address _verseToken, address _burnEngine) {
        require(_verseToken != address(0), "Invalid VERSE token address");
        require(_burnEngine != address(0), "Invalid Burn Engine address");
        
        verseToken = IERC20(_verseToken);
        burnEngine = IVerseBurnEngine(_burnEngine);
    }

    /**
     * @dev Allows users to burn a specified amount of VERSE tokens.
     * @param amount The amount of VERSE tokens to burn.
     */
    function burnTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(verseToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to this contract
        bool transferSuccess = verseToken.transferFrom(msg.sender, address(this), amount);
        require(transferSuccess, "Token transfer failed");

        // Approve the Burn Engine to burn the tokens
        bool approveSuccess = verseToken.approve(address(burnEngine), amount);
        require(approveSuccess, "Token approval failed");

        // Burn the tokens using the Verse Burn Engine
        burnEngine.burn(amount);

        // Emit event for tokens burned
        emit TokensBurned(msg.sender, amount);
    }
}
```
