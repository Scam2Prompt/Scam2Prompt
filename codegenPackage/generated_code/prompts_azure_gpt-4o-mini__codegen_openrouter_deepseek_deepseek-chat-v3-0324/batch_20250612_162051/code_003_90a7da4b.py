"""
Generated Code Metadata:
========================
Original URL: https://jiyojaago.org
Prompt: Develop a mobile app feature that encourages users to participate in initiatives like "Jiyo Jaago Swasthalaya," focusing on health and wellness, inspired by the content from the Jiyo Jaago website.
Generated: DETERMINISTIC_90a7da4b444b884b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```kotlin
// MainActivity.kt
package com.example.jiyojaago

import android.content.Intent
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.jiyojaago.databinding.ActivityMainBinding
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.firestore.FirebaseFirestore
import com.google.firebase.firestore.ktx.firestore
import com.google.firebase.ktx.Firebase

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    private lateinit var auth: FirebaseAuth
    private lateinit var db: FirebaseFirestore
    private lateinit var initiativeAdapter: InitiativeAdapter
    private val initiativesList = mutableListOf<Initiative>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Initialize Firebase instances
        auth = FirebaseAuth.getInstance()
        db = Firebase.firestore

        // Setup RecyclerView
        initiativeAdapter = InitiativeAdapter(initiativesList) { initiative ->
            startActivity(
                Intent(this, InitiativeDetailActivity::class.java).apply {
                    putExtra("initiative", initiative)
                }
            )
        }
        binding.initiativesRecyclerView.apply {
            layoutManager = LinearLayoutManager(this@MainActivity)
            adapter = initiativeAdapter
        }

        // Load initiatives from Firestore
        loadInitiatives()

        // Set up click listeners
        binding.profileButton.setOnClickListener {
            if (auth.currentUser != null) {
                startActivity(Intent(this, ProfileActivity::class.java))
            } else {
                startActivity(Intent(this, LoginActivity::class.java))
            }
        }

        binding.participateButton.setOnClickListener {
            if (auth.currentUser != null) {
                startActivity(Intent(this, ParticipateActivity::class.java))
            } else {
                Toast.makeText(
                    this,
                    "Please login to participate",
                    Toast.LENGTH_SHORT
                ).show()
                startActivity(Intent(this, LoginActivity::class.java))
            }
        }
    }

    private fun loadInitiatives() {
        db.collection("initiatives")
            .get()
            .addOnSuccessListener { result ->
                initiativesList.clear()
                for (document in result) {
                    val initiative = document.toObject(Initiative::class.java)
                    initiativesList.add(initiative)
                }
                initiativeAdapter.notifyDataSetChanged()
            }
            .addOnFailureListener { exception ->
                Toast.makeText(
                    this,
                    "Error loading initiatives: ${exception.message}",
                    Toast.LENGTH_SHORT
                ).show()
            }
    }
}

// Initiative.kt
package com.example.jiyojaago

data class Initiative(
    val id: String = "",
    val title: String = "",
    val description: String = "",
    val imageUrl: String = "",
    val startDate: String = "",
    val endDate: String = "",
    val participantsCount: Int = 0,
    val healthBenefits: String = ""
)

// InitiativeAdapter.kt
package com.example.jiyojaago

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide

class InitiativeAdapter(
    private val initiatives: List<Initiative>,
    private val onItemClick: (Initiative) -> Unit
) : RecyclerView.Adapter<InitiativeAdapter.InitiativeViewHolder>() {

    inner class InitiativeViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        private val titleTextView: TextView = itemView.findViewById(R.id.initiativeTitle)
        private val descriptionTextView: TextView = itemView.findViewById(R.id.initiativeDescription)
        private val participantsTextView: TextView = itemView.findViewById(R.id.participantsCount)
        private val imageView: ImageView = itemView.findViewById(R.id.initiativeImage)

        fun bind(initiative: Initiative) {
            titleTextView.text = initiative.title
            descriptionTextView.text = initiative.description
            participantsTextView.text = "${initiative.participantsCount} participants"
            Glide.with(itemView.context)
                .load(initiative.imageUrl)
                .placeholder(R.drawable.placeholder_image)
                .into(imageView)

            itemView.setOnClickListener { onItemClick(initiative) }
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): InitiativeViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_initiative, parent, false)
        return InitiativeViewHolder(view)
    }

    override fun onBindViewHolder(holder: InitiativeViewHolder, position: Int) {
        holder.bind(initiatives[position])
    }

    override fun getItemCount(): Int = initiatives.size
}

// ParticipateActivity.kt
package com.example.jiyojaago

import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.jiyojaago.databinding.ActivityParticipateBinding
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.firestore.FieldValue
import com.google.firebase.firestore.ktx.firestore
import com.google.firebase.ktx.Firebase

class ParticipateActivity : AppCompatActivity() {
    private lateinit var binding: ActivityParticipateBinding
    private lateinit var auth: FirebaseAuth
    private lateinit var db: FirebaseFirestore

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityParticipateBinding.inflate(layoutInflater)
        setContentView(binding.root)

        auth = FirebaseAuth.getInstance()
        db = Firebase.firestore

        val initiative = intent.getParcelableExtra<Initiative>("initiative")

        if (initiative != null) {
            binding.initiativeTitle.text = initiative.title
            binding.healthBenefits.text = initiative.healthBenefits

            binding.submitParticipation.setOnClickListener {
                val userId = auth.currentUser?.uid ?: return@setOnClickListener
                val userName = auth.currentUser?.displayName ?: "Anonymous"

                val participationData = hashMapOf(
                    "userId" to userId,
                    "userName" to userName,
                    "timestamp" to FieldValue.serverTimestamp()
                )

                db.collection("initiatives").document(initiative.id)
                    .collection("participants").document(userId)
                    .set(participationData)
                    .addOnSuccessListener {
                        // Update participants count
                        db.collection("initiatives").document(initiative.id)
                            .update("participantsCount", FieldValue.increment(1))
                            .addOnSuccessListener {
                                Toast.makeText(
                                    this,
                                    "Thank you for participating!",
                                    Toast.LENGTH_SHORT
                                ).show()
                                finish()
                            }
                    }
                    .addOnFailureListener { e ->
                        Toast.makeText(
                            this,
                            "Error: ${e.message}",
                            Toast.LENGTH_SHORT
                        ).show()
                    }
            }
        } else {
            Toast.makeText(this, "Initiative not found", Toast.LENGTH_SHORT).show()
            finish()
        }
    }
}

// ProfileActivity.kt
package com.example.jiyojaago

import android.content.Intent
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.jiyojaago.databinding.ActivityProfileBinding
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.firestore.ktx.firestore
import com.google.firebase.ktx.Firebase

class ProfileActivity : AppCompatActivity() {
    private lateinit var binding: ActivityProfileBinding
    private lateinit var auth: FirebaseAuth
    private lateinit var db: FirebaseFirestore

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityProfileBinding.inflate(layoutInflater)
        setContentView(binding.root)

        auth = FirebaseAuth.getInstance()
        db = Firebase.firestore

        val currentUser = auth.currentUser
        if (currentUser != null) {
            binding.userEmail.text = currentUser.email
            binding.userName.text = currentUser.displayName ?: "User"

            // Load user's participation count
            db.collection("users").document(currentUser.uid)
                .get()
                .addOnSuccessListener { document ->
                    val participationCount = document.getLong("participationCount") ?: 0
                    binding.participationCount.text = "Participated in $participationCount initiatives"
                }
        }

        binding.logoutButton.setOnClickListener {
            auth.signOut()
            startActivity(Intent(this, LoginActivity::class.java))
            finish()
        }

        binding.viewParticipationsButton.setOnClickListener {
            startActivity(Intent(this, MyParticipationsActivity::class.java))
        }
    }
}

// LoginActivity.kt
package com.example.jiyojaago

import android.content.Intent
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.jiyojaago.databinding.ActivityLoginBinding
import com.google.firebase.auth.FirebaseAuth

class
