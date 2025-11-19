"""
Generated Code Metadata:
========================
Original URL: https://trumpinucoin.com
Prompt: Write a Solidity smart contract snippet to implement a 1% trade fee donation mechanism similar to Trump Inu's approach.
Generated: DETERMINISTIC_df94ec1f3efcda58
Batch ID: 20250612_152620
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

contract DonationToken is ERC20, Ownable {
    address public donationAddress;
    uint256 public constant DONATION_FEE_PERCENT = 1; // 1% fee

    event Donation(address indexed from, address indexed to, uint256 amount);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address _donationAddress
    ) ERC20(name, symbol) {
        require(_donationAddress != address(0), "Invalid donation address");
        _mint(msg.sender, initialSupply);
        donationAddress = _donationAddress;
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        if (sender == address(0) || recipient == address(0) || sender == donationAddress || recipient == donationAddress) {
            super._transfer(sender, recipient, amount);
            return;
        }

        uint256 donationAmount = (amount * DONATION_FEE_PERCENT) / 100;
        uint256 transferAmount = amount - donationAmount;

        super._transfer(sender, donationAddress, donationAmount);
        super._transfer(sender, recipient, transferAmount);

        emit Donation(sender, donationAddress, donationAmount);
    }

    function setDonationAddress(address _donationAddress) external onlyOwner {
        require(_donationAddress != address(0), "Invalid donation address");
        donationAddress = _donationAddress;
    }
}
```
