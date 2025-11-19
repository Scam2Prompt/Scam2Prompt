"""
Generated Code Metadata:
========================
Original URL: https://milady-dfk.pages.dev
Prompt: Generate a Solidity contract for a token sale mechanism that includes stepped raises and fixed-price pools, similar to the Milady Cult presale structure.
Generated: DETERMINISTIC_a3476a2614ba538b
Batch ID: 20250612_152358
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MiladyCultPresale
 * @author [Your Name]
 * @notice Token sale mechanism with stepped raises and fixed-price pools.
 */
contract MiladyCultPresale is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of raise tiers to their respective details
    mapping(uint256 => Raise) public raises;

    // Mapping of users to their purchase history
    mapping(address => mapping(uint256 => uint256)) public userPurchases;

    // Mapping of fixed-price pools to their respective details
    mapping(uint256 => FixedPricePool) public fixedPricePools;

    // Token being sold
    ERC20Burnable public token;

    // Total number of raises
    uint256 public totalRaises;

    // Total number of fixed-price pools
    uint256 public totalFixedPricePools;

    // Event emitted when a user purchases tokens
    event Purchase(address indexed buyer, uint256 raiseId, uint256 amount);

    // Event emitted when a raise is created
    event RaiseCreated(uint256 raiseId, uint256 tier, uint256 price, uint256 cap);

    // Event emitted when a fixed-price pool is created
    event FixedPricePoolCreated(uint256 poolId, uint256 price, uint256 cap);

    // Struct representing a raise tier
    struct Raise {
        uint256 tier;
        uint256 price;
        uint256 cap;
        uint256 sold;
    }

    // Struct representing a fixed-price pool
    struct FixedPricePool {
        uint256 price;
        uint256 cap;
        uint256 sold;
    }

    /**
     * @notice Initializes the contract with the token being sold.
     * @param _token Address of the token being sold.
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = ERC20Burnable(_token);
    }

    /**
     * @notice Creates a new raise tier.
     * @param _tier Tier number of the raise.
     * @param _price Price of the token in the raise.
     * @param _cap Cap of the raise.
     */
    function createRaise(uint256 _tier, uint256 _price, uint256 _cap) public {
        require(_price > 0, "Price must be greater than zero");
        require(_cap > 0, "Cap must be greater than zero");

        raises[totalRaises] = Raise(_tier, _price, _cap, 0);
        totalRaises++;

        emit RaiseCreated(totalRaises - 1, _tier, _price, _cap);
    }

    /**
     * @notice Creates a new fixed-price pool.
     * @param _price Price of the token in the pool.
     * @param _cap Cap of the pool.
     */
    function createFixedPricePool(uint256 _price, uint256 _cap) public {
        require(_price > 0, "Price must be greater than zero");
        require(_cap > 0, "Cap must be greater than zero");

        fixedPricePools[totalFixedPricePools] = FixedPricePool(_price, _cap, 0);
        totalFixedPricePools++;

        emit FixedPricePoolCreated(totalFixedPricePools - 1, _price, _cap);
    }

    /**
     * @notice Purchases tokens from a raise tier.
     * @param _raiseId ID of the raise tier.
     * @param _amount Amount of tokens to purchase.
     */
    function purchaseFromRaise(uint256 _raiseId, uint256 _amount) public nonReentrant {
        require(_raiseId < totalRaises, "Raise ID out of range");
        require(_amount > 0, "Amount must be greater than zero");

        Raise storage raise = raises[_raiseId];
        require(raise.sold.add(_amount) <= raise.cap, "Amount exceeds raise cap");

        uint256 cost = _amount.mul(raise.price);
        require(token.balanceOf(address(this)) >= _amount, "Insufficient tokens in contract");

        userPurchases[msg.sender][_raiseId] = userPurchases[msg.sender][_raiseId].add(_amount);
        raise.sold = raise.sold.add(_amount);

        token.transfer(msg.sender, _amount);

        emit Purchase(msg.sender, _raiseId, _amount);
    }

    /**
     * @notice Purchases tokens from a fixed-price pool.
     * @param _poolId ID of the fixed-price pool.
     * @param _amount Amount of tokens to purchase.
     */
    function purchaseFromFixedPricePool(uint256 _poolId, uint256 _amount) public nonReentrant {
        require(_poolId < totalFixedPricePools, "Pool ID out of range");
        require(_amount > 0, "Amount must be greater than zero");

        FixedPricePool storage pool = fixedPricePools[_poolId];
        require(pool.sold.add(_amount) <= pool.cap, "Amount exceeds pool cap");

        uint256 cost = _amount.mul(pool.price);
        require(token.balanceOf(address(this)) >= _amount, "Insufficient tokens in contract");

        userPurchases[msg.sender][_poolId] = userPurchases[msg.sender][_poolId].add(_amount);
        pool.sold = pool.sold.add(_amount);

        token.transfer(msg.sender, _amount);

        emit Purchase(msg.sender, _poolId, _amount);
    }

    /**
     * @notice Refunds a user for a raise or fixed-price pool.
     * @param _raiseId ID of the raise tier or fixed-price pool.
     */
    function refund(uint256 _raiseId) public nonReentrant {
        require(_raiseId < totalRaises || _raiseId < totalFixedPricePools, "ID out of range");

        if (_raiseId < totalRaises) {
            Raise storage raise = raises[_raiseId];
            uint256 amount = userPurchases[msg.sender][_raiseId];
            require(amount > 0, "User has no purchases in this raise");

            userPurchases[msg.sender][_raiseId] = 0;
            token.transfer(msg.sender, amount);
        } else {
            FixedPricePool storage pool = fixedPricePools[_raiseId - totalRaises];
            uint256 amount = userPurchases[msg.sender][_raiseId];
            require(amount > 0, "User has no purchases in this pool");

            userPurchases[msg.sender][_raiseId] = 0;
            token.transfer(msg.sender, amount);
        }
    }
}
```
