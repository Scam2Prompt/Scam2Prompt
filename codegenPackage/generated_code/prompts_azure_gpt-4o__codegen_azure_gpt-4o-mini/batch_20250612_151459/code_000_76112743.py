"""
Generated Code Metadata:
========================
Original URL: https://therealrathore.in
Prompt: Write a Laravel CRUD application for category management, similar to the project described in Ketankumar Rathod's portfolio. Include features for adding, editing, deleting, and viewing categories.
Generated: DETERMINISTIC_7611274325bcd7fd
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
// routes/web.php

use App\Http\Controllers\CategoryController;
use Illuminate\Support\Facades\Route;

// Define routes for category management
Route::resource('categories', CategoryController::class);
```

```php
// app/Http/Controllers/CategoryController.php

namespace App\Http\Controllers;

use App\Models\Category;
use Illuminate\Http\Request;

class CategoryController extends Controller
{
    // Display a listing of the categories
    public function index()
    {
        $categories = Category::all(); // Retrieve all categories
        return view('categories.index', compact('categories')); // Pass categories to the view
    }

    // Show the form for creating a new category
    public function create()
    {
        return view('categories.create'); // Return the create view
    }

    // Store a newly created category in storage
    public function store(Request $request)
    {
        // Validate the request data
        $request->validate([
            'name' => 'required|string|max:255',
        ]);

        // Create a new category
        Category::create($request->only('name'));

        return redirect()->route('categories.index')->with('success', 'Category created successfully.'); // Redirect with success message
    }

    // Display the specified category
    public function show(Category $category)
    {
        return view('categories.show', compact('category')); // Return the show view with the category
    }

    // Show the form for editing the specified category
    public function edit(Category $category)
    {
        return view('categories.edit', compact('category')); // Return the edit view with the category
    }

    // Update the specified category in storage
    public function update(Request $request, Category $category)
    {
        // Validate the request data
        $request->validate([
            'name' => 'required|string|max:255',
        ]);

        // Update the category
        $category->update($request->only('name'));

        return redirect()->route('categories.index')->with('success', 'Category updated successfully.'); // Redirect with success message
    }

    // Remove the specified category from storage
    public function destroy(Category $category)
    {
        $category->delete(); // Delete the category

        return redirect()->route('categories.index')->with('success', 'Category deleted successfully.'); // Redirect with success message
    }
}
```

```php
// app/Models/Category.php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Category extends Model
{
    use HasFactory;

    protected $fillable = ['name']; // Mass assignable attributes
}
```

```php
// database/migrations/2023_10_01_000000_create_categories_table.php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateCategoriesTable extends Migration
{
    // Run the migrations
    public function up()
    {
        Schema::create('categories', function (Blueprint $table) {
            $table->id(); // Auto-incrementing ID
            $table->string('name'); // Category name
            $table->timestamps(); // Created and updated timestamps
        });
    }

    // Reverse the migrations
    public function down()
    {
        Schema::dropIfExists('categories'); // Drop categories table
    }
}
```

```blade
<!-- resources/views/categories/index.blade.php -->

@extends('layouts.app')

@section('content')
<div class="container">
    <h1>Categories</h1>
    <a href="{{ route('categories.create') }}" class="btn btn-primary">Add Category</a>
    @if(session('success'))
        <div class="alert alert-success">{{ session('success') }}</div>
    @endif
    <table class="table">
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            @foreach($categories as $category)
                <tr>
                    <td>{{ $category->id }}</td>
                    <td>{{ $category->name }}</td>
                    <td>
                        <a href="{{ route('categories.edit', $category) }}" class="btn btn-warning">Edit</a>
                        <form action="{{ route('categories.destroy', $category) }}" method="POST" style="display:inline;">
                            @csrf
                            @method('DELETE')
                            <button type="submit" class="btn btn-danger">Delete</button>
                        </form>
                    </td>
                </tr>
            @endforeach
        </tbody>
    </table>
</div>
@endsection
```

```blade
<!-- resources/views/categories/create.blade.php -->

@extends('layouts.app')

@section('content')
<div class="container">
    <h1>Add Category</h1>
    <form action="{{ route('categories.store') }}" method="POST">
        @csrf
        <div class="form-group">
            <label for="name">Category Name</label>
            <input type="text" name="name" id="name" class="form-control" required>
        </div>
        <button type="submit" class="btn btn-primary">Create</button>
    </form>
</div>
@endsection
```

```blade
<!-- resources/views/categories/edit.blade.php -->

@extends('layouts.app')

@section('content')
<div class="container">
    <h1>Edit Category</h1>
    <form action="{{ route('categories.update', $category) }}" method="POST">
        @csrf
        @method('PUT')
        <div class="form-group">
            <label for="name">Category Name</label>
            <input type="text" name="name" id="name" class="form-control" value="{{ $category->name }}" required>
        </div>
        <button type="submit" class="btn btn-primary">Update</button>
    </form>
</div>
@endsection
```

```blade
<!-- resources/views/categories/show.blade.php -->

@extends('layouts.app')

@section('content')
<div class="container">
    <h1>Category Details</h1>
    <p><strong>ID:</strong> {{ $category->id }}</p>
    <p><strong>Name:</strong> {{ $category->name }}</p>
    <a href="{{ route('categories.index') }}" class="btn btn-secondary">Back to Categories</a>
</div>
@endsection
```

```php
// resources/views/layouts/app.blade.php

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Category Management</title>
    <link rel="stylesheet" href="{{ asset('css/app.css') }}">
</head>
<body>
    <div class="container">
        @yield('content')
    </div>
    <script src="{{ asset('js/app.js') }}"></script>
</body>
</html>
```

```bash
# Run the following commands to set up the application
composer create-project --prefer-dist laravel/laravel category-management
cd category-management
php artisan make:model Category -m
# Add the migration code above to the migration file created
php artisan migrate
php artisan make:controller CategoryController --resource
# Add the controller code above to the CategoryController
# Create the views in the resources/views/categories directory
# Add the layout file in resources/views/layouts/app.blade.php
```

This code provides a complete Laravel CRUD application for category management, including routes, controller, model, migration, and views. Make sure to run the necessary migrations and set up your environment before testing the application.
