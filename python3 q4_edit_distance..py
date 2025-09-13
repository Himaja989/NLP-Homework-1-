# Q4: Word Pair - Edit Distance
import numpy as np

def min_edit_distance(s1, s2, sub_cost=1, ins_cost=1, del_cost=1):
    m, n = len(s1), len(s2)
    dp = np.zeros((m+1, n+1), dtype=int)

    # Initialize base cases
    for i in range(m+1):
        dp[i][0] = i * del_cost
    for j in range(n+1):
        dp[0][j] = j * ins_cost

    # Fill dp table
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # no cost
            else:
                dp[i][j] = min(
                    dp[i-1][j-1] + sub_cost,  # substitution
                    dp[i][j-1] + ins_cost,    # insertion
                    dp[i-1][j] + del_cost     # deletion
                )
    return dp

def get_edit_sequence(s1, s2, dp, sub_cost=1, ins_cost=1, del_cost=1):
    sequence = []
    i, j = len(s1), len(s2)
    while i > 0 or j > 0:
        if i > 0 and j > 0 and s1[i-1] == s2[j-1]:
            i, j = i-1, j-1
            sequence.append(f"Keep '{s1[i]}'")
        elif i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + sub_cost:
            i, j = i-1, j-1
            sequence.append(f"Substitute '{s1[i]}' → '{s2[j]}'")
        elif j > 0 and dp[i][j] == dp[i][j-1] + ins_cost:
            j -= 1
            sequence.append(f"Insert '{s2[j]}'")
        else:
            i -= 1
            sequence.append(f"Delete '{s1[i]}'")
    sequence.reverse()
    return sequence

# Words
word1 = "Sunday"
word2 = "Saturday"

# Model A: Sub=1, Ins=1, Del=1
dp_A = min_edit_distance(word1, word2, sub_cost=1, ins_cost=1, del_cost=1)
distance_A = dp_A[len(word1)][len(word2)]
seq_A = get_edit_sequence(word1, word2, dp_A, sub_cost=1, ins_cost=1, del_cost=1)

# Model B: Sub=2, Ins=1, Del=1
dp_B = min_edit_distance(word1, word2, sub_cost=2, ins_cost=1, del_cost=1)
distance_B = dp_B[len(word1)][len(word2)]
seq_B = get_edit_sequence(word1, word2, dp_B, sub_cost=2, ins_cost=1, del_cost=1)

# Output results
print("Minimum Edit Distance - Model A (Sub=1, Ins=1, Del=1):", distance_A)
print("One valid edit sequence (A):")
for step in seq_A:
    print(step)

print("\nMinimum Edit Distance - Model B (Sub=2, Ins=1, Del=1):", distance_B)
print("One valid edit sequence (B):")
for step in seq_B:
    print(step)
