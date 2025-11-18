"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api-stage.loyal-hub.com
Prompt: Write a Laravel deployment script using Laravel Envoyer to deploy a project to multiple servers.
Generated: DETERMINISTIC_621c01c3f99af66d
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

use Illuminate\Support\Facades\Artisan;
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;

/**
 * Deployment script for Laravel project using Envoyer
 */

// Define the servers to which the project will be deployed
$servers = [
    'server1.example.com' => [
        'user' => 'deployer',
        'path' => '/var/www/project1',
    ],
    'server2.example.com' => [
        'user' => 'deployer',
        'path' => '/var/www/project1',
    ],
];

// Define deployment steps
$deploySteps = [
    'git pull',
    'composer install --no-dev --optimize-autoloader',
    'php artisan migrate --force',
    'php artisan config:cache',
    'php artisan route:cache',
    'php artisan view:cache',
];

// Deploy to each server
foreach ($servers as $server => $details) {
    deployToServer($server, $details['user'], $details['path'], $deploySteps);
}

/**
 * Deploy the application to the specified server.
 *
 * @param string $server The server hostname
 * @param string $user The SSH user
 * @param string $path The path on the server where the project is located
 * @param array $steps The deployment steps to execute
 */
function deployToServer(string $server, string $user, string $path, array $steps)
{
    echo "Deploying to $server...\n";

    foreach ($steps as $step) {
        try {
            // Create the process for each deployment step
            $process = new Process(["ssh", "$user@$server", "cd $path && $step"]);
            $process->setTimeout(3600); // 1 hour timeout

            // Run the process
            $process->mustRun();

            // Output the command result
            echo $process->getOutput();
        } catch (ProcessFailedException $exception) {
            // Log error and halt deployment for this server
            echo "Error deploying to $server: " . $exception->getMessage() . "\n";
            break; // Stop further steps for the current server
        }
    }

    echo "Deployment to $server completed.\n";
}
```
