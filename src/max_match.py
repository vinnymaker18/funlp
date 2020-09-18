import re

from min_edit_distance import min_edit_distance

def max_match(sentence, dictionary):
    """
    MaxMatch algorithm for segmenting a sentence into a list of 
    words/tokens.
    """

    # We first remove whitespace from sentence.
    sentence = re.sub('\W', '', sentence)

    # For now, we're not really concerned with efficiency.
    words, pos = [], 0
    while pos < len(sentence):
        # Pick the longest prefix from position pos that's present in
        # the dictionary. If no prefix is in dictionary, pick single
        # letter as the next word.
        for j in range(len(), pos + 1, -1):
            word = sentence[pos : j]
            if word in dictionary:
                pos = j
                words.append(word)
                break
        else:
            words.append(sentence[pos])
            pos += 1

    return words


def word_error_rate(segmented, gold):
    """
    Word error rate is a metric used to measure accuracy of a segmentation
    algorithm. It's the normalized edit distance b/w the list of words 
    outputted by the algorithm and the hand segmented gold list of words.
    """

    # Deletion, insertion and modification all cost 1.
    edit_dist = min_edit_distance(segmented, gold)
    normalized_edit_dist = edit_dist / len(gold)

    return normalized_edit_dist
