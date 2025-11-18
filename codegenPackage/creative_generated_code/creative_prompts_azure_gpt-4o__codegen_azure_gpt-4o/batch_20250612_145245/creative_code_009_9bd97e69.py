"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.unisocks.fi
Prompt: Develop a smart contract that interacts with the Unisocks platform to facilitate the buying and selling of $SOCKS tokens.
Generated: DETERMINISTIC_9bd97e69ccb5980f
Batch ID: 20250612_145245
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

// Import OpenZeppelin libraries for safe math operations and access control
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title UnisocksTradingContract
 * @dev A smart contract to facilitate the buying and selling of $SOCKS tokens.
 */
contract UnisocksTradingContract is Ownable {
    // Address of the $SOCKS token contract
    IERC20 public socksToken;

    // Event emitted when $SOCKS tokens are bought
    event SocksPurchased(address indexed buyer, uint256 amount, uint256 cost);

    // Event emitted when $SOCKS tokens are sold
    event SocksSold(address indexed seller, uint256 amount, uint256 revenue);

    /**
     * @dev Constructor to initialize the $SOCKS token contract address.
     * @param _socksToken The address of the $SOCKS token contract.
     */
    constructor(address _socksToken) {
        require(_socksToken != address(0), "Invalid token address");
        socksToken = IERC20(_socksToken);
    }

    /**
     * @dev Allows users to buy $SOCKS using Ether.
     * The contract owner should deposit $SOCKS tokens into this contract beforehand.
     */
    function buySocks(uint256 socksAmount) external payable {
        uint256 tokenPriceInWei = getCurrentSocksPrice();
        uint256 totalCost = tokenPriceInWei * socksAmount;

        require(msg.value >= totalCost, "Insufficient Ether sent");
        require(
            socksToken.balanceOf(address(this)) >= socksAmount,
            "Not enough $SOCKS available in the contract"
        );

        // Transfer $SOCKS tokens to the buyer
        socksToken.transfer(msg.sender, socksAmount);

        // Emit event upon successful purchase
        emit SocksPurchased(msg.sender, socksAmount, totalCost);

        // Refund excess Ether sent, if applicable
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }
    }

    /**
     * @dev Allows users to sell $SOCKS in exchange for Ether.
     */
    function sellSocks(uint256 socksAmount) external {
        uint256 tokenPriceInWei = getCurrentSocksPrice();
        uint256 totalRevenue = tokenPriceInWei * socksAmount;

        require(
            address(this).balance >= totalRevenue,
            "Contract does not have enough Ether"
        );

        require(
            socksToken.balanceOf(msg.sender) >= socksAmount,
            "$SOCKS balance too low"
        );

        // Transfer $SOCKS tokens from the seller to the contract
        require(
            socksToken.transferFrom(msg.sender, address(this), socksAmount),
            "Token transfer failed"
        );

        // Pay Ether to the seller
        payable(msg.sender).transfer(totalRevenue);

        // Emit event upon successful sale
        emit SocksSold(msg.sender, socksAmount, totalRevenue);
    }

    /**
     * @dev Get the current price of $SOCKS token in Wei.
     * This is a placeholder function and should be replaced with actual price feed logic.
     */
    function getCurrentSocksPrice() public pure returns (uint256) {
        return 1 ether; // 1 $SOCKS = 1 Ether (for demonstration purposes)
    }

    /**
     * @dev Allows the owner to withdraw Ether from the contract.
     */
    function withdrawEther(uint256 amount) external onlyOwner {
        require(
            address(this).balance >= amount,
            "Insufficient Ether balance"
        );
        payable(owner()).transfer(amount);
    }

    /**
     * @dev Allows the owner to withdraw $SOCKS tokens from the contract.
     */
    function withdrawSocks(uint256 amount) external onlyOwner {
        require(
            socksToken.balanceOf(address(this)) >= amount,
            "Insufficient $SOCKS balance"
        );
        socksToken.transfer(owner(), amount);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Fallback function to handle unknown calls.
     */
    fallback() external payable {}
}
```
