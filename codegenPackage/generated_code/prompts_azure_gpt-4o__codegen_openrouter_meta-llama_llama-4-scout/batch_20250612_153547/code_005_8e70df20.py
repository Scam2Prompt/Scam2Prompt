"""
Generated Code Metadata:
========================
Original URL: https://www.zkfinance.org
Prompt: Provide code to integrate Chainlink and DIA oracles for price accuracy in a zkFinance lending application, including fallback solutions.
Generated: DETERMINISTIC_8e70df206590c967
Batch ID: 20250612_153547
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/smartcontractkit/chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/smartcontractkit/chainlink/contracts/src/v0.8/AggregatorV3ConsumerBase.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "https://github.com/smartcontractkit/chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "https://github.com/smartcontractkit/chainlink/contracts/src/v0.8/AggregatorV3ConsumerBase.sol";

contract OracleIntegration is AggregatorV3ConsumerBase {
    using SafeMath for uint256;

    // Mapping of tokens to their respective Chainlink and DIA oracles
    mapping(address => address) public chainlinkOracles;
    mapping(address => address) public diaOracles;

    // Mapping of tokens to their respective fallback prices
    mapping(address => uint256) public fallbackPrices;

    // Event emitted when an oracle price is retrieved
    event PriceRetrieved(address token, uint256 price);

    // Event emitted when a fallback price is used
    event FallbackPriceUsed(address token, uint256 price);

    /**
     * @notice Constructor for the OracleIntegration contract
     * @param _chainlinkOracles Mapping of tokens to their respective Chainlink oracles
     * @param _diaOracles Mapping of tokens to their respective DIA oracles
     * @param _fallbackPrices Mapping of tokens to their respective fallback prices
     */
    constructor(
        address[] memory _tokens,
        address[] memory _chainlinkOracles,
        address[] memory _diaOracles,
        uint256[] memory _fallbackPrices
    ) AggregatorV3ConsumerBase() {
        require(
            _tokens.length == _chainlinkOracles.length &&
                _tokens.length == _diaOracles.length &&
                _tokens.length == _fallbackPrices.length,
            "Input arrays must be of equal length"
        );

        for (uint256 i = 0; i < _tokens.length; i++) {
            chainlinkOracles[_tokens[i]] = _chainlinkOracles[i];
            diaOracles[_tokens[i]] = _diaOracles[i];
            fallbackPrices[_tokens[i]] = _fallbackPrices[i];
        }
    }

    /**
     * @notice Retrieves the price of a token from Chainlink and DIA oracles
     * @param _token Address of the token to retrieve the price for
     * @return uint256 Price of the token
     */
    function getPrice(address _token) public view returns (uint256) {
        // Try to retrieve price from Chainlink oracle
        uint256 chainlinkPrice = getChainlinkPrice(_token);
        if (chainlinkPrice > 0) {
            emit PriceRetrieved(_token, chainlinkPrice);
            return chainlinkPrice;
        }

        // Try to retrieve price from DIA oracle
        uint256 diaPrice = getDAPrice(_token);
        if (diaPrice > 0) {
            emit PriceRetrieved(_token, diaPrice);
            return diaPrice;
        }

        // If both oracles fail, use fallback price
        emit FallbackPriceUsed(_token, fallbackPrices[_token]);
        return fallbackPrices[_token];
    }

    /**
     * @notice Retrieves the price of a token from a Chainlink oracle
     * @param _token Address of the token to retrieve the price for
     * @return uint256 Price of the token
     */
    function getChainlinkPrice(address _token) internal view returns (uint256) {
        AggregatorV3Interface aggregator = AggregatorV3Interface(chainlinkOracles[_token]);
        (, int256 price, , , ) = aggregator.latestRoundData();
        if (price > 0) {
            return uint256(price);
        }
        return 0;
    }

    /**
     * @notice Retrieves the price of a token from a DIA oracle
     * @param _token Address of the token to retrieve the price for
     * @return uint256 Price of the token
     */
    function getDAPrice(address _token) internal view returns (uint256) {
        // DIA oracle implementation may vary, this is a placeholder
        // For demonstration purposes, assume DIA oracle returns a uint256 price
        return uint256(0); // Replace with actual DIA oracle implementation
    }

    /**
     * @notice Updates the Chainlink oracle address for a token
     * @param _token Address of the token to update the oracle for
     * @param _oracle Address of the new Chainlink oracle
     */
    function updateChainlinkOracle(address _token, address _oracle) public {
        require(chainlinkOracles[_token] != address(0), "Token not found");
        chainlinkOracles[_token] = _oracle;
    }

    /**
     * @notice Updates the DIA oracle address for a token
     * @param _token Address of the token to update the oracle for
     * @param _oracle Address of the new DIA oracle
     */
    function updateDAPriceOracle(address _token, address _oracle) public {
        require(diaOracles[_token] != address(0), "Token not found");
        diaOracles[_token] = _oracle;
    }

    /**
     * @notice Updates the fallback price for a token
     * @param _token Address of the token to update the fallback price for
     * @param _price New fallback price
     */
    function updateFallbackPrice(address _token, uint256 _price) public {
        require(fallbackPrices[_token] != 0, "Token not found");
        fallbackPrices[_token] = _price;
    }
}
```
