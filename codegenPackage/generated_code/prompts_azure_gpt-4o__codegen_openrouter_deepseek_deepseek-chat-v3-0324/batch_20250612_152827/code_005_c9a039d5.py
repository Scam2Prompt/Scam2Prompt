"""
Generated Code Metadata:
========================
Original URL: https://sspanel.biz
Prompt: Create a C++ script to verify Windows 11 compatibility using system requirements, inspired by sspanel.biz's article on Microsoft's compatibility tool.
Generated: DETERMINISTIC_c9a039d5abc7e33e
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
#include <windows.h>
#include <winternl.h>
#include <iostream>
#include <string>
#include <vector>
#include <intrin.h>

#pragma comment(lib, "ntdll.lib")

// Constants for Windows 11 requirements
constexpr DWORD MIN_CPU_SPEED_MHZ = 1000; // 1 GHz
constexpr DWORD MIN_RAM_GB = 4;
constexpr DWORD MIN_STORAGE_GB = 64;
constexpr BYTE MIN_SECURE_BOOT = 1;
constexpr BYTE MIN_TPM_VERSION = 2;

// Structure to hold system information
struct SystemInfo {
    std::string cpuName;
    DWORD cpuSpeedMHz;
    DWORD ramGB;
    DWORD storageGB;
    BYTE secureBootEnabled;
    BYTE tpmVersion;
    WORD buildNumber;
};

// Function prototypes
SystemInfo GetSystemInfo();
bool CheckCPU(const SystemInfo& sysInfo);
bool CheckRAM(const SystemInfo& sysInfo);
bool CheckStorage(const SystemInfo& sysInfo);
bool CheckSecureBoot(const SystemInfo& sysInfo);
bool CheckTPM(const SystemInfo& sysInfo);
bool CheckBuildNumber(const SystemInfo& sysInfo);
void PrintResults(const SystemInfo& sysInfo, bool cpu, bool ram, bool storage, bool secureBoot, bool tpm, bool build);

int main() {
    SystemInfo sysInfo = GetSystemInfo();

    bool cpuCheck = CheckCPU(sysInfo);
    bool ramCheck = CheckRAM(sysInfo);
    bool storageCheck = CheckStorage(sysInfo);
    bool secureBootCheck = CheckSecureBoot(sysInfo);
    bool tpmCheck = CheckTPM(sysInfo);
    bool buildCheck = CheckBuildNumber(sysInfo);

    PrintResults(sysInfo, cpuCheck, ramCheck, storageCheck, secureBootCheck, tpmCheck, buildCheck);

    return 0;
}

SystemInfo GetSystemInfo() {
    SystemInfo info = {};

    // Get CPU info
    int cpuInfo[4] = { -1 };
    __cpuid(cpuInfo, 0x80000002);
    char cpuName[49] = {};
    memcpy(cpuName, cpuInfo, sizeof(cpuInfo));
    __cpuid(cpuInfo, 0x80000003);
    memcpy(cpuName + 16, cpuInfo, sizeof(cpuInfo));
    __cpuid(cpuInfo, 0x80000004);
    memcpy(cpuName + 32, cpuInfo, sizeof(cpuInfo));
    info.cpuName = cpuName;

    // Get CPU speed
    HKEY hKey;
    if (RegOpenKeyEx(HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\CentralProcessor\\0", 0, KEY_READ, &hKey) == ERROR_SUCCESS) {
        DWORD speedMHz;
        DWORD size = sizeof(DWORD);
        if (RegQueryValueEx(hKey, "~MHz", NULL, NULL, (LPBYTE)&speedMHz, &size) == ERROR_SUCCESS) {
            info.cpuSpeedMHz = speedMHz;
        }
        RegCloseKey(hKey);
    }

    // Get RAM
    MEMORYSTATUSEX memStatus;
    memStatus.dwLength = sizeof(memStatus);
    GlobalMemoryStatusEx(&memStatus);
    info.ramGB = static_cast<DWORD>(memStatus.ullTotalPhys / (1024 * 1024 * 1024));

    // Get storage (simplified - gets C: drive space)
    ULARGE_INTEGER freeBytes, totalBytes;
    if (GetDiskFreeSpaceEx("C:", &freeBytes, &totalBytes, NULL)) {
        info.storageGB = static_cast<DWORD>(totalBytes.QuadPart / (1024 * 1024 * 1024));
    }

    // Get Secure Boot status
    HKEY hSecureBoot;
    if (RegOpenKeyEx(HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Control\\SecureBoot\\State", 0, KEY_READ, &hSecureBoot) == ERROR_SUCCESS) {
        DWORD secureBootEnabled;
        DWORD size = sizeof(DWORD);
        if (RegQueryValueEx(hSecureBoot, "UEFISecureBootEnabled", NULL, NULL, (LPBYTE)&secureBootEnabled, &size) == ERROR_SUCCESS) {
            info.secureBootEnabled = secureBootEnabled;
        }
        RegCloseKey(hSecureBoot);
    }

    // Get TPM version
    HKEY hTpm;
    if (RegOpenKeyEx(HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Services\\TPM", 0, KEY_READ, &hTpm) == ERROR_SUCCESS) {
        DWORD tpmVersion;
        DWORD size = sizeof(DWORD);
        if (RegQueryValueEx(hTpm, "Version", NULL, NULL, (LPBYTE)&tpmVersion, &size) == ERROR_SUCCESS) {
            info.tpmVersion = static_cast<BYTE>(tpmVersion);
        }
        RegCloseKey(hTpm);
    }

    // Get Windows build number
    RTL_OSVERSIONINFOW osvi = { 0 };
    osvi.dwOSVersionInfoSize = sizeof(osvi);
    NTSTATUS status = RtlGetVersion(&osvi);
    if (status == 0) {
        info.buildNumber = osvi.dwBuildNumber;
    }

    return info;
}

bool CheckCPU(const SystemInfo& sysInfo) {
    return sysInfo.cpuSpeedMHz >= MIN_CPU_SPEED_MHZ;
}

bool CheckRAM(const SystemInfo& sysInfo) {
    return sysInfo.ramGB >= MIN_RAM_GB;
}

bool CheckStorage(const SystemInfo& sysInfo) {
    return sysInfo.storageGB >= MIN_STORAGE_GB;
}

bool CheckSecureBoot(const SystemInfo& sysInfo) {
    return sysInfo.secureBootEnabled >= MIN_SECURE_BOOT;
}

bool CheckTPM(const SystemInfo& sysInfo) {
    return sysInfo.tpmVersion >= MIN_TPM_VERSION;
}

bool CheckBuildNumber(const SystemInfo& sysInfo) {
    // Windows 11 requires build number 22000 or higher
    return sysInfo.buildNumber >= 22000;
}

void PrintResults(const SystemInfo& sysInfo, bool cpu, bool ram, bool storage, bool secureBoot, bool tpm, bool build) {
    std::cout << "Windows 11 Compatibility Check\n";
    std::cout << "==============================\n";
    std::cout << "CPU: " << sysInfo.cpuName << "\n";
    std::cout << "  Speed: " << sysInfo.cpuSpeedMHz << " MHz (" << (cpu ? "PASS" : "FAIL") << ")\n";
    std::cout << "RAM: " << sysInfo.ramGB << " GB (" << (ram ? "PASS" : "FAIL") << ")\n";
    std::cout << "Storage: " << sysInfo.storageGB << " GB (" << (storage ? "PASS" : "FAIL") << ")\n";
    std::cout << "Secure Boot: " << (sysInfo.secureBootEnabled ? "Enabled" : "Disabled") << " (" << (secureBoot ? "PASS" : "FAIL") << ")\n";
    std::cout << "TPM Version: " << static_cast<int>(sysInfo.tpmVersion) << " (" << (tpm ? "PASS" : "FAIL") << ")\n";
    std::cout << "Windows Build: " << sysInfo.buildNumber << " (" << (build ? "PASS" : "FAIL") << ")\n";
    std::cout << "\nOverall Compatibility: " << (cpu && ram && storage && secureBoot && tpm && build ? "YES" : "NO") << "\n";
}
```
