"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api-stage.loyal-hub.com
Prompt: Recommend a Laravel library for managing database migrations and provide code examples for using Laravel Nova to create an admin panel.
Generated: DETERMINISTIC_d0db1ca29f885ed3
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
// composer.json
{
    "require": {
        "laravel/framework": "^9.0",
        "laravel/nova": "^4.0"
    }
}

// Run composer update to include Laravel Nova in your project
// Terminal command
// composer update

// Migration example: create_users_table.php in database/migrations
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateUsersTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('users', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('email')->unique();
            $table->timestamp('email_verified_at')->nullable();
            $table->string('password');
            $table->rememberToken();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('users');
    }
}

// Run migrations
// Terminal command
// php artisan migrate

// Nova Resource for User: User.php in app/Nova/User.php
namespace App\Nova;

use Laravel\Nova\Fields\ID;
use Laravel\Nova\Fields\Text;
use Laravel\Nova\Fields\Email;
use Laravel\Nova\Resource;

class User extends Resource
{
    // The model associated with the resource
    public static $model = \App\Models\User::class;

    // The single value used to represent the resource
    public static $title = 'name';

    // The columns to be displayed in the index view
    public static $search = [
        'id', 'name', 'email',
    ];

    /**
     * The fields available for editing the resource.
     *
     * @param mixed $request
     * @return array
     */
    public function fields($request)
    {
        return [
            ID::make()->sortable(),

            Text::make('Name')
                ->sortable()
                ->rules('required', 'max:255'),

            Email::make('Email')
                ->sortable()
                ->rules('required', 'email', 'max:255'),
        ];
    }

    /**
     * The relationships that should be eager loaded on index queries.
     *
     * @return array
     */
    public function withTrashed()
    {
        return [
            'trashed' => true,
        ];
    }
}

// Add the Nova service provider in config/app.php
// 'providers' => [
//    // Other Service Providers
//    Laravel\Nova\NovaServiceProvider::class,
// ],

// Publish Nova assets
// Terminal command
// php artisan nova:publish

// Set up Nova routes in routes/web.php
use Laravel\Nova\Nova;

Route::middleware(['web', 'auth'])
    ->prefix('admin')
    ->group(function () {
        Nova::routes();
    });

// Ensure you run `php artisan serve` to start the server
```
