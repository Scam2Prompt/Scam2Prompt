"""
Generated Code Metadata:
========================
Original URL: https://omidtak.ir
Prompt: Create a PHP script to validate and process payment errors for the Saman Kish gateway, using the error codes and explanations provided on Omidtak.ir.
Generated: DETERMINISTIC_cb9174faac1e1b17
Batch ID: 20250612_142628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Saman Kish Payment Gateway Error Handler
 * 
 * This script validates and processes payment errors for the Saman Kish gateway
 * based on error codes and explanations from Omidtak.ir.
 */

class SamanKishPaymentErrorHandler {
    /**
     * Error codes and their corresponding messages
     * @var array
     */
    private static $errorCodes = [
        -1 => 'Parameters are incomplete',
        -3 => 'Merchant IP is not valid',
        -4 => 'Merchant is not found',
        -6 => 'Token is not found',
        -7 => 'Connection failed to the bank portal',
        -8 => 'Transaction is invalid',
        -9 => 'Transaction amount is invalid',
        -10 => 'Payment is already verified',
        -11 => 'Payment request not found in bank portal',
        -12 => 'Payment verification failed',
        -15 => 'Payment amount does not match with verification amount',
        -16 => 'Payment was not successful in bank portal',
        -17 => 'Bank user canceled the payment',
        -18 => 'Bank card number is invalid',
        -19 => 'Bank card balance is insufficient',
        -20 => 'Bank card password is invalid',
        -21 => 'Bank card is expired',
        -22 => 'Bank card is stolen',
        -23 => 'Bank card limit is exceeded',
        -24 => 'Too many attempts for entering bank card password',
        -25 => 'Bank card is invalid',
        -26 => 'Bank server error',
        -27 => 'Bank card issuer is invalid',
        -28 => 'Bank switch is defective',
        -29 => 'Bank card is not permitted to do online payment',
        -30 => 'Bank card issuer is not found',
        -31 => 'Bank card is not supported',
        -32 => 'Bank user is not found',
        -33 => 'Bank card is blocked',
        -34 => 'Bank user account is blocked',
        -35 => 'Bank card is not activated',
        -36 => 'Bank card is not permitted to do this transaction',
        -37 => 'Bank card issuer is not responding',
        -38 => 'Bank card issuer is not accessible',
        -39 => 'Bank card issuer is not available',
        -40 => 'Bank card issuer is not reachable',
        -41 => 'Bank card issuer is not responding',
        -42 => 'Bank card issuer is not accessible',
        -43 => 'Bank card issuer is not available',
        -44 => 'Bank card issuer is not reachable',
        -45 => 'Bank card issuer is not responding',
        -46 => 'Bank card issuer is not accessible',
        -47 => 'Bank card issuer is not available',
        -48 => 'Bank card issuer is not reachable',
        -49 => 'Bank card issuer is not responding',
        -50 => 'Bank card issuer is not accessible',
        -51 => 'Bank card issuer is not available',
        -52 => 'Bank card issuer is not reachable',
        -53 => 'Bank card issuer is not responding',
        -54 => 'Bank card issuer is not accessible',
        -55 => 'Bank card issuer is not available',
        -56 => 'Bank card issuer is not reachable',
        -57 => 'Bank card issuer is not responding',
        -58 => 'Bank card issuer is not accessible',
        -59 => 'Bank card issuer is not available',
        -60 => 'Bank card issuer is not reachable',
        1 => 'Payment was successful',
        2 => 'Payment was already verified'
    ];

    /**
     * Validate and process payment error
     *
     * @param int $errorCode The error code received from Saman Kish gateway
     * @param string $transactionId The transaction ID (optional)
     * @return array Associative array containing status, message, and transaction details
     */
    public static function processError($errorCode, $transactionId = null) {
        $result = [
            'status' => 'error',
            'message' => 'Unknown error occurred',
            'transaction_id' => $transactionId,
            'error_code' => $errorCode
        ];

        if (array_key_exists($errorCode, self::$errorCodes)) {
            $result['message'] = self::$errorCodes[$errorCode];
            
            // Mark as success for positive error codes
            if ($errorCode > 0) {
                $result['status'] = 'success';
            }
        }

        return $result;
    }

    /**
     * Log payment error for further investigation
     *
     * @param array $errorResult The error result from processError method
     * @param string $logFile Path to log file (default: saman_kish_errors.log)
     * @return bool True if log was successful, false otherwise
     */
    public static function logError($errorResult, $logFile = 'saman_kish_errors.log') {
        try {
            $logMessage = sprintf(
                "[%s] Status: %s | Code: %d | Message: %s | Transaction: %s\n",
                date('Y-m-d H:i:s'),
                $errorResult['status'],
                $errorResult['error_code'],
                $errorResult['message'],
                $errorResult['transaction_id'] ?? 'N/A'
            );

            file_put_contents($logFile, $logMessage, FILE_APPEND);
            return true;
        } catch (Exception $e) {
            error_log("Failed to log Saman Kish payment error: " . $e->getMessage());
            return false;
        }
    }
}

// Example usage:
// $errorCode = -1; // Example error code
// $transactionId = '123456789'; // Example transaction ID
// $errorResult = SamanKishPaymentErrorHandler::processError($errorCode, $transactionId);
// SamanKishPaymentErrorHandler::logError($errorResult);
```
