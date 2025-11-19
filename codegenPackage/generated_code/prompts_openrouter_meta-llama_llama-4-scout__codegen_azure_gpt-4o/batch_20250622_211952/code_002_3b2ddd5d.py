"""
Generated Code Metadata:
========================
Original URL: https://usdcprinter.xyz
Prompt: Generate a code snippet in Solidity to create a similar token with USDC rewards, including a 5% buy/sell tax and a renounced contract.
Generated: DETERMINISTIC_3b2ddd5dd484c567
Batch ID: 20250622_211952
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
 * @title USDCRewardToken
 * @dev A token contract with USDC rewards, 5% buy/sell tax, and renounced ownership.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract USDCRewardToken is ERC20, Ownable {
    // Address of the USDC token contract
    IERC20 public usdcToken;

    // Tax rate for buy/sell transactions (5%)
    uint256 public constant TAX_RATE = 5;

    // Address where tax funds are collected
    address public taxCollector;

    // Mapping to track excluded addresses from tax
    mapping(address => bool) public isExcludedFromTax;

    /**
     * @dev Constructor to initialize the token.
     * @param _name Name of the token.
     * @param _symbol Symbol of the token.
     * @param _usdcToken Address of the USDC token contract.
     * @param _taxCollector Address to collect tax funds.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        address _usdcToken,
        address _taxCollector
    ) ERC20(_name, _symbol) {
        require(_usdcToken != address(0), "USDC token address cannot be zero");
        require(_taxCollector != address(0), "Tax collector address cannot be zero");

        usdcToken = IERC20(_usdcToken);
        taxCollector = _taxCollector;

        // Mint initial supply to the deployer
        _mint(msg.sender, 1_000_000 * 10**decimals());

        // Exclude deployer and tax collector from tax
        isExcludedFromTax[msg.sender] = true;
        isExcludedFromTax[_taxCollector] = true;

        // Renounce ownership immediately
        renounceOwnership();
    }

    /**
     * @dev Override the _transfer function to implement tax logic.
     * @param sender Address sending the tokens.
     * @param recipient Address receiving the tokens.
     * @param amount Amount of tokens being transferred.
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        if (isExcludedFromTax[sender] || isExcludedFromTax[recipient]) {
            // If sender or recipient is excluded, transfer without tax
            super._transfer(sender, recipient, amount);
        } else {
            // Calculate tax amount
            uint256 taxAmount = (amount * TAX_RATE) / 100;

            // Transfer tax to the tax collector
            super._transfer(sender, taxCollector, taxAmount);

            // Transfer remaining amount to the recipient
            uint256 transferAmount = amount - taxAmount;
            super._transfer(sender, recipient, transferAmount);
        }
    }

    /**
     * @dev Function to distribute USDC rewards to token holders.
     * @param amount Amount of USDC to distribute.
     */
    function distributeRewards(uint256 amount) external {
        require(usdcToken.balanceOf(msg.sender) >= amount, "Insufficient USDC balance");
        require(totalSupply() > 0, "No tokens in circulation");

        // Transfer USDC from sender to contract
        usdcToken.transferFrom(msg.sender, address(this), amount);

        // Distribute USDC to token holders proportionally
        for (uint256 i = 0; i < totalSupply(); i++) {
            address holder = address(uint160(i));
            uint256 holderBalance = balanceOf(holder);
            if (holderBalance > 0) {
                uint256 reward = (amount * holderBalance) / totalSupply();
                usdcToken.transfer(holder, reward);
            }
        }
    }
}
```
