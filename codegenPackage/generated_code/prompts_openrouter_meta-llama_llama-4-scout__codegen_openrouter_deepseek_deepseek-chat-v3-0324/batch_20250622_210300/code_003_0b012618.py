"""
Generated Code Metadata:
========================
Original URL: https://pepeunchained-as.web.app
Prompt: Generate a smart contract code snippet for creating a meme coin ecosystem on a layer 2 blockchain, inspired by Pepe Unchained's features and $PEPU tokenomics.
Generated: DETERMINISTIC_0b012618bca4bcea
Batch ID: 20250622_210300
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Snapshot.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract PEPU is ERC20, ERC20Burnable, ERC20Snapshot, Ownable, Pausable {
    using SafeMath for uint256;

    uint256 public constant MAX_SUPPLY = 420690000000000 * 10**18; // 420.69 trillion
    uint256 public constant INITIAL_SUPPLY = 210345000000000 * 10**18; // 50% of max supply
    uint256 public constant TAX_RATE = 5; // 5% tax
    address public treasuryWallet;
    address public stakingContract;
    address public bridgeContract;

    mapping(address => bool) private _isExcludedFromTax;
    mapping(address => bool) private _isBlacklisted;

    event TokensBridged(address indexed user, uint256 amount);
    event TreasuryWalletUpdated(address newWallet);
    event StakingContractUpdated(address newContract);
    event BridgeContractUpdated(address newContract);
    event BlacklistUpdated(address wallet, bool status);
    event TaxExclusionUpdated(address wallet, bool status);

    constructor(address _treasuryWallet) ERC20("Pepe Unchained", "PEPU") {
        require(_treasuryWallet != address(0), "Invalid treasury wallet");
        treasuryWallet = _treasuryWallet;
        _mint(msg.sender, INITIAL_SUPPLY);
        _isExcludedFromTax[msg.sender] = true;
        _isExcludedFromTax[_treasuryWallet] = true;
    }

    modifier onlyStakingOrBridge() {
        require(
            msg.sender == stakingContract || msg.sender == bridgeContract,
            "Caller is not staking or bridge contract"
        );
        _;
    }

    function snapshot() public onlyOwner {
        _snapshot();
    }

    function pause() public onlyOwner {
        _pause();
    }

    function unpause() public onlyOwner {
        _unpause();
    }

    function updateTreasuryWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Invalid address");
        treasuryWallet = newWallet;
        emit TreasuryWalletUpdated(newWallet);
    }

    function updateStakingContract(address newContract) external onlyOwner {
        require(newContract != address(0), "Invalid address");
        stakingContract = newContract;
        emit StakingContractUpdated(newContract);
    }

    function updateBridgeContract(address newContract) external onlyOwner {
        require(newContract != address(0), "Invalid address");
        bridgeContract = newContract;
        emit BridgeContractUpdated(newContract);
    }

    function setBlacklist(address wallet, bool status) external onlyOwner {
        _isBlacklisted[wallet] = status;
        emit BlacklistUpdated(wallet, status);
    }

    function setTaxExclusion(address wallet, bool status) external onlyOwner {
        _isExcludedFromTax[wallet] = status;
        emit TaxExclusionUpdated(wallet, status);
    }

    function mint(address to, uint256 amount) external onlyStakingOrBridge {
        require(totalSupply().add(amount) <= MAX_SUPPLY, "Max supply exceeded");
        _mint(to, amount);
    }

    function bridgeTokens(uint256 amount) external whenNotPaused {
        require(!_isBlacklisted[msg.sender], "Address is blacklisted");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        _burn(msg.sender, amount);
        emit TokensBridged(msg.sender, amount);
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20, ERC20Snapshot) whenNotPaused {
        require(!_isBlacklisted[from] && !_isBlacklisted[to], "Blacklisted address");
        super._beforeTokenTransfer(from, to, amount);
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        if (_isExcludedFromTax[sender] || _isExcludedFromTax[recipient]) {
            super._transfer(sender, recipient, amount);
        } else {
            uint256 taxAmount = amount.mul(TAX_RATE).div(100);
            uint256 transferAmount = amount.sub(taxAmount);
            
            super._transfer(sender, treasuryWallet, taxAmount);
            super._transfer(sender, recipient, transferAmount);
        }
    }

    function isBlacklisted(address wallet) public view returns (bool) {
        return _isBlacklisted[wallet];
    }

    function isExcludedFromTax(address wallet) public view returns (bool) {
        return _isExcludedFromTax[wallet];
    }
}
```
