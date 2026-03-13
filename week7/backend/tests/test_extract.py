from app.services.extraction import extract_action_items

def test_extract_action_items_sophisticated():
    """Test dengan berbagai pola Regex yang sudah kita buat"""
    text = """
    - TODO: write tests
    - ACTION: review PR
    - Perlu beli kopi untuk lembur.
    - Harus submit laporan sebelum deadline.
    - Jangan lupa cek email asdos.
    - Simpan file project ini.
    Not actionable text.
    """.strip()
    
    items = extract_action_items(text)
    
    # Asserting: Sekarang kita hanya mengambil isi pesannya saja (hasil capture group)
    assert "write tests" in items
    assert "review PR" in items
    assert "beli kopi untuk lembur" in items
    assert "submit laporan sebelum deadline" in items
    assert "cek email asdos" in items
    assert "file project ini" in items

def test_extract_empty_and_no_match():
    """Test untuk memastikan aman jika tidak ada kecocokan"""
    assert extract_action_items("Cuma teks biasa") == []
    assert extract_action_items("") == []