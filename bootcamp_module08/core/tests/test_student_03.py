from bootcamp_module08.core.student_03 import count_substring  # noqa
from bootcamp_module08.contrib.student_03 import reverse_string


def test_count_substring_single():
    test_string = "CGCTAGCGT"
    test_substring = "TAG"

    expected_count = 1
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_count_substring_repeated():
    test_string = "AGCTAGCAGT"
    test_substring = "AGC"

    expected_count = 2
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_count_substring_none():
    test_string = "AGTCCCCTAGA"
    test_substring = "AAA"

    expected_count = 0
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_count_substring_lowercase():
    test_string = "AGTCTAGCatgctATG"
    test_substring = "AtG"

    expected_count = 2
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_reverse_string():
    test_string = "hello this is a string"
    expected_reversed_string = "gnirts a si siht olleh"
    observed_reversed_string = reverse_string(test_string)
    assert expected_reversed_string == observed_reversed_string
