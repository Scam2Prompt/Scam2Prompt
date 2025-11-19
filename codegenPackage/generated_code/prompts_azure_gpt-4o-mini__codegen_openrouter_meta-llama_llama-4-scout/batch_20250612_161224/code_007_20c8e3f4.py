"""
Generated Code Metadata:
========================
Original URL: https://stage.loyal-hub.com
Prompt: Write a guide on how to leverage Laravel's Telescope for debugging and monitoring application performance.
Generated: DETERMINISTIC_20c8e3f46253d255
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
// File: app/Providers/TelescopeServiceProvider.php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;
use Laravel\Telescope\Telescope;
use Laravel\Telescope\TelescopeApplicationServiceProvider;

class TelescopeServiceProvider extends TelescopeApplicationServiceProvider
{
    /**
     * Register any application services.
     *
     * @return void
     */
    public function register()
    {
        // TelescopeServiceProvider 
        Telescope::nightly();

        // 
        $this->app->when(Telescope::class, function ($app, Telescope $telescope) {
            // 
            $telescope->storeJobs(true);
            $telescope->storeLogs(true);
            $telescope->storeQueries(true);
        });
    }

    /**
     * Bootstrap any package services.
     *
     * @return void
     */
    public function boot()
    {
        // 
        if ($this->app->environment('local')) {
            $this->configureTelescope();
        }

        // 
        $this->configurePublishing();
    }

    /**
     * Configure the Telescope settings.
     *
     * @return void
     */
    protected function configureTelescope()
    {
        // 
        Telescope::enable();

        // 
        Telescope::ignoreRequest([
            // 
            'telescope*',
        ]);
    }

    /**
     * Configure publishing for the package.
     *
     * @return void
     */
    protected function configurePublishing()
    {
        // 
        if ($this->app->runningInConsole()) {
            $this->publishes([
                __DIR__.'/../config/telescope.php' => config_path('telescope.php'),
            ], 'telescope-config');

            // 
            $this->commands([
                TelescopeServiceProvider::class,
            ]);
        }
    }
}
```

```php
// File: config/telescope.php

return [
    /*
    |--------------------------------------------------------------------------
    | Telescope Domain
    |--------------------------------------------------------------------------
    |
    | Here you may configure the domains on which Telescope will be available.
    |
    */

    'domain' => env('TELESCOPE_DOMAIN', ''),

    /*
    |--------------------------------------------------------------------------
    | Telescope Route Prefix
    |--------------------------------------------------------------------------
    |
    | Telescope will be available at the following URI prefix. Make sure
    | to use this setting if you intend to make Telescope available
    | to users of your application.
    |
    */

    'path' => env('TELESCOPE_PATH', 'telescope'),

    /*
    |--------------------------------------------------------------------------
    | Telescope Storage Driver
    |--------------------------------------------------------------------------
    |
    | Here you may configure the storage driver that Telescope will use
    | to store requests, queries, and other data. You may configure
    | any of the drivers supported by the package.
    |
    */

    'driver' => env('TELESCOPE_DRIVER', 'database'),

    /*
    |--------------------------------------------------------------------------
    | Telescope Storage
    |--------------------------------------------------------------------------
    |
    | Here you may configure the storage settings for each type of data.
    |
    */

    'storage' => [
        'database' => [
            'connection' => env('TELESCOPE_DB_CONNECTION', env('DB_CONNECTION', 'mysql')),
            'table' => env('TELESCOPE_TABLE', 'telescope_entries'),
        ],
    ],

    /*
    |--------------------------------------------------------------------------
    | Telescope Watchers
    |--------------------------------------------------------------------------
    |
    | Here you may configure the watchers that will be used to monitor
    | your application for incoming requests, queries, and other data.
    |
    */

    'watchers' => [
        \Laravel\Telescope\Watchers\RequestWatcher::class => env('TELESCOPE_REQUEST_WATCHER', true),
        \Laravel\Telescope\Watchers\QueryWatcher::class => env('TELESCOPE_QUERY_WATCHER', true),
        \Laravel\Telescope\Watchers\LogWatcher::class => env('TELESCOPE_LOG_WATCHER', true),
        \Laravel\Telescope\Watchers\JobWatcher::class => env('TELESCOPE_JOB_WATCHER', true),
        \Laravel\Telescope\Watchers\CacheWatcher::class => env('TELESCOPE_CACHE_WATCHER', true),
        \Laravel\Telescope\Watchers\SessionWatcher::class => env('TELESCOPE_SESSION_WATCHER', true),
        \Laravel\Telescope\Watchers\DumpWatcher::class => env('TELESCOPE_DUMP_WATCHER', true),
    ],

    /*
    |--------------------------------------------------------------------------
    | Telescope Excluded Paths
    |--------------------------------------------------------------------------
    |
    | Here you may configure the paths that Telescope will not monitor.
    |
    */

    'excluded_paths' => [
        '_ignition',
        'telescope*',
    ],
];
```

```php
// File: database/migrations/2023_12_01_000000_create_telescope_entries_table.php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateTelescopeEntriesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('telescope_entries', function (Blueprint $table) {
            $table->id();
            $table->string('batch_id')->nullable()->index();
            $table->string('family_hash')->nullable()->index();
            $table->string('type');
            $table->string('content')->nullable();
            $table->timestamps();

            $table->index(['type', 'batch_id', 'family_hash']);
        });

        Schema::create('telescope_entries_tags', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('entry_id');
            $table->string('tag');

            $table->timestamps();

            $table->index(['entry_id', 'tag']);
            $table->foreign('entry_id')->references('id')->on('telescope_entries')->onDelete('cascade');
        });

        Schema::create('telescope_entries_meta', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('entry_id');
            $table->string('key');
            $table->text('value');

            $table->timestamps();

            $table->index(['entry_id', 'key']);
            $table->foreign('entry_id')->references('id')->on('telescope_entries')->onDelete('cascade');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('telescope_entries_meta');
        Schema::dropIfExists('telescope_entries_tags');
        Schema::dropIfExists('telescope_entries');
    }
}
```
