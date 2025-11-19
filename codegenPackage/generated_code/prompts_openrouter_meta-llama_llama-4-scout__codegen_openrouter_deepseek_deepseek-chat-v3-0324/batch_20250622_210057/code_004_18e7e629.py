"""
Generated Code Metadata:
========================
Original URL: https://dop-io.web.app
Prompt: Design a smart contract using Solidity that leverages DOP's flexible transparency on Ethereum L1, enabling private transactions and selective disclosure of token holdings.
Generated: DETERMINISTIC_18e7e629cd2d438a
Batch ID: 20250622_210057
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

/**
 * @title PrivateToken
 * @dev An ERC20 token with flexible transparency features allowing for private transactions
 * and selective disclosure of token holdings.
 */
contract PrivateToken is ERC20, Ownable {
    struct Disclosure {
        address verifier;
        uint256 amount;
        uint256 timestamp;
        bool verified;
    }

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => Disclosure)) private _disclosures;
    mapping(address => bool) private _whitelistedVerifiers;

    event TokensMinted(address indexed to, uint256 amount);
    event TokensBurned(address indexed from, uint256 amount);
    event DisclosureRequested(address indexed holder, address indexed verifier, uint256 amount);
    event DisclosureVerified(address indexed holder, address indexed verifier, uint256 amount);
    event VerifierWhitelisted(address indexed verifier);
    event VerifierRemoved(address indexed verifier);

    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @dev Mint new tokens (owner only)
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Burn tokens (owner only)
     */
    function burn(address from, uint256 amount) public onlyOwner {
        _burn(from, amount);
        emit TokensBurned(from, amount);
    }

    /**
     * @dev Override ERC20 transfer to make transactions private by default
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        require(sender != address(0), "PrivateToken: transfer from the zero address");
        require(recipient != address(0), "PrivateToken: transfer to the zero address");
        require(_balances[sender] >= amount, "PrivateToken: transfer amount exceeds balance");

        _balances[sender] -= amount;
        _balances[recipient] += amount;

        emit Transfer(sender, recipient, amount);
    }

    /**
     * @dev Request disclosure of token holdings to a specific verifier
     */
    function requestDisclosure(address verifier, uint256 amount) public {
        require(_whitelistedVerifiers[verifier], "PrivateToken: verifier not whitelisted");
        require(balanceOf(msg.sender) >= amount, "PrivateToken: insufficient balance");

        _disclosures[msg.sender][verifier] = Disclosure({
            verifier: verifier,
            amount: amount,
            timestamp: block.timestamp,
            verified: false
        });

        emit DisclosureRequested(msg.sender, verifier, amount);
    }

    /**
     * @dev Verify a disclosure request (verifier only)
     */
    function verifyDisclosure(address holder) public {
        require(_whitelistedVerifiers[msg.sender], "PrivateToken: caller not whitelisted verifier");
        Disclosure storage disclosure = _disclosures[holder][msg.sender];
        require(disclosure.verifier == msg.sender, "PrivateToken: no disclosure request found");
        require(!disclosure.verified, "PrivateToken: disclosure already verified");

        disclosure.verified = true;
        emit DisclosureVerified(holder, msg.sender, disclosure.amount);
    }

    /**
     * @dev Get verified disclosure amount for a holder-verifier pair
     */
    function getDisclosedAmount(address holder, address verifier) public view returns (uint256) {
        Disclosure memory disclosure = _disclosures[holder][verifier];
        require(disclosure.verified, "PrivateToken: disclosure not verified");
        return disclosure.amount;
    }

    /**
     * @dev Whitelist a verifier (owner only)
     */
    function whitelistVerifier(address verifier) public onlyOwner {
        _whitelistedVerifiers[verifier] = true;
        emit VerifierWhitelisted(verifier);
    }

    /**
     * @dev Remove a verifier from whitelist (owner only)
     */
    function removeVerifier(address verifier) public onlyOwner {
        _whitelistedVerifiers[verifier] = false;
        emit VerifierRemoved(verifier);
    }

    /**
     * @dev Check if an address is a whitelisted verifier
     */
    function isVerifierWhitelisted(address verifier) public view returns (bool) {
        return _whitelistedVerifiers[verifier];
    }

    /**
     * @dev Override balanceOf to return 0 unless there's a verified disclosure
     */
    function balanceOf(address account) public view override returns (uint256) {
        if (_disclosures[account][msg.sender].verified) {
            return _balances[account];
        }
        return 0;
    }

    /**
     * @dev Get actual balance (for contract internal use)
     */
    function _getActualBalance(address account) private view returns (uint256) {
        return _balances[account];
    }
}
```
