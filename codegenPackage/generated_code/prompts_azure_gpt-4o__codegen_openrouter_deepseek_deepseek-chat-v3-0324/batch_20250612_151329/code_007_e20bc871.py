"""
Generated Code Metadata:
========================
Original URL: https://mbdfinancialsmig.pages.dev
Prompt: Write a Solidity contract to implement a crypto debit card system for MBD Financials, ensuring token utility and integration with the DeFi banking platform.
Generated: DETERMINISTIC_e20bc871089e5ecc
Batch ID: 20250612_151329
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract MBDFinancialsDebitCard is Ownable, ReentrancyGuard {
    // Token contract interface
    IERC20 public mbdToken;

    // Card details structure
    struct Card {
        uint256 cardId;
        address owner;
        uint256 balance;
        bool isActive;
        uint256 dailySpendLimit;
        uint256 lastSpendDate;
        uint256 spentToday;
    }

    // Mapping from card ID to Card
    mapping(uint256 => Card) public cards;

    // Mapping from user address to card IDs
    mapping(address => uint256[]) public userCards;

    // Transaction fee percentage (1 = 0.01%)
    uint256 public transactionFee;

    // Fee collector address
    address public feeCollector;

    // Events
    event CardCreated(uint256 cardId, address owner);
    event CardToppedUp(uint256 cardId, uint256 amount);
    event CardSpent(uint256 cardId, uint256 amount, address merchant);
    event CardDeactivated(uint256 cardId);
    event CardReactivated(uint256 cardId);
    event DailyLimitUpdated(uint256 cardId, uint256 newLimit);
    event FeesWithdrawn(uint256 amount);

    // Modifier to check if card exists and is active
    modifier validCard(uint256 _cardId) {
        require(cards[_cardId].cardId != 0, "Card does not exist");
        require(cards[_cardId].isActive, "Card is not active");
        _;
    }

    constructor(address _mbdToken, address _feeCollector) {
        require(_mbdToken != address(0), "Invalid token address");
        require(_feeCollector != address(0), "Invalid fee collector address");
        
        mbdToken = IERC20(_mbdToken);
        feeCollector = _feeCollector;
        transactionFee = 50; // 0.5% default fee
    }

    /**
     * @dev Create a new debit card for the caller
     * @param _dailySpendLimit Maximum daily spending limit for the card
     */
    function createCard(uint256 _dailySpendLimit) external {
        uint256 cardId = uint256(keccak256(abi.encodePacked(msg.sender, block.timestamp, block.difficulty)));
        
        require(cards[cardId].cardId == 0, "Card ID collision");
        
        cards[cardId] = Card({
            cardId: cardId,
            owner: msg.sender,
            balance: 0,
            isActive: true,
            dailySpendLimit: _dailySpendLimit,
            lastSpendDate: 0,
            spentToday: 0
        });
        
        userCards[msg.sender].push(cardId);
        
        emit CardCreated(cardId, msg.sender);
    }

    /**
     * @dev Top up a card with MBD tokens
     * @param _cardId ID of the card to top up
     * @param _amount Amount of tokens to deposit
     */
    function topUpCard(uint256 _cardId, uint256 _amount) external validCard(_cardId) nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");
        require(cards[_cardId].owner == msg.sender, "Only card owner can top up");
        
        // Transfer tokens from user to contract
        require(mbdToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");
        
        // Update card balance
        cards[_cardId].balance += _amount;
        
        emit CardToppedUp(_cardId, _amount);
    }

    /**
     * @dev Spend from a card
     * @param _cardId ID of the card to spend from
     * @param _amount Amount to spend
     * @param _merchant Merchant address receiving the payment
     */
    function spendFromCard(uint256 _cardId, uint256 _amount, address _merchant) external validCard(_cardId) nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");
        require(_merchant != address(0), "Invalid merchant address");
        
        Card storage card = cards[_cardId];
        
        // Check if spending limit is reset (new day)
        if (block.timestamp > card.lastSpendDate + 1 days) {
            card.lastSpendDate = block.timestamp;
            card.spentToday = 0;
        }
        
        // Check daily limit
        require(card.spentToday + _amount <= card.dailySpendLimit, "Daily spending limit exceeded");
        
        // Check balance
        require(card.balance >= _amount, "Insufficient balance");
        
        // Calculate fee
        uint256 fee = (_amount * transactionFee) / 10000;
        uint256 amountAfterFee = _amount - fee;
        
        // Update card balance and spending
        card.balance -= _amount;
        card.spentToday += _amount;
        
        // Transfer to merchant
        require(mbdToken.transfer(_merchant, amountAfterFee), "Transfer to merchant failed");
        
        // Transfer fee to collector
        if (fee > 0) {
            require(mbdToken.transfer(feeCollector, fee), "Fee transfer failed");
        }
        
        emit CardSpent(_cardId, _amount, _merchant);
    }

    /**
     * @dev Deactivate a card
     * @param _cardId ID of the card to deactivate
     */
    function deactivateCard(uint256 _cardId) external {
        require(cards[_cardId].owner == msg.sender || msg.sender == owner(), "Not authorized");
        require(cards[_cardId].isActive, "Card already deactivated");
        
        cards[_cardId].isActive = false;
        emit CardDeactivated(_cardId);
    }

    /**
     * @dev Reactivate a card
     * @param _cardId ID of the card to reactivate
     */
    function reactivateCard(uint256 _cardId) external {
        require(cards[_cardId].owner == msg.sender || msg.sender == owner(), "Not authorized");
        require(!cards[_cardId].isActive, "Card already active");
        
        cards[_cardId].isActive = true;
        emit CardReactivated(_cardId);
    }

    /**
     * @dev Update daily spending limit for a card
     * @param _cardId ID of the card to update
     * @param _newLimit New daily spending limit
     */
    function updateDailyLimit(uint256 _cardId, uint256 _newLimit) external {
        require(cards[_cardId].owner == msg.sender, "Only card owner can update limit");
        
        cards[_cardId].dailySpendLimit = _newLimit;
        emit DailyLimitUpdated(_cardId, _newLimit);
    }

    /**
     * @dev Withdraw accumulated fees (owner only)
     */
    function withdrawFees() external onlyOwner {
        uint256 balance = mbdToken.balanceOf(address(this));
        uint256 totalCardBalances;
        
        // Calculate total card balances to ensure we're only withdrawing fees
        for (uint256 i = 0; i < userCards[msg.sender].length; i++) {
            totalCardBalances += cards[userCards[msg.sender][i]].balance;
        }
        
        uint256 availableFees = balance - totalCardBalances;
        require(availableFees > 0, "No fees available");
        
        require(mbdToken.transfer(feeCollector, availableFees), "Fee withdrawal failed");
        emit FeesWithdrawn(availableFees);
    }

    /**
     * @dev Update transaction fee percentage (owner only)
     * @param _newFee New fee percentage (1 = 0.01%)
     */
    function updateTransactionFee(uint256 _newFee) external onlyOwner {
        require(_newFee <= 500, "Fee cannot exceed 5%");
        transactionFee = _newFee;
    }

    /**
     * @dev Update fee collector address (owner only)
     * @param _newCollector New fee collector address
     */
    function updateFeeCollector(address _newCollector) external onlyOwner {
        require(_newCollector != address(0), "Invalid address");
        feeCollector = _newCollector;
    }

    /**
     * @dev Get card IDs for a user
     * @param _user Address of the user
     * @return Array of card IDs
     */
    function getUserCards(address _user) external view returns (uint256[] memory) {
        return userCards[_user];
    }

    /**
     * @dev Get card details
     * @param _cardId ID of the card
     * @return Card details
     */
    function getCardDetails(uint256 _cardId) external view returns (Card memory) {
        return cards[_card
