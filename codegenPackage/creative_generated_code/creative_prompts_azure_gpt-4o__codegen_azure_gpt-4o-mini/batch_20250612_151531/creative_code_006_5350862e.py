"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qubetics-claim.web.app
Prompt: Develop a smart contract in Solidity for handling TICS token purchases, including multi-currency payment options (ETH, BNB, USDT, etc.), as described on the Qubetics platform.
Generated: DETERMINISTIC_5350862e6f3eaac0
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TICSTokenSale
 * @dev A smart contract for handling TICS token purchases with multi-currency payment options.
 */
contract TICSTokenSale is Ownable {
    // Variable to track the TICS token
    IERC20 public ticsToken;

    // Price of TICS token in ETH
    uint256 public ethPrice;
    // Price of TICS token in BNB
    uint256 public bnbPrice;
    // Price of TICS token in USDT
    uint256 public usdtPrice;

    // Event to emit when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount, string currency);

    /**
     * @dev Constructor to initialize the contract with token addresses and pricing.
     * @param _ticsToken The address of the TICS token contract
     * @param _ethPrice Price of one TICS token in ETH
     * @param _bnbPrice Price of one TICS token in BNB
     * @param _usdtPrice Price of one TICS token in USDT
     */
    constructor(
        address _ticsToken,
        uint256 _ethPrice,
        uint256 _bnbPrice,
        uint256 _usdtPrice
    ) {
        ticsToken = IERC20(_ticsToken);
        ethPrice = _ethPrice;
        bnbPrice = _bnbPrice;
        usdtPrice = _usdtPrice;
    }

    /**
     * @dev Function to buy TICS tokens with ETH.
     */
    function buyWithETH() external payable {
        require(msg.value > 0, "Must send ETH to purchase");
        uint256 amountToBuy = msg.value / ethPrice;
        require(ticsToken.balanceOf(address(this)) >= amountToBuy, "Not enough tokens available");

        // Transfer TICS tokens to buyer
        ticsToken.transfer(msg.sender, amountToBuy);
        
        emit TokensPurchased(msg.sender, amountToBuy, "ETH");
    }

    /**
     * @dev Function to buy TICS tokens with BNB.
     * Note: BNB is treated similarly to ETH in this contract.
     */
    function buyWithBNB() external payable {
        require(msg.value > 0, "Must send BNB to purchase");
        uint256 amountToBuy = msg.value / bnbPrice;
        require(ticsToken.balanceOf(address(this)) >= amountToBuy, "Not enough tokens available");

        // Transfer TICS tokens to buyer
        ticsToken.transfer(msg.sender, amountToBuy);
        
        emit TokensPurchased(msg.sender, amountToBuy, "BNB");
    }

    /**
     * @dev Function to buy TICS tokens with USDT.
     * @param amount The amount of USDT to send for purchase
     * @param usdtToken The address of the USDT token contract
     */
    function buyWithUSDT(uint256 amount, address usdtToken) external {
        require(amount > 0, "Must send USDT to purchase");
        
        // Calculate the equivalent TICS tokens
        uint256 ticsAmount = amount / usdtPrice;
        require(ticsToken.balanceOf(address(this)) >= ticsAmount, "Not enough tokens available");

        // Transfer USDT from buyer to this contract
        IERC20(usdtToken).transferFrom(msg.sender, address(this), amount);
        // Transfer TICS tokens to buyer
        ticsToken.transfer(msg.sender, ticsAmount);
        
        emit TokensPurchased(msg.sender, ticsAmount, "USDT");
    }

    /**
     * @dev Function for the owner to withdraw collected ETH, BNB, or USDT.
     * @param _token The token address to withdraw (0x0 for ETH/BNB)
     */
    function withdraw(address _token) external onlyOwner {
        if (_token == address(0)) {
            // Withdraw ETH/BNB
            payable(owner()).transfer(address(this).balance);
        } else {
            // Withdraw ERC20 tokens
            IERC20(_token).transfer(owner(), IERC20(_token).balanceOf(address(this)));
        }
    }

    /**
     * @dev Function to update the price of TICS tokens in different currencies.
     * @param _ethPrice New price of TICS token in ETH
     * @param _bnbPrice New price of TICS token in BNB
     * @param _usdtPrice New price of TICS token in USDT
     */
    function updatePrices(uint256 _ethPrice, uint256 _bnbPrice, uint256 _usdtPrice) external onlyOwner {
        ethPrice = _ethPrice;
        bnbPrice = _bnbPrice;
        usdtPrice = _usdtPrice;
    }
}
```
