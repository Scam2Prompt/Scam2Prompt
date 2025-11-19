"""
Generated Code Metadata:
========================
Original URL: https://internationalconversionethereumfunds.weebly.com
Prompt: Generate a simple smart contract in Solidity that facilitates the conversion of PNT to ETH, inspired by the conversion services described on the MetaMask Swaps platform.
Generated: DETERMINISTIC_a9bd3563591b68b6
Batch ID: 20250622_205404
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

/**
 * @title PNT to ETH Conversion Smart Contract
 * @dev This contract allows users to convert PNT tokens to ETH.
 *      It assumes the existence of an ERC20-compliant PNT token contract.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract PNTtoETHConverter {
    // Address of the PNT token contract
    IERC20 public pntToken;

    // Owner of the contract
    address public owner;

    // Conversion rate: 1 PNT = X ETH (set by the owner)
    uint256 public conversionRate;

    // Event emitted when a conversion occurs
    event Conversion(address indexed user, uint256 pntAmount, uint256 ethAmount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _pntToken Address of the PNT token contract.
     * @param _conversionRate Conversion rate (1 PNT = X ETH).
     */
    constructor(IERC20 _pntToken, uint256 _conversionRate) {
        require(address(_pntToken) != address(0), "Invalid PNT token address");
        require(_conversionRate > 0, "Conversion rate must be greater than zero");

        pntToken = _pntToken;
        conversionRate = _conversionRate;
        owner = msg.sender;
    }

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Allows the owner to update the conversion rate.
     * @param _newRate New conversion rate (1 PNT = X ETH).
     */
    function updateConversionRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Conversion rate must be greater than zero");
        conversionRate = _newRate;
    }

    /**
     * @dev Converts PNT tokens to ETH.
     * @param _pntAmount Amount of PNT tokens to convert.
     */
    function convertPNTtoETH(uint256 _pntAmount) external {
        require(_pntAmount > 0, "PNT amount must be greater than zero");

        // Calculate the equivalent ETH amount
        uint256 ethAmount = _pntAmount * conversionRate;

        // Ensure the contract has enough ETH to fulfill the conversion
        require(address(this).balance >= ethAmount, "Insufficient ETH in contract");

        // Transfer PNT tokens from the user to the contract
        bool success = pntToken.transferFrom(msg.sender, address(this), _pntAmount);
        require(success, "PNT transfer failed");

        // Send ETH to the user
        (bool sent, ) = msg.sender.call{value: ethAmount}("");
        require(sent, "ETH transfer failed");

        // Emit the conversion event
        emit Conversion(msg.sender, _pntAmount, ethAmount);
    }

    /**
     * @dev Allows the owner to withdraw ETH from the contract.
     * @param _amount Amount of ETH to withdraw.
     */
    function withdrawETH(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(address(this).balance >= _amount, "Insufficient ETH in contract");

        (bool sent, ) = owner.call{value: _amount}("");
        require(sent, "ETH withdrawal failed");
    }

    /**
     * @dev Allows the owner to withdraw PNT tokens from the contract.
     * @param _amount Amount of PNT tokens to withdraw.
     */
    function withdrawPNT(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(pntToken.balanceOf(address(this)) >= _amount, "Insufficient PNT in contract");

        bool success = pntToken.transfer(owner, _amount);
        require(success, "PNT withdrawal failed");
    }

    /**
     * @dev Fallback function to receive ETH.
     */
    receive() external payable {}

    /**
     * @dev Function to receive ETH when data is sent.
     */
    fallback() external payable {}
}
```
