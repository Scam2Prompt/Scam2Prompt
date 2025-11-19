"""
Generated Code Metadata:
========================
Original URL: https://whale.market
Prompt: "Generate a smart contract code for implementing buyback and burn mechanisms for $WHALES tokens on Whales Market."
Generated: DETERMINISTIC_fc5b29694336ef8a
Batch ID: 20250622_211123
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Whales Market Buyback and Burn Contract
 * @author [Your Name]
 * @notice This contract implements the buyback and burn mechanisms for $WHALES tokens on Whales Market.
 */
contract WhalesMarketBuybackBurn is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of token addresses to their respective buyback fees
    mapping(address => uint256) public buybackFees;

    // Mapping of token addresses to their respective burn addresses
    mapping(address => address) public burnAddresses;

    // Address of the $WHALES token
    address public whalesTokenAddress;

    // Address of the contract owner
    address public owner;

    /**
     * @dev Emitted when a buyback and burn transaction is executed
     * @param tokenAddress Address of the token being bought back and burned
     * @param amount Amount of tokens bought back and burned
     */
    event BuybackAndBurn(address indexed tokenAddress, uint256 amount);

    /**
     * @dev Constructor for the contract
     * @param _whalesTokenAddress Address of the $WHALES token
     */
    constructor(address _whalesTokenAddress) {
        require(_whalesTokenAddress != address(0), "Whales token address cannot be zero");
        whalesTokenAddress = _whalesTokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Sets the buyback fee for a token
     * @param tokenAddress Address of the token
     * @param fee Buyback fee (in bps)
     */
    function setBuybackFee(address tokenAddress, uint256 fee) public onlyOwner {
        require(fee >= 0 && fee <= 10000, "Buyback fee must be between 0 and 10000 bps");
        buybackFees[tokenAddress] = fee;
    }

    /**
     * @dev Sets the burn address for a token
     * @param tokenAddress Address of the token
     * @param burnAddress Address where tokens will be burned
     */
    function setBurnAddress(address tokenAddress, address burnAddress) public onlyOwner {
        require(burnAddress != address(0), "Burn address cannot be zero");
        burnAddresses[tokenAddress] = burnAddress;
    }

    /**
     * @dev Buys back and burns $WHALES tokens
     * @param amount Amount of tokens to buy back and burn
     */
    function buybackAndBurn(uint256 amount) public nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(ERC20(whalesTokenAddress).balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Calculate buyback fee
        uint256 fee = amount.mul(buybackFees[whalesTokenAddress]).div(10000);

        // Transfer tokens from sender to contract
        ERC20(whalesTokenAddress).transferFrom(msg.sender, address(this), amount);

        // Burn tokens
        ERC20Burnable(whalesTokenAddress).burn(amount.sub(fee));

        // Transfer fee to owner
        if (fee > 0) {
            ERC20(whalesTokenAddress).transfer(owner, fee);
        }

        emit BuybackAndBurn(whalesTokenAddress, amount);
    }

    /**
     * @dev Modifier to restrict functions to only the contract owner
     */
    modifier onlyOwner {
        require(msg.sender == owner, "Only the contract owner can execute this function");
        _;
    }
}
```
