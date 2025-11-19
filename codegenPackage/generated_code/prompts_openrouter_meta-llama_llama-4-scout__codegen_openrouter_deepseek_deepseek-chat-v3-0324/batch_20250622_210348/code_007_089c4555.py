"""
Generated Code Metadata:
========================
Original URL: https://bafybeifqb523rma32dtbtz2yeebyhpqrdvv7pt4basdjhn2uhdzoyvslai.ipfs.dweb.link
Prompt: Design a smart contract to create a custom trading pair on gTrade's decentralized leveraged trading platform.
Generated: DETERMINISTIC_089c4555542ad4f9
Batch ID: 20250622_210348
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IGTradeFactory {
    function createPair(address tokenA, address tokenB, uint256 leverage) external returns (address pair);
    function setTradingFee(uint256 _fee) external;
    function setMaxLeverage(uint256 _maxLeverage) external;
}

contract GTradePairCreator is Ownable, ReentrancyGuard {
    IGTradeFactory public gTradeFactory;
    
    // Events
    event PairCreated(address indexed tokenA, address indexed tokenB, address pair, uint256 leverage);
    event FactoryUpdated(address indexed newFactory);
    event TradingFeeUpdated(uint256 newFee);
    event MaxLeverageUpdated(uint256 newMaxLeverage);

    /**
     * @dev Constructor initializes the GTrade factory address
     * @param _factory Address of the GTrade factory contract
     */
    constructor(address _factory) {
        require(_factory != address(0), "Invalid factory address");
        gTradeFactory = IGTradeFactory(_factory);
    }

    /**
     * @dev Creates a new trading pair on GTrade
     * @param tokenA Address of first token in the pair
     * @param tokenB Address of second token in the pair
     * @param leverage Initial leverage for the pair (1-100x)
     */
    function createPair(
        address tokenA,
        address tokenB,
        uint256 leverage
    ) external onlyOwner nonReentrant returns (address pair) {
        require(tokenA != address(0) && tokenB != address(0), "Invalid token address");
        require(tokenA != tokenB, "Identical tokens");
        require(leverage >= 1 && leverage <= 100, "Invalid leverage");

        // Check if tokens are valid ERC20 contracts
        require(_isContract(tokenA), "TokenA is not a contract");
        require(_isContract(tokenB), "TokenB is not a contract");

        pair = gTradeFactory.createPair(tokenA, tokenB, leverage);
        emit PairCreated(tokenA, tokenB, pair, leverage);
    }

    /**
     * @dev Updates the GTrade factory address
     * @param newFactory Address of the new GTrade factory contract
     */
    function updateFactory(address newFactory) external onlyOwner {
        require(newFactory != address(0), "Invalid factory address");
        gTradeFactory = IGTradeFactory(newFactory);
        emit FactoryUpdated(newFactory);
    }

    /**
     * @dev Updates the trading fee for all pairs
     * @param newFee New trading fee (in basis points)
     */
    function updateTradingFee(uint256 newFee) external onlyOwner {
        require(newFee <= 100, "Fee too high"); // Max 1%
        gTradeFactory.setTradingFee(newFee);
        emit TradingFeeUpdated(newFee);
    }

    /**
     * @dev Updates the maximum leverage for all pairs
     * @param newMaxLeverage New maximum leverage (1-100x)
     */
    function updateMaxLeverage(uint256 newMaxLeverage) external onlyOwner {
        require(newMaxLeverage >= 1 && newMaxLeverage <= 100, "Invalid leverage");
        gTradeFactory.setMaxLeverage(newMaxLeverage);
        emit MaxLeverageUpdated(newMaxLeverage);
    }

    /**
     * @dev Internal function to check if address is a contract
     * @param addr Address to check
     */
    function _isContract(address addr) internal view returns (bool) {
        uint256 size;
        assembly {
            size := extcodesize(addr)
        }
        return size > 0;
    }
}
```
