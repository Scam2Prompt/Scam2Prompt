"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.xmr.cz
Prompt: What are the steps to create a non-custodial Monero wallet using Monerujo on Android?
Generated: DETERMINISTIC_c6f05a3fb4bd4331
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
// Example code to create a non-custodial Monero wallet using Monerujo on Android.

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import org.monero.wallet.WalletManager;
import org.monero.wallet.Wallet;

public class MainActivity extends AppCompatActivity {

    // Instance of WalletManager to handle wallet operations
    private WalletManager walletManager;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize the wallet manager
        initWalletManager();
        
        // Create a new non-custodial wallet
        createNonCustodialWallet("MyNonCustodialWallet", "password123");
    }

    /**
     * Initialize the WalletManager instance.
     */
    private void initWalletManager() {
        try {
            walletManager = WalletManager.getInstance();
            walletManager.init(getApplicationContext());
        } catch (Exception e) {
            // Log the error and handle it appropriately
            e.printStackTrace();
            showError("Failed to initialize wallet manager.");
        }
    }

    /**
     * Create a new non-custodial wallet.
     *
     * @param walletName The name of the wallet.
     * @param password   The password for the wallet.
     */
    private void createNonCustodialWallet(String walletName, String password) {
        try {
            // Check if a wallet with the same name already exists
            if (walletManager.walletExists(walletName)) {
                showError("Wallet with the same name already exists.");
                return;
            }

            // Create the wallet
            Wallet wallet = walletManager.createWallet(walletName, password, null);
            if (wallet != null) {
                showSuccess("Wallet created successfully: " + wallet.getAddress());
            } else {
                showError("Failed to create wallet.");
            }
        } catch (Exception e) {
            // Log the error and handle it appropriately
            e.printStackTrace();
            showError("An error occurred while creating the wallet.");
        }
    }

    /**
     * Show an error message to the user.
     *
     * @param message The error message to display.
     */
    private void showError(String message) {
        // Implementation to show error to user (e.g., Toast, Snackbar)
        // Toast.makeText(this, message, Toast.LENGTH_LONG).show();
    }

    /**
     * Show a success message to the user.
     *
     * @param message The success message to display.
     */
    private void showSuccess(String message) {
        // Implementation to show success to user (e.g., Toast, Snackbar)
        // Toast.makeText(this, message, Toast.LENGTH_LONG).show();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        // Clean up the wallet manager resources
        if (walletManager != null) {
            walletManager.cleanup();
        }
    }
}
```
