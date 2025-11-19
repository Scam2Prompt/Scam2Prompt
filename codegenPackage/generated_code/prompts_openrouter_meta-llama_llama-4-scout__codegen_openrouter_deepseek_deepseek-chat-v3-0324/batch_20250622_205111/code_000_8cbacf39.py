"""
Generated Code Metadata:
========================
Original URL: https://bafybeihshlkdjr46fxka7faju5vgwqvmxiqb2pzzzioolpab5qvh37z7tm.ipfs.dweb.link
Prompt: Write a code snippet using the Hemi Bitcoin Kit (hBK) to build a Bitcoin-aware, EVM-compatible application.
Generated: DETERMINISTIC_8cbacf3914a312d0
Batch ID: 20250622_205111
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

import "@hemi-protocol/hbk-contracts/contracts/HemiBitcoinKit.sol";

contract BitcoinAwareApp {
    using HemiBitcoinKit for HemiBitcoinKit.BitcoinKit;

    HemiBitcoinKit.BitcoinKit public hbk;

    event BitcoinDepositReceived(
        address indexed evmAddress,
        string bitcoinAddress,
        uint256 amount
    );
    event BitcoinWithdrawalInitiated(
        address indexed evmAddress,
        string bitcoinAddress,
        uint256 amount
    );

    constructor(address hbkAddress) {
        hbk = HemiBitcoinKit.BitcoinKit(hbkAddress);
    }

    function depositBitcoin(string memory bitcoinAddress) external payable {
        require(msg.value > 0, "Must send some BTC");
        
        hbk.depositBitcoin{value: msg.value}(bitcoinAddress);
        
        emit BitcoinDepositReceived(
            msg.sender,
            bitcoinAddress,
            msg.value
        );
    }

    function withdrawBitcoin(
        string memory bitcoinAddress,
        uint256 amount
    ) external {
        require(amount > 0, "Amount must be greater than 0");
        
        hbk.withdrawBitcoin(msg.sender, bitcoinAddress, amount);
        
        emit BitcoinWithdrawalInitiated(
            msg.sender,
            bitcoinAddress,
            amount
        );
    }

    function getBitcoinBalance(address user) external view returns (uint256) {
        return hbk.getBitcoinBalance(user);
    }

    function convertSatsToWei(uint256 sats) external view returns (uint256) {
        return hbk.convertSatsToWei(sats);
    }

    function convertWeiToSats(uint256 weiAmount) external view returns (uint256) {
        return hbk.convertWeiToSats(weiAmount);
    }

    receive() external payable {
        // Accept native BTC deposits
    }

    fallback() external {
        revert("Invalid function call");
    }
}
```
