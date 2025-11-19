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

use Illuminate\Http\Request;
use App\Models\Post; // Assuming 'Post' is the model

class PostController extends Controller
{
    /**
     * Display a listing of the posts.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        // Fetch all posts and pass them to the view
        $posts = Post::all();
        return view('posts.index', compact('posts')); // 'posts.index' is the Blade file
    }

    /**
     * Show the form for creating a new post.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        // Display the form for creating a new post
        return view('posts.create');
    }

    /**
     * Store a newly created post in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        // Validate the incoming request
        $validated = $request->validate([
            'title' => 'required|string|max:255',
            'content' => 'required|string',
        ]);

        // Create the post using validated data
        Post::create($validated);

        // Redirect to the index page with a success message
        return redirect()->route('posts.index')->with('success', 'Post created successfully!');
    }

    /**
     * Display the specified post.
     *
     * @param  \App\Models\Post  $post
     * @return \Illuminate\Http\Response
     */
    public function show(Post $post)
    {
        // Show a single post
        return view('posts.show', compact('post'));
    }

    /**
     * Show the form for editing the specified post.
     *
     * @param  \App\Models\Post  $post
     * @return \Illuminate\Http\Response
     */
    public function edit(Post $post)
    {
        // Display the edit form for the post
        return view('posts.edit', compact('post'));
    }

    /**
     * Update the specified post in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Models\Post  $post
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Post $post)
    {
        // Validate the incoming request
        $validated = $request->validate([
            'title' => 'required|string|max:255',
            'content' => 'required|string',
        ]);

        // Update the post with validated data
        $post->update($validated);

        // Redirect to the index page with a success message
        return redirect()->route('posts.index')->with('success', 'Post updated successfully!');
    }

    /**
     * Remove the specified post from storage.
     *
     * @param  \App\Models\Post  $post
     * @return \Illuminate\Http\Response
     */
    public function destroy(Post $post)
    {
        // Delete the post
        $post->delete();

        // Redirect to the index page with a success message
        return redirect()->route('posts.index')->with('success', 'Post deleted successfully!');
    }
}
```

**Instructions for Setup:**
1. Create a `Post` model and migration:
   ```bash
   php artisan make:model Post -m
   ```
   Add columns `title` and `content` in the migration file, then migrate the database:
   ```php
   Schema::create('posts', function (Blueprint $table) {
       $table->id();
       $table->string('title');
       $table->text('content');
       $table->timestamps();
   });
   ```
2. Set up routes in `web.php`:
   ```php
   use App\Http\Controllers\PostController;

   Route::resource('posts', PostController::class);
   ```
3. Create corresponding Blade files (`index.blade.php`, `create.blade.php`, `edit.blade.php`, etc.) under the `resources/views/posts` directory.

This code is ready for production and follows Laravel best practices.
