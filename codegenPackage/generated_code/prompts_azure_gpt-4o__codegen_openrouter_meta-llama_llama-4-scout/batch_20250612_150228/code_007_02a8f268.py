"""
Generated Code Metadata:
========================
Original URL: https://bafybeig2qxervlifeg5gur3hrsbgo6hrco4esjxaz2r6nixoqkc6nhhjbe.ipfs.dweb.link
Prompt: Write a Solidity contract to support exotic options trading as part of the Pencils Protocol Vaults yield strategies.
Generated: DETERMINISTIC_02a8f268dc6aa932
Batch ID: 20250612_150228
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ExoticOptionsTradingContract
 * @author Pencils Protocol
 * @notice This contract supports exotic options trading as part of the Pencils Protocol Vaults yield strategies.
 */
contract ExoticOptionsTradingContract is Ownable {
    using SafeMath for uint256;

    // Mapping of option types to their respective addresses
    mapping(string => address) public optionTypes;

    // Mapping of users to their respective balances
    mapping(address => mapping(string => uint256)) public userBalances;

    // Mapping of option types to their respective strike prices
    mapping(string => uint256) public strikePrices;

    // Mapping of option types to their respective expiration timestamps
    mapping(string => uint256) public expirationTimestamps;

    // Event emitted when an option is purchased
    event OptionPurchased(address indexed buyer, string optionType, uint256 amount);

    // Event emitted when an option is exercised
    event OptionExercised(address indexed exerciser, string optionType, uint256 amount);

    // Event emitted when an option expires
    event OptionExpired(string optionType);

    /**
     * @notice Adds a new option type to the contract
     * @param optionType The type of option to add
     * @param optionAddress The address of the option token
     * @param strikePrice The strike price of the option
     * @param expirationTimestamp The expiration timestamp of the option
     */
    function addOptionType(string memory optionType, address optionAddress, uint256 strikePrice, uint256 expirationTimestamp) public onlyOwner {
        require(optionTypes[optionType] == address(0), "Option type already exists");
        require(optionAddress != address(0), "Option address cannot be zero");
        require(strikePrice > 0, "Strike price must be greater than zero");
        require(expirationTimestamp > block.timestamp, "Expiration timestamp must be in the future");

        optionTypes[optionType] = optionAddress;
        strikePrices[optionType] = strikePrice;
        expirationTimestamps[optionType] = expirationTimestamp;
    }

    /**
     * @notice Purchases an option
     * @param optionType The type of option to purchase
     * @param amount The amount of options to purchase
     */
    function purchaseOption(string memory optionType, uint256 amount) public {
        require(optionTypes[optionType] != address(0), "Option type does not exist");
        require(amount > 0, "Amount must be greater than zero");

        address optionAddress = optionTypes[optionType];
        IERC20(optionAddress).transferFrom(msg.sender, address(this), amount);

        userBalances[msg.sender][optionType] = userBalances[msg.sender][optionType].add(amount);

        emit OptionPurchased(msg.sender, optionType, amount);
    }

    /**
     * @notice Exercises an option
     * @param optionType The type of option to exercise
     * @param amount The amount of options to exercise
     */
    function exerciseOption(string memory optionType, uint256 amount) public {
        require(optionTypes[optionType] != address(0), "Option type does not exist");
        require(amount > 0, "Amount must be greater than zero");
        require(userBalances[msg.sender][optionType] >= amount, "Insufficient balance");
        require(block.timestamp < expirationTimestamps[optionType], "Option has expired");

        userBalances[msg.sender][optionType] = userBalances[msg.sender][optionType].sub(amount);

        // Perform payout logic here

        emit OptionExercised(msg.sender, optionType, amount);
    }

    /**
     * @notice Expires an option
     * @param optionType The type of option to expire
     */
    function expireOption(string memory optionType) public {
        require(optionTypes[optionType] != address(0), "Option type does not exist");
        require(block.timestamp >= expirationTimestamps[optionType], "Option has not expired");

        emit OptionExpired(optionType);
    }

    /**
     * @notice Withdraws excess tokens from the contract
     * @param tokenAddress The address of the token to withdraw
     * @param amount The amount of tokens to withdraw
     */
    function withdrawExcessTokens(address tokenAddress, uint256 amount) public onlyOwner {
        require(tokenAddress != address(0), "Token address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");

        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
