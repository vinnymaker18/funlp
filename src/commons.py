"""Common algorithms encountered in NLP."""


# Levenshtein distance.
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

    # We use a constant substitution const of 1 when the function is not
    # specified.
    subst_cost = subst_cost or (lambda a, b: 1 if a != b else 0)

    # We use dynamic programming to compute minimal edit distance b/w two
    # lists. If m = |original| and n = |target|, then runtime complexity 
    # is O(m * n). We can cut down memory usage to O(M) or O(N).
    M, N = len(original), len(target)
    dp = [0] * (N + 1)
    for i in range(M + 1):
        dp2 = [0] * (N + 1)
        for j in range(N + 1):
            # dp2[j] = m.e.d b/w original[:i] and target[:j]
            dp2[j] = i * delete_cost + j * insert_cost
            if i == 0 or j == 0:
                continue

            # Delete original[i]. 
            dp2[j] = delete_cost + dp[j]

            # Insert Target[j] after original[i] in original.
            dp2[j] = min(dp2[j], insert_cost + dp2[j - 1])

            # Modify original[i] into target[j]
            dp2[j] = min(dp2[j], subst_cost(original[i - 1], target[j - 1]) + dp[j - 1])

        dp = dp2

    return dp[N]
