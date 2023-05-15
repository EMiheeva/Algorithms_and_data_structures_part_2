alphabet = 256 
def Finite_Automat(pattern, M, table):
	longest_prefix_suffix = 0

	for symbol in range(alphabet):
		table[0][symbol] = 0
	table[0][ord(pattern[0])] = 1

	for i in range(1, M+1):
		for symbol in range(alphabet):
			table[i][symbol] = table[longest_prefix_suffix][symbol]
		if (i < M):
			table[i][ord(pattern[i])] = i + 1
			longest_prefix_suffix = table[longest_prefix_suffix][ord(pattern[i])]

def search_with_FA(pattern, text):
	M = len(pattern)
	N = len(text)
	checking_1 = False
	table = [[0 for i in range(alphabet)] for j in range(M + 1)]
	Finite_Automat(pattern, M, table)
	j = 0
	for i in range(N):
		j = table[j][ord(text[i])]
		if (j == M):
			print(f"Совпадение! Начальный индекс подстроки: {i-M+1}")
			checking_1 = True
	return checking_1
