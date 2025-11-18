"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-overlay.pages.dev
Prompt: Provide an example of a Solidity contract that integrates with Overlay Protocol to spin up a market based on real-world scalar data, ensuring compliance with the protocol's security standards.
Generated: DETERMINISTIC_7509077b92718652
Batch ID: 20250612_152511
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

interface IOverlayProtocol {
    function createMarket(
        string calldata _description,
        uint256 _eventId,
        uint256 _expirationTime,
        uint256 _minStake,
        uint256 _maxStake
    ) external returns (uint256 marketId);
}

contract RealWorldMarket is Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _marketIdCounter;

    // Overlay Protocol interface
    IOverlayProtocol public overlayProtocol;

    // Struct to store market details
    struct Market {
        uint256 id;
        string description;
        uint256 eventId;
        uint256 expirationTime;
        uint256 minStake;
        uint256 maxStake;
        bool isActive;
    }

    // Mapping to store markets by their ID
    mapping(uint256 => Market) public markets;

    // Event emitted when a market is created
    event MarketCreated(uint256 indexed marketId, string description, uint256 eventId);

    // Constructor to set the Overlay Protocol address
    constructor(address _overlayProtocolAddress) {
        require(_overlayProtocolAddress != address(0), "Invalid address");
        overlayProtocol = IOverlayProtocol(_overlayProtocolAddress);
    }

    /**
     * @dev Create a new market with real-world scalar data.
     * @param _description A brief description of the market.
     * @param _eventId Identifier for the associated real-world event.
     * @param _expirationTime The timestamp after which the market is no longer valid.
     * @param _minStake Minimum amount of tokens required to participate in the market.
     * @param _maxStake Maximum amount of tokens allowed to be staked in the market.
     */
    function createMarket(
        string calldata _description,
        uint256 _eventId,
        uint256 _expirationTime,
        uint256 _minStake,
        uint256 _maxStake
    ) external onlyOwner {
        require(_expirationTime > block.timestamp, "Expiration time must be in the future");
        require(_minStake > 0 && _maxStake > _minStake, "Invalid stake range");

        // Increment market ID counter
        uint256 marketId = _marketIdCounter.current();
        _marketIdCounter.increment();

        // Integrate with Overlay Protocol to create the market
        uint256 overlayMarketId = overlayProtocol.createMarket(
            _description,
            _eventId,
            _expirationTime,
            _minStake,
            _maxStake
        );

        // Store the market details
        markets[marketId] = Market({
            id: marketId,
            description: _description,
            eventId: _eventId,
            expirationTime: _expirationTime,
            minStake: _minStake,
            maxStake: _maxStake,
            isActive: true
        });

        emit MarketCreated(marketId, _description, _eventId);
    }

    /**
     * @dev Retrieve market details by ID.
     * @param marketId The ID of the market to retrieve.
     * @return The market details.
     */
    function getMarket(uint256 marketId) external view returns (Market memory) {
        require(markets[marketId].id == marketId, "Market does not exist");
        return markets[marketId];
    }

    /**
     * @dev Deactivate a market.
     * @param marketId The ID of the market to deactivate.
     */
    function deactivateMarket(uint256 marketId) external onlyOwner {
        require(markets[marketId].isActive, "Market is already inactive");
        markets[marketId].isActive = false;
    }
}
```
