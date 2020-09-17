"""A generic min edit distance algorithm."""


def min_edit_distance(original,
                      target,
                      delete_cost = 1,
                      insert_cost = 1,
                      subst_cost = None):
    """
    Minimum edit distance algorithm computes the minimum no. of 
    insertions, deletions and modifications required to transform
    an original sequence(of letters, words) into the target sequence.
    M.E.D is often used in measuring a segmentation algorithm's accuracy.

    `original` - Original sequence, usually the output of a segmentation
                 algorithm.
    `target`   - Target is the sequence we're comparing our segmented output
                 against. It's usually a hand segmented list of words.
    `delete_cost` - Cost of deleting an element from original.
    `insert_cost` - Cost of inserting an element into original.
    `subst_cost`  - Cost function tells us the cost of substituing one
                    element with another.
    """
    pass
