"""
Generated Code Metadata:
========================
Original URL: https://to-ousd.pages.dev
Prompt: Generate a code example in Solidity to create a simple smart contract that utilizes OUSD's automated, on-chain, blue-chip stablecoin strategies, such as deploying funds to Morpho's Compound or Aave markets.
Generated: DETERMINISTIC_58c9200d4ba31c9d
Batch ID: 20250622_211131
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

// Assuming OUSD and Morpho contracts are already deployed and have the following interfaces
interface IOUSD {
    function deployFunds(address strategy) external;
    function undeployFunds(address strategy) external;
}

interface IMorpho {
    function supply(address market, uint256 amount) external;
    function withdraw(address market, uint256 amount) external;
}

contract OUSDStrategy {
    using SafeMath for uint256;

    // Mapping of supported markets
    mapping(address => bool) public supportedMarkets;

    // OUSD contract instance
    IOUSD public ousd;

    // Morpho contract instance
    IMorpho public morpho;

    // Compound market address
    address public constant COMPOUND_MARKET = 0x...;

    // Aave market address
    address public constant AAVE_MARKET = 0x...;

    /**
     * @param _ousd OUSD contract address
     * @param _morpho Morpho contract address
     */
    constructor(address _ousd, address _morpho) public {
        require(_ousd != address(0), "OUSD contract address cannot be zero");
        require(_morpho != address(0), "Morpho contract address cannot be zero");

        ousd = IOUSD(_ousd);
        morpho = IMorpho(_morpho);

        // Initialize supported markets
        supportedMarkets[COMPOUND_MARKET] = true;
        supportedMarkets[AAVE_MARKET] = true;
    }

    /**
     * Deploy funds to a Morpho market
     * @param market Market address to deploy funds to
     * @param amount Amount of funds to deploy
     */
    function deployFunds(address market, uint256 amount) public {
        require(supportedMarkets[market], "Market not supported");
        require(amount > 0, "Amount must be greater than zero");

        // Deploy funds from OUSD
        ousd.deployFunds(market);

        // Supply funds to Morpho market
        IERC20(ousd).transfer(market, amount);
        morpho.supply(market, amount);
    }

    /**
     * Undeploy funds from a Morpho market
     * @param market Market address to undeploy funds from
     * @param amount Amount of funds to undeploy
     */
    function undeployFunds(address market, uint256 amount) public {
        require(supportedMarkets[market], "Market not supported");
        require(amount > 0, "Amount must be greater than zero");

        // Withdraw funds from Morpho market
        morpho.withdraw(market, amount);

        // Undeploy funds to OUSD
        ousd.undeployFunds(market);
    }

    /**
     * Add a market to the supported markets list
     * @param market Market address to add
     */
    function addMarket(address market) public onlyOwner {
        supportedMarkets[market] = true;
    }

    /**
     * Remove a market from the supported markets list
     * @param market Market address to remove
     */
    function removeMarket(address market) public onlyOwner {
        supportedMarkets[market] = false;
    }

    modifier onlyOwner {
        require(msg.sender == owner(), "Only the owner can call this function");
        _;
    }

    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
