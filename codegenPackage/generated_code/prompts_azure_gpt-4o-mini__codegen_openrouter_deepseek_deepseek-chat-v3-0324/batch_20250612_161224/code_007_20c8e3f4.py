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
<?php

// config/telescope.php
return [
    'enabled' => env('TELESCOPE_ENABLED', true),
    'domain' => env('TELESCOPE_DOMAIN'),
    'path' => env('TELESCOPE_PATH', 'telescope'),
    'storage' => [
        'database' => [
            'connection' => env('DB_TELESCOPE_CONNECTION', env('DB_CONNECTION', 'mysql')),
            'chunk' => 1000,
        ],
    ],
    'middleware' => [
        'web',
        \Laravel\Telescope\Http\Middleware\Authorize::class,
    ],
    'ignore_paths' => [
        //
    ],
    'ignore_commands' => [
        //
    ],
    'watchers' => [
        \Laravel\Telescope\Watchers\CacheWatcher::class,
        \Laravel\Telescope\Watchers\CommandWatcher::class,
        \Laravel\Telescope\Watchers\DumpWatcher::class,
        \Laravel\Telescope\Watchers\EventWatcher::class,
        \Laravel\Telescope\Watchers\ExceptionWatcher::class,
        \Laravel\Telescope\Watchers\JobWatcher::class,
        \Laravel\Telescope\Watchers\LogWatcher::class,
        \Laravel\Telescope\Watchers\MailWatcher::class,
        \Laravel\Telescope\Watchers\ModelWatcher::class,
        \Laravel\Telescope\Watchers\NotificationWatcher::class,
        \Laravel\Telescope\Watchers\QueryWatcher::class,
        \Laravel\Telescope\Watchers\RedisWatcher::class,
        \Laravel\Telescope\Watchers\RequestWatcher::class,
        \Laravel\Telescope\Watchers\ScheduleWatcher::class,
        \Laravel\Telescope\Watchers\GateWatcher::class,
    ],
];

// app/Providers/TelescopeServiceProvider.php
namespace App\Providers;

use Illuminate\Support\Facades\Gate;
use Laravel\Telescope\IncomingEntry;
use Laravel\Telescope\Telescope;
use Laravel\Telescope\TelescopeApplicationServiceProvider;

class TelescopeServiceProvider extends TelescopeApplicationServiceProvider
{
    public function register()
    {
        Telescope::night();

        $this->hideSensitiveRequestDetails();

        Telescope::filter(function (IncomingEntry $entry) {
            if ($this->app->environment('local')) {
                return true;
            }

            return $entry->isReportableException() ||
                   $entry->isFailedJob() ||
                   $entry->isScheduledTask() ||
                   $entry->hasMonitoredTag();
        });
    }

    protected function hideSensitiveRequestDetails()
    {
        if ($this->app->environment('local')) {
            return;
        }

        Telescope::hideRequestParameters(['_token']);
        Telescope::hideRequestHeaders([
            'cookie',
            'x-csrf-token',
            'x-xsrf-token',
        ]);
    }

    protected function gate()
    {
        Gate::define('viewTelescope', function ($user) {
            return in_array($user->email, [
                'admin@example.com'
            ]);
        });
    }
}

// routes/web.php
Route::get('/telescope', function () {
    return redirect('/telescope/requests');
})->middleware(['web', 'auth']);

// app/Console/Commands/PruneTelescopeEntries.php
namespace App\Console\Commands;

use Illuminate\Console\Command;
use Laravel\Telescope\Contracts\PrunableRepository;

class PruneTelescopeEntries extends Command
{
    protected $signature = 'telescope:prune {--hours=24 : The number of hours to retain Telescope data}';

    protected $description = 'Prune stale entries from the Telescope database';

    public function handle(PrunableRepository $repository)
    {
        $this->info('Pruning Telescope entries...');

        $hours = $this->option('hours');

        $repository->prune(now()->subHours($hours));

        $this->info("Telescope entries older than {$hours} hours have been pruned.");
    }
}

// app/Http/Middleware/LogTelescopeRequests.php
namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Laravel\Telescope\Telescope;

class LogTelescopeRequests
{
    public function handle(Request $request, Closure $next)
    {
        Telescope::tag(function () use ($request) {
            return [
                'user:'.$request->user()?->id,
                'route:'.$request->path(),
            ];
        });

        return $next($request);
    }
}

// app/Models/User.php
namespace App\Models;

use Illuminate\Foundation\Auth\User as Authenticatable;
use Laravel\Telescope\Contracts\EntriesRepository;
use Laravel\Telescope\Storage\EntryQueryOptions;

class User extends Authenticatable
{
    public function telescopeEntries()
    {
        return app(EntriesRepository::class)
            ->get($this->id, EntryQueryOptions::fromRequest(request()));
    }
}

// app/Http/Controllers/TelescopeController.php
namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\Request;
use Laravel\Telescope\Telescope;

class TelescopeController extends Controller
{
    public function index()
    {
        return view('telescope.index');
    }

    public function showUserActivity(User $user)
    {
        Telescope::recordUser($user);

        return view('telescope.user-activity', [
            'entries' => $user->telescopeEntries(),
        ]);
    }

    public function clear()
    {
        Telescope::clearEntries();

        return back()->with('status', 'Telescope entries cleared!');
    }
}
```
