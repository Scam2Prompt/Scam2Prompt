"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-daomars-com.pages.dev
Prompt: Write a Solidity contract for an Initial Wallet Offering (IWO) platform similar to the MDAO Maker described in the MarsDAO ecosystem.
Generated: DETERMINISTIC_a7eca580344548d9
Batch ID: 20250612_152439
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title Initial Wallet Offering (IWO) Contract
 * @dev This contract allows users to participate in an Initial Wallet Offering.
 */
contract IWOPlatform is Ownable {
    struct Iwo {
        address tokenAddress;  // Address of the token being offered
        uint256 totalSupply;   // Total supply of tokens available for the IWO
        uint256 price;         // Price per token in wei
        uint256 tokensSold;    // Total tokens sold
        uint256 startTime;     // Start time of the IWO
        uint256 endTime;       // End time of the IWO
        bool isActive;         // Status of the IWO
    }

    // Mapping of IWO IDs to IWO struct
    mapping(uint256 => Iwo) public iwos;
    uint256 public iwoCount;  // Counter for IWO IDs

    // Event emitted when an IWO is created
    event IwoCreated(uint256 indexed iwoId, address tokenAddress, uint256 totalSupply, uint256 price, uint256 startTime, uint256 endTime);
  
    // Event emitted when a purchase is made
    event TokensPurchased(uint256 indexed iwoId, address buyer, uint256 amount);

    /**
     * @dev Creates a new Initial Wallet Offering.
     * @param _tokenAddress Address of the token being offered
     * @param _totalSupply Total supply of tokens available for the IWO
     * @param _price Price per token in wei
     * @param _startTime Start time of the IWO (in Unix timestamp)
     * @param _endTime End time of the IWO (in Unix timestamp)
     */
    function createIwo(
        address _tokenAddress,
        uint256 _totalSupply,
        uint256 _price,
        uint256 _startTime,
        uint256 _endTime
    ) external onlyOwner {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_totalSupply > 0, "Total supply must be greater than 0");
        require(_price > 0, "Price must be greater than 0");
        require(_startTime < _endTime, "Start time must be before end time");

        iwos[iwoCount] = Iwo({
            tokenAddress: _tokenAddress,
            totalSupply: _totalSupply,
            price: _price,
            tokensSold: 0,
            startTime: _startTime,
            endTime: _endTime,
            isActive: true
        });

        emit IwoCreated(iwoCount, _tokenAddress, _totalSupply, _price, _startTime, _endTime);
        iwoCount++;
    }

    /**
     * @dev Purchases tokens from an ongoing IWO.
     * @param _iwoId ID of the IWO from which to purchase tokens
     * @param _amount Number of tokens to purchase
     */
    function purchaseTokens(uint256 _iwoId, uint256 _amount) external payable {
        Iwo storage iwo = iwos[_iwoId];

        require(iwo.isActive, "IWO is not active");
        require(block.timestamp >= iwo.startTime && block.timestamp <= iwo.endTime, "IWO is not active during this time");
        require(_amount > 0, "Amount must be greater than 0");
        require(iwo.tokensSold + _amount <= iwo.totalSupply, "Not enough tokens available");
        require(msg.value == iwo.price * _amount, "Incorrect ETH amount sent");

        // Update state
        iwo.tokensSold += _amount;

        // Transfer tokens to the buyer
        IERC20(iwo.tokenAddress).transfer(msg.sender, _amount);

        emit TokensPurchased(_iwoId, msg.sender, _amount);
    }

    /**
     * @dev Ends an ongoing IWO.
     * @param _iwoId ID of the IWO to end
     */
    function endIwo(uint256 _iwoId) external onlyOwner {
        Iwo storage iwo = iwos[_iwoId];
        require(iwo.isActive, "IWO is not active");

        iwo.isActive = false;
    }

    /**
     * @dev Withdraws ETH collected from the IWO to the owner's address.
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers to the contract.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
