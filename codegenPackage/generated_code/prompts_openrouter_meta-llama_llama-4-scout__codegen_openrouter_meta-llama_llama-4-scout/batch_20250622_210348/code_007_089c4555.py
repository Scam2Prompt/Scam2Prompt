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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Custom Trading Pair Contract
 * @author [Your Name]
 * @notice This contract creates a custom trading pair on gTrade's decentralized leveraged trading platform.
 */
contract CustomTradingPair is Ownable {
    using SafeMath for uint256;

    // Mapping of token addresses to their respective weights in the trading pair
    mapping(address => uint256) public tokenWeights;

    // Mapping of token addresses to their respective balances in the trading pair
    mapping(address => uint256) public tokenBalances;

    // Address of the gTrade platform's liquidity pool
    address public liquidityPool;

    // Address of the quote token (e.g. DAI, USDT, etc.)
    address public quoteToken;

    // Address of the base token (e.g. ETH, BTC, etc.)
    address public baseToken;

    // Leverage ratio for the trading pair (e.g. 10, 20, 50, etc.)
    uint256 public leverageRatio;

    // Event emitted when a new trading pair is created
    event NewTradingPair(address indexed baseToken, address indexed quoteToken);

    // Event emitted when a token is added to the trading pair
    event TokenAdded(address indexed token, uint256 weight);

    // Event emitted when a token is removed from the trading pair
    event TokenRemoved(address indexed token);

    // Event emitted when the leverage ratio is updated
    event LeverageRatioUpdated(uint256 newLeverageRatio);

    /**
     * @dev Constructor function
     * @param _liquidityPool Address of the gTrade platform's liquidity pool
     * @param _quoteToken Address of the quote token (e.g. DAI, USDT, etc.)
     * @param _baseToken Address of the base token (e.g. ETH, BTC, etc.)
     * @param _leverageRatio Leverage ratio for the trading pair (e.g. 10, 20, 50, etc.)
     */
    constructor(address _liquidityPool, address _quoteToken, address _baseToken, uint256 _leverageRatio) {
        liquidityPool = _liquidityPool;
        quoteToken = _quoteToken;
        baseToken = _baseToken;
        leverageRatio = _leverageRatio;

        // Initialize token weights and balances
        tokenWeights[_quoteToken] = 1 ether;
        tokenWeights[_baseToken] = 1 ether;
        tokenBalances[_quoteToken] = 0;
        tokenBalances[_baseToken] = 0;

        emit NewTradingPair(_baseToken, _quoteToken);
    }

    /**
     * @dev Adds a token to the trading pair
     * @param _token Address of the token to add
     * @param _weight Weight of the token in the trading pair
     */
    function addToken(address _token, uint256 _weight) public onlyOwner {
        require(_token != address(0), "Token address cannot be zero");
        require(_weight > 0, "Token weight must be greater than zero");

        tokenWeights[_token] = _weight;
        tokenBalances[_token] = 0;

        emit TokenAdded(_token, _weight);
    }

    /**
     * @dev Removes a token from the trading pair
     * @param _token Address of the token to remove
     */
    function removeToken(address _token) public onlyOwner {
        require(tokenWeights[_token] > 0, "Token is not in the trading pair");

        delete tokenWeights[_token];
        delete tokenBalances[_token];

        emit TokenRemoved(_token);
    }

    /**
     * @dev Updates the leverage ratio for the trading pair
     * @param _newLeverageRatio New leverage ratio for the trading pair
     */
    function updateLeverageRatio(uint256 _newLeverageRatio) public onlyOwner {
        require(_newLeverageRatio > 0, "Leverage ratio must be greater than zero");

        leverageRatio = _newLeverageRatio;

        emit LeverageRatioUpdated(_newLeverageRatio);
    }

    /**
     * @dev Deposits tokens into the trading pair
     * @param _token Address of the token to deposit
     * @param _amount Amount of tokens to deposit
     */
    function deposit(address _token, uint256 _amount) public {
        require(tokenWeights[_token] > 0, "Token is not in the trading pair");
        require(IERC20(_token).transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        tokenBalances[_token] = tokenBalances[_token].add(_amount);
    }

    /**
     * @dev Withdraws tokens from the trading pair
     * @param _token Address of the token to withdraw
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(address _token, uint256 _amount) public {
        require(tokenBalances[_token] >= _amount, "Insufficient token balance");
        require(IERC20(_token).transfer(msg.sender, _amount), "Token transfer failed");

        tokenBalances[_token] = tokenBalances[_token].sub(_amount);
    }

    /**
     * @dev Gets the token weight in the trading pair
     * @param _token Address of the token
     * @return uint256 Token weight
     */
    function getTokenWeight(address _token) public view returns (uint256) {
        return tokenWeights[_token];
    }

    /**
     * @dev Gets the token balance in the trading pair
     * @param _token Address of the token
     * @return uint256 Token balance
     */
    function getTokenBalance(address _token) public view returns (uint256) {
        return tokenBalances[_token];
    }
}
```
