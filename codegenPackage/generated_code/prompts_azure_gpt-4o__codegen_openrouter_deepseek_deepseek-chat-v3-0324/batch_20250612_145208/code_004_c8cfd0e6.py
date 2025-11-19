"""
Generated Code Metadata:
========================
Original URL: https://lite-nuxt-git-f-veda-vault-instadapp-eng.vercel.app
Prompt: Develop a smart contract that integrates with Instadapp Lite to execute cross-protocol refinancing strategies, leveraging protocols like AAVE and Compound.
Generated: DETERMINISTIC_c8cfd0e6c5f834d7
Batch ID: 20250612_145208
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
import "./interfaces/InstadappLite.sol";
import "./interfaces/AAVE.sol";
import "./interfaces/Compound.sol";

contract CrossProtocolRefinancer is Ownable, ReentrancyGuard {
    IInstadappLite public immutable instadappLite;
    ILendingPool public immutable aaveLendingPool;
    IComptroller public immutable compoundComptroller;

    mapping(address => bool) public authorizedStrategists;

    event RefinanceExecuted(
        address indexed user,
        address indexed fromProtocol,
        address indexed toProtocol,
        uint256 amount
    );
    event StrategistAuthorized(address strategist);
    event StrategistRevoked(address strategist);

    constructor(
        address _instadappLite,
        address _aaveLendingPool,
        address _compoundComptroller
    ) {
        require(_instadappLite != address(0), "Invalid Instadapp address");
        require(_aaveLendingPool != address(0), "Invalid AAVE address");
        require(_compoundComptroller != address(0), "Invalid Compound address");

        instadappLite = IInstadappLite(_instadappLite);
        aaveLendingPool = ILendingPool(_aaveLendingPool);
        compoundComptroller = IComptroller(_compoundComptroller);
    }

    modifier onlyStrategist() {
        require(authorizedStrategists[msg.sender], "Not authorized strategist");
        _;
    }

    function authorizeStrategist(address _strategist) external onlyOwner {
        authorizedStrategists[_strategist] = true;
        emit StrategistAuthorized(_strategist);
    }

    function revokeStrategist(address _strategist) external onlyOwner {
        authorizedStrategists[_strategist] = false;
        emit StrategistRevoked(_strategist);
    }

    function refinanceAAVEToCompound(
        address _token,
        uint256 _amount,
        address _cToken
    ) external onlyStrategist nonReentrant {
        require(_token != address(0), "Invalid token address");
        require(_cToken != address(0), "Invalid cToken address");
        require(_amount > 0, "Amount must be greater than 0");

        // 1. Withdraw from AAVE
        bytes memory withdrawData = abi.encodeWithSignature(
            "withdraw(address,uint256,address)",
            _token,
            _amount,
            address(this)
        );
        instadappLite.dsaCast(address(aaveLendingPool), withdrawData);

        // 2. Approve token for Compound
        IERC20(_token).approve(_cToken, _amount);

        // 3. Deposit to Compound
        bytes memory mintData = abi.encodeWithSignature(
            "mint(uint256)",
            _amount
        );
        instadappLite.dsaCast(_cToken, mintData);

        emit RefinanceExecuted(
            msg.sender,
            address(aaveLendingPool),
            _cToken,
            _amount
        );
    }

    function refinanceCompoundToAAVE(
        address _token,
        uint256 _amount,
        address _cToken
    ) external onlyStrategist nonReentrant {
        require(_token != address(0), "Invalid token address");
        require(_cToken != address(0), "Invalid cToken address");
        require(_amount > 0, "Amount must be greater than 0");

        // 1. Redeem from Compound
        bytes memory redeemData = abi.encodeWithSignature(
            "redeemUnderlying(uint256)",
            _amount
        );
        instadappLite.dsaCast(_cToken, redeemData);

        // 2. Approve token for AAVE
        IERC20(_token).approve(address(aaveLendingPool), _amount);

        // 3. Deposit to AAVE
        bytes memory depositData = abi.encodeWithSignature(
            "deposit(address,uint256,address,uint16)",
            _token,
            _amount,
            address(this),
            0
        );
        instadappLite.dsaCast(address(aaveLendingPool), depositData);

        emit RefinanceExecuted(
            msg.sender,
            _cToken,
            address(aaveLendingPool),
            _amount
        );
    }

    function emergencyWithdraw(
        address _token,
        uint256 _amount,
        address _recipient
    ) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        require(_recipient != address(0), "Invalid recipient address");
        IERC20(_token).transfer(_recipient, _amount);
    }
}
```
