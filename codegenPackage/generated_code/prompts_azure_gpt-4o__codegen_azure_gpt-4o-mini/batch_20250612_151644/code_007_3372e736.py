"""
Generated Code Metadata:
========================
Original URL: https://blurapp.net
Prompt: Write a Kotlin function to implement a photo gallery view in an Android app that allows users to select images for editing, as described in the Blur App's dashboard functionality.
Generated: DETERMINISTIC_3372e736119cbeeb
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```kotlin
package com.example.photogallery

import android.content.Intent
import android.graphics.Bitmap
import android.net.Uri
import android.os.Bundle
import android.provider.MediaStore
import android.widget.GridView
import android.widget.ImageView
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import androidx.core.graphics.drawable.toBitmap

class PhotoGalleryActivity : AppCompatActivity() {

    private lateinit var gridView: GridView
    private lateinit var imageAdapter: ImageAdapter
    private val selectedImages = mutableListOf<Bitmap>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_photo_gallery)

        gridView = findViewById(R.id.gridView)
        imageAdapter = ImageAdapter(this, selectedImages)
        gridView.adapter = imageAdapter

        // Launch the image picker when the activity starts
        pickImages()
    }

    private fun pickImages() {
        val intent = Intent(Intent.ACTION_PICK, MediaStore.Images.Media.EXTERNAL_CONTENT_URI)
        intent.putExtra(Intent.EXTRA_ALLOW_MULTIPLE, true)

        // Use ActivityResultLauncher to handle the result of the image picker
        val pickImagesLauncher = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result ->
            if (result.resultCode == RESULT_OK) {
                result.data?.let { data ->
                    if (data.clipData != null) {
                        // Multiple images selected
                        val count = data.clipData!!.itemCount
                        for (i in 0 until count) {
                            val imageUri: Uri = data.clipData!!.getItemAt(i).uri
                            addImageToGallery(imageUri)
                        }
                    } else {
                        // Single image selected
                        data.data?.let { uri ->
                            addImageToGallery(uri)
                        }
                    }
                }
            } else {
                Toast.makeText(this, "Image selection cancelled", Toast.LENGTH_SHORT).show()
            }
        }

        pickImagesLauncher.launch(intent)
    }

    private fun addImageToGallery(imageUri: Uri) {
        try {
            // Convert the URI to a Bitmap
            val bitmap = MediaStore.Images.Media.getBitmap(contentResolver, imageUri)
            selectedImages.add(bitmap)
            imageAdapter.notifyDataSetChanged()
        } catch (e: Exception) {
            Toast.makeText(this, "Error loading image: ${e.message}", Toast.LENGTH_SHORT).show()
        }
    }
}

// Adapter class for displaying images in a GridView
class ImageAdapter(private val context: PhotoGalleryActivity, private val images: List<Bitmap>) : BaseAdapter() {

    override fun getCount(): Int = images.size

    override fun getItem(position: Int): Bitmap = images[position]

    override fun getItemId(position: Int): Long = position.toLong()

    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val imageView: ImageView = if (convertView == null) {
            ImageView(context).apply {
                layoutParams = GridView.LayoutParams(200, 200)
                scaleType = ImageView.ScaleType.CENTER_CROP
                setPadding(8, 8, 8, 8)
            }
        } else {
            convertView as ImageView
        }

        imageView.setImageBitmap(getItem(position))
        return imageView
    }
}
```

**Note:** Ensure you have the necessary permissions to read external storage in your AndroidManifest.xml and handle runtime permissions if targeting Android 6.0 (API level 23) or higher.
