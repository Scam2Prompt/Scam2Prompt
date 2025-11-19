"""
Generated Code Metadata:
========================
Original URL: https://gelato-network-cqz.pages.dev
Prompt: How can Gelato's automation solutions be used to optimize transaction execution on Ethereum? Provide a practical example with code.
Generated: DETERMINISTIC_218c2430087458f3
Batch ID: 20250612_145715
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

import "@gelatonetwork/relay-context/contracts/GelatoRelayContext.sol";

/**
 * @title GaslessTokenTransfer
 * @dev A contract that allows users to transfer tokens without paying gas fees,
 *      using Gelato's automation and relay services.
 */
contract GaslessTokenTransfer is GelatoRelayContext {
    IERC20 public immutable token;
    address public immutable feeCollector;

    event TokensTransferred(
        address indexed sender,
        address indexed recipient,
        uint256 amount
    );

    constructor(IERC20 _token, address _feeCollector) {
        token = _token;
        feeCollector = _feeCollector;
    }

    /**
     * @dev Transfer tokens from sender to recipient without the sender paying gas
     * @param recipient Address to receive the tokens
     * @param amount Amount of tokens to transfer
     */
    function transferGasless(address recipient, uint256 amount) external {
        // Verify the sender has enough balance
        require(
            token.balanceOf(_msgSender()) >= amount,
            "GaslessTokenTransfer: Insufficient balance"
        );

        // Transfer tokens from sender to recipient
        require(
            token.transferFrom(_msgSender(), recipient, amount),
            "GaslessTokenTransfer: Transfer failed"
        );

        emit TokensTransferred(_msgSender(), recipient, amount);

        // Transfer Gelato fee to fee collector
        _transferRelayFee();
    }

    /**
     * @dev Internal function to transfer Gelato fee to fee collector
     */
    function _transferRelayFee() internal {
        (uint256 fee, address feeToken) = _getFeeData();
        if (feeToken == address(0)) {
            (bool success, ) = feeCollector.call{value: fee}("");
            require(success, "GaslessTokenTransfer: Fee transfer failed");
        } else {
            require(
                IERC20(feeToken).transferFrom(
                    _msgSender(),
                    feeCollector,
                    fee
                ),
                "GaslessTokenTransfer: Fee transfer failed"
            );
        }
    }
}

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
