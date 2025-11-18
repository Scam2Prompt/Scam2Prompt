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

use Laravel\Nova\Fields\ID;
use Laravel\Nova\Fields\Text;
use Laravel\Nova\Fields\Textarea;
use Laravel\Nova\Fields\Number;
use Laravel\Nova\Fields\HasMany;
use Laravel\Nova\Resource;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;

class CustomResource extends Resource
{
    // Define the resource's model
    public static $model = 'App\\Models\\YourModel';

    // Define the display name for the resource
    public static $title = 'name';

    // Define the searchable fields
    public static $search = [
        'id', 'name', 'description'
    ];

    // Define the fields in the resource
    public function fields(Request $request)
    {
        return [
            ID::make()->sortable(),

            Text::make('Name')
                ->rules('required', 'max:255')
                ->creationRules('required', 'unique:your_table,name')
                ->updateRules('required', 'unique:your_table,name,{{resourceId}}'),

            Textarea::make('Description')
                ->rules('nullable', 'max:500'),

            Number::make('Quantity')
                ->rules('required', 'integer', 'min:0'),

            HasMany::make('Related Items', 'relatedItems', RelatedItem::class),
        ];
    }

    // Define actions for the resource (if needed)
    public function actions(Request $request)
    {
        return [];
    }

    // Define filters for the resource (if needed)
    public function filters(Request $request)
    {
        return [];
    }

    // Define lenses for the resource (if needed)
    public function lenses(Request $request)
    {
        return [];
    }

    // Define cards for the resource (if needed)
    public function cards(Request $request)
    {
        return [];
    }

    // Custom validation logic can be placed here
    protected function validateData(array $data)
    {
        $validator = Validator::make($data, [
            'name' => 'required|max:255|unique:your_table,name',
            'description' => 'nullable|max:500',
            'quantity' => 'required|integer|min:0',
        ]);

        if ($validator->fails()) {
            throw new \Illuminate\Validation\ValidationException($validator);
        }
    }
}
```

Make sure to replace `YourModel` and `your_table` with the actual model and table names you're using in your Laravel application.
