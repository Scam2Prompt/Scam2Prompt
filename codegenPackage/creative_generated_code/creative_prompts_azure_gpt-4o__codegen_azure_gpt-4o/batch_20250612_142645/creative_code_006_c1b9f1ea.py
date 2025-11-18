"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jellybabiesnft.web.app
Prompt: Create a smart contract function for a token flipping game, similar to the "Jelly Flip" feature mentioned on the Jelly Babies NFT site, where users can wager $Jelly tokens.
Generated: DETERMINISTIC_c1b9f1eac14f869c
Batch ID: 20250612_142645
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
 * @title TokenFlipGame
 * @dev A smart contract for a token flipping game where users can wager $Jelly tokens.
 */
contract TokenFlipGame {
    // Interface for the $Jelly token
    IERC20 public jellyToken;

    // Mapping to store user balances in the contract
    mapping(address => uint256) public userBalances;

    // Event emitted when a wager is made
    event WagerPlaced(address indexed user, uint256 amount, bool won);

    /**
     * @dev Constructor to initialize the $Jelly token address.
     * @param _jellyToken Address of the $Jelly token contract.
     */
    constructor(address _jellyToken) {
        require(_jellyToken != address(0), "Token address cannot be zero.");
        jellyToken = IERC20(_jellyToken);
    }

    /**
     * @dev Allows a user to place a wager and flip a virtual coin.
     *      If the user wins, they double their wager; if they lose, they forfeit their wager.
     * @param amount Amount of $Jelly tokens to wager.
     */
    function flipCoin(uint256 amount) external {
        require(amount > 0, "Wager amount must be greater than zero.");
        require(jellyToken.balanceOf(msg.sender) >= amount, "Insufficient token balance.");
        require(jellyToken.allowance(msg.sender, address(this)) >= amount, "Insufficient token allowance.");

        // Transfer tokens from user to contract
        bool success = jellyToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed.");

        // Simulate a coin flip (pseudo-random outcome)
        bool won = _randomFlip();

        if (won) {
            // User wins: Double the wager and send back to the user
            uint256 reward = amount * 2;
            userBalances[msg.sender] += reward;
            emit WagerPlaced(msg.sender, amount, true);
        } else {
            // User loses: Wager is forfeited
            emit WagerPlaced(msg.sender, amount, false);
        }
    }

    /**
     * @dev Allows users to withdraw their winnings.
     */
    function withdrawWinnings() external {
        uint256 balance = userBalances[msg.sender];
        require(balance > 0, "No winnings to withdraw.");
        
        userBalances[msg.sender] = 0; // Reset balance before transfer to prevent reentrancy
        bool success = jellyToken.transfer(msg.sender, balance);
        require(success, "Token transfer failed.");
    }

    /**
     * @dev Internal function to simulate a coin flip. 
     *      Uses block.timestamp and msg.sender for pseudo-randomness.
     * @return True if the user wins, false otherwise.
     */
    function _randomFlip() internal view returns (bool) {
        return (uint256(keccak256(abi.encodePacked(block.timestamp, msg.sender))) % 2) == 0;
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function allowance(address owner, address spender) external view returns (uint256);
}
```
