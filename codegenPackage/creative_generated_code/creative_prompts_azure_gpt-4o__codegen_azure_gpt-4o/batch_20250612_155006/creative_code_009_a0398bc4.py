"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lotto.exchange
Prompt: Write a smart contract in Solidity to integrate a lottery system with Uniswap, similar to Lotto Exchange.
Generated: DETERMINISTIC_a0398bc4a0686853
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

// Importing OpenZeppelin libraries for safe math and token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

/**
 * @title LotteryWithUniswap
 * @dev A smart contract for a lottery system that integrates with Uniswap.
 */
contract LotteryWithUniswap is Ownable, ReentrancyGuard {
    // Declare variables
    address public immutable uniswapRouter; // Address of the Uniswap Router
    address public immutable lotteryToken; // ERC20 token used for lottery
    uint256 public ticketPrice; // Price of a single lottery ticket
    uint256 public lotteryPool; // Total pool for the lottery
    address[] public participants; // List of participants

    event TicketPurchased(address indexed buyer, uint256 amount);
    event LotteryWon(address indexed winner, uint256 prize);
    event FundsSwapped(address indexed tokenOut, uint256 amountOut);

    /**
     * @dev Constructor to initialize the contract.
     * @param _uniswapRouter Address of the Uniswap Router.
     * @param _lotteryToken Address of the ERC20 token used for lottery tickets.
     * @param _ticketPrice Price of a single lottery ticket in tokens.
     */
    constructor(address _uniswapRouter, address _lotteryToken, uint256 _ticketPrice) {
        require(_uniswapRouter != address(0), "Invalid Uniswap router address");
        require(_lotteryToken != address(0), "Invalid token address");
        require(_ticketPrice > 0, "Ticket price must be greater than zero");

        uniswapRouter = _uniswapRouter;
        lotteryToken = _lotteryToken;
        ticketPrice = _ticketPrice;
    }

    /**
     * @dev Purchase lottery tickets.
     * Users must approve the contract to spend their tokens before calling this function.
     * @param _amount Number of tickets to purchase.
     */
    function purchaseTickets(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");

        uint256 totalCost = ticketPrice * _amount;

        // Transfer lottery tokens from the participant to the contract
        IERC20(lotteryToken).transferFrom(msg.sender, address(this), totalCost);

        // Update lottery pool and participants
        lotteryPool += totalCost;
        for (uint256 i = 0; i < _amount; i++) {
            participants.push(msg.sender);
        }

        emit TicketPurchased(msg.sender, _amount);
    }

    /**
     * @dev Pick a random winner and distribute the lottery pool.
     * Only callable by the contract owner.
     */
    function pickWinner() external onlyOwner nonReentrant {
        require(participants.length > 0, "No participants in the lottery");

        // Generate a random index
        uint256 randomIndex = _random() % participants.length;

        // Determine the winner
        address winner = participants[randomIndex];

        // Transfer the lottery pool to the winner
        uint256 prize = lotteryPool;
        lotteryPool = 0;
        participants = new address[](0); // Reset participants
        IERC20(lotteryToken).transfer(winner, prize);

        emit LotteryWon(winner, prize);
    }

    /**
     * @dev Swap lottery tokens for another token using Uniswap.
     * @param _tokenOut Address of the token to swap to.
     * @param _amountOutMin Minimum amount of tokens to receive.
     */
    function swapTokens(address _tokenOut, uint256 _amountOutMin) external onlyOwner nonReentrant {
        require(_tokenOut != address(0), "Invalid output token");
        require(lotteryPool > 0, "Insufficient lottery pool");

        IERC20(lotteryToken).approve(uniswapRouter, lotteryPool);

        address[] memory path = new address[](2);
        path[0] = lotteryToken;
        path[1] = _tokenOut;

        uint256[] memory amounts = IUniswapV2Router02(uniswapRouter).swapExactTokensForTokens(
            lotteryPool,
            _amountOutMin,
            path,
            address(this),
            block.timestamp
        );

        emit FundsSwapped(_tokenOut, amounts[1]);
    }

    /**
     * @dev Generate a pseudo-random number.
     * @return Random number.
     */
    function _random() private view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, participants)));
    }

    /**
     * @dev Update the ticket price.
     * @param _newTicketPrice New price for a single lottery ticket.
     */
    function updateTicketPrice(uint256 _newTicketPrice) external onlyOwner {
        require(_newTicketPrice > 0, "Ticket price must be greater than zero");
        ticketPrice = _newTicketPrice;
    }

    /**
     * @dev Emergency function to withdraw tokens from the contract.
     * @param _token Address of the token to withdraw.
     * @param _amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(address _token, uint256 _amount) external onlyOwner {
        IERC20(_token).transfer(owner(), _amount);
    }
}
```
