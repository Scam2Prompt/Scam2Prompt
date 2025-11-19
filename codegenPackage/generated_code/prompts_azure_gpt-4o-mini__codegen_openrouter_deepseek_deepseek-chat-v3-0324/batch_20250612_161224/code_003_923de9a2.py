"""
Generated Code Metadata:
========================
Original URL: https://api-stage.loyal-hub.com
Prompt: Provide an example of how to deploy a Laravel application using Forge, including necessary configurations.
Generated: DETERMINISTIC_923de9a207f5333d
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

// config/forge.php
return [
    'server_provider' => env('FORGE_SERVER_PROVIDER', 'aws'),
    'server_name' => env('FORGE_SERVER_NAME', 'production'),
    'server_size' => env('FORGE_SERVER_SIZE', '2GB'),
    'server_region' => env('FORGE_SERVER_REGION', 'us-east-1'),
    'php_version' => env('FORGE_PHP_VERSION', '8.2'),
    'database_name' => env('FORGE_DB_NAME', 'forge'),
    'database_user' => env('FORGE_DB_USER', 'forge'),
    'database_password' => env('FORGE_DB_PASSWORD', ''),
    'site_domain' => env('FORGE_SITE_DOMAIN', 'example.com'),
    'site_directory' => env('FORGE_SITE_DIRECTORY', '/public'),
    'deployment_script' => env('FORGE_DEPLOYMENT_SCRIPT', <<<'EOD'
    cd /home/forge/example.com
    git pull origin main
    composer install --no-interaction --prefer-dist --optimize-autoloader
    npm install && npm run production
    php artisan migrate --force
    php artisan queue:restart
    EOD),
];

// .env.example
FORGE_SERVER_PROVIDER=aws
FORGE_SERVER_NAME=production
FORGE_SERVER_SIZE=2GB
FORGE_SERVER_REGION=us-east-1
FORGE_PHP_VERSION=8.2
FORGE_DB_NAME=forge
FORGE_DB_USER=forge
FORGE_DB_PASSWORD=
FORGE_SITE_DOMAIN=example.com
FORGE_SITE_DIRECTORY=/public

// forge-deploy.php
<?php

require __DIR__.'/vendor/autoload.php';

use Illuminate\Support\Facades\Dotenv;

Dotenv::createImmutable(__DIR__)->load();

$forge = new \Laravel\Forge\Forge(env('FORGE_API_TOKEN'));

try {
    // Create server
    $server = $forge->createServer([
        'provider' => env('FORGE_SERVER_PROVIDER'),
        'name' => env('FORGE_SERVER_NAME'),
        'size' => env('FORGE_SERVER_SIZE'),
        'region' => env('FORGE_SERVER_REGION'),
        'php_version' => env('FORGE_PHP_VERSION'),
    ]);

    // Wait for server to be ready
    while ($server->isReady() === false) {
        sleep(30);
        $server = $forge->server($server->id);
    }

    // Create site
    $site = $forge->createSite($server->id, [
        'domain' => env('FORGE_SITE_DOMAIN'),
        'project_type' => 'php',
        'directory' => env('FORGE_SITE_DIRECTORY'),
    ]);

    // Configure database
    $forge->createDatabase($server->id, [
        'name' => env('FORGE_DB_NAME'),
        'user' => env('FORGE_DB_USER'),
        'password' => env('FORGE_DB_PASSWORD'),
    ]);

    // Set deployment script
    $forge->updateSiteDeploymentScript($server->id, $site->id, env('FORGE_DEPLOYMENT_SCRIPT'));

    echo "Deployment setup completed successfully!\n";

} catch (\Exception $e) {
    echo "Error during deployment: " . $e->getMessage() . "\n";
    exit(1);
}

// composer.json (partial)
{
    "require": {
        "laravel/forge-sdk": "^3.0"
    }
}
```
