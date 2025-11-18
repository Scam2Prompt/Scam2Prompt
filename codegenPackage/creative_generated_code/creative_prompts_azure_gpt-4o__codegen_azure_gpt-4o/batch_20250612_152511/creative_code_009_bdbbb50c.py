"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stage.loyal-hub.com
Prompt: Write a Laravel script using the Nova library to create a custom admin panel for managing database records.
Generated: DETERMINISTIC_bdbbb50c718f690c
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

namespace App\Nova;

use Laravel\Nova\Resource;
use Laravel\Nova\Fields\ID;
use Laravel\Nova\Fields\Text;
use Laravel\Nova\Fields\Number;
use Laravel\Nova\Fields\DateTime;

class ExampleResource extends Resource
{
    /**
     * The model the resource corresponds to.
     *
     * @var string
     */
    public static $model = 'App\Models\ExampleModel';

    /**
     * The single value that should be used to represent the resource.
     *
     * @var string
     */
    public static $title = 'name';

    /**
     * The columns that should be searched.
     *
     * @var array
     */
    public static $search = [
        'id', 'name'
    ];

    /**
     * Get the fields displayed by the resource.
     *
     * @return array
     */
    public function fields(Request $request)
    {
        return [
            ID::make()->sortable(), // Primary key field
            Text::make('Name')      // Text field for entity name
                ->sortable()
                ->rules('required', 'max:255'), // Validation rules for the 'name' field
            Number::make('Value')   // Numeric field for entity value
                ->sortable()
                ->rules('nullable', 'numeric'), // Validation rules for numeric data
            DateTime::make('Created At', 'created_at')->exceptOnForms(), // Display created_at timestamp
            DateTime::make('Updated At', 'updated_at')->exceptOnForms(), // Display updated_at timestamp
        ];
    }

    /**
     * Get the cards available for the request.
     *
     * @return array
     */
    public function cards(Request $request)
    {
        return [];
    }

    /**
     * Get the filters available for the resource.
     *
     * @return array
     */
    public function filters(Request $request)
    {
        return [];
    }

    /**
     * Get the lenses available for the resource.
     *
     * @return array
     */
    public function lenses(Request $request)
    {
        return [];
    }

    /**
     * Get the actions available for the resource.
     *
     * @return array
     */
    public function actions(Request $request)
    {
        return [];
    }
}
```

```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class ExampleModel extends Model
{
    // Table associated with the model
    protected $table = 'example_table';

    // Attributes that are mass assignable
    protected $fillable = ['name', 'value'];

    // Attributes that should be hidden for arrays
    protected $hidden = ['created_at', 'updated_at'];

    // Attributes that should be cast to native types
    protected $casts = [
        'value' => 'integer',
        'created_at' => 'datetime',
        'updated_at' => 'datetime',
    ];
}
```

```php
// NovaServiceProvider.php
<?php

namespace App\Providers;

use Laravel\Nova\Nova;
use Laravel\Nova\NovaApplicationServiceProvider;

class NovaServiceProvider extends NovaApplicationServiceProvider
{
    /**
     * Register the Nova resources.
     *
     * @return void
     */
    protected function resources()
    {
        Nova::resources([
            \App\Nova\ExampleResource::class, // Register the custom resource
        ]);
    }

    /**
     * Register any additional services for Nova.
     *
     * @return void
     */
    protected function tools()
    {
        // Register tools here if necessary
    }

    /**
     * Register the Nova routes.
     *
     * @return void
     */
    protected function routes()
    {
        Nova::routes()
            ->withAuthenticationRoutes()
            ->withPasswordResetRoutes()
            ->register();
    }
}
```

```php
// Run the following migration to create the database table
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateExampleTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('example_table', function (Blueprint $table) {
            $table->id();
            $table->string('name')->nullable(false); // Name field
            $table->integer('value')->nullable();    // Value field
            $table->timestamps();                   // Created and updated timestamps
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('example_table');
    }
}
```

This code creates a Laravel Nova custom admin panel for managing database records in the `example_table` table.
