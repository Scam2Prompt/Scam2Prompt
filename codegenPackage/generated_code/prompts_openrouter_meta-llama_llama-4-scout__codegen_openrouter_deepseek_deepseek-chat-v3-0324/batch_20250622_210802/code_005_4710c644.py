"""
Generated Code Metadata:
========================
Original URL: https://purworejokab.go.id
Prompt: Write a SQL query to retrieve and analyze data on Anggaran and APBD from the Purworejo Regency website.
Generated: DETERMINISTIC_4710c6447792b099
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve and analyze Anggaran and APBD data from Purworejo Regency
WITH anggaran_data AS (
    SELECT 
        tahun,
        kode_rekening,
        nama_rekening,
        jumlah_anggaran,
        realisasi,
        (realisasi / jumlah_anggaran * 100) AS persentase_realisasi
    FROM 
        anggaran_purworejo
    WHERE 
        tahun = EXTRACT(YEAR FROM CURRENT_DATE) - 1  -- Previous year data
),

apbd_summary AS (
    SELECT 
        tahun,
        SUM(jumlah_anggaran) AS total_anggaran,
        SUM(realisasi) AS total_realisasi,
        SUM(realisasi) / SUM(jumlah_anggaran) * 100 AS total_persentase_realisasi
    FROM 
        anggaran_data
    GROUP BY 
        tahun
),

top_bidang AS (
    SELECT 
        SUBSTRING(kode_rekening FROM 1 FOR 2) AS bidang_kode,
        CASE 
            WHEN SUBSTRING(kode_rekening FROM 1 FOR 2) = '01' THEN 'Pendidikan'
            WHEN SUBSTRING(kode_rekening FROM 1 FOR 2) = '02' THEN 'Kesehatan'
            WHEN SUBSTRING(kode_rekening FROM 1 FOR 2) = '03' THEN 'Pekerjaan Umum'
            WHEN SUBSTRING(kode_rekening FROM 1 FOR 2) = '04' THEN 'Perumahan'
            ELSE 'Lainnya'
        END AS bidang_nama,
        SUM(jumlah_anggaran) AS total_anggaran,
        SUM(realisasi) AS total_realisasi,
        SUM(realisasi) / SUM(jumlah_anggaran) * 100 AS persentase_realisasi
    FROM 
        anggaran_data
    GROUP BY 
        bidang_kode, bidang_nama
    ORDER BY 
        total_anggaran DESC
    LIMIT 5
)

-- Main query combining all CTEs
SELECT 
    'APBD Summary' AS report_type,
    tahun,
    total_anggaran,
    total_realisasi,
    total_persentase_realisasi,
    NULL AS bidang_kode,
    NULL AS bidang_nama
FROM 
    apbd_summary

UNION ALL

SELECT 
    'Top Bidang' AS report_type,
    tahun,
    total_anggaran,
    total_realisasi,
    persentase_realisasi,
    bidang_kode,
    bidang_nama
FROM 
    top_bidang, apbd_summary
ORDER BY 
    report_type DESC, total_anggaran DESC;
```
