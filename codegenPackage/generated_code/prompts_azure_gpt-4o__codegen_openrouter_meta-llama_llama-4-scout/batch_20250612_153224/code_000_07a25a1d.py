"""
Generated Code Metadata:
========================
Original URL: https://storebari.com
Prompt: Write PHP code to define the missing function `astra_sites_has_import_started()` for the Astra Sites WordPress plugin to prevent fatal errors during plugin execution.
Generated: DETERMINISTIC_07a25a1ddb15c844
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
/**
 * Checks if Astra Sites import process has started.
 *
 * @since 1.0.0
 *
 * @return bool True if import has started, False otherwise.
 */
function astra_sites_has_import_started() {
    // Check if the transient is set, which indicates import has started
    $import_started = get_option( 'astra-sites-import-started', false );

    // Return true if import has started, false otherwise
    return (bool) $import_started;
}
```
