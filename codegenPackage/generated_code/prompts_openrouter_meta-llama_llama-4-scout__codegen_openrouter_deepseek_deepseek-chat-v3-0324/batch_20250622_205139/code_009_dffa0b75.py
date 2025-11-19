"""
Generated Code Metadata:
========================
Original URL: https://linea-web3.pages.dev
Prompt: "Propose a decentralized finance (DeFi) use case on Linea, utilizing its institutional DeFi features and security partnerships."
Generated: DETERMINISTIC_dffa0b75fce0a317
Batch ID: 20250622_205139
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title InstitutionalYieldVault
 * @dev A secure DeFi vault for institutional investors on Linea with:
 * - Whitelisted institutional access
 * - Multi-signature security
 * - Audited yield strategies
 * - Compliance features
 */
contract InstitutionalYieldVault is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Security partner addresses (to be set during deployment)
    address public auditor;
    address public complianceOfficer;
    address public riskManager;

    // Supported stablecoin
    IERC20 public immutable stablecoin;

    // Whitelist mapping for institutional investors
    mapping(address => bool) public whitelistedInstitutions;

    // Investor balances
    mapping(address => uint256) public balances;

    // Total assets under management
    uint256 public totalAUM;

    // Yield strategy parameters
    uint256 public currentAPY; // Annual Percentage Yield
    uint256 public lastYieldDistribution;
    uint256 public yieldDistributionInterval = 30 days;

    // Multi-sig requirements
    uint256 public constant REQUIRED_SIGNATURES = 2;
    mapping(address => bool) public signers;
    mapping(bytes32 => mapping(address => bool)) public confirmations;

    // Events
    event WhitelistUpdated(address institution, bool status);
    event Deposited(address indexed investor, uint256 amount);
    event Withdrawn(address indexed investor, uint256 amount);
    event YieldDistributed(uint256 amount);
    event StrategyUpdated(uint256 newAPY);
    event SignerAdded(address signer);
    event SignerRemoved(address signer);
    event TransactionConfirmed(bytes32 txHash, address signer);

    modifier onlyWhitelisted() {
        require(whitelistedInstitutions[msg.sender], "Not whitelisted");
        _;
    }

    modifier onlySigner() {
        require(signers[msg.sender], "Not authorized signer");
        _;
    }

    constructor(
        address _stablecoin,
        address _auditor,
        address _complianceOfficer,
        address _riskManager
    ) {
        require(_stablecoin != address(0), "Invalid stablecoin address");
        require(_auditor != address(0), "Invalid auditor address");
        require(_complianceOfficer != address(0), "Invalid compliance address");
        require(_riskManager != address(0), "Invalid risk manager address");

        stablecoin = IERC20(_stablecoin);
        auditor = _auditor;
        complianceOfficer = _complianceOfficer;
        riskManager = _riskManager;

        // Initialize the multi-sig signers
        signers[msg.sender] = true;
        signers[_auditor] = true;
        signers[_complianceOfficer] = true;
    }

    /**
     * @dev Deposit stablecoins into the vault
     * @param amount Amount of stablecoins to deposit
     */
    function deposit(uint256 amount) external nonReentrant onlyWhitelisted {
        require(amount > 0, "Amount must be positive");

        // Transfer stablecoins from investor to vault
        require(
            stablecoin.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );

        balances[msg.sender] = balances[msg.sender].add(amount);
        totalAUM = totalAUM.add(amount);

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw stablecoins from the vault
     * @param amount Amount of stablecoins to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant onlyWhitelisted {
        require(amount > 0, "Amount must be positive");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] = balances[msg.sender].sub(amount);
        totalAUM = totalAUM.sub(amount);

        // Transfer stablecoins back to investor
        require(stablecoin.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Distribute yield to all investors
     */
    function distributeYield() external nonReentrant {
        require(
            block.timestamp >= lastYieldDistribution + yieldDistributionInterval,
            "Too soon for next distribution"
        );

        uint256 yieldAmount = calculateYield();
        require(yieldAmount > 0, "No yield to distribute");

        // Simulate yield distribution (in a real implementation, this would interact with yield strategies)
        lastYieldDistribution = block.timestamp;

        emit YieldDistributed(yieldAmount);
    }

    /**
     * @dev Calculate current yield based on APY and time passed
     */
    function calculateYield() public view returns (uint256) {
        uint256 timePassed = block.timestamp.sub(lastYieldDistribution);
        return totalAUM.mul(currentAPY).mul(timePassed).div(365 days).div(100);
    }

    /**
     * @dev Update the yield strategy (requires multi-sig)
     * @param newAPY The new annual percentage yield
     * @param txHash The transaction hash for multi-sig confirmation
     */
    function updateStrategy(uint256 newAPY, bytes32 txHash) external onlySigner {
        confirmTransaction(txHash);

        if (isConfirmed(txHash)) {
            currentAPY = newAPY;
            emit StrategyUpdated(newAPY);
        }
    }

    /**
     * @dev Whitelist an institutional investor (requires multi-sig)
     * @param institution Address to whitelist
     * @param status Whitelist status
     * @param txHash The transaction hash for multi-sig confirmation
     */
    function updateWhitelist(
        address institution,
        bool status,
        bytes32 txHash
    ) external onlySigner {
        confirmTransaction(txHash);

        if (isConfirmed(txHash)) {
            whitelistedInstitutions[institution] = status;
            emit WhitelistUpdated(institution, status);
        }
    }

    /**
     * @dev Add a new signer to the multi-sig (requires multi-sig)
     * @param newSigner Address to add as signer
     * @param txHash The transaction hash for multi-sig confirmation
     */
    function addSigner(address newSigner, bytes32 txHash) external onlySigner {
        confirmTransaction(txHash);

        if (isConfirmed(txHash)) {
            signers[newSigner] = true;
            emit SignerAdded(newSigner);
        }
    }

    /**
     * @dev Remove a signer from the multi-sig (requires multi-sig)
     * @param signerToRemove Address to remove as signer
     * @param txHash The transaction hash for multi-sig confirmation
     */
    function removeSigner(address signerToRemove, bytes32 txHash) external onlySigner {
        confirmTransaction(txHash);

        if (isConfirmed(txHash)) {
            require(signers[signerToRemove], "Not a current signer");
            signers[signerToRemove] = false;
            emit SignerRemoved(signerToRemove);
        }
    }

    /**
     * @dev Confirm a multi-sig transaction
     * @param txHash The transaction hash to confirm
     */
    function confirmTransaction(bytes32 txHash) public onlySigner {
        confirmations[txHash][msg.sender] = true;
        emit TransactionConfirmed(txHash, msg.sender);
    }

    /**
     * @dev Check if a transaction has enough confirmations
     * @param txHash The transaction hash to check
     */
    function isConfirmed(bytes32 txHash) public view returns (bool) {
        uint256 count = 0;
        for (uint256 i = 0; i < REQUIRED_SIGNATURES; i++) {
            if (confirmations[txHash][address(uint160(i))]) {
                count += 1;
            }
            if (count >= REQUIRED_SIGNATURES) {
                return true;
            }
        }
        return false;
    }

    /**
     * @dev Emergency pause all operations (requires multi-sig)
     * @param txHash The transaction hash for multi-sig confirmation
     */
    function emergencyPause(bytes32 txHash) external onlySigner {
        confirmTransaction(txHash);

        if (isConfirmed(txHash)) {
            _pause();
        }
    }
}
```
