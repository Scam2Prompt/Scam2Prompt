"""
Generated Code Metadata:
========================
Original URL: https://ziber.io
Prompt: Generate a smart contract in Solidity for the Ziber ICO that accepts Ethereum payments and distributes Ziber tokens based on the snapshot of Bitcoin and Ethereum wallets.
Generated: DETERMINISTIC_b6ae8faefd8dbcf0
Batch ID: 20250612_160600
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title Ziber ICO Contract
 * @author [Your Name]
 * @notice This contract manages the Ziber ICO, allowing users to purchase Ziber tokens with Ethereum.
 * @dev This contract uses the SafeERC20 and SafeMath libraries for secure token management and arithmetic operations.
 */
contract ZiberICO {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user contributions
    mapping (address => uint256) public contributions;

    // Mapping of user token balances
    mapping (address => uint256) public tokenBalances;

    // Ziber token contract
    IERC20 public ziberToken;

    // Ethereum address for the ICO wallet
    address public icoWallet;

    // Bitcoin and Ethereum wallet snapshot
    mapping (address => uint256) public btcSnapshot;
    mapping (address => uint256) public ethSnapshot;

    // Token price in Wei
    uint256 public tokenPrice;

    // ICO start and end timestamps
    uint256 public icoStart;
    uint256 public icoEnd;

    // Total tokens sold
    uint256 public totalTokensSold;

    // Event emitted when a user purchases tokens
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Event emitted when the ICO ends
    event ICOEnded();

    /**
     * @dev Constructor for the Ziber ICO contract
     * @param _ziberToken Address of the Ziber token contract
     * @param _icoWallet Address of the ICO wallet
     * @param _tokenPrice Price of the token in Wei
     * @param _icoDuration Duration of the ICO in seconds
     */
    constructor(
        address _ziberToken,
        address _icoWallet,
        uint256 _tokenPrice,
        uint256 _icoDuration
    ) public {
        require(_ziberToken != address(0), "Ziber token address cannot be zero");
        require(_icoWallet != address(0), "ICO wallet address cannot be zero");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_icoDuration > 0, "ICO duration must be greater than zero");

        ziberToken = IERC20(_ziberToken);
        icoWallet = _icoWallet;
        tokenPrice = _tokenPrice;
        icoStart = block.timestamp;
        icoEnd = icoStart.add(_icoDuration);
    }

    /**
     * @dev Fallback function to purchase tokens with Ethereum
     */
    receive() external payable {
        purchaseTokens();
    }

    /**
     * @dev Function to purchase tokens with Ethereum
     */
    function purchaseTokens() public payable {
        require(msg.value > 0, "Purchase amount must be greater than zero");
        require(block.timestamp >= icoStart && block.timestamp <= icoEnd, "ICO is not active");

        uint256 tokensToPurchase = msg.value.div(tokenPrice);
        require(tokensToPurchase > 0, "Insufficient Ether to purchase tokens");

        // Update user's contribution
        contributions[msg.sender] = contributions[msg.sender].add(msg.value);

        // Transfer tokens to user
        ziberToken.safeTransfer(msg.sender, tokensToPurchase);

        // Update token balance
        tokenBalances[msg.sender] = tokenBalances[msg.sender].add(tokensToPurchase);

        // Update total tokens sold
        totalTokensSold = totalTokensSold.add(tokensToPurchase);

        // Emit event
        emit TokensPurchased(msg.sender, tokensToPurchase);
    }

    /**
     * @dev Function to snapshot Bitcoin and Ethereum wallets
     * @param _btcWallet Address of the Bitcoin wallet
     * @param _ethWallet Address of the Ethereum wallet
     * @param _btcBalance Bitcoin balance
     * @param _ethBalance Ethereum balance
     */
    function snapshotWallets(
        address _btcWallet,
        address _ethWallet,
        uint256 _btcBalance,
        uint256 _ethBalance
    ) public {
        require(msg.sender == icoWallet, "Only the ICO wallet can snapshot wallets");

        btcSnapshot[_btcWallet] = _btcBalance;
        ethSnapshot[_ethWallet] = _ethBalance;
    }

    /**
     * @dev Function to end the ICO
     */
    function endICO() public {
        require(msg.sender == icoWallet, "Only the ICO wallet can end the ICO");
        require(block.timestamp >= icoEnd, "ICO has not ended yet");

        emit ICOEnded();
    }

    /**
     * @dev Function to withdraw Ether from the ICO wallet
     */
    function withdrawEther() public {
        require(msg.sender == icoWallet, "Only the ICO wallet can withdraw Ether");

        msg.sender.transfer(address(this).balance);
    }
}
```
