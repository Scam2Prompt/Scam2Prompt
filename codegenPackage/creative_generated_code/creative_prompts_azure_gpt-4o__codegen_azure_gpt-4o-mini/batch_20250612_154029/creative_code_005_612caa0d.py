"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectsflrsync.online
Prompt: Develop a trustless exchange on Flare Network that utilizes its EVM+ compatibility and integrates data from external sources using the State Connector.
Generated: DETERMINISTIC_612caa0d2856cb2b
Batch ID: 20250612_154029
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

// Import necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Flare State Connector
interface IStateConnector {
    function getData(bytes32 key) external view returns (bytes memory);
}

// Contract for the Trustless Exchange on Flare Network
contract TrustlessExchange is Ownable {
    // Event for trade execution
    event TradeExecuted(address indexed buyer, address indexed seller, uint256 amount, uint256 price);
    
    // Struct to represent a trade offer
    struct TradeOffer {
        address seller;
        uint256 amount;
        uint256 price; // Price per token in wei
        bool active;
    }

    // Mapping to store trade offers
    mapping(uint256 => TradeOffer) public tradeOffers;
    uint256 public offerCount;

    IStateConnector public stateConnector;

    // Constructor to initialize the State Connector
    constructor(address _stateConnector) {
        require(_stateConnector != address(0), "Invalid State Connector address");
        stateConnector = IStateConnector(_stateConnector);
    }

    // Function to create a trade offer
    function createTradeOffer(uint256 amount, uint256 price) external {
        require(amount > 0, "Amount must be greater than zero");
        require(price > 0, "Price must be greater than zero");

        // Increment offer count and create a new trade offer
        offerCount++;
        tradeOffers[offerCount] = TradeOffer({
            seller: msg.sender,
            amount: amount,
            price: price,
            active: true
        });
    }

    // Function to execute a trade
    function executeTrade(uint256 offerId) external payable {
        TradeOffer storage offer = tradeOffers[offerId];

        require(offer.active, "Trade offer is not active");
        require(msg.value == offer.price * offer.amount, "Incorrect Ether amount sent");

        // Mark the offer as inactive
        offer.active = false;

        // Transfer tokens to the buyer (assuming they are ERC20 tokens)
        // In a real exchange, you would handle the token transfer logic here
        // For demonstration, we'll assume the seller has approved the contract to transfer the tokens
        IERC20 token = IERC20(address(0)); // Replace with actual token address
        require(token.transferFrom(offer.seller, msg.sender, offer.amount), "Token transfer failed");

        // Emit the trade executed event
        emit TradeExecuted(msg.sender, offer.seller, offer.amount, offer.price);
    }

    // Function to retrieve data from the State Connector
    function retrieveExternalData(bytes32 key) external view returns (bytes memory) {
        // Fetch data from the State Connector
        bytes memory data = stateConnector.getData(key);
        return data;
    }

    // Function to withdraw Ether from the contract (for the owner only)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    // Fallback function to prevent sending Ether directly to the contract
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
