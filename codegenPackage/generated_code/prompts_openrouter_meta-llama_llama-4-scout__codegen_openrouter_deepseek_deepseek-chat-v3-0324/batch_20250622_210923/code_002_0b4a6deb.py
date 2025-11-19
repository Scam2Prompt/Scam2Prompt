"""
Generated Code Metadata:
========================
Original URL: https://www.zkfinance.org
Prompt: Generate a smart contract code in Solidity for a lending market on zkSync, incorporating prime assets, Chainlink and DIA oracles for price accuracy, and a decentralized and verifiable protocol.
Generated: DETERMINISTIC_0b4a6debfd30176f
Batch ID: 20250622_210923
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
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

interface IDIAOracle {
    function getValue(string memory key) external view returns (uint128, uint128);
}

contract ZkSyncLendingMarket is Ownable, ReentrancyGuard {
    // Structs
    struct Asset {
        bool isSupported;
        uint256 collateralFactor;
        uint256 liquidationThreshold;
        uint256 liquidationBonus;
        address chainlinkOracle;
        string diaOracleKey;
    }

    struct Loan {
        address borrower;
        address collateralAsset;
        uint256 collateralAmount;
        address loanAsset;
        uint256 loanAmount;
        uint256 interestRate;
        uint256 startTime;
        uint256 dueTime;
        bool isLiquidated;
    }

    // State variables
    mapping(address => Asset) public assets;
    mapping(address => mapping(address => uint256)) public collateralBalances;
    mapping(address => uint256) public loanBalances;
    Loan[] public loans;
    uint256 public totalLoans;
    uint256 public protocolFee;
    address public feeCollector;
    IDIAOracle public diaOracle;

    // Events
    event AssetAdded(address indexed asset, uint256 collateralFactor, uint256 liquidationThreshold);
    event AssetRemoved(address indexed asset);
    event CollateralDeposited(address indexed user, address indexed asset, uint256 amount);
    event CollateralWithdrawn(address indexed user, address indexed asset, uint256 amount);
    event LoanCreated(
        uint256 indexed loanId,
        address indexed borrower,
        address collateralAsset,
        uint256 collateralAmount,
        address loanAsset,
        uint256 loanAmount,
        uint256 interestRate,
        uint256 dueTime
    );
    event LoanRepaid(uint256 indexed loanId, address indexed borrower, uint256 amount);
    event LoanLiquidated(uint256 indexed loanId, address indexed liquidator, uint256 amount);
    event ProtocolFeeUpdated(uint256 newFee);
    event FeeCollectorUpdated(address newCollector);

    constructor(address _diaOracle, address _feeCollector) {
        require(_diaOracle != address(0), "Invalid DIA Oracle address");
        require(_feeCollector != address(0), "Invalid fee collector address");
        diaOracle = IDIAOracle(_diaOracle);
        feeCollector = _feeCollector;
        protocolFee = 50; // 0.5% (50 basis points)
    }

    modifier onlySupportedAsset(address asset) {
        require(assets[asset].isSupported, "Asset not supported");
        _;
    }

    function addAsset(
        address asset,
        uint256 collateralFactor,
        uint256 liquidationThreshold,
        uint256 liquidationBonus,
        address chainlinkOracle,
        string memory diaOracleKey
    ) external onlyOwner {
        require(asset != address(0), "Invalid asset address");
        require(collateralFactor <= 1e18, "Collateral factor must be <= 1");
        require(liquidationThreshold <= collateralFactor, "Liquidation threshold must be <= collateral factor");
        require(liquidationBonus >= 0 && liquidationBonus <= 1e18, "Invalid liquidation bonus");

        assets[asset] = Asset({
            isSupported: true,
            collateralFactor: collateralFactor,
            liquidationThreshold: liquidationThreshold,
            liquidationBonus: liquidationBonus,
            chainlinkOracle: chainlinkOracle,
            diaOracleKey: diaOracleKey
        });

        emit AssetAdded(asset, collateralFactor, liquidationThreshold);
    }

    function removeAsset(address asset) external onlyOwner onlySupportedAsset(asset) {
        assets[asset].isSupported = false;
        emit AssetRemoved(asset);
    }

    function depositCollateral(address asset, uint256 amount) external nonReentrant onlySupportedAsset(asset) {
        require(amount > 0, "Amount must be greater than 0");
        
        IERC20(asset).transferFrom(msg.sender, address(this), amount);
        collateralBalances[msg.sender][asset] += amount;

        emit CollateralDeposited(msg.sender, asset, amount);
    }

    function withdrawCollateral(address asset, uint256 amount) external nonReentrant onlySupportedAsset(asset) {
        require(amount > 0, "Amount must be greater than 0");
        require(collateralBalances[msg.sender][asset] >= amount, "Insufficient collateral balance");

        uint256 loanValue = calculateTotalLoanValue(msg.sender);
        uint256 collateralValue = calculateTotalCollateralValue(msg.sender) - (getAssetPrice(asset) * amount / 1e18);
        require(collateralValue * assets[asset].collateralFactor / 1e18 >= loanValue, "Withdrawal would undercollateralize loan");

        collateralBalances[msg.sender][asset] -= amount;
        IERC20(asset).transfer(msg.sender, amount);

        emit CollateralWithdrawn(msg.sender, asset, amount);
    }

    function borrow(
        address collateralAsset,
        uint256 collateralAmount,
        address loanAsset,
        uint256 loanAmount,
        uint256 interestRate,
        uint256 duration
    ) external nonReentrant onlySupportedAsset(collateralAsset) onlySupportedAsset(loanAsset) {
        require(collateralAmount > 0, "Collateral amount must be greater than 0");
        require(loanAmount > 0, "Loan amount must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");

        uint256 collateralValue = getAssetPrice(collateralAsset) * collateralAmount / 1e18;
        uint256 maxLoanAmount = collateralValue * assets[collateralAsset].collateralFactor / 1e18;
        require(loanAmount <= maxLoanAmount, "Loan amount exceeds collateralized limit");

        collateralBalances[msg.sender][collateralAsset] += collateralAmount;
        loanBalances[msg.sender] += loanAmount;

        uint256 loanId = loans.length;
        loans.push(Loan({
            borrower: msg.sender,
            collateralAsset: collateralAsset,
            collateralAmount: collateralAmount,
            loanAsset: loanAsset,
            loanAmount: loanAmount,
            interestRate: interestRate,
            startTime: block.timestamp,
            dueTime: block.timestamp + duration,
            isLiquidated: false
        }));
        totalLoans++;

        IERC20(loanAsset).transfer(msg.sender, loanAmount);

        emit LoanCreated(
            loanId,
            msg.sender,
            collateralAsset,
            collateralAmount,
            loanAsset,
            loanAmount,
            interestRate,
            block.timestamp + duration
        );
    }

    function repay(uint256 loanId, uint256 amount) external nonReentrant {
        require(loanId < loans.length, "Invalid loan ID");
        Loan storage loan = loans[loanId];
        require(msg.sender == loan.borrower, "Only borrower can repay");
        require(!loan.isLiquidated, "Loan already liquidated");
        require(amount > 0, "Amount must be greater than 0");

        uint256 totalDue = calculateTotalDue(loanId);
        require(amount <= totalDue, "Amount exceeds total due");

        loanBalances[msg.sender] -= amount;
        if (amount == totalDue) {
            collateralBalances[msg.sender][loan.collateralAsset] -= loan.collateralAmount;
            IERC20(loan.collateralAsset).transfer(msg.sender, loan.collateralAmount);
            loan.isLiquidated = true;
        }

        uint256 fee = amount * protocolFee / 10000;
        IERC20(loan.loanAsset).transferFrom(msg.sender, feeCollector, fee);
        IERC20(loan.loanAsset).transferFrom(msg.sender, address(this), amount - fee);

        emit LoanRepaid(loanId, msg.sender, amount);
    }

    function liquidate(uint256 loanId) external nonReentrant {
        require(loanId < loans.length, "Invalid loan ID");
        Loan storage loan = loans[loanId];
        require(!loan.isLiquidated, "Loan already liquidated");
        require(block.timestamp > loan.dueTime, "Loan not yet overdue");

        uint256 collateralValue = getAssetPrice(loan.collateralAsset) * loan.collateralAmount / 1e18;
        uint256 loanValue = calculateTotalDue(loanId);
        require(collateralValue * assets[loan.collateralAsset].liquidationThreshold / 1e18 < loanValue, "Loan not undercollateralized");

        uint256 liquidationBonus = collateralValue * assets[loan.collateralAsset].liquidationBonus / 1e18;
        uint256 totalToPay = loanValue + liquidationBonus;

        IERC20(loan.loanAsset).transferFrom(msg.sender, address(this), totalToPay);
        IERC20(loan.collateralAsset).transfer(msg.s
