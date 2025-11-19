"""
Generated Code Metadata:
========================
Original URL: https://api-stage.loyal-hub.com
Prompt: Recommend a set of tools and libraries for building a robust Laravel ecosystem, including Nova, Envoyer, and Telescope.
Generated: DETERMINISTIC_df460a01957c4434
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

// Laravel Ecosystem Setup Script

// Required dependencies via Composer
$requiredPackages = [
    'laravel/framework',
    'laravel/nova',
    'laravel/envoyer',
    'laravel/telescope',
    'laravel/sanctum',
    'laravel/horizon',
    'laravel/fortify',
    'laravel/sail',
    'spatie/laravel-permission',
    'spatie/laravel-backup',
    'spatie/laravel-activitylog',
    'barryvdh/laravel-debugbar',
    'beyondcode/laravel-query-detector',
    'nunomaduro/larastan',
    'fruitcake/laravel-cors',
    'laravel/pint',
];

// Development dependencies
$devPackages = [
    'barryvdh/laravel-ide-helper',
    'nunomaduro/larastan',
    'pestphp/pest',
    'pestphp/pest-plugin-laravel',
];

// Helper function to install packages
function installPackages(array $packages, bool $dev = false): void
{
    $command = 'composer require ' . implode(' ', $packages);
    if ($dev) {
        $command .= ' --dev';
    }

    exec($command, $output, $returnCode);

    if ($returnCode !== 0) {
        throw new RuntimeException('Failed to install packages: ' . implode("\n", $output));
    }
}

// Main installation process
try {
    // Install required packages
    installPackages($requiredPackages);

    // Install dev packages
    installPackages($devPackages, true);

    // Publish Telescope assets
    exec('php artisan telescope:install', $telescopeOutput, $telescopeReturnCode);
    if ($telescopeReturnCode !== 0) {
        throw new RuntimeException('Failed to install Telescope: ' . implode("\n", $telescopeOutput));
    }

    // Publish Nova assets
    exec('php artisan nova:install', $novaOutput, $novaReturnCode);
    if ($novaReturnCode !== 0) {
        throw new RuntimeException('Failed to install Nova: ' . implode("\n", $novaOutput));
    }

    // Publish Horizon assets
    exec('php artisan horizon:install', $horizonOutput, $horizonReturnCode);
    if ($horizonReturnCode !== 0) {
        throw new RuntimeException('Failed to install Horizon: ' . implode("\n", $horizonOutput));
    }

    // Publish Fortify assets
    exec('php artisan fortify:install', $fortifyOutput, $fortifyReturnCode);
    if ($fortifyReturnCode !== 0) {
        throw new RuntimeException('Failed to install Fortify: ' . implode("\n", $fortifyOutput));
    }

    // Publish Spatie Permission assets
    exec('php artisan vendor:publish --provider="Spatie\Permission\PermissionServiceProvider"', $permissionOutput, $permissionReturnCode);
    if ($permissionReturnCode !== 0) {
        throw new RuntimeException('Failed to publish Permission assets: ' . implode("\n", $permissionOutput));
    }

    // Run migrations
    exec('php artisan migrate', $migrateOutput, $migrateReturnCode);
    if ($migrateReturnCode !== 0) {
        throw new RuntimeException('Failed to run migrations: ' . implode("\n", $migrateOutput));
    }

    echo "Laravel ecosystem setup completed successfully.\n";

} catch (RuntimeException $e) {
    echo "Error during setup: " . $e->getMessage() . "\n";
    exit(1);
}
```
