import re


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
    Word error rate is the normalized edit distance b/w the segmented
    output list of words and the gold sentence words.
    """
