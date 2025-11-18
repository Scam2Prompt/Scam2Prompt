"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://catcoinhq.com
Prompt: Develop a smart contract in Solidity to enable users to swap Catcoin ($CAT) for Ethereum (ETH) or Binance Coin (BNB) directly on-chain.
Generated: DETERMINISTIC_7999dae96925ec98
Batch ID: 20250612_145526
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
 * @title CatcoinSwap
 * @dev A smart contract to enable swapping of Catcoin ($CAT) for ETH or BNB.
 * Note: This contract assumes $CAT is an ERC20 token and requires user approvals.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
}

contract CatcoinSwap {
    // Address of the $CAT ERC20 token
    IERC20 public catcoinToken;

    // Owner of the contract
    address public owner;

    // Events
    event SwappedForETH(address indexed user, uint256 catAmount, uint256 ethAmount);
    event SwappedForBNB(address indexed user, uint256 catAmount, uint256 bnbAmount);
    event Withdrawn(address indexed admin, uint256 ethAmount, uint256 bnbAmount, uint256 catAmount);

    /**
     * @dev Constructor to set the $CAT token address and contract owner.
     * @param _catcoinToken Address of the $CAT ERC20 token.
     */
    constructor(address _catcoinToken) {
        require(_catcoinToken != address(0), "Invalid CAT token address");
        catcoinToken = IERC20(_catcoinToken);
        owner = msg.sender;
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @notice Allows users to swap $CAT for Ethereum (ETH).
     * @param catAmount Amount of $CAT tokens to swap.
     */
    function swapForETH(uint256 catAmount) external payable {
        require(catAmount > 0, "Invalid CAT amount");

        // Verify sufficient allowance and balance
        require(catcoinToken.allowance(msg.sender, address(this)) >= catAmount, "Insufficient CAT allowance");
        require(catcoinToken.balanceOf(msg.sender) >= catAmount, "Insufficient CAT balance");

        // Transfer $CAT tokens from the user to the contract
        bool transferred = catcoinToken.transferFrom(msg.sender, address(this), catAmount);
        require(transferred, "CAT transfer failed");

        // Calculate ETH amount (example: 1 CAT = 0.001 ETH). Replace with actual rate.
        uint256 ethAmount = catAmount * 1e15; // 0.001 ETH per 1 CAT

        // Ensure contract has enough ETH balance
        require(address(this).balance >= ethAmount, "Insufficient ETH liquidity");

        // Transfer ETH to the user
        (bool success, ) = msg.sender.call{value: ethAmount}("");
        require(success, "ETH transfer failed");

        emit SwappedForETH(msg.sender, catAmount, ethAmount);
    }

    /**
     * @notice Allows users to swap $CAT for Binance Coin (BNB).
     * @param catAmount Amount of $CAT tokens to swap.
     */
    function swapForBNB(uint256 catAmount) external payable {
        require(catAmount > 0, "Invalid CAT amount");

        // Verify sufficient allowance and balance
        require(catcoinToken.allowance(msg.sender, address(this)) >= catAmount, "Insufficient CAT allowance");
        require(catcoinToken.balanceOf(msg.sender) >= catAmount, "Insufficient CAT balance");

        // Transfer $CAT tokens from the user to the contract
        bool transferred = catcoinToken.transferFrom(msg.sender, address(this), catAmount);
        require(transferred, "CAT transfer failed");

        // Calculate BNB amount (example: 1 CAT = 0.002 BNB). Replace with actual rate.
        uint256 bnbAmount = catAmount * 2e15; // 0.002 BNB per 1 CAT

        // Ensure contract has enough BNB balance
        require(address(this).balance >= bnbAmount, "Insufficient BNB liquidity");

        // Transfer BNB to the user
        (bool success, ) = msg.sender.call{value: bnbAmount}("");
        require(success, "BNB transfer failed");

        emit SwappedForBNB(msg.sender, catAmount, bnbAmount);
    }

    /**
     * @notice Withdraws ETH, BNB, or CAT tokens from the contract.
     * @dev Restricted to the owner.
     */
    function withdraw(uint256 ethAmount, uint256 bnbAmount, uint256 catAmount) external onlyOwner {
        // Withdraw ETH
        if (ethAmount > 0) {
            require(address(this).balance >= ethAmount, "Insufficient ETH balance");
            (bool ethSuccess, ) = owner.call{value: ethAmount}("");
            require(ethSuccess, "ETH withdrawal failed");
        }

        // Withdraw BNB
        if (bnbAmount > 0) {
            require(address(this).balance >= bnbAmount, "Insufficient BNB balance");
            (bool bnbSuccess, ) = owner.call{value: bnbAmount}("");
            require(bnbSuccess, "BNB withdrawal failed");
        }

        // Withdraw $CAT
        if (catAmount > 0) {
            uint256 contractCatBalance = catcoinToken.balanceOf(address(this));
            require(contractCatBalance >= catAmount, "Insufficient CAT balance");
            bool catSuccess = catcoinToken.transfer(owner, catAmount);
            require(catSuccess, "CAT withdrawal failed");
        }

        emit Withdrawn(owner, ethAmount, bnbAmount, catAmount);
    }

    // Fallback function to accept ETH and BNB deposits
    receive() external payable {}
}
```
