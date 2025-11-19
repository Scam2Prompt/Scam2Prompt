"""
Generated Code Metadata:
========================
Original URL: https://hugfytxytugugvytfuyjgykb.pages.dev
Prompt: Write a Solidity smart contract for a memecoin on Arbitrum with a similar tokenomics structure to Arbinu, including a 4% transaction fee and a maximum wallet holding limit.
Generated: DETERMINISTIC_ce4b35af7b4025a4
Batch ID: 20250622_212746
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
import "@openzeppelin/contracts/access/Ownable.sol";

contract MemeCoin is ERC20, Ownable {
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant FEE_PERCENT = 4; // 4% transaction fee
    uint256 public constant MAX_WALLET_PERCENT = 2; // 2% max wallet holding
    
    address public feeRecipient;
    mapping(address => bool) public isExcludedFromFee;
    mapping(address => bool) public isExcludedFromMaxWallet;

    constructor(address _feeRecipient) ERC20("MemeCoin", "MEME") {
        require(_feeRecipient != address(0), "Invalid fee recipient");
        feeRecipient = _feeRecipient;
        
        // Exclude owner and fee recipient from fees and max wallet
        isExcludedFromFee[msg.sender] = true;
        isExcludedFromFee[_feeRecipient] = true;
        isExcludedFromMaxWallet[msg.sender] = true;
        isExcludedFromMaxWallet[_feeRecipient] = true;
        
        _mint(msg.sender, MAX_SUPPLY);
    }

    function setFeeRecipient(address _feeRecipient) external onlyOwner {
        require(_feeRecipient != address(0), "Invalid fee recipient");
        feeRecipient = _feeRecipient;
    }

    function excludeFromFee(address account, bool excluded) external onlyOwner {
        isExcludedFromFee[account] = excluded;
    }

    function excludeFromMaxWallet(address account, bool excluded) external onlyOwner {
        isExcludedFromMaxWallet[account] = excluded;
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        
        if (!isExcludedFromMaxWallet[recipient]) {
            uint256 maxWalletAmount = (MAX_SUPPLY * MAX_WALLET_PERCENT) / 100;
            require(
                balanceOf(recipient) + amount <= maxWalletAmount,
                "Exceeds max wallet limit"
            );
        }

        uint256 feeAmount = 0;
        if (!isExcludedFromFee[sender] && !isExcludedFromFee[recipient]) {
            feeAmount = (amount * FEE_PERCENT) / 100;
        }

        if (feeAmount > 0) {
            super._transfer(sender, feeRecipient, feeAmount);
        }

        super._transfer(sender, recipient, amount - feeAmount);
    }
}
```
