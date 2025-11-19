"""
Generated Code Metadata:
========================
Original URL: https://therealrathore.in
Prompt: Provide a code example for a CRUD operation in Laravel, inspired by the Udemy Laravel CRUD Project mentioned in Ketan Rathod's portfolio.
Generated: DETERMINISTIC_136917d0e5033c7f
Batch ID: 20250612_164151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

namespace App\Http\Controllers;

use App\Models\Post; // Import the Post model
use Illuminate\Http\Request; // Import the Request class
use Illuminate\Support\Facades\Validator; // Import the Validator facade

class PostController extends Controller
{
    /**
     * Display a listing of the posts.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        // Retrieve all posts from the database
        $posts = Post::all();
        return response()->json($posts);
    }

    /**
     * Show the form for creating a new post.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        // Return a view to create a new post (if using Blade)
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
        // Validate the incoming request data
        $validator = Validator::make($request->all(), [
            'title' => 'required|string|max:255',
            'content' => 'required|string',
        ]);

        // Handle validation failure
        if ($validator->fails()) {
            return response()->json($validator->errors(), 422);
        }

        // Create a new post
        $post = Post::create($request->all());
        return response()->json($post, 201);
    }

    /**
     * Display the specified post.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        // Find the post by ID or fail with a 404 error
        $post = Post::findOrFail($id);
        return response()->json($post);
    }

    /**
     * Show the form for editing the specified post.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        // Find the post by ID or fail with a 404 error
        $post = Post::findOrFail($id);
        return view('posts.edit', compact('post'));
    }

    /**
     * Update the specified post in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        // Validate the incoming request data
        $validator = Validator::make($request->all(), [
            'title' => 'required|string|max:255',
            'content' => 'required|string',
        ]);

        // Handle validation failure
        if ($validator->fails()) {
            return response()->json($validator->errors(), 422);
        }

        // Find the post by ID or fail with a 404 error
        $post = Post::findOrFail($id);
        $post->update($request->all());
        return response()->json($post);
    }

    /**
     * Remove the specified post from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        // Find the post by ID or fail with a 404 error
        $post = Post::findOrFail($id);
        $post->delete();
        return response()->json(null, 204);
    }
}
```

### Notes:
- Ensure that the `Post` model is created and has the necessary fillable properties.
- Adjust the routes in `web.php` or `api.php` as needed to point to this controller.
- This code assumes you are using Laravel's built-in validation and response handling.
