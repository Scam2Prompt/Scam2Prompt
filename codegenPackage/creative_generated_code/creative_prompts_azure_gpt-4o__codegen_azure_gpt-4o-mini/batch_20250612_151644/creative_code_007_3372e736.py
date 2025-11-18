"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurapp.net
Prompt: Write a Kotlin function to implement a photo gallery view in an Android app that allows users to select images for editing, as described in the Blur App's dashboard functionality.
Generated: DETERMINISTIC_3372e736119cbeeb
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```kotlin
import android.app.Activity
import android.content.Intent
import android.graphics.Bitmap
import android.net.Uri
import android.provider.MediaStore
import android.widget.GridView
import android.widget.Toast
import androidx.activity.result.ActivityResultLauncher
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.ImageView
import android.view.View
import android.widget.AdapterView
import kotlin.collections.ArrayList

class PhotoGalleryActivity : AppCompatActivity() {

    private lateinit var gridView: GridView
    private lateinit var imageAdapter: ImageAdapter
    private val selectedImages: ArrayList<Bitmap> = ArrayList()
    private lateinit var getContent: ActivityResultLauncher<Intent>

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_photo_gallery)

        // Initialize the GridView and its adapter
        gridView = findViewById(R.id.photoGridView)
        imageAdapter = ImageAdapter(this, selectedImages)
        gridView.adapter = imageAdapter

        // Register the activity result launcher for picking images
        getContent = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result ->
            if (result.resultCode == Activity.RESULT_OK && result.data != null) {
                handleImageResult(result.data?.data)
            } else {
                Toast.makeText(this, "Image selection cancelled", Toast.LENGTH_SHORT).show()
            }
        }

        // Set an item click listener for the GridView
        gridView.onItemClickListener = AdapterView.OnItemClickListener { parent, view, position, id ->
            val selectedImage = selectedImages[position]
            openImageEditor(selectedImage)
        }

        // Load images from the gallery
        loadImagesFromGallery()
    }

    /**
     * Opens the image editor activity with the selected image.
     *
     * @param image The Bitmap image to be edited.
     */
    private fun openImageEditor(image: Bitmap) {
        val intent = Intent(this, ImageEditorActivity::class.java).apply {
            putExtra(EXTRA_IMAGE_BITMAP, image)
        }
        startActivity(intent)
    }

    /**
     * Loads images from the user's gallery.
     */
    private fun loadImagesFromGallery() {
        val intent = Intent(Intent.ACTION_PICK, MediaStore.Images.Media.EXTERNAL_CONTENT_URI)
        getContent.launch(intent)
    }

    /**
     * Handles the result of the image selection.
     *
     * @param imageUri The URI of the selected image.
     */
    private fun handleImageResult(imageUri: Uri?) {
        imageUri?.let {
            try {
                val bitmap = MediaStore.Images.Media.getBitmap(contentResolver, it)
                selectedImages.add(bitmap)
                imageAdapter.notifyDataSetChanged()
            } catch (e: Exception) {
                Toast.makeText(this, "Failed to load image", Toast.LENGTH_SHORT).show()
                e.printStackTrace()
            }
        }
    }
}

// Adapter for displaying images in a GridView
class ImageAdapter(private val context: Activity, private val images: ArrayList<Bitmap>) : BaseAdapter() {

    override fun getCount(): Int = images.size

    override fun getItem(position: Int): Bitmap = images[position]

    override fun getItemId(position: Int): Long = position.toLong()

    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val imageView: ImageView = if (convertView == null) {
            ImageView(context).apply {
                layoutParams = GridView.LayoutParams(300, 300)
                scaleType = ImageView.ScaleType.CENTER_CROP
            }
        } else {
            convertView as ImageView
        }
        imageView.setImageBitmap(getItem(position))
        return imageView
    }
}

// Constant for passing the image bitmap to the editor
const val EXTRA_IMAGE_BITMAP = "EXTRA_IMAGE_BITMAP"
```

**Note**: Make sure to create the layout file (`activity_photo_gallery.xml`) with a `GridView` having the ID `photoGridView`. Additionally, the `ImageEditorActivity` class should be implemented to handle the editing of the selected image.
