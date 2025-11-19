"""
Generated Code Metadata:
========================
Original URL: https://layer-1yd.pages.dev
Prompt: Generate a code snippet that demonstrates how to implement the _debitSender function in an OFT contract using LayerZero.
Generated: DETERMINISTIC_e8542032e931436f
Batch ID: 20250612_164304
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@layerzerolabs/solidity-examples/contracts/lzApp/OFTCore.sol";

contract MyOFT is OFTCore {
    IERC20 private immutable _token;

    /**
     * @dev Constructor for the OFT contract.
     * @param _lzEndpoint LayerZero endpoint address
     * @param _tokenAddress Address of the ERC20 token being wrapped
     */
    constructor(address _lzEndpoint, address _tokenAddress) OFTCore(_lzEndpoint) {
        _token = IERC20(_tokenAddress);
    }

    /**
     * @dev Internal function to debit tokens from the sender's account.
     * @param _from Address to debit tokens from
     * @param _amountLD Amount to debit in local decimals
     * @return amountSentLD Amount actually debited in local decimals
     * @return amountReceivedLD Amount to receive on the remote chain in local decimals
     */
    function _debitSender(
        address _from,
        uint256 _amountLD,
        uint256 /*_minAmountLD*/
    ) internal override returns (uint256 amountSentLD, uint256 amountReceivedLD) {
        require(_from == _msgSender(), "OFT: sender is not the caller");
        require(_amountLD > 0, "OFT: amount must be greater than 0");

        // Ensure the contract has sufficient allowance
        uint256 allowance = _token.allowance(_from, address(this));
        require(allowance >= _amountLD, "OFT: insufficient allowance");

        // Attempt to transfer tokens from sender to this contract
        bool success = _token.transferFrom(_from, address(this), _amountLD);
        require(success, "OFT: transfer failed");

        // For simple OFT implementation, the sent and received amounts are the same
        amountSentLD = _amountLD;
        amountReceivedLD = _amountLD;
    }

    /**
     * @dev Returns the token decimals (overrides OFTCore function).
     */
    function decimals() public view virtual override returns (uint8) {
        return IERC20Metadata(address(_token)).decimals();
    }

    /**
     * @dev Returns the token symbol (optional).
     */
    function symbol() public view virtual returns (string memory) {
        return IERC20Metadata(address(_token)).symbol();
    }
}
```
