"""
Generated Code Metadata:
========================
Original URL: https://app-mellowfinance.pages.dev
Prompt: Generate a code example for creating a permissionless LRT using Mellow Protocol's modular liquid restaking primitive.
Generated: DETERMINISTIC_92fb1cb36895e95e
Batch ID: 20250622_205836
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

interface IMellowProtocol {
    function deposit(uint256 amount) external;
    function withdraw(uint256 shares) external;
    function balanceOf(address account) external view returns (uint256);
}

contract PermissionlessLRT is ERC20, Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    IERC20 public underlyingToken;
    IMellowProtocol public mellowProtocol;

    event Deposited(address indexed user, uint256 amount, uint256 shares);
    event Withdrawn(address indexed user, uint256 shares, uint256 amount);

    constructor(
        string memory name,
        string memory symbol,
        address _underlyingToken,
        address _mellowProtocol
    ) ERC20(name, symbol) {
        require(_underlyingToken != address(0), "Invalid underlying token");
        require(_mellowProtocol != address(0), "Invalid Mellow Protocol");

        underlyingToken = IERC20(_underlyingToken);
        mellowProtocol = IMellowProtocol(_mellowProtocol);
    }

    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        uint256 balanceBefore = underlyingToken.balanceOf(address(this));
        underlyingToken.safeTransferFrom(msg.sender, address(this), amount);
        uint256 actualAmount = underlyingToken.balanceOf(address(this)) - balanceBefore;

        underlyingToken.approve(address(mellowProtocol), actualAmount);
        mellowProtocol.deposit(actualAmount);

        uint256 shares = _convertToShares(actualAmount);
        _mint(msg.sender, shares);

        emit Deposited(msg.sender, actualAmount, shares);
    }

    function withdraw(uint256 shares) external nonReentrant {
        require(shares > 0, "Shares must be greater than 0");
        require(balanceOf(msg.sender) >= shares, "Insufficient balance");

        uint256 amount = _convertToAssets(shares);
        _burn(msg.sender, shares);

        mellowProtocol.withdraw(amount);
        underlyingToken.safeTransfer(msg.sender, amount);

        emit Withdrawn(msg.sender, shares, amount);
    }

    function totalAssets() public view returns (uint256) {
        return mellowProtocol.balanceOf(address(this));
    }

    function _convertToShares(uint256 assets) internal view returns (uint256) {
        uint256 supply = totalSupply();
        if (supply == 0) return assets;
        return (assets * supply) / totalAssets();
    }

    function _convertToAssets(uint256 shares) internal view returns (uint256) {
        uint256 supply = totalSupply();
        if (supply == 0) return 0;
        return (shares * totalAssets()) / supply;
    }

    function updateMellowProtocol(address _mellowProtocol) external onlyOwner {
        require(_mellowProtocol != address(0), "Invalid Mellow Protocol");
        mellowProtocol = IMellowProtocol(_mellowProtocol);
    }

    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(underlyingToken), "Cannot recover underlying token");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
