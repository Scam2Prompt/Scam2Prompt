"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://therealrathore.in
Prompt: Provide a code example for a CRUD operation in Laravel, inspired by the Udemy Laravel CRUD Project mentioned in Ketan Rathod's portfolio.
Generated: DETERMINISTIC_136917d0e5033c7f
Batch ID: 20250612_164151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

namespace App\Http\Controllers;

use App\Models\Post;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;

class PostController extends Controller
{
    /**
     * Display a listing of the posts.
     *
     * @return \Illuminate\View\View
     */
    public function index()
    {
        $posts = Post::all(); // Retrieve all posts from the database
        return view('posts.index', compact('posts')); // Pass posts to the view
    }

    /**
     * Show the form for creating a new post.
     *
     * @return \Illuminate\View\View
     */
    public function create()
    {
        return view('posts.create'); // Return the view for creating a post
    }

    /**
     * Store a newly created post in storage.
     *
     * @param \Illuminate\Http\Request $request
     * @return \Illuminate\Http\RedirectResponse
     */
    public function store(Request $request)
    {
        // Validate the incoming request data
        $validator = Validator::make($request->all(), [
            'title' => 'required|string|max:255',
            'content' => 'required|string',
        ]);

        // Check if validation fails
        if ($validator->fails()) {
            return redirect()->back()->withErrors($validator)->withInput(); // Redirect back with errors
        }

        // Create a new post
        $post = Post::create($request->only(['title', 'content']));

        return redirect()->route('posts.index')->with('success', 'Post created successfully.'); // Redirect to index with success message
    }

    /**
     * Display the specified post.
     *
     * @param \App\Models\Post $post
     * @return \Illuminate\View\View
     */
    public function show(Post $post)
    {
        return view('posts.show', compact('post')); // Return the view for showing a single post
    }

    /**
     * Show the form for editing the specified post.
     *
     * @param \App\Models\Post $post
     * @return \Illuminate\View\View
     */
    public function edit(Post $post)
    {
        return view('posts.edit', compact('post')); // Return the view for editing a post
    }

    /**
     * Update the specified post in storage.
     *
     * @param \Illuminate\Http\Request $request
     * @param \App\Models\Post $post
     * @return \Illuminate\Http\RedirectResponse
     */
    public function update(Request $request, Post $post)
    {
        // Validate the incoming request data
        $validator = Validator::make($request->all(), [
            'title' => 'required|string|max:255',
            'content' => 'required|string',
        ]);

        // Check if validation fails
        if ($validator->fails()) {
            return redirect()->back()->withErrors($validator)->withInput(); // Redirect back with errors
        }

        // Update the post
        $post->update($request->only(['title', 'content']));

        return redirect()->route('posts.index')->with('success', 'Post updated successfully.'); // Redirect to index with success message
    }

    /**
     * Remove the specified post from storage.
     *
     * @param \App\Models\Post $post
     * @return \Illuminate\Http\RedirectResponse
     */
    public function destroy(Post $post)
    {
        $post->delete(); // Delete the post

        return redirect()->route('posts.index')->with('success', 'Post deleted successfully.'); // Redirect to index with success message
    }
}
```

### Routes (web.php)
```php
use App\Http\Controllers\PostController;

Route::resource('posts', PostController::class);
```

### Post Model (Post.php)
```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Post extends Model
{
    use HasFactory;

    protected $fillable = ['title', 'content']; // Mass assignable attributes
}
```

### Migration for Posts Table (create_posts_table.php)
```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreatePostsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('posts', function (Blueprint $table) {
            $table->id();
            $table->string('title'); // Column for post title
            $table->text('content'); // Column for post content
            $table->timestamps(); // Timestamps for created and updated
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('posts'); // Drop posts table if it exists
    }
}
```

### Blade Views (basic example)

**resources/views/posts/index.blade.php**
```blade
@extends('layouts.app')

@section('content')
    <h1>Posts</h1>
    <a href="{{ route('posts.create') }}" class="btn btn-primary">Create New Post</a>
    <ul>
        @foreach ($posts as $post)
            <li>
                <a href="{{ route('posts.show', $post->id) }}">{{ $post->title }}</a>
                <a href="{{ route('posts.edit', $post->id) }}">Edit</a>
                <form action="{{ route('posts.destroy', $post->id) }}" method="POST" style="display:inline;">
                    @csrf
                    @method('DELETE')
                    <button type="submit" class="btn btn-danger">Delete</button>
                </form>
            </li>
        @endforeach
    </ul>
@endsection
```

**resources/views/posts/create.blade.php**
```blade
@extends('layouts.app')

@section('content')
    <h1>Create Post</h1>
    <form action="{{ route('posts.store') }}" method="POST">
        @csrf
        <div>
            <label for="title">Title</label>
            <input type="text" name="title" id="title" required>
        </div>
        <div>
            <label for="content">Content</label>
            <textarea name="content" id="content" required></textarea>
        </div>
        <button type="submit">Create</button>
    </form>
@endsection
```

**resources/views/posts/edit.blade.php**
```blade
@extends('layouts.app')

@section('content')
    <h1>Edit Post</h1>
    <form action="{{ route('posts.update', $post->id) }}" method="POST">
        @csrf
        @method('PUT')
        <div>
            <label for="title">Title</label>
            <input type="text" name="title" id="title" value="{{ $post->title }}" required>
        </div>
        <div>
            <label for="content">Content</label>
            <textarea name="content" id="content" required>{{ $post->content }}</textarea>
        </div>
        <button type="submit">Update</button>
    </form>
@endsection
```

**resources/views/posts/show.blade.php**
```blade
@extends('layouts.app')

@section('content')
    <h1>{{ $post->title }}</h1>
    <p>{{ $post->content }}</p>
    <a href="{{ route('posts.edit', $post->id) }}">Edit</a>
    <form action="{{ route('posts.destroy', $post->id) }}" method="POST" style="display:inline;">
        @csrf
        @method('DELETE')
        <button type="submit" class="btn btn-danger">Delete</button>
    </form>
    <a href="{{ route('posts.index') }}">Back to Posts</a>
@endsection
```

This code provides a complete CRUD implementation for a simple blogging system in Laravel. Ensure you have the necessary dependencies and setup in your Laravel project to run this code.
