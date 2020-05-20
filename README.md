# Smmothing

Here we created a language model that does two kinds of smoothing and then finds the probability of a given sentence

Ways to run:
python3 language_model.py {n-gram} {type} path/to/corpus
{n-gram} can be 1,2,3 for unigram, bigram and trigrams
{type} can be 'k' for Kneser ney and 'w' for Witten Bell

Notes:
1. It doesn't handle the unknown words.
2. it uses sliding window technique
3. Data has beeen cleaned using regex bt removing commas and other symbols

Comparision:
1. On introduction of singulat occurances like "Tathagata Raha", it is giving very high probabilities.
2. On using d values higher for trigrams and lower for bigrams, we get better results.
3. In my code. both of them have same time complexity is same.
5. Kneser ney had to be tuned more manually, that is d values had to be set
6. Both the models don't handle unigrams. So they give shitty probs for unigrams
