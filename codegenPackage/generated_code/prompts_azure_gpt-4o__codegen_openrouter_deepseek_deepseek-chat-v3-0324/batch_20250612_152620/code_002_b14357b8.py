"""
Generated Code Metadata:
========================
Original URL: https://polkabridge.pages.dev
Prompt: Develop a code snippet to simulate the escrow functionality described in PolkaBridge's P2P trading process, ensuring secure transaction handling.
Generated: DETERMINISTIC_b14357b8f6673f76
Batch ID: 20250612_152620
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PolkaBridgeEscrow
 * @dev Implements an escrow system for P2P trading with secure transaction handling
 */
contract PolkaBridgeEscrow is ReentrancyGuard, Ownable {
    // Struct to store trade details
    struct Trade {
        address buyer;
        address seller;
        address tokenAddress;
        uint256 amount;
        bool isFiatInvolved;
        bool isBuyerApproved;
        bool isSellerApproved;
        bool isCompleted;
        bool isDisputed;
    }

    // Mapping of trade ID to Trade struct
    mapping(bytes32 => Trade) public trades;
    
    // Escrow fee percentage (1 = 0.01%)
    uint256 public escrowFeePercentage;
    
    // Address to collect escrow fees
    address public feeCollector;
    
    // Events
    event TradeCreated(
        bytes32 indexed tradeId,
        address indexed buyer,
        address indexed seller,
        address tokenAddress,
        uint256 amount,
        bool isFiatInvolved
    );
    
    event FundsDeposited(bytes32 indexed tradeId, uint256 amount);
    event BuyerApproved(bytes32 indexed tradeId);
    event SellerApproved(bytes32 indexed tradeId);
    event TradeCompleted(bytes32 indexed tradeId);
    event TradeDisputed(bytes32 indexed tradeId);
    event DisputeResolved(bytes32 indexed tradeId, bool buyerWins);
    
    /**
     * @dev Constructor
     * @param _feeCollector Address to collect escrow fees
     * @param _escrowFeePercentage Escrow fee percentage (1 = 0.01%)
     */
    constructor(address _feeCollector, uint256 _escrowFeePercentage) {
        require(_feeCollector != address(0), "Invalid fee collector address");
        feeCollector = _feeCollector;
        escrowFeePercentage = _escrowFeePercentage;
    }
    
    /**
     * @dev Create a new trade
     * @param _tradeId Unique trade identifier
     * @param _seller Seller address
     * @param _tokenAddress ERC20 token address (address(0) for native currency)
     * @param _amount Trade amount
     * @param _isFiatInvolved Whether fiat is involved in the trade
     */
    function createTrade(
        bytes32 _tradeId,
        address _seller,
        address _tokenAddress,
        uint256 _amount,
        bool _isFiatInvolved
    ) external {
        require(_seller != address(0), "Invalid seller address");
        require(_amount > 0, "Amount must be greater than 0");
        require(trades[_tradeId].buyer == address(0), "Trade already exists");
        
        trades[_tradeId] = Trade({
            buyer: msg.sender,
            seller: _seller,
            tokenAddress: _tokenAddress,
            amount: _amount,
            isFiatInvolved: _isFiatInvolved,
            isBuyerApproved: false,
            isSellerApproved: false,
            isCompleted: false,
            isDisputed: false
        });
        
        emit TradeCreated(_tradeId, msg.sender, _seller, _tokenAddress, _amount, _isFiatInvolved);
    }
    
    /**
     * @dev Deposit funds into escrow
     * @param _tradeId Trade identifier
     */
    function depositFunds(bytes32 _tradeId) external payable nonReentrant {
        Trade storage trade = trades[_tradeId];
        require(trade.buyer == msg.sender, "Only buyer can deposit");
        require(!trade.isBuyerApproved, "Funds already deposited");
        
        if (trade.tokenAddress == address(0)) {
            // Native currency
            require(msg.value == trade.amount, "Incorrect amount sent");
        } else {
            // ERC20 token
            IERC20 token = IERC20(trade.tokenAddress);
            require(token.transferFrom(msg.sender, address(this), trade.amount), "Token transfer failed");
        }
        
        trade.isBuyerApproved = true;
        emit FundsDeposited(_tradeId, trade.amount);
    }
    
    /**
     * @dev Approve trade as seller
     * @param _tradeId Trade identifier
     */
    function approveAsSeller(bytes32 _tradeId) external {
        Trade storage trade = trades[_tradeId];
        require(trade.seller == msg.sender, "Only seller can approve");
        require(trade.isBuyerApproved, "Buyer has not deposited funds");
        require(!trade.isSellerApproved, "Already approved by seller");
        
        trade.isSellerApproved = true;
        emit SellerApproved(_tradeId);
    }
    
    /**
     * @dev Complete trade and release funds
     * @param _tradeId Trade identifier
     */
    function completeTrade(bytes32 _tradeId) external nonReentrant {
        Trade storage trade = trades[_tradeId];
        require(trade.buyer == msg.sender || trade.seller == msg.sender, "Unauthorized");
        require(trade.isBuyerApproved && trade.isSellerApproved, "Trade not fully approved");
        require(!trade.isCompleted, "Trade already completed");
        require(!trade.isDisputed, "Trade is disputed");
        
        trade.isCompleted = true;
        
        uint256 feeAmount = (trade.amount * escrowFeePercentage) / 10000;
        uint256 amountToSeller = trade.amount - feeAmount;
        
        if (trade.tokenAddress == address(0)) {
            // Native currency
            (bool feeSuccess, ) = feeCollector.call{value: feeAmount}("");
            (bool sellerSuccess, ) = trade.seller.call{value: amountToSeller}("");
            require(feeSuccess && sellerSuccess, "Transfer failed");
        } else {
            // ERC20 token
            IERC20 token = IERC20(trade.tokenAddress);
            require(token.transfer(feeCollector, feeAmount), "Fee transfer failed");
            require(token.transfer(trade.seller, amountToSeller), "Seller transfer failed");
        }
        
        emit TradeCompleted(_tradeId);
    }
    
    /**
     * @dev Raise a dispute
     * @param _tradeId Trade identifier
     */
    function raiseDispute(bytes32 _tradeId) external {
        Trade storage trade = trades[_tradeId];
        require(trade.buyer == msg.sender || trade.seller == msg.sender, "Unauthorized");
        require(!trade.isCompleted, "Trade already completed");
        require(!trade.isDisputed, "Dispute already raised");
        
        trade.isDisputed = true;
        emit TradeDisputed(_tradeId);
    }
    
    /**
     * @dev Resolve a dispute (only owner)
     * @param _tradeId Trade identifier
     * @param _buyerWins Whether buyer wins the dispute
     */
    function resolveDispute(bytes32 _tradeId, bool _buyerWins) external onlyOwner nonReentrant {
        Trade storage trade = trades[_tradeId];
        require(trade.isDisputed, "No dispute to resolve");
        require(!trade.isCompleted, "Trade already completed");
        
        trade.isCompleted = true;
        
        uint256 feeAmount = (trade.amount * escrowFeePercentage) / 10000;
        uint256 amountToRecipient = trade.amount - feeAmount;
        address recipient = _buyerWins ? trade.buyer : trade.seller;
        
        if (trade.tokenAddress == address(0)) {
            // Native currency
            (bool feeSuccess, ) = feeCollector.call{value: feeAmount}("");
            (bool recipientSuccess, ) = recipient.call{value: amountToRecipient}("");
            require(feeSuccess && recipientSuccess, "Transfer failed");
        } else {
            // ERC20 token
            IERC20 token = IERC20(trade.tokenAddress);
            require(token.transfer(feeCollector, feeAmount), "Fee transfer failed");
            require(token.transfer(recipient, amountToRecipient), "Recipient transfer failed");
        }
        
        emit DisputeResolved(_tradeId, _buyerWins);
    }
    
    /**
     * @dev Update escrow fee percentage (only owner)
     * @param _newPercentage New fee percentage (1 = 0.01%)
     */
    function updateEscrowFeePercentage(uint256 _newPercentage) external onlyOwner {
        require(_newPercentage <= 1000, "Fee too high"); // Max 10%
        escrowFeePercentage = _newPercentage;
    }
    
    /**
     * @dev Update fee collector address (only owner)
     * @param _newFeeCollector New fee collector address
     */
    function updateFeeCollector(address _newFeeCollector) external onlyOwner {
        require(_newFeeCollector != address(0), "Invalid address");
        feeCollector = _newFeeCollector;
    }
