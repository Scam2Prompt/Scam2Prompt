"""
Generated Code Metadata:
========================
Original URL: https://inqubeta-ai.pages.dev
Prompt: Write a smart contract in Solidity to implement the tokenomics of $QUBE, including buy tax, sell tax, rewards pool, liquidity, marketing, and burn functions.
Generated: DETERMINISTIC_2a5fffb843d1ade3
Batch ID: 20250612_153225
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

contract QUBE is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Tokenomics
    uint256 public constant BUY_TAX = 2; // 2% buy tax
    uint256 public constant SELL_TAX = 3; // 3% sell tax
    uint256 public constant REWARDS_POOL_FEE = 2; // 2% rewards pool fee
    uint256 public constant LIQUIDITY_FEE = 1; // 1% liquidity fee
    uint256 public constant MARKETING_FEE = 1; // 1% marketing fee
    uint256 public constant BURN_FEE = 1; // 1% burn fee

    // Addresses
    address public rewardsPoolAddress;
    address public liquidityAddress;
    address public marketingAddress;
    address public owner;

    // Mapping for excluded accounts from fees
    mapping(address => bool) public isExcludedFromFees;

    // Mapping for balances
    mapping(address => uint256) public balances;

    // Events
    event BuyTaxApplied(address indexed buyer, uint256 amount);
    event SellTaxApplied(address indexed seller, uint256 amount);
    event RewardsPoolFunded(uint256 amount);
    event LiquidityFunded(uint256 amount);
    event MarketingFunded(uint256 amount);
    event Burned(uint256 amount);

    constructor() ERC20("QUBE", "QUBE") {
        owner = msg.sender;
        rewardsPoolAddress = msg.sender;
        liquidityAddress = msg.sender;
        marketingAddress = msg.sender;

        // Mint initial supply
        _mint(msg.sender, 1000000 * 10**18);
    }

    // Modifier to check if the sender is the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Function to set excluded accounts from fees
    function setExcludedFromFees(address account, bool excluded) public onlyOwner {
        isExcludedFromFees[account] = excluded;
    }

    // Function to set addresses
    function setAddresses(address _rewardsPoolAddress, address _liquidityAddress, address _marketingAddress) public onlyOwner {
        rewardsPoolAddress = _rewardsPoolAddress;
        liquidityAddress = _liquidityAddress;
        marketingAddress = _liquidityAddress;
    }

    // Override transfer function to apply taxes
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        uint256 tax = calculateTax(msg.sender, recipient, amount);
        uint256 sendAmount = amount.sub(tax);
        balances[msg.sender] = balances[msg.sender].sub(amount);
        balances[recipient] = balances[recipient].add(sendAmount);

        if (tax > 0) {
            // Distribute tax
            distributeTax(tax);
        }

        emit Transfer(msg.sender, recipient, sendAmount);
        return true;
    }

    // Override transferFrom function to apply taxes
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 tax = calculateTax(sender, recipient, amount);
        uint256 sendAmount = amount.sub(tax);
        balances[sender] = balances[sender].sub(amount);
        balances[recipient] = balances[recipient].add(sendAmount);

        if (tax > 0) {
            // Distribute tax
            distributeTax(tax);
        }

        emit Transfer(sender, recipient, sendAmount);
        return true;
    }

    // Function to calculate tax
    function calculateTax(address sender, address recipient, uint256 amount) internal view returns (uint256) {
        uint256 tax;

        if (isExcludedFromFees[sender] || isExcludedFromFees[recipient]) {
            return 0;
        }

        if (recipient == address(this)) {
            // Buy
            tax = amount.mul(BUY_TAX).div(100);
            emit BuyTaxApplied(sender, tax);
        } else {
            // Sell
            tax = amount.mul(SELL_TAX).div(100);
            emit SellTaxApplied(sender, tax);
        }

        return tax;
    }

    // Function to distribute tax
    function distributeTax(uint256 tax) internal {
        uint256 rewardsPoolAmount = tax.mul(REWARDS_POOL_FEE).div(100);
        uint256 liquidityAmount = tax.mul(LIQUIDITY_FEE).div(100);
        uint256 marketingAmount = tax.mul(MARKETING_FEE).div(100);
        uint256 burnAmount = tax.mul(BURN_FEE).div(100);

        // Fund rewards pool
        _transfer(address(this), rewardsPoolAddress, rewardsPoolAmount);
        emit RewardsPoolFunded(rewardsPoolAmount);

        // Fund liquidity
        _transfer(address(this), liquidityAddress, liquidityAmount);
        emit LiquidityFunded(liquidityAmount);

        // Fund marketing
        _transfer(address(this), marketingAddress, marketingAmount);
        emit MarketingFunded(marketingAmount);

        // Burn
        _burn(address(this), burnAmount);
        emit Burned(burnAmount);
    }

    // Override _beforeTokenTransfer to track balances
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256[] memory ids
    ) internal override {
        for (uint256 i = 0; i < ids.length; i++) {
            uint256 id = ids[i];
            balances[from] = balances[from].sub(1);
            balances[to] = balances[to].add(1);
        }
    }
}
```
