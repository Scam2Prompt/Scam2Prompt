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

// File: deploy.php

/**
 * Deploy Laravel application to Forge server.
 */

// Configuration
$config = [
    'forge_api_token' => env('FORGE_API_TOKEN'),
    'forge_server_id' => env('FORGE_SERVER_ID'),
    'app_name' => env('APP_NAME'),
    'app_path' => '/path/to/your/app',
    'branch' => 'main',
    'composer' => true,
    'npm' => true,
    'env' => [
        'DB_HOST' => env('DB_HOST'),
        'DB_PORT' => env('DB_PORT'),
        'DB_DATABASE' => env('DB_DATABASE'),
        'DB_USERNAME' => env('DB_USERNAME'),
        'DB_PASSWORD' => env('DB_PASSWORD'),
    ],
];

// Initialize Forge API
use Laravel\Forge\Forge;

$forge = new Forge($config['forge_api_token']);

// Deploy application
try {
    // Create server deployment
    $deployment = $forge->deployments()->create($config['forge_server_id'], [
        'title' => "Deploy {$config['app_name']}",
        'script' => [
            'type' => 'laravel',
            'path' => $config['app_path'],
            'branch' => $config['branch'],
        ],
    ]);

    // Run deployment
    $forge->deployments()->run($config['forge_server_id'], $deployment['id']);

    // Wait for deployment to complete
    $status = $forge->deployments()->status($config['forge_server_id'], $deployment['id']);
    while ($status['status'] !== 'completed') {
        sleep(5);
        $status = $forge->deployments()->status($config['forge_server_id'], $deployment['id']);
    }

    // Run post-deploy commands
    if ($config['composer']) {
        $forge->commands()->run($config['forge_server_id'], "cd {$config['app_path']} && composer install --no-interaction --prefer-dist");
    }

    if ($config['npm']) {
        $forge->commands()->run($config['forge_server_id'], "cd {$config['app_path']} && npm install && npm run build");
    }

    // Set environment variables
    foreach ($config['env'] as $key => $value) {
        $forge->environment()->set($config['forge_server_id'], $key, $value);
    }

    echo "Deployment completed successfully!";
} catch (\Exception $e) {
    echo "Deployment failed: " . $e->getMessage();
}

// File: .env.example

FORGE_API_TOKEN=your-forge-api-token
FORGE_SERVER_ID=your-forge-server-id
APP_NAME=your-app-name
DB_HOST=your-db-host
DB_PORT=your-db-port
DB_DATABASE=your-db-database
DB_USERNAME=your-db-username
DB_PASSWORD=your-db-password

// File: composer.json (add to scripts section)

"scripts": {
    "deploy": [
        "php deploy.php"
    ]
}
```

**.github/workflows/deploy.yml**
```yml
name: Deploy to Forge

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Deploy to Forge
        env:
          FORGE_API_TOKEN: ${{ secrets.FORGE_API_TOKEN }}
          FORGE_SERVER_ID: ${{ secrets.FORGE_SERVER_ID }}
          APP_NAME: ${{ secrets.APP_NAME }}
          DB_HOST: ${{ secrets.DB_HOST }}
          DB_PORT: ${{ secrets.DB_PORT }}
          DB_DATABASE: ${{ secrets.DB_DATABASE }}
          DB_USERNAME: ${{ secrets.DB_USERNAME }}
          DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
        run: |
          php deploy.php
```

**README.md**
```markdown
# Deploying to Forge

## Prerequisites

* Laravel application with Forge server
* `FORGE_API_TOKEN` and `FORGE_SERVER_ID` environment variables set
* `composer` and `npm` installed on server

## Deployment

 Run `composer run-script deploy` to deploy application to Forge server.

## Environment Variables

* `FORGE_API_TOKEN`: Forge API token
* `FORGE_SERVER_ID`: Forge server ID
* `APP_NAME`: Application name
* `DB_HOST`: Database host
* `DB_PORT`: Database port
* `DB_DATABASE`: Database name
* `DB_USERNAME`: Database username
* `DB_PASSWORD`: Database password
```
