"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whale.market
Prompt: Write a smart contract in Solidity that enables secure OTC trading of tokens without slippage, referencing the decentralized features described in Whales Market's platform.
Generated: DETERMINISTIC_00844477f21591ea
Batch ID: 20250612_153820
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title OTCTrading
 * @dev A smart contract for Over-The-Counter (OTC) token trading without slippage.
 */
contract OTCTrading is Ownable {
    // Event emitted on successful trade
    event TradeExecuted(address indexed buyer, address indexed seller, address indexed token, uint256 amount);

    // Struct to represent a trade offer
    struct TradeOffer {
        address seller;
        address token;
        uint256 amount;
        uint256 price; // price in terms of token per Ether
    }

    // Mapping to store trade offers
    mapping(uint256 => TradeOffer) public tradeOffers;
    uint256 public nextOfferId;

    // Modifier to check if the offer exists
    modifier offerExists(uint256 offerId) {
        require(offerId < nextOfferId, "Offer does not exist.");
        _;
    }

    /**
     * @dev Creates a new trade offer.
     * @param _token The address of the ERC20 token being sold.
     * @param _amount The amount of tokens for sale.
     * @param _price The price of the tokens in Ether.
     */
    function createOffer(address _token, uint256 _amount, uint256 _price) external {
        require(_amount > 0, "Amount must be greater than zero.");
        require(_price > 0, "Price must be greater than zero.");

        // Transfer tokens from seller to contract
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);

        // Create and store the new trade offer
        tradeOffers[nextOfferId] = TradeOffer({
            seller: msg.sender,
            token: _token,
            amount: _amount,
            price: _price
        });

        emit TradeExecuted(address(0), msg.sender, _token, _amount); // Event for offer creation
        nextOfferId++;
    }

    /**
     * @dev Executes a trade for an existing offer.
     * @param offerId The ID of the trade offer.
     */
    function executeTrade(uint256 offerId) external payable offerExists(offerId) {
        TradeOffer storage offer = tradeOffers[offerId];

        // Ensure the buyer sends the exact amount of Ether required
        uint256 requiredEtherAmount = offer.amount * offer.price;
        require(msg.value == requiredEtherAmount, "Incorrect Ether amount sent.");

        // Transfer tokens from contract to buyer
        IERC20(offer.token).transfer(msg.sender, offer.amount);

        // Transfer Ether to the seller
        (bool success, ) = offer.seller.call{value: msg.value}("");
        require(success, "Transfer failed.");

        // Emit an event for the trade execution
        emit TradeExecuted(msg.sender, offer.seller, offer.token, offer.amount);
        
        // Clean up the trade offer
        delete tradeOffers[offerId];
    }

    /**
     * @dev Allows the owner to withdraw accidentally sent tokens.
     * @param _token The address of the ERC20 token to withdraw.
     * @param _amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        IERC20(_token).transfer(msg.sender, _amount);
    }

    /**
     * @dev Allows the owner to withdraw Ether from the contract.
     */
    function withdrawEther() external onlyOwner {
        (bool success, ) = msg.sender.call{value: address(this).balance}("");
        require(success, "Ether transfer failed.");
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
