"""
Generated Code Metadata:
========================
Original URL: https://www.unisocks.fi
Prompt: Develop a smart contract that interacts with the Unisocks platform to facilitate the buying and selling of $SOCKS tokens.
Generated: DETERMINISTIC_9bd97e69ccb5980f
Batch ID: 20250612_145245
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IUnisocks {
    function token() external view returns (address);
    function getCurrentPrice() external view returns (uint256);
    function buy(uint256 amount) external payable;
    function withdraw(uint256 amount) external;
}

contract SocksMarket is Ownable, ReentrancyGuard {
    IUnisocks public unisocks;
    IERC20 public socksToken;

    event Bought(address indexed buyer, uint256 amount, uint256 totalPrice);
    event Sold(address indexed seller, uint256 amount, uint256 totalPrice);
    event Withdrawn(address indexed owner, uint256 amount);

    constructor(address _unisocksAddress) {
        require(_unisocksAddress != address(0), "Invalid Unisocks address");
        unisocks = IUnisocks(_unisocksAddress);
        socksToken = IERC20(unisocks.token());
    }

    /**
     * @dev Buy SOCKS tokens from Unisocks
     * @param amount Number of SOCKS tokens to buy
     */
    function buySocks(uint256 amount) external payable nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        uint256 price = unisocks.getCurrentPrice() * amount;
        require(msg.value >= price, "Insufficient ETH sent");
        
        unisocks.buy{value: price}(amount);
        
        // Transfer SOCKS tokens to buyer
        require(socksToken.transfer(msg.sender, amount), "SOCKS transfer failed");
        
        // Refund any excess ETH
        if (msg.value > price) {
            payable(msg.sender).transfer(msg.value - price);
        }
        
        emit Bought(msg.sender, amount, price);
    }

    /**
     * @dev Sell SOCKS tokens back to Unisocks
     * @param amount Number of SOCKS tokens to sell
     */
    function sellSocks(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer SOCKS tokens from seller to this contract
        require(socksToken.transferFrom(msg.sender, address(this), amount), "SOCKS transfer failed");
        
        // Approve Unisocks to spend SOCKS tokens
        require(socksToken.approve(address(unisocks), amount), "Approval failed");
        
        // Withdraw ETH from Unisocks
        unisocks.withdraw(amount);
        
        // Transfer ETH to seller
        payable(msg.sender).transfer(address(this).balance);
        
        emit Sold(msg.sender, amount, unisocks.getCurrentPrice() * amount);
    }

    /**
     * @dev Withdraw ETH from contract (owner only)
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        
        payable(owner()).transfer(balance);
        emit Withdrawn(owner(), balance);
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent by mistake
     * @param tokenAddress Address of the token contract
     * @param tokenAmount Amount of tokens to recover
     */
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(socksToken), "Cannot recover SOCKS tokens");
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
