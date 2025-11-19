"""
Generated Code Metadata:
========================
Original URL: https://dev-x-studios.com
Prompt: Write Unity C# code for a game that incorporates immersive storytelling, inspired by the mission of Dev-X-Studios to transport players to new worlds and create unforgettable experiences.
Generated: DETERMINISTIC_1db8c56b1830ea4b
Batch ID: 20250612_145208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using UnityEngine;
using UnityEngine.SceneManagement;
using System.Collections;
using System.Collections.Generic;

/// <summary>
/// Main game manager handling immersive storytelling experience
/// </summary>
public class StoryGameManager : MonoBehaviour
{
    [System.Serializable]
    public class StoryChapter
    {
        public string chapterName;
        public string sceneName;
        public AudioClip backgroundMusic;
        public List<GameObject> environmentPrefabs;
        public string narrativeText;
    }

    [Header("Story Configuration")]
    [SerializeField] private List<StoryChapter> storyChapters = new List<StoryChapter>();
    [SerializeField] private float fadeDuration = 1.5f;
    [SerializeField] private AudioSource musicSource;
    [SerializeField] private AudioSource sfxSource;
    [SerializeField] private CanvasGroup fadeCanvas;
    [SerializeField] private TMPro.TextMeshProUGUI narrativeTextUI;

    private int currentChapterIndex = 0;
    private bool isTransitioning = false;

    private void Start()
    {
        if (storyChapters.Count == 0)
        {
            Debug.LogError("No story chapters configured!");
            return;
        }

        InitializeChapter(currentChapterIndex);
    }

    private void InitializeChapter(int chapterIndex)
    {
        if (chapterIndex < 0 || chapterIndex >= storyChapters.Count)
        {
            Debug.LogError("Invalid chapter index!");
            return;
        }

        StoryChapter currentChapter = storyChapters[chapterIndex];
        
        // Load scene if needed
        if (!string.IsNullOrEmpty(currentChapter.sceneName))
        {
            SceneManager.LoadScene(currentChapter.sceneName);
        }

        // Set up environment
        foreach (GameObject prefab in currentChapter.environmentPrefabs)
        {
            if (prefab != null)
            {
                Instantiate(prefab, Vector3.zero, Quaternion.identity);
            }
        }

        // Play music
        if (currentChapter.backgroundMusic != null && musicSource != null)
        {
            musicSource.clip = currentChapter.backgroundMusic;
            musicSource.Play();
        }

        // Display narrative text
        if (narrativeTextUI != null && !string.IsNullOrEmpty(currentChapter.narrativeText))
        {
            narrativeTextUI.text = currentChapter.narrativeText;
            StartCoroutine(FadeInText());
        }
    }

    private IEnumerator FadeInText()
    {
        float elapsedTime = 0f;
        Color originalColor = narrativeTextUI.color;
        Color targetColor = new Color(originalColor.r, originalColor.g, originalColor.b, 1f);

        while (elapsedTime < fadeDuration)
        {
            narrativeTextUI.color = Color.Lerp(originalColor, targetColor, elapsedTime / fadeDuration);
            elapsedTime += Time.deltaTime;
            yield return null;
        }

        narrativeTextUI.color = targetColor;
    }

    public void AdvanceStory()
    {
        if (isTransitioning) return;

        StartCoroutine(TransitionToNextChapter());
    }

    private IEnumerator TransitionToNextChapter()
    {
        isTransitioning = true;

        // Fade out
        yield return StartCoroutine(FadeScreen(1f));

        // Clean up current chapter
        CleanCurrentChapter();

        // Move to next chapter
        currentChapterIndex++;
        if (currentChapterIndex >= storyChapters.Count)
        {
            currentChapterIndex = 0; // Loop or handle game completion
        }

        // Initialize next chapter
        InitializeChapter(currentChapterIndex);

        // Fade in
        yield return StartCoroutine(FadeScreen(0f));

        isTransitioning = false;
    }

    private IEnumerator FadeScreen(float targetAlpha)
    {
        if (fadeCanvas == null) yield break;

        float startAlpha = fadeCanvas.alpha;
        float elapsedTime = 0f;

        while (elapsedTime < fadeDuration)
        {
            fadeCanvas.alpha = Mathf.Lerp(startAlpha, targetAlpha, elapsedTime / fadeDuration);
            elapsedTime += Time.deltaTime;
            yield return null;
        }

        fadeCanvas.alpha = targetAlpha;
    }

    private void CleanCurrentChapter()
    {
        // Clean up instantiated environment objects
        foreach (GameObject prefab in storyChapters[currentChapterIndex].environmentPrefabs)
        {
            if (prefab != null)
            {
                GameObject[] instances = GameObject.FindGameObjectsWithTag(prefab.tag);
                foreach (GameObject instance in instances)
                {
                    Destroy(instance);
                }
            }
        }

        // Clear narrative text
        if (narrativeTextUI != null)
        {
            narrativeTextUI.text = "";
        }
    }

    public void PlaySFX(AudioClip clip)
    {
        if (sfxSource != null && clip != null)
        {
            sfxSource.PlayOneShot(clip);
        }
    }

    // For debugging purposes
    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            AdvanceStory();
        }
    }
}

/// <summary>
/// Interactive object that triggers narrative events
/// </summary>
public class InteractiveObject : MonoBehaviour
{
    [SerializeField] private AudioClip interactionSound;
    [SerializeField] private string interactionText;
    [SerializeField] private StoryGameManager gameManager;

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            if (gameManager != null)
            {
                gameManager.PlaySFX(interactionSound);
            }
        }
    }

    private void OnMouseDown()
    {
        if (gameManager != null && !string.IsNullOrEmpty(interactionText))
        {
            gameManager.PlaySFX(interactionSound);
            // Could trigger specific narrative events here
        }
    }
}

/// <summary>
/// Player controller with basic movement for exploration
/// </summary>
[RequireComponent(typeof(CharacterController))]
public class PlayerController : MonoBehaviour
{
    [SerializeField] private float moveSpeed = 5f;
    [SerializeField] private float rotationSpeed = 10f;
    [SerializeField] private float gravity = -9.81f;
    [SerializeField] private Transform groundCheck;
    [SerializeField] private float groundDistance = 0.4f;
    [SerializeField] private LayerMask groundMask;

    private CharacterController controller;
    private Vector3 velocity;
    private bool isGrounded;
    private Camera mainCamera;

    private void Awake()
    {
        controller = GetComponent<CharacterController>();
        mainCamera = Camera.main;
    }

    private void Update()
    {
        HandleMovement();
        HandleGravity();
    }

    private void HandleMovement()
    {
        float horizontal = Input.GetAxis("Horizontal");
        float vertical = Input.GetAxis("Vertical");

        Vector3 moveDirection = new Vector3(horizontal, 0f, vertical).normalized;

        if (moveDirection.magnitude >= 0.1f)
        {
            float targetAngle = Mathf.Atan2(moveDirection.x, moveDirection.z) * Mathf.Rad2Deg + mainCamera.transform.eulerAngles.y;
            Vector3 move = Quaternion.Euler(0f, targetAngle, 0f) * Vector3.forward;
            controller.Move(move * moveSpeed * Time.deltaTime);
        }
    }

    private void HandleGravity()
    {
        isGrounded = Physics.CheckSphere(groundCheck.position, groundDistance, groundMask);

        if (isGrounded && velocity.y < 0)
        {
            velocity.y = -2f;
        }

        velocity.y += gravity * Time.deltaTime;
        controller.Move(velocity * Time.deltaTime);
    }
}
```
