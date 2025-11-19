"""
Generated Code Metadata:
========================
Original URL: https://apatheia.pages.dev
Prompt: Create a smart contract or backend logic to retrieve token data and calculate hypothetical earnings for a wallet, as seen on the Apatheia platform.
Generated: DETERMINISTIC_db203a1119e304f8
Batch ID: 20250612_153517
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract TokenEarningsCalculator {
    using SafeMath for uint256;

    struct TokenData {
        address tokenAddress;
        string symbol;
        uint256 balance;
        uint256 priceInETH;
        uint256 priceInUSD;
        uint256 potentialEarnings;
    }

    address public owner;
    uint256 public ethPriceInUSD;

    event TokenDataRetrieved(address indexed wallet, TokenData[] tokens);
    event EarningsCalculated(address indexed wallet, uint256 totalPotentialEarnings);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(uint256 _ethPriceInUSD) {
        owner = msg.sender;
        ethPriceInUSD = _ethPriceInUSD;
    }

    function setEthPrice(uint256 _newPrice) external onlyOwner {
        ethPriceInUSD = _newPrice;
    }

    function getTokenData(
        address _wallet,
        address[] memory _tokenAddresses,
        string[] memory _symbols,
        uint256[] memory _pricesInETH
    ) external returns (TokenData[] memory) {
        require(
            _tokenAddresses.length == _symbols.length && 
            _tokenAddresses.length == _pricesInETH.length,
            "Input arrays must have same length"
        );

        TokenData[] memory tokens = new TokenData[](_tokenAddresses.length);
        
        for (uint256 i = 0; i < _tokenAddresses.length; i++) {
            uint256 balance = IERC20(_tokenAddresses[i]).balanceOf(_wallet);
            uint256 priceInUSD = _pricesInETH[i].mul(ethPriceInUSD).div(1 ether);
            
            tokens[i] = TokenData({
                tokenAddress: _tokenAddresses[i],
                symbol: _symbols[i],
                balance: balance,
                priceInETH: _pricesInETH[i],
                priceInUSD: priceInUSD,
                potentialEarnings: balance.mul(priceInUSD).div(1 ether)
            });
        }

        emit TokenDataRetrieved(_wallet, tokens);
        return tokens;
    }

    function calculateTotalEarnings(TokenData[] memory _tokens) public pure returns (uint256) {
        uint256 total = 0;
        for (uint256 i = 0; i < _tokens.length; i++) {
            total = total.add(_tokens[i].potentialEarnings);
        }
        return total;
    }

    function getWalletEarnings(
        address _wallet,
        address[] memory _tokenAddresses,
        string[] memory _symbols,
        uint256[] memory _pricesInETH
    ) external returns (uint256) {
        TokenData[] memory tokens = getTokenData(_wallet, _tokenAddresses, _symbols, _pricesInETH);
        uint256 totalEarnings = calculateTotalEarnings(tokens);
        
        emit EarningsCalculated(_wallet, totalEarnings);
        return totalEarnings;
    }
}
```
