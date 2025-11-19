"""
Generated Code Metadata:
========================
Original URL: https://layer-1yd.pages.dev
Prompt: Provide a Solidity implementation for transferring tokens across multiple blockchains using LayerZero's OFT standard, ensuring compatibility with Ethereum and Binance Smart Chain.
Generated: DETERMINISTIC_ff8d10297fc69815
Batch ID: 20250612_150226
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
import "@layerzerolabs/solidity-examples/contracts/token/oft/IOFTCore.sol";
import "@layerzerolabs/solidity-examples/contracts/token/oft/OFTCore.sol";

contract CrossChainToken is ERC20, OFTCore, Ownable {
    uint256 private _initialSupply;

    constructor(
        string memory _name,
        string memory _symbol,
        uint256 initialSupply_,
        address _lzEndpoint
    ) ERC20(_name, _symbol) OFTCore(_lzEndpoint) {
        _initialSupply = initialSupply_;
        _mint(msg.sender, initialSupply_);
    }

    function supportsInterface(bytes4 interfaceId) public view virtual override(OFTCore, ERC20) returns (bool) {
        return interfaceId == type(IOFTCore).interfaceId || interfaceId == type(IERC20).interfaceId || super.supportsInterface(interfaceId);
    }

    function token() public view virtual override returns (address) {
        return address(this);
    }

    function circulatingSupply() public view virtual override returns (uint256) {
        return totalSupply();
    }

    function _debitFrom(address _from, uint16, bytes memory, uint256 _amount) internal virtual override returns (uint256) {
        address spender = _msgSender();
        if (_from != spender) _spendAllowance(_from, spender, _amount);
        _burn(_from, _amount);
        return _amount;
    }

    function _creditTo(uint16, address _toAddress, uint256 _amount) internal virtual override returns (uint256) {
        _mint(_toAddress, _amount);
        return _amount;
    }

    function estimateSendFee(
        uint16 _dstChainId,
        bytes memory _toAddress,
        uint256 _amount,
        bool _useZro,
        bytes memory _adapterParams
    ) public view virtual override returns (uint256 nativeFee, uint256 zroFee) {
        return _estimateSendFee(_dstChainId, _toAddress, _amount, _useZro, _adapterParams);
    }

    function sendFrom(
        address _from,
        uint16 _dstChainId,
        bytes memory _toAddress,
        uint256 _amount,
        address payable _refundAddress,
        address _zroPaymentAddress,
        bytes memory _adapterParams
    ) public payable virtual override {
        _send(_from, _dstChainId, _toAddress, _amount, _refundAddress, _zroPaymentAddress, _adapterParams);
    }

    function mint(address account, uint256 amount) external onlyOwner {
        _mint(account, amount);
    }

    function burn(address account, uint256 amount) external onlyOwner {
        _burn(account, amount);
    }
}
```
