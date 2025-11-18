"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-scottytheai-io.pages.dev
Prompt: Develop a Solidity contract to facilitate token swaps on Scotty Swap, ensuring secure and optimized transactions for $SCOTTY tokens.
Generated: DETERMINISTIC_4ad2c1f7aea43716
Batch ID: 20250612_152620
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

/**
 * @title ScottySwap
 * @dev A contract to facilitate secure token swaps for $SCOTTY tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract ScottySwap {
    // Address of the $SCOTTY token contract
    address public immutable scottyToken;

    // Address of the owner/admin for contract management
    address public owner;

    // Event emitted for token swap transactions
    event TokenSwap(address indexed user, uint256 tokenOutAmount, uint256 ethAmount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Initializes the contract with the $SCOTTY token address.
     * @param _scottyToken Address of the $SCOTTY token contract.
     */
    constructor(address _scottyToken) {
        require(_scottyToken != address(0), "Invalid token address");
        scottyToken = _scottyToken;
        owner = msg.sender; // Set the deployer as the contract owner
    }

    /**
     * @dev Allows token swaps for $SCOTTY. Users send ETH and receive $SCOTTY tokens.
     * @param tokenOutAmount Amount of $SCOTTY tokens to be swapped for the sent ETH.
     */
    function swap(uint256 tokenOutAmount) external payable {
        require(msg.value > 0, "ETH required for swap");
        require(tokenOutAmount > 0, "Invalid token out amount");

        uint256 scottyBalance = IERC20(scottyToken).balanceOf(address(this));
        require(scottyBalance >= tokenOutAmount, "Insufficient $SCOTTY token liquidity");

        // Transfer the $SCOTTY tokens to the sender
        bool success = IERC20(scottyToken).transfer(msg.sender, tokenOutAmount);
        require(success, "Token transfer failed");

        // Emit the swap event
        emit TokenSwap(msg.sender, tokenOutAmount, msg.value);
    }

    /**
     * @dev Allows the owner to withdraw ETH collected in the contract.
     * @param amount Amount of ETH to withdraw.
     */
    function withdrawETH(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient ETH balance");
        payable(owner).transfer(amount);
    }

    /**
     * @dev Allows the owner to withdraw $SCOTTY tokens from the contract.
     * @param amount Amount of $SCOTTY tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(IERC20(scottyToken).balanceOf(address(this)) >= amount, "Insufficient token balance");

        // Transfer the tokens to the owner
        bool success = IERC20(scottyToken).transfer(owner, amount);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Fallback function to accept ETH. This enables direct deposits to the contract.
     */
    receive() external payable {}

    /**
     * @dev Function to check the ETH balance of the contract.
     * @return The ETH balance of the contract.
     */
    function getEthBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Function to check the $SCOTTY token balance of the contract.
     * @return The $SCOTTY token balance of the contract.
     */
    function getTokenBalance() external view returns (uint256) {
        return IERC20(scottyToken).balanceOf(address(this));
    }
}
```
