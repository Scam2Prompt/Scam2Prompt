"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lotto.exchange
Prompt: How can I implement a lottery mechanism in a decentralized app using the Uniswap interface, similar to Lotto Exchange?
Generated: DETERMINISTIC_ee037ae7cb259593
Batch ID: 20250612_155006
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
 * @title LotteryContract
 * @dev Implements a simple lottery mechanism using a decentralized structure.
 * Users can purchase lottery tickets by sending ETH. At the end of the round, 
 * the winner is chosen randomly using a secure mechanism. The contract interacts 
 * with the Uniswap interface to swap ETH for tokens as part of the prize pool.
 */

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Context.sol";
import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract LotteryContract is Ownable, ReentrancyGuard {
    // Events
    event TicketPurchased(address indexed user, uint256 amount);
    event WinnerChosen(address indexed winner, uint256 prize);
    
    // Uniswap Router
    IUniswapV2Router02 public uniswapRouter;
    address public prizeToken;

    // Lottery variables
    address[] public participants;
    uint256 public ticketPrice;
    uint256 public roundDuration; // in seconds
    uint256 public roundEndTime;
    address public lastWinner;

    // Prize pool
    uint256 public prizePool;

    // Constructor to initialize Uniswap router and lottery settings
    constructor(
        address _uniswapRouter,
        address _prizeToken,
        uint256 _ticketPrice,
        uint256 _roundDuration
    ) {
        require(_uniswapRouter != address(0), "Invalid Uniswap Router address");
        require(_prizeToken != address(0), "Invalid prize token address");
        require(_ticketPrice > 0, "Ticket price must be greater than zero");
        require(_roundDuration > 0, "Round duration must be greater than zero");

        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
        prizeToken = _prizeToken;
        ticketPrice = _ticketPrice;
        roundDuration = _roundDuration;
        roundEndTime = block.timestamp + _roundDuration;
    }

    /**
     * @dev Purchase a lottery ticket by sending ETH.
     * Adds the sender to the participants list.
     */
    function purchaseTicket() external payable nonReentrant {
        require(msg.value == ticketPrice, "Incorrect ticket price");
        require(block.timestamp <= roundEndTime, "Lottery round has ended");

        participants.push(msg.sender);
        prizePool += msg.value;

        emit TicketPurchased(msg.sender, msg.value);
    }

    /**
     * @dev Ends the current lottery round, selects a winner, and starts a new round.
     * Uses the blockhash for randomness (not ideal for production, but illustrative).
     */
    function endRoundAndPickWinner() external onlyOwner nonReentrant {
        require(block.timestamp > roundEndTime, "Round is still ongoing");
        require(participants.length > 0, "No participants");

        // Pick a random winner
        uint256 randomIndex = uint256(
            keccak256(abi.encodePacked(block.timestamp, block.difficulty))
        ) % participants.length;
        lastWinner = participants[randomIndex];

        // Swap ETH prize pool for tokens using Uniswap
        _swapEthForTokens(prizePool, lastWinner);

        emit WinnerChosen(lastWinner, prizePool);

        // Reset lottery state
        participants = new address[](0);
        prizePool = 0;
        roundEndTime = block.timestamp + roundDuration;
    }

    /**
     * @dev Internal function to swap ETH for tokens using the Uniswap router.
     * Sends the swapped tokens to the winner.
     */
    function _swapEthForTokens(uint256 amount, address recipient) internal {
        require(amount > 0, "Prize pool must be greater than zero");
        require(recipient != address(0), "Invalid recipient address");

        // Generate Uniswap swap path: ETH -> Prize Token
        address[] memory path = new address[](2);
        path[0] = uniswapRouter.WETH();
        path[1] = prizeToken;

        // Execute the swap
        uniswapRouter.swapExactETHForTokens{value: amount}(
            0, // Accept any amount of tokens
            path,
            recipient,
            block.timestamp
        );
    }

    /**
     * @dev Withdraw contract balance to owner (for emergency purposes only).
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No balance to withdraw");

        (bool success, ) = owner().call{value: contractBalance}("");
        require(success, "Withdraw failed");
    }

    /**
     * @dev Fallback function to accept ETH directly sent to the contract.
     */
    receive() external payable {
        prizePool += msg.value;
    }
}
```
