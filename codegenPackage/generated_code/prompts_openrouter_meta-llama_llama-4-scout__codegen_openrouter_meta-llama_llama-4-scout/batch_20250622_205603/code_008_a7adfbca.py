"""
Generated Code Metadata:
========================
Original URL: https://v2-pancake.pages.dev
Prompt: "Translate the PancakeSwap lottery rules into a set of smart contract functions using Solidity."
Generated: DETERMINISTIC_a7adfbca1530c13c
Batch ID: 20250622_205603
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PancakeSwap Lottery Contract
 * @author [Your Name]
 * @notice This contract manages the PancakeSwap lottery functionality
 */
contract PancakeSwapLottery is Ownable {
    using SafeMath for uint256;

    // Constants
    uint256 public constant TICKET_PRICE = 1 ether;
    uint256 public constant MAX_TICKETS_PER_USER = 10;
    uint256 public constant LOTTERY_DRAW_INTERVAL = 30 minutes;
    uint256 public constant GRAND_PRIZE_POOL_PERCENTAGE = 50;
    uint256 public constant SMALL_PRIZE_POOL_PERCENTAGE = 30;
    uint256 public constant MEDIUM_PRIZE_POOL_PERCENTAGE = 20;

    // State variables
    address public ticketToken; // Token used to purchase tickets
    uint256 public lotteryId;
    uint256 public ticketSales; // Total ticket sales
    uint256 public grandPrizePool;
    uint256 public smallPrizePool;
    uint256 public mediumPrizePool;
    mapping(address => uint256) public userTickets; // Mapping of user to ticket count
    mapping(uint256 => address) public ticketHolders; // Mapping of ticket ID to holder

    // Events
    event LotteryDrawn(uint256 indexed lotteryId, address[] winners);
    event TicketsPurchased(address indexed buyer, uint256 amount);
    event LotteryStarted(uint256 indexed lotteryId);

    /**
     * @notice Initializes the contract
     * @param _ticketToken Token used to purchase tickets
     */
    constructor(address _ticketToken) {
        require(_ticketToken != address(0), "Invalid token address");
        ticketToken = _ticketToken;
    }

    /**
     * @notice Purchase lottery tickets
     * @param _amount Number of tickets to purchase
     */
    function purchaseTickets(uint256 _amount) external {
        require(_amount > 0, "Invalid ticket amount");
        require(userTickets[msg.sender].add(_amount) <= MAX_TICKETS_PER_USER, "Exceeded max tickets per user");
        require(IERC20(ticketToken).balanceOf(msg.sender) >= TICKET_PRICE.mul(_amount), "Insufficient token balance");

        // Transfer tokens from user to contract
        IERC20(ticketToken).transferFrom(msg.sender, address(this), TICKET_PRICE.mul(_amount));

        // Update state
        userTickets[msg.sender] = userTickets[msg.sender].add(_amount);
        ticketSales = ticketSales.add(_amount);

        // Assign ticket IDs to buyer
        for (uint256 i = 0; i < _amount; i++) {
            ticketHolders[lotteryId * MAX_TICKETS_PER_USER + i] = msg.sender;
        }

        emit TicketsPurchased(msg.sender, _amount);
    }

    /**
     * @notice Start a new lottery
     */
    function startLottery() external onlyOwner {
        require(ticketSales > 0, "No tickets sold");

        // Calculate prize pools
        grandPrizePool = ticketSales.mul(GRAND_PRIZE_POOL_PERCENTAGE) / 100;
        smallPrizePool = ticketSales.mul(SMALL_PRIZE_POOL_PERCENTAGE) / 100;
        mediumPrizePool = ticketSales.mul(MEDIUM_PRIZE_POOL_PERCENTAGE) / 100;

        // Reset state
        lotteryId++;
        ticketSales = 0;

        emit LotteryStarted(lotteryId);
    }

    /**
     * @notice Draw the lottery
     */
    function drawLottery() external onlyOwner {
        require(lotteryId > 0, "No lottery in progress");

        // Select winners
        uint256 grandPrizeWinner = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty))) % ticketSales;
        address[] memory winners = new address[](3);
        winners[0] = ticketHolders[grandPrizeWinner];

        // Small prize winners
        for (uint256 i = 1; i < 3; i++) {
            uint256 smallPrizeWinner = (grandPrizeWinner + i) % ticketSales;
            winners[i] = ticketHolders[smallPrizeWinner];
        }

        // Transfer prizes
        IERC20(ticketToken).transfer(winners[0], grandPrizePool);
        IERC20(ticketToken).transfer(winners[1], smallPrizePool);
        IERC20(ticketToken).transfer(winners[2], mediumPrizePool);

        emit LotteryDrawn(lotteryId, winners);
    }

    /**
     * @notice Claim ticket refund
     */
    function claimRefund() external {
        require(userTickets[msg.sender] > 0, "No tickets to refund");

        // Transfer token refund
        IERC20(ticketToken).transfer(msg.sender, TICKET_PRICE.mul(userTickets[msg.sender]));

        // Reset user tickets
        userTickets[msg.sender] = 0;
    }

    /**
     * @notice Get user ticket count
     * @param _user User address
     * @return User ticket count
     */
    function getUserTickets(address _user) external view returns (uint256) {
        return userTickets[_user];
    }
}
```
