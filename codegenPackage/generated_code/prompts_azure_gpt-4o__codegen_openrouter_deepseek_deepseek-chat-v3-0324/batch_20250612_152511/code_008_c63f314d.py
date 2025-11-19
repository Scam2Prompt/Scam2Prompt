"""
Generated Code Metadata:
========================
Original URL: https://stage.loyal-hub.com
Prompt: Create a Laravel application using the Vapor platform to deploy serverless applications. Include configuration details and code examples.
Generated: DETERMINISTIC_c63f314d310cfa26
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

// config/vapor.php
return [
    'id' => env('VAPOR_APPLICATION_ID'),
    'token' => env('VAPOR_API_TOKEN'),
    'team' => env('VAPOR_TEAM'),
    'region' => env('VAPOR_REGION', 'us-east-1'),
    'asset_url' => env('VAPOR_ASSET_URL'),
];

// config/filesystems.php
return [
    'disks' => [
        's3' => [
            'driver' => 's3',
            'key' => env('AWS_ACCESS_KEY_ID'),
            'secret' => env('AWS_SECRET_ACCESS_KEY'),
            'region' => env('AWS_DEFAULT_REGION'),
            'bucket' => env('AWS_BUCKET'),
            'url' => env('AWS_URL'),
            'endpoint' => env('AWS_ENDPOINT'),
            'use_path_style_endpoint' => env('AWS_USE_PATH_STYLE_ENDPOINT', false),
        ],
    ],
];

// app/Http/Middleware/TrustProxies.php
namespace App\Http\Middleware;

use Illuminate\Http\Middleware\TrustProxies as Middleware;
use Illuminate\Http\Request;

class TrustProxies extends Middleware
{
    protected $proxies = '*';
    protected $headers = Request::HEADER_X_FORWARDED_AWS_ELB;
}

// app/Providers/AppServiceProvider.php
namespace App\Providers;

use Illuminate\Support\ServiceProvider;
use Illuminate\Support\Facades\URL;

class AppServiceProvider extends ServiceProvider
{
    public function boot()
    {
        if ($this->app->environment('production')) {
            URL::forceScheme('https');
        }
    }
}

// routes/web.php
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

// routes/api.php
use Illuminate\Support\Facades\Route;

Route::get('/hello', function () {
    return response()->json(['message' => 'Hello from Vapor!']);
});

// vapor.yml
id: ${VAPOR_APPLICATION_ID}
name: my-vapor-app
environments:
    production:
        memory: 1024
        cli-memory: 512
        runtime: 'php-8.2'
        build:
            - 'composer install --no-dev'
            - 'php artisan event:cache'
            - 'php artisan view:cache'
        deploy:
            - 'php artisan migrate --force'
        storage:
            - 'storage/framework/cache'
            - 'storage/framework/sessions'
            - 'storage/framework/views'
            - 'storage/logs'
        database: my-database
        cache: my-cache

// .env.example
APP_NAME="My Vapor App"
APP_ENV=production
APP_KEY=
APP_DEBUG=false
APP_URL=${APP_URL}
APP_TIMEZONE=UTC

LOG_CHANNEL=stderr

DB_CONNECTION=mysql
DB_HOST=${DB_HOST}
DB_PORT=3306
DB_DATABASE=${DB_DATABASE}
DB_USERNAME=${DB_USERNAME}
DB_PASSWORD=${DB_PASSWORD}

CACHE_DRIVER=redis
SESSION_DRIVER=redis
QUEUE_CONNECTION=sqs

REDIS_HOST=${REDIS_HOST}
REDIS_PORT=6379

AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION}
AWS_BUCKET=${AWS_BUCKET}
AWS_URL=${AWS_URL}

VAPOR_APPLICATION_ID=${VAPOR_APPLICATION_ID}
VAPOR_API_TOKEN=${VAPOR_API_TOKEN}
VAPOR_TEAM=${VAPOR_TEAM}
VAPOR_REGION=${VAPOR_REGION}
VAPOR_ASSET_URL=${VAPOR_ASSET_URL}

// composer.json
{
    "require": {
        "php": "^8.1",
        "laravel/framework": "^10.0",
        "laravel/vapor-core": "^3.0"
    },
    "require-dev": {
        "laravel/pint": "^1.0",
        "laravel/telescope": "^4.0"
    },
    "scripts": {
        "post-autoload-dump": [
            "Illuminate\\Foundation\\ComposerScripts::postAutoloadDump",
            "@php artisan package:discover --ansi"
        ],
        "post-root-package-install": [
            "@php -r \"file_exists('.env') || copy('.env.example', '.env');\""
        ],
        "post-create-project-cmd": [
            "@php artisan key:generate --ansi"
        ]
    },
    "extra": {
        "laravel": {
            "dont-discover": []
        }
    }
}

// app/Console/Commands/VaporDeploy.php
namespace App\Console\Commands;

use Illuminate\Console\Command;

class VaporDeploy extends Command
{
    protected $signature = 'vapor:deploy {environment=production}';
    protected $description = 'Deploy the application to Vapor';

    public function handle()
    {
        $environment = $this->argument('environment');
        
        $this->info("Deploying to {$environment} environment...");
        
        passthru("vapor deploy {$environment}", $return);
        
        if ($return !== 0) {
            $this->error('Deployment failed');
            return 1;
        }
        
        $this->info('Deployment successful');
        return 0;
    }
}
```
