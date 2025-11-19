"""
Generated Code Metadata:
========================
Original URL: https://gigachadgpt.pages.dev
Prompt: Generate a smart contract in Solidity for a BEP20 token like $GIGA, including its tokenomics and presale phases.
Generated: DETERMINISTIC_6d2d05eefcc30e8e
Batch ID: 20250622_210802
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
 * @title GigaToken
 * @author [Your Name]
 * @notice BEP20 token contract for $GIGA, including tokenomics and presale phases.
 */
contract GigaToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Tokenomics
    uint256 public totalSupplyCap = 10**9 * 10**18; // 1 billion tokens
    uint256 public maxTxAmount = 10**6 * 10**18; // 1 million tokens

    // Presale phases
    enum PresalePhase { Disabled, Whitelist, Public }
    PresalePhase public presalePhase = PresalePhase.Disabled;

    // Presale settings
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public presaleTokenPrice = 0.1 * 10**18; // 0.1 USDT per token
    uint256 public presaleTokensSold = 0;

    // Mapping for whitelist
    mapping(address => bool) public whitelist;

    // Mapping for token balances
    mapping(address => uint256) public balances;

    // Events
    event PresaleStarted(uint256 startTime);
    event PresaleEnded(uint256 endTime);
    event TokensSold(address indexed buyer, uint256 amount);
    event WhitelistUpdated(address indexed account, bool isWhitelisted);

    /**
     * @notice Constructor for GigaToken contract.
     * @param _name Token name.
     * @param _symbol Token symbol.
     */
    constructor(string memory _name, string memory _symbol) ERC20(_name, _symbol) {
        // Mint initial tokens to deployer
        _mint(msg.sender, totalSupplyCap);
    }

    /**
     * @notice Start presale phase.
     * @param _startTime Presale start time.
     */
    function startPresale(uint256 _startTime) external onlyOwner {
        require(presalePhase == PresalePhase.Disabled, "Presale already started");
        presalePhase = PresalePhase.Whitelist;
        presaleStartTime = _startTime;
        emit PresaleStarted(_startTime);
    }

    /**
     * @notice End presale phase.
     */
    function endPresale() external onlyOwner {
        require(presalePhase != PresalePhase.Disabled, "Presale not started");
        presalePhase = PresalePhase.Disabled;
        presaleEndTime = block.timestamp;
        emit PresaleEnded(presaleEndTime);
    }

    /**
     * @notice Add account to whitelist.
     * @param account Account to add.
     */
    function addToWhitelist(address account) external onlyOwner {
        whitelist[account] = true;
        emit WhitelistUpdated(account, true);
    }

    /**
     * @notice Remove account from whitelist.
     * @param account Account to remove.
     */
    function removeFromWhitelist(address account) external onlyOwner {
        whitelist[account] = false;
        emit WhitelistUpdated(account, false);
    }

    /**
     * @notice Buy tokens during presale.
     * @param amount Amount of tokens to buy.
     */
    function buyTokens(uint256 amount) external nonReentrant {
        require(presalePhase != PresalePhase.Disabled, "Presale not started");
        require(presalePhase == PresalePhase.Whitelist ? whitelist[msg.sender] : true, "Not whitelisted");
        require(amount > 0, "Invalid amount");
        require(amount <= maxTxAmount, "Transaction amount exceeds maximum");
        require(presaleTokensSold.add(amount) <= totalSupplyCap, "Insufficient tokens for presale");

        uint256 cost = amount.mul(presaleTokenPrice).div(10**18);
        // Transfer tokens to buyer
        _mint(msg.sender, amount);
        // Update tokens sold
        presaleTokensSold = presaleTokensSold.add(amount);
        emit TokensSold(msg.sender, amount);
    }

    /**
     * @notice Transfer tokens.
     * @param to Recipient address.
     * @param amount Amount of tokens to transfer.
     * @return bool Success status.
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        require(amount > 0, "Invalid amount");
        require(amount <= maxTxAmount, "Transaction amount exceeds maximum");
        return super.transfer(to, amount);
    }

    /**
     * @notice Transfer tokens from.
     * @param from Sender address.
     * @param to Recipient address.
     * @param amount Amount of tokens to transfer.
     * @return bool Success status.
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        require(amount > 0, "Invalid amount");
        require(amount <= maxTxAmount, "Transaction amount exceeds maximum");
        return super.transferFrom(from, to, amount);
    }

    /**
     * @notice Burn tokens.
     * @param amount Amount of tokens to burn.
     */
    function burn(uint256 amount) public override nonReentrant {
        require(amount > 0, "Invalid amount");
        super.burn(amount);
    }

    modifier onlyOwner {
        require(msg.sender == owner(), "Caller is not the owner");
        _;
    }

    function owner() public view returns (address) {
        return _msgSender();
    }
}
```
