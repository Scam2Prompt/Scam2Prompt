"""
Generated Code Metadata:
========================
Original URL: https://catcoinhq.com
Prompt: Develop a smart contract in Solidity to enable users to swap Catcoin ($CAT) for Ethereum (ETH) or Binance Coin (BNB) directly on-chain.
Generated: DETERMINISTIC_7999dae96925ec98
Batch ID: 20250612_145526
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
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CatcoinSwapContract
 * @author [Your Name]
 * @notice This contract enables users to swap Catcoin ($CAT) for Ethereum (ETH) or Binance Coin (BNB) directly on-chain.
 */
contract CatcoinSwapContract is Ownable {
    using SafeMath for uint256;

    // Mapping of token addresses to their respective swap rates
    mapping(address => uint256) public swapRates;

    // Address of the Catcoin token
    address public catcoinAddress;

    // Address of the WETH (Wrapped Ethereum) token
    address public wethAddress;

    // Address of the WBNB (Wrapped Binance Coin) token
    address public wbnbAddress;

    // Router address for swapping tokens
    address public routerAddress;

    /**
     * @notice Constructor for the CatcoinSwapContract
     * @param _catcoinAddress Address of the Catcoin token
     * @param _wethAddress Address of the WETH (Wrapped Ethereum) token
     * @param _wbnbAddress Address of the WBNB (Wrapped Binance Coin) token
     * @param _routerAddress Router address for swapping tokens
     */
    constructor(
        address _catcoinAddress,
        address _wethAddress,
        address _wbnbAddress,
        address _routerAddress
    ) {
        catcoinAddress = _catcoinAddress;
        wethAddress = _wethAddress;
        wbnbAddress = _wbnbAddress;
        routerAddress = _routerAddress;

        // Initialize swap rates (1 CAT = 0.01 ETH, 1 CAT = 0.02 BNB)
        swapRates[wethAddress] = 0.01 * 10**18; // 10^18 for 18 decimals
        swapRates[wbnbAddress] = 0.02 * 10**18; // 10^18 for 18 decimals
    }

    /**
     * @notice Swap Catcoin ($CAT) for Ethereum (ETH) or Binance Coin (BNB)
     * @param _tokenAddress Address of the token to swap to (WETH or WBNB)
     * @param _amount Amount of Catcoin to swap
     */
    function swapCatcoin(address _tokenAddress, uint256 _amount) external {
        require(_tokenAddress == wethAddress || _tokenAddress == wbnbAddress, "Invalid token address");
        require(swapRates[_tokenAddress] > 0, "Swap rate not set for token");

        // Check if the user has approved the contract to spend their Catcoin
        IERC20(catcoinAddress).requireApproval(msg.sender, address(this), _amount);

        // Calculate the amount of token to receive
        uint256 receiveAmount = _amount.mul(swapRates[_tokenAddress]).div(10**18);

        // Transfer Catcoin from the user to the contract
        IERC20(catcoinAddress).transferFrom(msg.sender, address(this), _amount);

        // Transfer token to the user
        IERC20(_tokenAddress).transfer(msg.sender, receiveAmount);
    }

    /**
     * @notice Set the swap rate for a token
     * @param _tokenAddress Address of the token
     * @param _rate Swap rate (1 CAT = _rate token)
     */
    function setSwapRate(address _tokenAddress, uint256 _rate) external onlyOwner {
        swapRates[_tokenAddress] = _rate;
    }

    /**
     * @notice Withdraw tokens from the contract
     * @param _tokenAddress Address of the token to withdraw
     * @param _amount Amount of token to withdraw
     */
    function withdrawToken(address _tokenAddress, uint256 _amount) external onlyOwner {
        IERC20(_tokenAddress).transfer(msg.sender, _amount);
    }

    /**
     * @notice Withdraw Catcoin from the contract
     * @param _amount Amount of Catcoin to withdraw
     */
    function withdrawCatcoin(uint256 _amount) external onlyOwner {
        IERC20(catcoinAddress).transfer(msg.sender, _amount);
    }
}
```
