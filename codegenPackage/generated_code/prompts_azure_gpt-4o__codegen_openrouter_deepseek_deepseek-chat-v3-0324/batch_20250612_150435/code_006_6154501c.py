"""
Generated Code Metadata:
========================
Original URL: https://enterkuroro.pages.dev
Prompt: Create a function in Unity to simulate elemental powers for collectible game characters, inspired by the 12 unique elements of Kuroro Beasts.
Generated: DETERMINISTIC_6154501c87d5c627
Batch ID: 20250612_150435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using UnityEngine;
using System.Collections.Generic;

public enum ElementType
{
    Fire,
    Water,
    Earth,
    Air,
    Lightning,
    Ice,
    Nature,
    Metal,
    Light,
    Dark,
    Chaos,
    Aether
}

[System.Serializable]
public class ElementalPower
{
    public ElementType Type;
    public string Name;
    public Color ElementColor;
    public float BasePower;
    public float ChargeRate;
    public GameObject EffectPrefab;
    public AudioClip ActivationSound;
    
    [TextArea]
    public string Description;
}

public class ElementalCharacter : MonoBehaviour
{
    [Header("Elemental Settings")]
    public List<ElementalPower> AvailablePowers = new List<ElementalPower>();
    public float CurrentCharge = 0f;
    public float MaxCharge = 100f;
    
    [Header("References")]
    public Transform PowerOrigin;
    public AudioSource AudioSource;
    
    private ElementalPower _currentPower;
    private bool _isCharging = false;
    
    private void Start()
    {
        if (AvailablePowers.Count > 0)
        {
            _currentPower = AvailablePowers[0];
        }
        
        if (AudioSource == null)
        {
            AudioSource = GetComponent<AudioSource>();
            if (AudioSource == null)
            {
                AudioSource = gameObject.AddComponent<AudioSource>();
            }
        }
    }
    
    private void Update()
    {
        if (_isCharging)
        {
            ChargePower();
        }
    }
    
    public void SwitchPower(int powerIndex)
    {
        if (powerIndex >= 0 && powerIndex < AvailablePowers.Count)
        {
            _currentPower = AvailablePowers[powerIndex];
            Debug.Log($"Switched to {_currentPower.Name} power");
        }
        else
        {
            Debug.LogWarning("Invalid power index");
        }
    }
    
    public void StartCharging()
    {
        if (_currentPower == null) return;
        _isCharging = true;
    }
    
    public void StopCharging()
    {
        _isCharging = false;
    }
    
    private void ChargePower()
    {
        if (CurrentCharge < MaxCharge)
        {
            CurrentCharge += _currentPower.ChargeRate * Time.deltaTime;
            CurrentCharge = Mathf.Clamp(CurrentCharge, 0f, MaxCharge);
        }
    }
    
    public void ActivatePower()
    {
        if (_currentPower == null || CurrentCharge <= 0f) return;
        
        if (_currentPower.EffectPrefab != null)
        {
            Instantiate(_currentPower.EffectPrefab, PowerOrigin.position, PowerOrigin.rotation);
        }
        
        if (_currentPower.ActivationSound != null && AudioSource != null)
        {
            AudioSource.PlayOneShot(_currentPower.ActivationSound);
        }
        
        ApplyElementalEffect();
        CurrentCharge = 0f;
    }
    
    private void ApplyElementalEffect()
    {
        switch (_currentPower.Type)
        {
            case ElementType.Fire:
                ApplyFireEffect();
                break;
            case ElementType.Water:
                ApplyWaterEffect();
                break;
            case ElementType.Earth:
                ApplyEarthEffect();
                break;
            case ElementType.Air:
                ApplyAirEffect();
                break;
            case ElementType.Lightning:
                ApplyLightningEffect();
                break;
            case ElementType.Ice:
                ApplyIceEffect();
                break;
            case ElementType.Nature:
                ApplyNatureEffect();
                break;
            case ElementType.Metal:
                ApplyMetalEffect();
                break;
            case ElementType.Light:
                ApplyLightEffect();
                break;
            case ElementType.Dark:
                ApplyDarkEffect();
                break;
            case ElementType.Chaos:
                ApplyChaosEffect();
                break;
            case ElementType.Aether:
                ApplyAetherEffect();
                break;
        }
    }
    
    private void ApplyFireEffect()
    {
        Collider[] hitColliders = Physics.OverlapSphere(transform.position, 5f);
        foreach (var hitCollider in hitColliders)
        {
            if (hitCollider.CompareTag("Enemy"))
            {
                hitCollider.GetComponent<Enemy>().TakeDamage(_currentPower.BasePower);
                hitCollider.GetComponent<Enemy>().ApplyBurnEffect(3f);
            }
        }
    }
    
    private void ApplyWaterEffect()
    {
        Collider[] hitColliders = Physics.OverlapSphere(transform.position, 7f);
        foreach (var hitCollider in hitColliders)
        {
            if (hitCollider.CompareTag("Enemy"))
            {
                hitCollider.GetComponent<Enemy>().SlowDown(0.5f, 4f);
            }
        }
    }
    
    private void ApplyEarthEffect()
    {
        // Create a protective barrier
        GameObject barrier = GameObject.CreatePrimitive(PrimitiveType.Sphere);
        barrier.transform.position = transform.position;
        barrier.transform.localScale = Vector3.one * 3f;
        barrier.GetComponent<Collider>().isTrigger = true;
        barrier.AddComponent<EarthBarrier>().Initialize(5f, _currentPower.BasePower);
        Destroy(barrier, 8f);
    }
    
    private void ApplyAirEffect()
    {
        Collider[] hitColliders = Physics.OverlapSphere(transform.position, 10f);
        foreach (var hitCollider in hitColliders)
        {
            Rigidbody rb = hitCollider.GetComponent<Rigidbody>();
            if (rb != null && !hitCollider.CompareTag("Player"))
            {
                rb.AddExplosionForce(500f, transform.position, 10f, 1f, ForceMode.Impulse);
            }
        }
    }
    
    private void ApplyLightningEffect()
    {
        // Chain lightning effect
        GameObject nearestEnemy = FindNearestEnemy();
        if (nearestEnemy != null)
        {
            LightningChain lightning = new GameObject("LightningChain").AddComponent<LightningChain>();
            lightning.Initialize(nearestEnemy.transform, 5, _currentPower.BasePower * 0.7f, 8f);
            Destroy(lightning.gameObject, 1f);
        }
    }
    
    private void ApplyIceEffect()
    {
        Collider[] hitColliders = Physics.OverlapSphere(transform.position, 6f);
        foreach (var hitCollider in hitColliders)
        {
            if (hitCollider.CompareTag("Enemy"))
            {
                hitCollider.GetComponent<Enemy>().Freeze(2f);
            }
        }
    }
    
    private void ApplyNatureEffect()
    {
        // Heal allies in range
        Collider[] hitColliders = Physics.OverlapSphere(transform.position, 8f);
        foreach (var hitCollider in hitColliders)
        {
            if (hitCollider.CompareTag("Player"))
            {
                hitCollider.GetComponent<PlayerHealth>().Heal(_currentPower.BasePower * 0.5f);
            }
        }
    }
    
    private void ApplyMetalEffect()
    {
        // Create metal spikes around player
        for (int i = 0; i < 8; i++)
        {
            float angle = i * Mathf.PI * 2 / 8;
            Vector3 pos = transform.position + new Vector3(Mathf.Cos(angle), 0, Mathf.Sin(angle)) * 3f;
            GameObject spike = GameObject.CreatePrimitive(PrimitiveType.Cylinder);
            spike.transform.position = pos;
            spike.transform.localScale = new Vector3(0.5f, 1.5f, 0.5f);
            spike.AddComponent<MetalSpike>().Initialize(_currentPower.BasePower, 6f);
            Destroy(spike, 6f);
        }
    }
    
    private void ApplyLightEffect()
    {
        // Create a blinding flash
        Light flash = new GameObject("LightFlash").AddComponent<Light>();
        flash.type = LightType.Point;
        flash.range = 15f;
        flash.intensity = 10f;
        flash.color = Color.white;
        flash.transform.position = transform.position;
        
        // Stun enemies
        Collider[] hitColliders = Physics.OverlapSphere(transform.position, 12f);
        foreach (var hitCollider in hitColliders)
        {
            if (hitCollider.CompareTag("Enemy"))
            {
                hitCollider.GetComponent<Enemy>().Stun(3f);
            }
        }
        
        Destroy(flash.gameObject, 0.5f);
    }
    
    private void ApplyDarkEffect()
    {
        // Create a life-draining aura
        GameObject aura = new GameObject("DarkAura");
        aura.transform.position = transform.position;
        DarkAura darkAura = aura.AddComponent<DarkAura>();
        darkAura.Initialize(5f, _currentPower.BasePower * 0.3f, 8f);
        Destroy(aura, 8f);
    }
    
    private void ApplyChaosEffect()
    {
        // Random effect from other elements
        int randomIndex = Random.Range(0, AvailablePowers.Count);
        ElementalPower randomPower = AvailablePowers[random
