"""
Generated Code Metadata:
========================
Original URL: https://jito.pro
Prompt: Suggest a game development framework to build a first-person shooter game like "Last Day On Earth: Zombie Shooting" featured on jito.pro, and explain how to integrate realistic graphics.
Generated: DETERMINISTIC_85b2e251ee3460c9
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates setting up a basic first-person shooter (FPS) game using the 
Unity game engine with C# scripting. It includes:
1. Basic player controller setup
2. Simple enemy AI
3. Realistic graphics integration using Unity's HDRP
"""

using UnityEngine;
using UnityEngine.AI;

// Player Controller for FPS movement
[RequireComponent(typeof(CharacterController))]
public class PlayerController : MonoBehaviour
{
    [Header("Movement Settings")]
    public float walkSpeed = 5f;
    public float runSpeed = 10f;
    public float jumpHeight = 2f;
    public float gravity = -9.81f;
    
    [Header("Look Settings")]
    public float mouseSensitivity = 100f;
    public Transform playerCamera;
    
    private CharacterController controller;
    private Vector3 velocity;
    private float xRotation = 0f;
    private bool isGrounded;

    private void Start()
    {
        controller = GetComponent<CharacterController>();
        Cursor.lockState = CursorLockMode.Locked;
    }

    private void Update()
    {
        HandleMovement();
        HandleMouseLook();
    }

    private void HandleMovement()
    {
        isGrounded = controller.isGrounded;
        if (isGrounded && velocity.y < 0)
        {
            velocity.y = -2f;
        }

        float x = Input.GetAxis("Horizontal");
        float z = Input.GetAxis("Vertical");
        
        float currentSpeed = Input.GetKey(KeyCode.LeftShift) ? runSpeed : walkSpeed;
        Vector3 move = transform.right * x + transform.forward * z;
        controller.Move(move * currentSpeed * Time.deltaTime);

        if (Input.GetButtonDown("Jump") && isGrounded)
        {
            velocity.y = Mathf.Sqrt(jumpHeight * -2f * gravity);
        }

        velocity.y += gravity * Time.deltaTime;
        controller.Move(velocity * Time.deltaTime);
    }

    private void HandleMouseLook()
    {
        float mouseX = Input.GetAxis("Mouse X") * mouseSensitivity * Time.deltaTime;
        float mouseY = Input.GetAxis("Mouse Y") * mouseSensitivity * Time.deltaTime;

        xRotation -= mouseY;
        xRotation = Mathf.Clamp(xRotation, -90f, 90f);

        playerCamera.localRotation = Quaternion.Euler(xRotation, 0f, 0f);
        transform.Rotate(Vector3.up * mouseX);
    }
}

// Basic Zombie Enemy AI
[RequireComponent(typeof(NavMeshAgent))]
public class ZombieAI : MonoBehaviour
{
    public float detectionRange = 15f;
    public float attackRange = 2f;
    public int damage = 10;
    public float attackCooldown = 1f;
    
    private NavMeshAgent agent;
    private Transform player;
    private float lastAttackTime;
    private Animator animator;

    private void Start()
    {
        agent = GetComponent<NavMeshAgent>();
        animator = GetComponent<Animator>();
        player = GameObject.FindGameObjectWithTag("Player").transform;
    }

    private void Update()
    {
        float distanceToPlayer = Vector3.Distance(transform.position, player.position);
        
        if (distanceToPlayer <= detectionRange)
        {
            agent.SetDestination(player.position);
            animator.SetBool("IsWalking", true);
            
            if (distanceToPlayer <= attackRange && Time.time > lastAttackTime + attackCooldown)
            {
                AttackPlayer();
                lastAttackTime = Time.time;
            }
        }
        else
        {
            animator.SetBool("IsWalking", false);
        }
    }

    private void AttackPlayer()
    {
        animator.SetTrigger("Attack");
        // In a real game, you would implement player health reduction here
    }
}

/*
To integrate realistic graphics in Unity:
1. Use High Definition Render Pipeline (HDRP) for advanced lighting and materials
2. Implement post-processing effects (Bloom, Ambient Occlusion, etc.)
3. Use high-quality PBR materials for objects
4. Add realistic particle effects for gunfire, explosions, etc.
5. Implement screen-space reflections and global illumination
*/

// Example of a weapon script with visual effects
public class Weapon : MonoBehaviour
{
    public float damage = 25f;
    public float range = 100f;
    public float fireRate = 15f;
    public int maxAmmo = 30;
    public float reloadTime = 2f;
    
    public Camera fpsCam;
    public ParticleSystem muzzleFlash;
    public GameObject impactEffect;
    
    private int currentAmmo;
    private float nextTimeToFire = 0f;
    private bool isReloading = false;

    private void Start()
    {
        currentAmmo = maxAmmo;
    }

    private void OnEnable()
    {
        isReloading = false;
    }

    private void Update()
    {
        if (isReloading)
            return;
            
        if (currentAmmo <= 0 || (Input.GetKeyDown(KeyCode.R) && currentAmmo < maxAmmo))
        {
            StartCoroutine(Reload());
            return;
        }
        
        if (Input.GetButton("Fire1") && Time.time >= nextTimeToFire)
        {
            nextTimeToFire = Time.time + 1f / fireRate;
            Shoot();
        }
    }

    IEnumerator Reload()
    {
        isReloading = true;
        yield return new WaitForSeconds(reloadTime);
        currentAmmo = maxAmmo;
        isReloading = false;
    }

    void Shoot()
    {
        muzzleFlash.Play();
        currentAmmo--;
        
        RaycastHit hit;
        if (Physics.Raycast(fpsCam.transform.position, fpsCam.transform.forward, out hit, range))
        {
            ZombieAI target = hit.transform.GetComponent<ZombieAI>();
            if (target != null)
            {
                // Apply damage to target
            }
            
            GameObject impact = Instantiate(impactEffect, hit.point, Quaternion.LookRotation(hit.normal));
            Destroy(impact, 2f);
        }
    }
}
```
