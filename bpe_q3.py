from collections import Counter, defaultdict

# Toy corpus from class
corpus = ["low", "low", "low", "low", "low", 
          "lowest", "lowest", 
          "newer", "newer", "newer", "newer", "newer", "newer", 
          "wider", "wider", "wider", 
          "new", "new"]

# 1. Add end-of-word marker "_"
corpus_eow = [list(word) + ['_'] for word in corpus]
print("Initial corpus with end-of-word marker:")
for word in corpus_eow:
    print("".join(word))

# 2. Create initial vocabulary (all characters + _)
vocab = set(char for word in corpus_eow for char in word)
print("\nInitial vocabulary:", sorted(vocab))

# 3. Function to count bigrams
def get_bigrams(corpus):
    pairs = Counter()
    for word in corpus:
        for i in range(len(word)-1):
            pairs[(word[i], word[i+1])] += 1
    return pairs

# 4. Perform first 3 merges manually
for step in range(1, 4):
    pairs = get_bigrams(corpus_eow)
    most_common = pairs.most_common(1)[0][0]
    print(f"\nStep {step}: most frequent pair {most_common}")
    # Merge the pair in corpus
    new_corpus = []
    for word in corpus_eow:
        new_word = []
        i = 0
        while i < len(word):
            if i < len(word)-1 and (word[i], word[i+1]) == most_common:
                new_word.append(word[i]+word[i+1])
                i += 2
            else:
                new_word.append(word[i])
                i += 1
        new_corpus.append(new_word)
    corpus_eow = new_corpus
    # Update vocabulary
    vocab.update([most_common[0]+most_common[1]])
    print("Updated corpus snippet:")
    for word in corpus_eow[:5]:
        print(word)
    print("Updated vocabulary:", sorted(vocab))

# 5. Mini BPE learner (code)
def learn_bpe(corpus, num_merges=10):
    corpus = [list(word)+['_'] for word in corpus]
    vocab = set(char for word in corpus for char in word)
    merges = []
    for _ in range(num_merges):
        pairs = get_bigrams(corpus)
        if not pairs:
            break
        most_common = pairs.most_common(1)[0][0]
        merges.append(most_common)
        new_corpus = []
        for word in corpus:
            new_word = []
            i = 0
            while i < len(word):
                if i < len(word)-1 and (word[i], word[i+1]) == most_common:
                    new_word.append(word[i]+word[i+1])
                    i += 2
                else:
                    new_word.append(word[i])
                    i += 1
            new_corpus.append(new_word)
        corpus = new_corpus
        vocab.update([most_common[0]+most_common[1]])
    return merges, corpus, vocab

# 6. Learn BPE on the toy corpus
merges, final_corpus, final_vocab = learn_bpe(corpus, num_merges=10)
print("\nTop BPE merges:", merges)
print("Final vocabulary:", sorted(final_vocab))
print("Segmented words example:")
for word in ["new", "newer", "lowest", "wider", "newestest"]:
    w = list(word)+['_']
    for pair in merges:
        i = 0
        while i < len(w)-1:
            if (w[i], w[i+1]) == pair:
                w[i:i+2] = [w[i]+w[i+1]]
            else:
                i += 1
    print(word, "→", w)
