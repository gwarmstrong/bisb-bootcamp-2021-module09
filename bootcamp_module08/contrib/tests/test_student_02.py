from bootcamp_module08.contrib.student_02 import make_complementary_DNA_strand

def test_complement_strand_all_upper():
    strand_to_complement = "ATCGATCGATCG"
    complementary_strand = make_complementary_DNA_strand(strand_to_complement)
    assert complementary_strand == "TAGCTAGCTAGC"

def test_complement_strand_all_lower():
    strand_to_complement = "atcgtcga".lower()
    complementary_strand = make_complementary_DNA_strand(strand_to_complement)
    assert complementary_strand == "tagcagct".upper()

def test_complement_strand_invalid_base():
    strand_to_complement = "aUcgtcga".lower()
    complementary_strand = make_complementary_DNA_strand(strand_to_complement)
    assert complementary_strand == "Unrecognized base U at position 1 (first base is position 0)"  # Don't know how to detect a custom exception.
