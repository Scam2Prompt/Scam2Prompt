"""
Generated Code Metadata:
========================
Original URL: https://api-stage.loyal-hub.com
Prompt: Write a Laravel deployment script using Laravel Envoyer to deploy a project to multiple servers.
Generated: DETERMINISTIC_621c01c3f99af66d
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**deploy.sh**
```bash
#!/bin/bash

# Define the project name and environment
PROJECT_NAME="my-project"
ENVIRONMENT="production"

# Define the servers
SERVERS=(
  "user@server1-ip:/path/to/project"
  "user@server2-ip:/path/to/project"
)

# Define the Envoyer configuration
ENVoyer_BIN="/path/to/envoyer"
ENVoyer_TOKEN="your-envoyer-token"
ENVoyer_SECRET="your-envoyer-secret"

# Deploy to each server
for SERVER in "${SERVERS[@]}"; do
  # Parse server details
  USER=$(echo "$SERVER" | cut -d'@' -f1)
  HOST=$(echo "$SERVER" | cut -d'@' -f2 | cut -d':' -f1)
  PATH=$(echo "$SERVER" | cut -d':' -f2)

  # Deploy using Envoyer
  $ENVoyer_BIN deploy \
    --project="$PROJECT_NAME" \
    --environment="$ENVIRONMENT" \
    --server="$USER@$HOST:$PATH" \
    --token="$ENVoyer_TOKEN" \
    --secret="$ENVoyer_SECRET"

  # Handle deployment errors
  if [ $? -ne 0 ]; then
    echo "Deployment to $USER@$HOST:$PATH failed."
    exit 1
  fi
done

echo "Deployment successful."
```

**deploy.php (Laravel Envoyer configuration file)**
```php
<?php

return [
  /*
  |--------------------------------------------------------------------------
  | Deploy Environments
  |--------------------------------------------------------------------------
  |
  | Here you may define the deploy environments for your application.
  |
  */

  'environments' => [
    'production' => [
      'servers' => [
        [
          'host' => 'server1-ip',
          'username' => 'user',
          'path' => '/path/to/project',
        ],
        [
          'host' => 'server2-ip',
          'username' => 'user',
          'path' => '/path/to/project',
        ],
      ],
    ],
  ],

  /*
  |--------------------------------------------------------------------------
  | Deploy Scripts
  |--------------------------------------------------------------------------
  |
  | Here you may define custom deploy scripts for your application.
  |
  */

  'scripts' => [
    'production' => [
      'before' => [
        'php artisan down',
        'composer install --no-interaction --prefer-dist',
        'php artisan migrate --force',
        'php artisan up',
      ],
      'after' => [
        'php artisan clear:cache',
        'php artisan clear:views',
      ],
    ],
  ],
];
```

**.env (Laravel Envoyer environment variables)**
```makefile
ENVoyer_TOKEN=your-envoyer-token
ENVoyer_SECRET=your-envoyer-secret
```

**envoy.blade.php (Laravel Envoyer deployment template)**
```php
@servers(['server1' => 'user@server1-ip:/path/to/project', 'server2' => 'user@server2-ip:/path/to/project'])

@task('deploy', ['on' => 'server1,server2'])
    cd {{ $path }}
    git pull origin {{ $branch }}
    composer install --no-interaction --prefer-dist
    php artisan migrate --force
    php artisan up
@endtask
```
