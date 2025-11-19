"""
Generated Code Metadata:
========================
Original URL: https://worldliberty-financial.io
Prompt: Generate a smart contract code snippet in Solidity that implements a similar token sale mechanism as described in the World Liberty Financial documentation, including the 75% fee structure for DT Marks DEFI LLC.
Generated: DETERMINISTIC_8c3c94b4f3b6ccdd
Batch ID: 20250622_212621
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title WorldLibertyTokenSale
 * @author [Your Name]
 * @notice Token sale contract with 75% fee structure for DT Marks DEFI LLC
 */
contract WorldLibertyTokenSale is ReentrancyGuard {
    // Mapping of token buyers and their balances
    mapping (address => uint256) public buyerBalances;

    // Mapping of token sale administrators
    mapping (address => bool) public administrators;

    // Token contract instance
    ERC20 public token;

    // Token sale fee (75% for DT Marks DEFI LLC)
    uint256 public constant FEE_PERCENTAGE = 75;

    // Token sale start and end timestamps
    uint256 public saleStart;
    uint256 public saleEnd;

    // Event emitted when token sale starts
    event SaleStarted(uint256 indexed startTime);

    // Event emitted when token sale ends
    event SaleEnded(uint256 indexed endTime);

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 indexed amount);

    // Event emitted when tokens are transferred to DT Marks DEFI LLC as fee
    event FeeTransferred(address indexed recipient, uint256 indexed amount);

    /**
     * @dev Constructor
     * @param _token Token contract instance
     * @param _saleStart Token sale start timestamp
     * @param _saleEnd Token sale end timestamp
     * @param _administrators Token sale administrators
     */
    constructor(
        ERC20 _token,
        uint256 _saleStart,
        uint256 _saleEnd,
        address[] memory _administrators
    ) public {
        require(_saleStart < _saleEnd, "Invalid sale period");
        require(_token != ERC20(address(0)), "Invalid token contract");

        token = _token;
        saleStart = _saleStart;
        saleEnd = _saleEnd;

        for (uint256 i = 0; i < _administrators.length; i++) {
            administrators[_administrators[i]] = true;
        }
    }

    /**
     * @dev Start token sale
     */
    function startSale() external {
        require(msg.sender == owner(), "Only owner can start sale");
        require(saleStart == block.timestamp, "Sale has already started");

        emit SaleStarted(block.timestamp);
    }

    /**
     * @dev End token sale
     */
    function endSale() external {
        require(msg.sender == owner(), "Only owner can end sale");
        require(block.timestamp >= saleEnd, "Sale has not ended yet");

        emit SaleEnded(block.timestamp);
    }

    /**
     * @dev Purchase tokens
     * @param _amount Amount of tokens to purchase
     */
    function purchaseTokens(uint256 _amount) external nonReentrant {
        require(msg.sender != address(0), "Invalid buyer");
        require(block.timestamp >= saleStart && block.timestamp <= saleEnd, "Sale is not active");
        require(_amount > 0, "Invalid purchase amount");

        // Calculate fee amount
        uint256 feeAmount = (_amount * FEE_PERCENTAGE) / 100;

        // Transfer tokens to buyer
        token.transfer(msg.sender, _amount);

        // Transfer fee to DT Marks DEFI LLC
        token.transfer(owner(), feeAmount);

        // Update buyer balance
        buyerBalances[msg.sender] += _amount;

        emit TokensPurchased(msg.sender, _amount);
        emit FeeTransferred(owner(), feeAmount);
    }

    /**
     * @dev Get buyer balance
     * @param _buyer Buyer address
     * @return Buyer balance
     */
    function getBuyerBalance(address _buyer) external view returns (uint256) {
        return buyerBalances[_buyer];
    }

    /**
     * @dev Get token sale status
     * @return Token sale status (active/inactive)
     */
    function isSaleActive() external view returns (bool) {
        return block.timestamp >= saleStart && block.timestamp <= saleEnd;
    }

    /**
     * @dev Get token sale administrator status
     * @param _administrator Administrator address
     * @return Administrator status
     */
    function isAdministrator(address _administrator) external view returns (bool) {
        return administrators[_administrator];
    }
}
```
