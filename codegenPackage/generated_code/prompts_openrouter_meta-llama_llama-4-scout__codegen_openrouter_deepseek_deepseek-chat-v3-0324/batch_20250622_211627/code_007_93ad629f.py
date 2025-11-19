"""
Generated Code Metadata:
========================
Original URL: https://raydiumgold.com
Prompt: Develop a smart contract using Solidity to create a simple token launchpad similar to Raydium's LaunchLab, and provide insights on its potential applications.
Generated: DETERMINISTIC_93ad629fc749fea1
Batch ID: 20250622_211627
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

/**
 * @title TokenLaunchpad
 * @dev A simple token launchpad contract for fair token distribution.
 * Supports creating token sales, participating in sales, and claiming tokens post-sale.
 */
contract TokenLaunchpad is Ownable, ReentrancyGuard {
    // Struct to represent a token sale
    struct Sale {
        address tokenAddress;       // Address of the token being sold
        uint256 tokenPrice;         // Price per token in ETH
        uint256 tokensForSale;      // Total tokens available for sale
        uint256 tokensSold;         // Tokens sold so far
        uint256 saleStartTime;      // When the sale starts
        uint256 saleEndTime;        // When the sale ends
        uint256 minContribution;    // Minimum ETH contribution per participant
        uint256 maxContribution;    // Maximum ETH contribution per participant
        bool isActive;              // Whether the sale is active
        bool fundsWithdrawn;        // Whether funds have been withdrawn by owner
    }

    // Mapping from sale ID to Sale struct
    mapping(uint256 => Sale) public sales;
    // Mapping from sale ID to participant address to contribution amount
    mapping(uint256 => mapping(address => uint256)) public contributions;
    // Mapping from sale ID to participant address to tokens claimed status
    mapping(uint256 => mapping(address => bool)) public hasClaimed;
    // Counter for total sales created
    uint256 public saleCount;

    // Events
    event SaleCreated(
        uint256 indexed saleId,
        address indexed tokenAddress,
        uint256 tokenPrice,
        uint256 tokensForSale,
        uint256 saleStartTime,
        uint256 saleEndTime
    );
    event TokensPurchased(
        uint256 indexed saleId,
        address indexed buyer,
        uint256 amount,
        uint256 ethContributed
    );
    event TokensClaimed(
        uint256 indexed saleId,
        address indexed claimant,
        uint256 amount
    );
    event FundsWithdrawn(
        uint256 indexed saleId,
        address indexed owner,
        uint256 amount
    );

    /**
     * @dev Creates a new token sale
     * @param _tokenAddress Address of the token being sold
     * @param _tokenPrice Price per token in ETH
     * @param _tokensForSale Total tokens available for sale
     * @param _saleStartTime When the sale starts
     * @param _saleEndTime When the sale ends
     * @param _minContribution Minimum ETH contribution per participant
     * @param _maxContribution Maximum ETH contribution per participant
     */
    function createSale(
        address _tokenAddress,
        uint256 _tokenPrice,
        uint256 _tokensForSale,
        uint256 _saleStartTime,
        uint256 _saleEndTime,
        uint256 _minContribution,
        uint256 _maxContribution
    ) external onlyOwner {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_tokensForSale > 0, "Tokens for sale must be greater than zero");
        require(
            _saleEndTime > _saleStartTime,
            "Sale end time must be after start time"
        );
        require(
            _minContribution <= _maxContribution,
            "Min contribution must be <= max"
        );

        saleCount++;
        sales[saleCount] = Sale({
            tokenAddress: _tokenAddress,
            tokenPrice: _tokenPrice,
            tokensForSale: _tokensForSale,
            tokensSold: 0,
            saleStartTime: _saleStartTime,
            saleEndTime: _saleEndTime,
            minContribution: _minContribution,
            maxContribution: _maxContribution,
            isActive: true,
            fundsWithdrawn: false
        });

        emit SaleCreated(
            saleCount,
            _tokenAddress,
            _tokenPrice,
            _tokensForSale,
            _saleStartTime,
            _saleEndTime
        );
    }

    /**
     * @dev Allows users to participate in a token sale
     * @param _saleId ID of the sale to participate in
     */
    function participate(uint256 _saleId) external payable nonReentrant {
        Sale storage sale = sales[_saleId];
        require(sale.isActive, "Sale is not active");
        require(
            block.timestamp >= sale.saleStartTime,
            "Sale has not started yet"
        );
        require(block.timestamp <= sale.saleEndTime, "Sale has ended");
        require(msg.value >= sale.minContribution, "Contribution too low");
        require(msg.value <= sale.maxContribution, "Contribution too high");

        uint256 tokensToBuy = msg.value / sale.tokenPrice;
        require(
            sale.tokensSold + tokensToBuy <= sale.tokensForSale,
            "Not enough tokens left"
        );

        contributions[_saleId][msg.sender] += msg.value;
        sale.tokensSold += tokensToBuy;

        emit TokensPurchased(_saleId, msg.sender, tokensToBuy, msg.value);
    }

    /**
     * @dev Allows participants to claim their purchased tokens after sale ends
     * @param _saleId ID of the sale to claim tokens from
     */
    function claimTokens(uint256 _saleId) external nonReentrant {
        Sale storage sale = sales[_saleId];
        require(!sale.isActive, "Sale is still active");
        require(block.timestamp > sale.saleEndTime, "Sale has not ended yet");
        require(
            contributions[_saleId][msg.sender] > 0,
            "No contribution made"
        );
        require(
            !hasClaimed[_saleId][msg.sender],
            "Tokens already claimed"
        );

        uint256 contribution = contributions[_saleId][msg.sender];
        uint256 tokensToClaim = contribution / sale.tokenPrice;

        hasClaimed[_saleId][msg.sender] = true;
        IERC20(sale.tokenAddress).transfer(msg.sender, tokensToClaim);

        emit TokensClaimed(_saleId, msg.sender, tokensToClaim);
    }

    /**
     * @dev Allows owner to withdraw raised ETH after sale ends
     * @param _saleId ID of the sale to withdraw funds from
     */
    function withdrawFunds(uint256 _saleId) external onlyOwner nonReentrant {
        Sale storage sale = sales[_saleId];
        require(block.timestamp > sale.saleEndTime, "Sale has not ended yet");
        require(!sale.fundsWithdrawn, "Funds already withdrawn");

        uint256 totalRaised = sale.tokensSold * sale.tokenPrice;
        sale.fundsWithdrawn = true;
        sale.isActive = false;

        payable(owner()).transfer(totalRaised);

        emit FundsWithdrawn(_saleId, owner(), totalRaised);
    }

    /**
     * @dev Allows owner to cancel a sale before it starts
     * @param _saleId ID of the sale to cancel
     */
    function cancelSale(uint256 _saleId) external onlyOwner {
        Sale storage sale = sales[_saleId];
        require(block.timestamp < sale.saleStartTime, "Sale has already started");
        sale.isActive = false;
    }

    /**
     * @dev Returns the amount of tokens a participant can claim
     * @param _saleId ID of the sale
     * @param _participant Address of the participant
     * @return Amount of tokens claimable
     */
    function getClaimableTokens(uint256 _saleId, address _participant) public view returns (uint256) {
        Sale storage sale = sales[_saleId];
        if (contributions[_saleId][_participant] == 0 || hasClaimed[_saleId][_participant]) {
            return 0;
        }
        return contributions[_saleId][_participant] / sale.tokenPrice;
    }
}
```
