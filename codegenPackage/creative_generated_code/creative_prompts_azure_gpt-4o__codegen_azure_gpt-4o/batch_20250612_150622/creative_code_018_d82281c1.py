"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeth-route.pages.dev
Prompt: Develop a Solidity contract that integrates with Flux to lend stablecoins to borrowers collateralized by OUSG, as described in the OUSD yield strategies.
Generated: DETERMINISTIC_d82281c10d4d0262
Batch ID: 20250612_150622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import required libraries and interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

interface IFluxLending {
    function lend(address token, uint256 amount) external;
    function repay(address token, uint256 amount) external;
}

interface IPriceOracle {
    function getPrice(address asset) external view returns (uint256);
}

contract StablecoinLending is Ownable {
    // Stablecoin and collateral token addresses
    IERC20 public stablecoin;
    IERC20 public ousg;

    // Flux Lending protocol address
    IFluxLending public fluxLending;

    // Price Oracle for OUSG collateral valuation
    IPriceOracle public priceOracle;

    // Collateralization ratio (e.g., 150% collateral required)
    uint256 public collateralizationRatio = 150; // 150%

    // Events for logging activity
    event LoanIssued(address indexed borrower, uint256 collateralAmount, uint256 loanAmount);
    event LoanRepaid(address indexed borrower, uint256 repaymentAmount);
    event CollateralSeized(address indexed borrower, uint256 collateralAmount);

    // Mapping to store borrower data
    struct BorrowerData {
        uint256 collateralAmount;
        uint256 loanAmount;
    }
    mapping(address => BorrowerData) public borrowers;

    // Modifier to ensure valid collateralization ratio
    modifier validCollateralization(uint256 collateralAmount, uint256 loanAmount) {
        uint256 collateralValue = collateralAmount * priceOracle.getPrice(address(ousg)) / (10 ** 18); // Adjust for price unit
        require(collateralValue >= (loanAmount * collateralizationRatio / 100), "Insufficient collateral");
        _;
    }

    constructor(
        address _stablecoin,
        address _ousg,
        address _fluxLending,
        address _priceOracle
    ) {
        stablecoin = IERC20(_stablecoin);
        ousg = IERC20(_ousg);
        fluxLending = IFluxLending(_fluxLending);
        priceOracle = IPriceOracle(_priceOracle);
    }

    /**
     * @dev Allows a borrower to deposit collateral and receive a stablecoin loan.
     * @param collateralAmount Amount of OUSG collateral to deposit.
     * @param loanAmount Amount of stablecoins to borrow.
     */
    function borrow(uint256 collateralAmount, uint256 loanAmount) external validCollateralization(collateralAmount, loanAmount) {
        // Transfer collateral from borrower to contract
        require(ousg.transferFrom(msg.sender, address(this), collateralAmount), "Collateral transfer failed");

        // Issue loan via Flux Lending
        fluxLending.lend(address(stablecoin), loanAmount);

        // Transfer stablecoins to borrower
        require(stablecoin.transfer(msg.sender, loanAmount), "Stablecoin transfer failed");

        // Record borrower data
        borrowers[msg.sender] = BorrowerData({
            collateralAmount: collateralAmount,
            loanAmount: loanAmount
        });

        emit LoanIssued(msg.sender, collateralAmount, loanAmount);
    }

    /**
     * @dev Allows a borrower to repay their loan and retrieve their collateral.
     * @param repaymentAmount Amount of stablecoins to repay.
     */
    function repay(uint256 repaymentAmount) external {
        BorrowerData storage data = borrowers[msg.sender];
        require(data.loanAmount >= repaymentAmount, "Repayment exceeds loan amount");

        // Transfer repayment from borrower to contract
        require(stablecoin.transferFrom(msg.sender, address(this), repaymentAmount), "Repayment transfer failed");

        // Repay loan via Flux Lending
        fluxLending.repay(address(stablecoin), repaymentAmount);

        // Update loan data
        data.loanAmount -= repaymentAmount;

        // Return collateral if loan is fully repaid
        if (data.loanAmount == 0) {
            uint256 collateralToReturn = data.collateralAmount;
            data.collateralAmount = 0;
            require(ousg.transfer(msg.sender, collateralToReturn), "Collateral transfer failed");
            emit LoanRepaid(msg.sender, repaymentAmount);
        }
    }

    /**
     * @dev Allows the contract owner to seize collateral in case of default.
     * @param borrower Address of the borrower in default.
     */
    function seizeCollateral(address borrower) external onlyOwner {
        BorrowerData storage data = borrowers[borrower];
        require(data.loanAmount > 0, "No active loan");

        uint256 collateralToSeize = data.collateralAmount;
        data.collateralAmount = 0;
        data.loanAmount = 0;

        // Transfer collateral to the contract owner
        require(ousg.transfer(owner(), collateralToSeize), "Collateral transfer failed");

        emit CollateralSeized(borrower, collateralToSeize);
    }

    /**
     * @dev Sets a new collateralization ratio.
     * @param _collateralizationRatio New collateralization ratio (percentage).
     */
    function setCollateralizationRatio(uint256 _collateralizationRatio) external onlyOwner {
        require(_collateralizationRatio >= 100, "Collateralization ratio must be at least 100%");
        collateralizationRatio = _collateralizationRatio;
    }
}
```
