"""
Generated Code Metadata:
========================
Original URL: https://de-agent.com
Prompt: Write a smart contract in Solidity that manages a prize pool for a guessing game, inspired by the 16,000,000+ prize pool mentioned on de-agent.com.
Generated: DETERMINISTIC_619398dcbbda3435
Batch ID: 20250612_155153
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
 * @title PrizePoolGuessingGame
 * @dev A smart contract to manage a prize pool for a guessing game.
 * Players can participate by guessing a number, and the winner takes the prize pool.
 */
contract PrizePoolGuessingGame {
    // Owner of the contract
    address public owner;

    // Prize pool balance
    uint256 public prizePool;

    // The secret number to guess
    uint256 private secretNumber;

    // Minimum participation fee
    uint256 public constant participationFee = 0.01 ether;

    // Event emitted when a player wins
    event WinnerDeclared(address indexed winner, uint256 prizeAmount);

    // Event emitted when the prize pool is updated
    event PrizePoolUpdated(uint256 newPrizePool);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _secretNumber The secret number to guess (set by the owner).
     */
    constructor(uint256 _secretNumber) {
        require(_secretNumber > 0, "Secret number must be greater than zero");
        owner = msg.sender;
        secretNumber = _secretNumber;
    }

    /**
     * @dev Allows players to participate in the guessing game.
     * @param _guess The number guessed by the player.
     */
    function guess(uint256 _guess) external payable {
        // Ensure the player has paid the participation fee
        require(msg.value == participationFee, "Incorrect participation fee");

        // Add the participation fee to the prize pool
        prizePool += msg.value;
        emit PrizePoolUpdated(prizePool);

        // Check if the guess is correct
        if (_guess == secretNumber) {
            // Transfer the prize pool to the winner
            uint256 prizeAmount = prizePool;
            prizePool = 0; // Reset the prize pool
            emit PrizePoolUpdated(prizePool);
            emit WinnerDeclared(msg.sender, prizeAmount);
            payable(msg.sender).transfer(prizeAmount);
        }
    }

    /**
     * @dev Allows the owner to update the secret number.
     * @param _newSecretNumber The new secret number to set.
     */
    function updateSecretNumber(uint256 _newSecretNumber) external onlyOwner {
        require(_newSecretNumber > 0, "Secret number must be greater than zero");
        secretNumber = _newSecretNumber;
    }

    /**
     * @dev Allows the owner to withdraw any remaining funds in the contract.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```
