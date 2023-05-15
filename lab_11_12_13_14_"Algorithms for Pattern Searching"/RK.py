alphabet = 256 
def search_with_Rabin_Karp(pattern, text):
    M = len(pattern)
    N = len(text)
    Q = 997
    hash_pattern = 0 
    hash_text = 0 
    hash = 1
    checking_5 = False
    
    for i in range(M-1):
        hash = (hash * alphabet) % Q 
    
    for i in range(M):
        hash_pattern = (hash_pattern * alphabet + ord(pattern[i]))% Q
        hash_text = (hash_text * alphabet + ord(text[i]))% Q
    
    for i in range(N-M + 1):
        if hash_pattern == hash_text: 
            for j in range(M):
                if text[i + j] != pattern[j]:
                    break
            j += 1
            if j == M:
                print(f"Совпадение! Начальный индекс подстроки: {i}")
                checking_5 = True
        if i < N-M:
            hash_text = (alphabet*(hash_text-ord(text[i])*hash) + ord(text[i + M]))% Q
            if hash_text < 0:
                hash_text = hash_text + Q 
    return checking_5
