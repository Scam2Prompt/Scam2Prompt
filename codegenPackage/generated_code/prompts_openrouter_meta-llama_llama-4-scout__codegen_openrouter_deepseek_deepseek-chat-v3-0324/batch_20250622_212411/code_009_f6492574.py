"""
Generated Code Metadata:
========================
Original URL: https://solvfinance.biz
Prompt: "Propose a scalable blockchain infrastructure for DeFi applications using Solv Protocol's innovative solutions."
Generated: DETERMINISTIC_f6492574b29ecb7a
Batch ID: 20250622_212411
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title SolvDeFiProtocol
 * @dev A scalable DeFi infrastructure leveraging Solv Protocol's solutions
 */
contract SolvDeFiProtocol is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to represent a financial instrument
    struct Instrument {
        address issuer;
        address underlyingAsset;
        uint256 totalSupply;
        uint256 maturityDate;
        bool isActive;
    }

    // Mapping from instrument ID to Instrument
    mapping(uint256 => Instrument) public instruments;

    // Mapping from user address to instrument ID to balance
    mapping(address => mapping(uint256 => uint256)) public balances;

    // Counter for instrument IDs
    uint256 public nextInstrumentId;

    // Events
    event InstrumentCreated(
        uint256 indexed instrumentId,
        address indexed issuer,
        address underlyingAsset,
        uint256 totalSupply,
        uint256 maturityDate
    );
    event InstrumentPurchased(
        uint256 indexed instrumentId,
        address indexed buyer,
        uint256 amount
    );
    event InstrumentRedeemed(
        uint256 indexed instrumentId,
        address indexed redeemer,
        uint256 amount
    );

    /**
     * @dev Create a new financial instrument
     * @param _underlyingAsset Address of the underlying ERC20 token
     * @param _totalSupply Total supply of the instrument
     * @param _maturityDate Unix timestamp of maturity date
     */
    function createInstrument(
        address _underlyingAsset,
        uint256 _totalSupply,
        uint256 _maturityDate
    ) external onlyOwner {
        require(_underlyingAsset != address(0), "Invalid asset address");
        require(_totalSupply > 0, "Supply must be positive");
        require(_maturityDate > block.timestamp, "Maturity must be in future");

        uint256 instrumentId = nextInstrumentId++;
        instruments[instrumentId] = Instrument({
            issuer: msg.sender,
            underlyingAsset: _underlyingAsset,
            totalSupply: _totalSupply,
            maturityDate: _maturityDate,
            isActive: true
        });

        emit InstrumentCreated(
            instrumentId,
            msg.sender,
            _underlyingAsset,
            _totalSupply,
            _maturityDate
        );
    }

    /**
     * @dev Purchase an instrument
     * @param _instrumentId ID of the instrument to purchase
     * @param _amount Amount to purchase
     */
    function purchaseInstrument(uint256 _instrumentId, uint256 _amount)
        external
        nonReentrant
    {
        Instrument storage instrument = instruments[_instrumentId];
        require(instrument.isActive, "Instrument not active");
        require(_amount > 0, "Amount must be positive");
        require(
            IERC20(instrument.underlyingAsset).balanceOf(msg.sender) >= _amount,
            "Insufficient balance"
        );

        // Transfer tokens from buyer to contract
        IERC20(instrument.underlyingAsset).transferFrom(
            msg.sender,
            address(this),
            _amount
        );

        // Update balances
        balances[msg.sender][_instrumentId] = balances[msg.sender][_instrumentId]
            .add(_amount);

        emit InstrumentPurchased(_instrumentId, msg.sender, _amount);
    }

    /**
     * @dev Redeem an instrument after maturity
     * @param _instrumentId ID of the instrument to redeem
     * @param _amount Amount to redeem
     */
    function redeemInstrument(uint256 _instrumentId, uint256 _amount)
        external
        nonReentrant
    {
        Instrument storage instrument = instruments[_instrumentId];
        require(block.timestamp >= instrument.maturityDate, "Not matured yet");
        require(
            balances[msg.sender][_instrumentId] >= _amount,
            "Insufficient balance"
        );

        // Update balances
        balances[msg.sender][_instrumentId] = balances[msg.sender][_instrumentId]
            .sub(_amount);

        // Transfer underlying asset back to user
        IERC20(instrument.underlyingAsset).transfer(msg.sender, _amount);

        emit InstrumentRedeemed(_instrumentId, msg.sender, _amount);
    }

    /**
     * @dev Emergency function to deactivate an instrument
     * @param _instrumentId ID of the instrument to deactivate
     */
    function deactivateInstrument(uint256 _instrumentId) external onlyOwner {
        require(instruments[_instrumentId].isActive, "Already inactive");
        instruments[_instrumentId].isActive = false;
    }
}
```
