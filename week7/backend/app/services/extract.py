import re

def extract_action_items(text: str) -> list[str]:
    """
    Ekstraksi tugas yang lebih canggih menggunakan Regex.
    Mampu menangkap tugas di tengah kalimat dan berbagai kata kunci perintah.
    """
    # Pola Regex:
    # 1. Menangkap penanda (TODO, ACTION, FIXME)
    # 2. Menangkap kata kerja perintah (Kirim, Buat, Update, Simpan)
    # 3. Menangkap frasa pengingat (Jangan lupa, Perlu, Harus)
    patterns = [
        r"(?:TODO|ACTION|FIXME)[:\s]+(.*?)(?:\.|$|\n)",
        r"(?:Perlu|Harus|Jangan lupa)\s+(.*?)(?:\.|$|\n)",
        r"^(?:Simpan|Update|Kirim|Buat|Cek)\s+(.*?)(?:\.|$|\n)"
    ]
    
    results: list[str] = []
    lines = text.splitlines()
    
    for line in lines:
        line = line.strip("- ")
        if not line:
            continue
            
        for p in patterns:
            # Menggunakan re.IGNORECASE agar tidak sensitif huruf besar/kecil
            match = re.search(p, line, re.IGNORECASE)
            if match:
                results.append(match.group(1).strip() if match.groups() else line)
                break # Berhenti jika satu pola sudah ketemu
    
    return list(set(results)) # Hapus duplikat