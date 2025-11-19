"""
Generated Code Metadata:
========================
Original URL: https://substantial-belgium-incalculable.on-fleek.app
Prompt: Generate a LayerZero-compatible smart contract that utilizes the protocol's messaging system to transfer value across supported blockchains. Ensure the contract adheres to LayerZero security stack recommendations.
Generated: DETERMINISTIC_4b4514a109cea3f2
Batch ID: 20250612_150040
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

import "@layerzerolabs/solidity-examples/contracts/lzApp/NonblockingLzApp.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

contract CrossChainValueTransfer is NonblockingLzApp {
    using SafeERC20 for IERC20;

    struct TransferData {
        address token;
        address receiver;
        uint256 amount;
    }

    event ValueSent(
        uint16 indexed dstChainId,
        address indexed sender,
        address indexed receiver,
        address token,
        uint256 amount
    );
    event ValueReceived(
        uint16 indexed srcChainId,
        address indexed sender,
        address indexed receiver,
        address token,
        uint256 amount
    );

    constructor(address _lzEndpoint) NonblockingLzApp(_lzEndpoint) {}

    function estimateFees(
        uint16 _dstChainId,
        address _token,
        address _receiver,
        uint256 _amount,
        bool _useZro,
        bytes calldata _adapterParams
    ) external view returns (uint256 nativeFee, uint256 zroFee) {
        bytes memory payload = abi.encode(
            TransferData({token: _token, receiver: _receiver, amount: _amount})
        );
        return
            lzEndpoint.estimateFees(
                _dstChainId,
                address(this),
                payload,
                _useZro,
                _adapterParams
            );
    }

    function sendValue(
        uint16 _dstChainId,
        address _token,
        address _receiver,
        uint256 _amount,
        address payable _refundAddress,
        address _zroPaymentAddress,
        bytes calldata _adapterParams
    ) external payable {
        require(
            IERC20(_token).balanceOf(msg.sender) >= _amount,
            "Insufficient token balance"
        );
        require(
            IERC20(_token).allowance(msg.sender, address(this)) >= _amount,
            "Token allowance too low"
        );

        IERC20(_token).safeTransferFrom(msg.sender, address(this), _amount);

        bytes memory payload = abi.encode(
            TransferData({token: _token, receiver: _receiver, amount: _amount})
        );

        _lzSend(
            _dstChainId,
            payload,
            _refundAddress,
            _zroPaymentAddress,
            _adapterParams,
            msg.value
        );

        emit ValueSent(
            _dstChainId,
            msg.sender,
            _receiver,
            _token,
            _amount
        );
    }

    function _nonblockingLzReceive(
        uint16 _srcChainId,
        bytes memory _srcAddress,
        uint64 _nonce,
        bytes memory _payload
    ) internal override {
        TransferData memory data = abi.decode(_payload, (TransferData));

        IERC20(data.token).safeTransfer(data.receiver, data.amount);

        emit ValueReceived(
            _srcChainId,
            address(bytes20(_srcAddress)),
            data.receiver,
            data.token,
            data.amount
        );
    }

    function withdrawToken(
        address _token,
        uint256 _amount
    ) external onlyOwner {
        IERC20(_token).safeTransfer(msg.sender, _amount);
    }

    receive() external payable {}
}
```
