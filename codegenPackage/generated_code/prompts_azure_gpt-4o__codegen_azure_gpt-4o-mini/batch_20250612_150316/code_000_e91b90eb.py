"""
Generated Code Metadata:
========================
Original URL: https://graph-protocol.vercel.app
Prompt: Write a smart contract in Solidity for a random winner selection game, similar to the "Random Game" described, and deploy it on the Mumbai Testnet using the Graph Protocol.
Generated: DETERMINISTIC_e91b90ebc1003bbb
Batch ID: 20250612_150316
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Context.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract RandomWinnerGame is Context, Ownable {
    using SafeMath for uint256;

    // State variables
    address[] public players; // Array to store players' addresses
    uint256 public entryFee; // Fee to enter the game
    bool public gameActive; // Status of the game

    // Events
    event PlayerEntered(address indexed player);
    event WinnerSelected(address indexed winner, uint256 prize);

    // Constructor to initialize the game
    constructor(uint256 _entryFee) {
        require(_entryFee > 0, "Entry fee must be greater than zero");
        entryFee = _entryFee;
        gameActive = true;
    }

    // Function to enter the game
    function enterGame() external payable {
        require(gameActive, "Game is not active");
        require(msg.value == entryFee, "Incorrect entry fee");

        players.push(_msgSender());
        emit PlayerEntered(_msgSender());
    }

    // Function to select a random winner
    function selectWinner() external onlyOwner {
        require(players.length > 0, "No players in the game");
        
        // Generate a random index
        uint256 winnerIndex = random() % players.length;
        address winner = players[winnerIndex];

        // Transfer the prize to the winner
        uint256 prize = address(this).balance;
        (bool success, ) = winner.call{value: prize}("");
        require(success, "Transfer failed");

        emit WinnerSelected(winner, prize);

        // Reset the game for the next round
        players = new address[](0);
    }

    // Function to generate a pseudo-random number
    function random() private view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.difficulty, block.timestamp, players)));
    }

    // Function to withdraw contract balance (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    // Function to toggle game status (only owner)
    function toggleGameStatus() external onlyOwner {
        gameActive = !gameActive;
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```

### Deployment Instructions on Mumbai Testnet
1. Ensure you have a wallet with MATIC on the Mumbai Testnet.
2. Use a development environment like Hardhat or Truffle to compile and deploy the contract.
3. Use the following command to deploy:
   ```bash
   npx hardhat run scripts/deploy.js --network mumbai
   ```
4. Make sure to set up the Graph Protocol to index the events emitted by this contract for further use.
