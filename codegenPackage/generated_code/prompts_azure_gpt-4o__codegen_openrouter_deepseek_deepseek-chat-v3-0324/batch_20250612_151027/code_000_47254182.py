"""
Generated Code Metadata:
========================
Original URL: https://moxie.credit
Prompt: Write a smart contract for launching Fan Tokens using Moxie Bonding Curves, ensuring utility-focused price discovery as described in the Moxie Protocol documentation.
Generated: DETERMINISTIC_472541826768fb7c
Batch ID: 20250612_151027
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title FanToken
 * @dev Implementation of a Fan Token using Moxie Bonding Curves for price discovery
 */
contract FanToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Bonding curve parameters
    uint256 public reserveRatio; // Reserve ratio in basis points (1-10000)
    uint256 public initialPrice; // Initial price in wei
    uint256 public initialSupply; // Initial token supply
    uint256 public reserveBalance; // Current reserve balance in wei

    // Events
    event TokensMinted(address indexed buyer, uint256 amount, uint256 cost);
    event TokensBurned(address indexed seller, uint256 amount, uint256 refund);

    /**
     * @dev Constructor
     * @param _name Token name
     * @param _symbol Token symbol
     * @param _reserveRatio Reserve ratio (1-10000)
     * @param _initialPrice Initial price in wei
     * @param _initialSupply Initial token supply
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _reserveRatio,
        uint256 _initialPrice,
        uint256 _initialSupply
    ) ERC20(_name, _symbol) {
        require(_reserveRatio > 0 && _reserveRatio <= 10000, "Invalid reserve ratio");
        require(_initialPrice > 0, "Initial price must be positive");
        require(_initialSupply > 0, "Initial supply must be positive");

        reserveRatio = _reserveRatio;
        initialPrice = _initialPrice;
        initialSupply = _initialSupply;

        // Mint initial supply to contract creator
        _mint(msg.sender, _initialSupply);
    }

    /**
     * @dev Calculate price to buy tokens
     * @param _amount Amount of tokens to buy
     * @return price in wei
     */
    function calculatePurchasePrice(uint256 _amount) public view returns (uint256) {
        require(_amount > 0, "Amount must be positive");
        
        uint256 supply = totalSupply();
        uint256 newSupply = supply.add(_amount);
        
        return _integralPrice(supply, newSupply);
    }

    /**
     * @dev Calculate refund for selling tokens
     * @param _amount Amount of tokens to sell
     * @return refund in wei
     */
    function calculateSaleRefund(uint256 _amount) public view returns (uint256) {
        require(_amount > 0, "Amount must be positive");
        require(balanceOf(msg.sender) >= _amount, "Insufficient balance");
        
        uint256 supply = totalSupply();
        uint256 newSupply = supply.sub(_amount);
        
        return _integralPrice(newSupply, supply);
    }

    /**
     * @dev Buy tokens by sending ETH
     */
    function buyTokens() external payable {
        require(msg.value > 0, "Must send ETH to buy tokens");
        
        uint256 supply = totalSupply();
        uint256 amount = _calculateMintAmount(msg.value, supply);
        
        require(amount > 0, "Amount must be positive");
        
        _mint(msg.sender, amount);
        reserveBalance = reserveBalance.add(msg.value);
        
        emit TokensMinted(msg.sender, amount, msg.value);
    }

    /**
     * @dev Sell tokens and receive ETH
     * @param _amount Amount of tokens to sell
     */
    function sellTokens(uint256 _amount) external {
        require(_amount > 0, "Amount must be positive");
        require(balanceOf(msg.sender) >= _amount, "Insufficient balance");
        
        uint256 refund = calculateSaleRefund(_amount);
        require(address(this).balance >= refund, "Insufficient contract balance");
        
        _burn(msg.sender, _amount);
        reserveBalance = reserveBalance.sub(refund);
        
        payable(msg.sender).transfer(refund);
        emit TokensBurned(msg.sender, _amount, refund);
    }

    /**
     * @dev Internal function to calculate integral price between two supply points
     */
    function _integralPrice(uint256 _fromSupply, uint256 _toSupply) internal view returns (uint256) {
        if (_fromSupply == 0) {
            return initialPrice.mul(_toSupply);
        }
        
        uint256 fromValue = _bondingCurveIntegral(_fromSupply);
        uint256 toValue = _bondingCurveIntegral(_toSupply);
        
        return toValue.sub(fromValue);
    }

    /**
     * @dev Internal bonding curve integral calculation
     */
    function _bondingCurveIntegral(uint256 _supply) internal view returns (uint256) {
        uint256 ratio = reserveRatio;
        uint256 exponent = 1e36 / ratio;
        
        // Calculate (supply + initialSupply)^exponent
        uint256 term = _supply.add(initialSupply).pow(exponent);
        return term.mul(initialPrice).div(initialSupply.pow(exponent));
    }

    /**
     * @dev Internal function to calculate mint amount for given ETH
     */
    function _calculateMintAmount(uint256 _ethAmount, uint256 _currentSupply) internal view returns (uint256) {
        if (_currentSupply == 0) {
            return _ethAmount.div(initialPrice);
        }
        
        uint256 ratio = reserveRatio;
        uint256 exponent = ratio / 1e36;
        
        uint256 term = reserveBalance.add(_ethAmount).pow(exponent);
        term = term.mul(_currentSupply.add(initialSupply)).div(reserveBalance.pow(exponent));
        
        return term.sub(_currentSupply.add(initialSupply));
    }

    /**
     * @dev Withdraw ETH from contract (owner only)
     */
    function withdraw(uint256 _amount) external onlyOwner {
        require(_amount <= address(this).balance, "Insufficient balance");
        payable(owner()).transfer(_amount);
    }

    /**
     * @dev Receive ETH fallback
     */
    receive() external payable {
        buyTokens();
    }
}
```
