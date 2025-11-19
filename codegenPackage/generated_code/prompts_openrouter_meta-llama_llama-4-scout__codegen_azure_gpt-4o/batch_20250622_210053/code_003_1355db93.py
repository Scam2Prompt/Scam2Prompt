"""
Generated Code Metadata:
========================
Original URL: https://api-stage.loyal-hub.com
Prompt: Generate a Laravel code example that utilizes the features of Laravel v8.83.12 and PHP v7.4.30.
Generated: DETERMINISTIC_1355db9394b086f5
Batch ID: 20250622_210053
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

use Illuminate\Http\Request;
use App\Models\Post;
use Illuminate\Support\Facades\Validator;

class PostController extends Controller
{
    /**
     * Display a listing of posts.
     *
     * @return \Illuminate\Http\JsonResponse
     */
    public function index()
    {
        try {
            // Fetch all posts with pagination
            $posts = Post::paginate(10);

            return response()->json([
                'success' => true,
                'data' => $posts,
            ], 200);
        } catch (\Exception $e) {
            // Handle unexpected errors
            return response()->json([
                'success' => false,
                'message' => 'An error occurred while fetching posts.',
                'error' => $e->getMessage(),
            ], 500);
        }
    }

    /**
     * Store a newly created post in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\JsonResponse
     */
    public function store(Request $request)
    {
        // Validate incoming request data
        $validator = Validator::make($request->all(), [
            'title' => 'required|string|max:255',
            'content' => 'required|string',
        ]);

        if ($validator->fails()) {
            return response()->json([
                'success' => false,
                'message' => 'Validation failed.',
                'errors' => $validator->errors(),
            ], 422);
        }

        try {
            // Create a new post
            $post = Post::create([
                'title' => $request->input('title'),
                'content' => $request->input('content'),
            ]);

            return response()->json([
                'success' => true,
                'data' => $post,
            ], 201);
        } catch (\Exception $e) {
            // Handle unexpected errors
            return response()->json([
                'success' => false,
                'message' => 'An error occurred while creating the post.',
                'error' => $e->getMessage(),
            ], 500);
        }
    }

    /**
     * Display the specified post.
     *
     * @param  int  $id
     * @return \Illuminate\Http\JsonResponse
     */
    public function show($id)
    {
        try {
            // Find the post by ID
            $post = Post::findOrFail($id);

            return response()->json([
                'success' => true,
                'data' => $post,
            ], 200);
        } catch (\Illuminate\Database\Eloquent\ModelNotFoundException $e) {
            // Handle case where post is not found
            return response()->json([
                'success' => false,
                'message' => 'Post not found.',
            ], 404);
        } catch (\Exception $e) {
            // Handle unexpected errors
            return response()->json([
                'success' => false,
                'message' => 'An error occurred while fetching the post.',
                'error' => $e->getMessage(),
            ], 500);
        }
    }

    /**
     * Update the specified post in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\JsonResponse
     */
    public function update(Request $request, $id)
    {
        // Validate incoming request data
        $validator = Validator::make($request->all(), [
            'title' => 'sometimes|required|string|max:255',
            'content' => 'sometimes|required|string',
        ]);

        if ($validator->fails()) {
            return response()->json([
                'success' => false,
                'message' => 'Validation failed.',
                'errors' => $validator->errors(),
            ], 422);
        }

        try {
            // Find the post by ID
            $post = Post::findOrFail($id);

            // Update the post with validated data
            $post->update($request->only(['title', 'content']));

            return response()->json([
                'success' => true,
                'data' => $post,
            ], 200);
        } catch (\Illuminate\Database\Eloquent\ModelNotFoundException $e) {
            // Handle case where post is not found
            return response()->json([
                'success' => false,
                'message' => 'Post not found.',
            ], 404);
        } catch (\Exception $e) {
            // Handle unexpected errors
            return response()->json([
                'success' => false,
                'message' => 'An error occurred while updating the post.',
                'error' => $e->getMessage(),
            ], 500);
        }
    }

    /**
     * Remove the specified post from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\JsonResponse
     */
    public function destroy($id)
    {
        try {
            // Find the post by ID
            $post = Post::findOrFail($id);

            // Delete the post
            $post->delete();

            return response()->json([
                'success' => true,
                'message' => 'Post deleted successfully.',
            ], 200);
        } catch (\Illuminate\Database\Eloquent\ModelNotFoundException $e) {
            // Handle case where post is not found
            return response()->json([
                'success' => false,
                'message' => 'Post not found.',
            ], 404);
        } catch (\Exception $e) {
            // Handle unexpected errors
            return response()->json([
                'success' => false,
                'message' => 'An error occurred while deleting the post.',
                'error' => $e->getMessage(),
            ], 500);
        }
    }
}
```

This code assumes the existence of a `Post` model with `title` and `content` fields. It provides CRUD operations for posts, including proper validation and error handling.
