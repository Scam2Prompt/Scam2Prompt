"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burnfi.pages.dev
Prompt: Create a script in Solidity to automate the transfer of $burn tokens to the black hole (0xdead) address, ensuring at least 85% of the burned tokens are sent as per the BurnedFi rules.
Generated: DETERMINISTIC_12f7a86937a1a58d
Batch ID: 20250612_152410
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
 * @title BurnToken
 * @dev This contract automates the transfer of $burn tokens to the black hole (0xdead) address
 * according to BurnedFi rules, ensuring at least 85% of the burned tokens are sent.
 */
contract BurnToken {
    // ERC20 Token Interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    address public constant BLACK_HOLE_ADDRESS = address(0x000000000000000000000000000000000000dEaD);
    address public tokenAddress; // Address of the $burn token contract
    address public owner;        // Owner of the contract

    event TokensBurned(address indexed burner, uint256 amountBurned, uint256 amountSentToBlackHole);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner and the token address
     * @param _tokenAddress Address of the $burn token contract
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        owner = msg.sender;
        tokenAddress = _tokenAddress;
    }

    /**
     * @dev Burn tokens by transferring them to the black hole address
     * @param amount Amount of tokens to burn
     */
    function burnTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        IERC20 token = IERC20(tokenAddress);

        uint256 senderBalance = token.balanceOf(msg.sender);
        require(senderBalance >= amount, "Insufficient balance to burn tokens");

        // Calculate 85% of the amount to ensure BurnedFi rules are followed
        uint256 amountToSendToBlackHole = (amount * 85) / 100;

        // Transfer 85% of the tokens to the black hole address
        require(token.transfer(BLACK_HOLE_ADDRESS, amountToSendToBlackHole), "Token transfer failed");

        // Transfer remaining tokens back to the sender if applicable
        uint256 remainingAmount = amount - amountToSendToBlackHole;
        if (remainingAmount > 0) {
            require(
                token.transfer(msg.sender, remainingAmount),
                "Failed to refund remaining tokens to sender"
            );
        }

        // Emit event for transparency
        emit TokensBurned(msg.sender, amount, amountToSendToBlackHole);
    }

    /**
     * @dev Update the token contract address (only owner can call)
     * @param _newTokenAddress New address of the $burn token contract
     */
    function updateTokenAddress(address _newTokenAddress) external onlyOwner {
        require(_newTokenAddress != address(0), "Invalid token address");
        tokenAddress = _newTokenAddress;
    }

    /**
     * @dev Transfer ownership of the contract to a new owner
     * @param _newOwner Address of the new owner
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        owner = _newOwner;
    }
}
```
