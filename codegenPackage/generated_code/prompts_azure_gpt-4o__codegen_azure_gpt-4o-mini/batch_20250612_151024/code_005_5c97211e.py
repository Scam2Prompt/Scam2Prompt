"""
Generated Code Metadata:
========================
Original URL: https://grooveup.pages.dev
Prompt: Generate a Solidity contract for managing artist token presales on the GrooveUP platform. Include functionality for seed funding and token allocation based on the provided tokenomics.
Generated: DETERMINISTIC_5c97211ebcbea0cf
Batch ID: 20250612_151024
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title GrooveUP Presale Contract
 * @dev This contract manages artist token presales, including seed funding and token allocation.
 */
contract GrooveUPPresale is Ownable {
    using SafeMath for uint256;

    // Struct to hold presale details
    struct Presale {
        address artist;
        uint256 totalTokens;
        uint256 tokensSold;
        uint256 pricePerToken;
        bool isActive;
    }

    // Mapping of presale ID to Presale details
    mapping(uint256 => Presale) public presales;
    uint256 public presaleCount;

    // Event emitted when a new presale is created
    event PresaleCreated(uint256 indexed presaleId, address indexed artist, uint256 totalTokens, uint256 pricePerToken);
    
    // Event emitted when tokens are purchased
    event TokensPurchased(uint256 indexed presaleId, address indexed buyer, uint256 amount);

    // Event emitted when a presale is finalized
    event PresaleFinalized(uint256 indexed presaleId);

    /**
     * @dev Create a new presale for an artist.
     * @param _artist The address of the artist.
     * @param _totalTokens The total number of tokens available for the presale.
     * @param _pricePerToken The price per token in wei.
     */
    function createPresale(address _artist, uint256 _totalTokens, uint256 _pricePerToken) external onlyOwner {
        require(_artist != address(0), "Invalid artist address");
        require(_totalTokens > 0, "Total tokens must be greater than zero");
        require(_pricePerToken > 0, "Price per token must be greater than zero");

        presaleCount++;
        presales[presaleCount] = Presale({
            artist: _artist,
            totalTokens: _totalTokens,
            tokensSold: 0,
            pricePerToken: _pricePerToken,
            isActive: true
        });

        emit PresaleCreated(presaleCount, _artist, _totalTokens, _pricePerToken);
    }

    /**
     * @dev Purchase tokens from a presale.
     * @param _presaleId The ID of the presale.
     * @param _amount The number of tokens to purchase.
     */
    function purchaseTokens(uint256 _presaleId, uint256 _amount) external payable {
        Presale storage presale = presales[_presaleId];

        require(presale.isActive, "Presale is not active");
        require(_amount > 0, "Amount must be greater than zero");
        require(presale.tokensSold.add(_amount) <= presale.totalTokens, "Not enough tokens available");
        require(msg.value == presale.pricePerToken.mul(_amount), "Incorrect Ether value sent");

        presale.tokensSold = presale.tokensSold.add(_amount);
        emit TokensPurchased(_presaleId, msg.sender, _amount);
    }

    /**
     * @dev Finalize a presale, marking it as inactive.
     * @param _presaleId The ID of the presale to finalize.
     */
    function finalizePresale(uint256 _presaleId) external onlyOwner {
        Presale storage presale = presales[_presaleId];
        require(presale.isActive, "Presale is already finalized");

        presale.isActive = false;
        emit PresaleFinalized(_presaleId);
    }

    /**
     * @dev Withdraw funds from the contract.
     * @param _to The address to withdraw funds to.
     * @param _amount The amount of funds to withdraw.
     */
    function withdrawFunds(address payable _to, uint256 _amount) external onlyOwner {
        require(_to != address(0), "Invalid address");
        require(address(this).balance >= _amount, "Insufficient balance");

        _to.transfer(_amount);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
