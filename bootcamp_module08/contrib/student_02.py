def make_complementary_DNA_strand(strand_in):
    """Complements the DNA strand inputted.

    Parameters
    ----------
    strand_in : str
        The strand to complement

    Returns
    -------
    str
        The complementary DNA strand to the inputted strand_in

    """
    base_pair_complements = {"A": "T", "C": "G", "G": "C", "T": "A"}
    complementary_strand_out = ""
    for i, base in enumerate(strand_in.upper()):
        if base not in base_pair_complements:
            return "Unrecognized base {} at position {} (first base is position 0)".format(base, i)
        complementary_strand_out += base_pair_complements[base]
    return complementary_strand_out
