"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://therealrathore.in
Prompt: Write a Laravel CRUD application for category management, similar to the project described in Ketankumar Rathod's portfolio. Include features for adding, editing, deleting, and viewing categories.
Generated: DETERMINISTIC_7611274325bcd7fd
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\CategoryController;

// Route definitions for Category management
Route::resource('categories', CategoryController::class);

// CategoryController.php

namespace App\Http\Controllers;

use App\Models\Category;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;

class CategoryController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $categories = Category::all(); // Retrieve all categories
        return view('categories.index', compact('categories')); // Return view with categories
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        return view('categories.create'); // Return the create category view
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param \Illuminate\Http\Request $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        // Validate the incoming request data
        $validator = Validator::make($request->all(), [
            'name' => 'required|string|max:255',
        ]);

        if ($validator->fails()) {
            return redirect()->back()->withErrors($validator)->withInput(); // Redirect back with errors
        }

        // Create a new category
        Category::create($request->only('name'));
        return redirect()->route('categories.index')->with('success', 'Category created successfully.'); // Redirect to index with success message
    }

    /**
     * Display the specified resource.
     *
     * @param \App\Models\Category $category
     * @return \Illuminate\Http\Response
     */
    public function show(Category $category)
    {
        return view('categories.show', compact('category')); // Return the show view for the category
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param \App\Models\Category $category
     * @return \Illuminate\Http\Response
     */
    public function edit(Category $category)
    {
        return view('categories.edit', compact('category')); // Return the edit view for the category
    }

    /**
     * Update the specified resource in storage.
     *
     * @param \Illuminate\Http\Request $request
     * @param \App\Models\Category $category
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Category $category)
    {
        // Validate the incoming request data
        $validator = Validator::make($request->all(), [
            'name' => 'required|string|max:255',
        ]);

        if ($validator->fails()) {
            return redirect()->back()->withErrors($validator)->withInput(); // Redirect back with errors
        }

        // Update the category
        $category->update($request->only('name'));
        return redirect()->route('categories.index')->with('success', 'Category updated successfully.'); // Redirect to index with success message
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param \App\Models\Category $category
     * @return \Illuminate\Http\Response
     */
    public function destroy(Category $category)
    {
        $category->delete(); // Delete the category
        return redirect()->route('categories.index')->with('success', 'Category deleted successfully.'); // Redirect to index with success message
    }
}

// Category.php (Model)

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Category extends Model
{
    use HasFactory;

    protected $fillable = ['name']; // Allow mass assignment for 'name' attribute
}

// Create the migration for categories table

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateCategoriesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('categories', function (Blueprint $table) {
            $table->id();
            $table->string('name')->unique(); // Ensure category names are unique
            $table->timestamps(); // Include created_at and updated_at timestamps
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('categories'); // Drop categories table
    }
}

// Resources/views/categories/index.blade.php

@extends('layouts.app')

@section('content')
    <h1>Categories</h1>
    <a href="{{ route('categories.create') }}">Add Category</a>
    <ul>
        @foreach($categories as $category)
            <li>
                {{ $category->name }}
                <a href="{{ route('categories.edit', $category) }}">Edit</a>
                <form action="{{ route('categories.destroy', $category) }}" method="POST" style="display:inline;">
                    @csrf
                    @method('DELETE')
                    <button type="submit">Delete</button>
                </form>
            </li>
        @endforeach
    </ul>
@endsection

// Resources/views/categories/create.blade.php

@extends('layouts.app')

@section('content')
    <h1>Add Category</h1>
    <form action="{{ route('categories.store') }}" method="POST">
        @csrf
        <input type="text" name="name" placeholder="Category Name" required>
        <button type="submit">Create</button>
    </form>
@endsection

// Resources/views/categories/edit.blade.php

@extends('layouts.app')

@section('content')
    <h1>Edit Category</h1>
    <form action="{{ route('categories.update', $category) }}" method="POST">
        @csrf
        @method('PUT')
        <input type="text" name="name" value="{{ $category->name }}" required>
        <button type="submit">Update</button>
    </form>
@endsection

// Resources/views/categories/show.blade.php (optional)

@extends('layouts.app')

@section('content')
    <h1>{{ $category->name }}</h1>
    <a href="{{ route('categories.index') }}">Back to Categories</a>
@endsection

// Layout file: resources/views/layouts/app.blade.php

<!DOCTYPE html>
<html>
<head>
    <title>Category Management</title>
</head>
<body>
    <div class="container">
        @yield('content')
    </div>
</body>
</html
```
