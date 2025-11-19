"""
Generated Code Metadata:
========================
Original URL: https://layer-1yd.pages.dev
Prompt: Generate a Solidity implementation of an Omnichain Fungible Token (OFT) using LayerZero's `OFTCore` interface. Ensure the contract supports cross-chain token transfers without asset wrapping.
Generated: DETERMINISTIC_19817a65aa34052b
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

contract OmnichainFungibleToken is OFTCore, ERC20, Ownable {
    uint256 private _initialSupply;

    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _initialAmount,
        address _lzEndpoint
    ) ERC20(_name, _symbol) OFTCore(_lzEndpoint) {
        _initialSupply = _initialAmount;
        _mint(msg.sender, _initialAmount);
    }

    function supportsInterface(bytes4 interfaceId) public view virtual override(OFTCore, IERC165) returns (bool) {
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
        if (_from != spender) {
            _spendAllowance(_from, spender, _amount);
        }
        _burn(_from, _amount);
        return _amount;
    }

    function _creditTo(uint16, address _toAddress, uint256 _amount) internal virtual override returns (uint256) {
        _mint(_toAddress, _amount);
        return _amount;
    }

    function mint(address _to, uint256 _amount) external onlyOwner {
        _mint(_to, _amount);
    }

    function burn(address _from, uint256 _amount) external onlyOwner {
        _burn(_from, _amount);
    }
}
```
