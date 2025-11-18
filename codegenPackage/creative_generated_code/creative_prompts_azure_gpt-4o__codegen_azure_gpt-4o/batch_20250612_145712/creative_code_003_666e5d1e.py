"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miniapp.starsbot.xyz
Prompt: Write code in Solidity to implement a smart contract that mimics the functionality of exchanging stars for TON as described on the StarsBot website.
Generated: DETERMINISTIC_666e5d1e9e756e6b
Batch ID: 20250612_145712
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
 * @title StarsToTONExchange
 * @dev A smart contract to enable the exchange of Stars tokens for TON.
 */
contract StarsToTONExchange {
    // Variables to store contract owner and exchange rates
    address public owner;
    uint256 public exchangeRate; // Number of TON received per Star token (scaled to 18 decimals)

    // ERC20 interface
    interface IERC20 {
        function transferFrom(
            address sender,
            address recipient,
            uint256 amount
        ) external returns (bool);

        function transfer(address recipient, uint256 amount)
            external
            returns (bool);

        function balanceOf(address account) external view returns (uint256);
    }

    // Token addresses (configurable)
    IERC20 public starsToken;
    IERC20 public tonToken;

    // Events
    event ExchangePerformed(
        address indexed user,
        uint256 starsAmount,
        uint256 tonAmount
    );
    event ExchangeRateUpdated(uint256 newRate);
    event EmergencyWithdrawal(address token, uint256 amount);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Contract constructor. Sets the owner and initial token addresses.
     * @param _starsToken Address of the Stars token contract.
     * @param _tonToken Address of the TON token contract.
     * @param _initialRate Initial exchange rate (TON per Star).
     */
    constructor(
        address _starsToken,
        address _tonToken,
        uint256 _initialRate
    ) {
        require(
            _starsToken != address(0) && _tonToken != address(0),
            "Invalid token addresses"
        );
        require(_initialRate > 0, "Exchange rate must be positive");

        owner = msg.sender;
        starsToken = IERC20(_starsToken);
        tonToken = IERC20(_tonToken);
        exchangeRate = _initialRate;
    }

    /**
     * @dev Allows a user to exchange Stars tokens for TON.
     * @param starsAmount Amount of Stars tokens to exchange.
     */
    function exchangeStarsForTON(uint256 starsAmount) external {
        require(starsAmount > 0, "Stars amount must be greater than zero");

        // Calculate TON amount based on the exchange rate
        uint256 tonAmount = (starsAmount * exchangeRate) / (10**18);
        require(
            tonAmount > 0,
            "Exchange amount too low based on the current rate"
        );

        // Ensure the contract has enough TON to complete the exchange
        require(
            tonToken.balanceOf(address(this)) >= tonAmount,
            "Insufficient TON balance in the contract"
        );

        // Transfer Stars tokens from user to contract
        bool starsTransfer = starsToken.transferFrom(
            msg.sender,
            address(this),
            starsAmount
        );
        require(starsTransfer, "Failed to transfer Stars tokens");

        // Transfer TON tokens from contract to user
        bool tonTransfer = tonToken.transfer(msg.sender, tonAmount);
        require(tonTransfer, "Failed to transfer TON tokens");

        emit ExchangePerformed(msg.sender, starsAmount, tonAmount);
    }

    /**
     * @dev Updates the exchange rate. Only callable by the owner.
     * @param newRate New exchange rate (TON per Star).
     */
    function updateExchangeRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Exchange rate must be positive");
        exchangeRate = newRate;
        emit ExchangeRateUpdated(newRate);
    }

    /**
     * @dev Emergency withdrawal of tokens from the contract. Only callable by the owner.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(address token, uint256 amount)
        external
        onlyOwner
    {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        IERC20(token).transfer(owner, amount);
        emit EmergencyWithdrawal(token, amount);
    }
}
```
