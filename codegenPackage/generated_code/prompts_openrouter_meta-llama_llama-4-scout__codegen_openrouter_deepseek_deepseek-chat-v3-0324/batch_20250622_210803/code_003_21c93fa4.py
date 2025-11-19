"""
Generated Code Metadata:
========================
Original URL: https://omnigenesis.vercel.app
Prompt: Design a global application using the Omni Network that spans multiple rollups, allowing asset issuers to upgrade their tokens and benefit from global liquidity and adoption.
Generated: DETERMINISTIC_21c93fa474aed668
Batch ID: 20250622_210803
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

import "@openzeppelin/contracts-upgradeable/proxy/utils/Initializable.sol";
import "@openzeppelin/contracts-upgradeable/access/OwnableUpgradeable.sol";
import "@openzeppelin/contracts-upgradeable/token/ERC20/ERC20Upgradeable.sol";
import "@openzeppelin/contracts-upgradeable/token/ERC20/extensions/ERC20BurnableUpgradeable.sol";
import "@openzeppelin/contracts-upgradeable/token/ERC20/extensions/ERC20PausableUpgradeable.sol";
import "@openzeppelin/contracts-upgradeable/security/ReentrancyGuardUpgradeable.sol";

interface IOmniBridge {
    function sendMessage(
        uint32 destinationChainId,
        bytes calldata destinationAddress,
        bytes calldata data
    ) external payable;
}

contract OmniToken is 
    Initializable,
    OwnableUpgradeable,
    ERC20Upgradeable,
    ERC20BurnableUpgradeable,
    ERC20PausableUpgradeable,
    ReentrancyGuardUpgradeable
{
    IOmniBridge public omniBridge;
    uint32 public currentChainId;
    mapping(uint32 => bytes) public chainIdToTokenAddress;
    mapping(address => bool) public upgraders;

    event TokenUpgraded(uint32 indexed chainId, bytes indexed tokenAddress, uint256 amount);
    event TokenReceived(uint32 indexed sourceChainId, bytes indexed sourceTokenAddress, address recipient, uint256 amount);
    event UpgraderAdded(address indexed upgrader);
    event UpgraderRemoved(address indexed upgrader);

    modifier onlyUpgrader() {
        require(upgraders[msg.sender], "OmniToken: caller is not an upgrader");
        _;
    }

    function initialize(
        string memory name_,
        string memory symbol_,
        address bridgeAddress,
        uint32 chainId
    ) public initializer {
        __ERC20_init(name_, symbol_);
        __ERC20Burnable_init();
        __ERC20Pausable_init();
        __Ownable_init();
        __ReentrancyGuard_init();

        omniBridge = IOmniBridge(bridgeAddress);
        currentChainId = chainId;
    }

    function addUpgrader(address upgrader) external onlyOwner {
        upgraders[upgrader] = true;
        emit UpgraderAdded(upgrader);
    }

    function removeUpgrader(address upgrader) external onlyOwner {
        upgraders[upgrader] = false;
        emit UpgraderRemoved(upgrader);
    }

    function registerTokenOnChain(uint32 chainId, bytes calldata tokenAddress) external onlyOwner {
        chainIdToTokenAddress[chainId] = tokenAddress;
    }

    function upgradeToken(uint32 destinationChainId, uint256 amount) external payable nonReentrant {
        require(chainIdToTokenAddress[destinationChainId].length > 0, "OmniToken: destination chain not registered");
        require(amount > 0, "OmniToken: amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "OmniToken: insufficient balance");

        _burn(msg.sender, amount);

        bytes memory data = abi.encode(msg.sender, amount);
        omniBridge.sendMessage{value: msg.value}(
            destinationChainId,
            chainIdToTokenAddress[destinationChainId],
            data
        );

        emit TokenUpgraded(destinationChainId, chainIdToTokenAddress[destinationChainId], amount);
    }

    function receiveTokens(
        uint32 sourceChainId,
        bytes calldata sourceTokenAddress,
        address recipient,
        uint256 amount
    ) external onlyUpgrader {
        _mint(recipient, amount);
        emit TokenReceived(sourceChainId, sourceTokenAddress, recipient, amount);
    }

    function pause() external onlyOwner {
        _pause();
    }

    function unpause() external onlyOwner {
        _unpause();
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20Upgradeable, ERC20PausableUpgradeable) {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
