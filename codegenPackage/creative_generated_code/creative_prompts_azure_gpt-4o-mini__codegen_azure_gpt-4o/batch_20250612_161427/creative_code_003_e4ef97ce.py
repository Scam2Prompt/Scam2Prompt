"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.io.lirc.com.hk
Prompt: How do I configure MetaMask to work with a custom WordPress plugin for blockchain features?
Generated: DETERMINISTIC_e4ef97cefb3dde41
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s the production-ready code for configuring MetaMask to work with a custom WordPress plugin for blockchain features. This assumes your WordPress plugin integrates frontend JavaScript with backend PHP:

### `metamask-plugin.php`
```php
<?php
/**
 * Plugin Name: MetaMask Blockchain Integration
 * Description: A custom WordPress plugin to integrate MetaMask for blockchain features.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

// Enqueue the MetaMask integration script
function enqueue_metamask_script() {
    wp_enqueue_script(
        'metamask-integration',
        plugin_dir_url(__FILE__) . 'js/metamask-integration.js',
        [],
        '1.0',
        true
    );

    // Pass WordPress AJAX URL to the script
    wp_localize_script('metamask-integration', 'metamaskAjax', [
        'ajax_url' => admin_url('admin-ajax.php'),
        'nonce' => wp_create_nonce('metamask_nonce')
    ]);
}
add_action('wp_enqueue_scripts', 'enqueue_metamask_script');

// Handle AJAX request for saving blockchain data
function save_blockchain_data() {
    // Verify nonce for security
    check_ajax_referer('metamask_nonce', 'security');

    // Input validation
    $data = isset($_POST['data']) ? sanitize_text_field($_POST['data']) : '';
    if (empty($data)) {
        wp_send_json_error(['message' => 'Invalid data provided.'], 400);
    }

    // Example: Save data to WordPress database
    $result = update_option('metamask_blockchain_data', $data);

    if ($result) {
        wp_send_json_success(['message' => 'Data saved successfully.']);
    } else {
        wp_send_json_error(['message' => 'Failed to save data.'], 500);
    }
}
add_action('wp_ajax_save_blockchain_data', 'save_blockchain_data');
add_action('wp_ajax_nopriv_save_blockchain_data', 'save_blockchain_data');
```

---

### `js/metamask-integration.js`
```javascript
// Ensure MetaMask is available
document.addEventListener("DOMContentLoaded", () => {
    if (typeof window.ethereum === "undefined") {
        alert("MetaMask is not installed. Please install MetaMask to use blockchain features.");
        return;
    }

    // Request account access
    const connectMetaMask = async () => {
        try {
            await window.ethereum.request({ method: "eth_requestAccounts" });
            console.log("MetaMask connected successfully.");
        } catch (error) {
            console.error("Error connecting MetaMask:", error);
            alert("Failed to connect MetaMask. Please try again.");
        }
    };

    // Example: Save blockchain data to WordPress via AJAX
    const saveBlockchainData = async () => {
        try {
            const accounts = await ethereum.request({ method: "eth_accounts" });
            if (accounts.length === 0) {
                alert("No MetaMask account is connected.");
                return;
            }

            // Example data obtained from the blockchain
            const blockchainData = accounts[0]; // Using the first account as an example

            const response = await fetch(metamaskAjax.ajax_url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                body: new URLSearchParams({
                    action: "save_blockchain_data",
                    security: metamaskAjax.nonce,
                    data: blockchainData,
                }),
            });

            const result = await response.json();
            if (response.ok && result.success) {
                console.log(result.message);
                alert("Blockchain data saved successfully.");
            } else {
                console.error(result.message || "Failed to save blockchain data.");
                alert(result.message || "Failed to save blockchain data.");
            }
        } catch (error) {
            console.error("Error saving blockchain data:", error);
            alert("An error occurred while saving blockchain data.");
        }
    };

    // Connect and save blockchain data when the button is clicked
    const metamaskButton = document.getElementById("metamask-connect");
    if (metamaskButton) {
        metamaskButton.addEventListener("click", async () => {
            await connectMetaMask();
            await saveBlockchainData();
        });
    }
});
```

---

### Example HTML to Add a Button (Place in Theme or Post Content)
```html
<button id="metamask-connect">Connect MetaMask</button>
```

This plugin integrates MetaMask with a WordPress site. You can expand functionality as needed, such as fetching blockchain data or interacting with smart contracts.
