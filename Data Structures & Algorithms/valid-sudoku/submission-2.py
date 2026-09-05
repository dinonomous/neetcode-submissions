class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9,1):
            hash_set_c = set()
            for j in board[i]:
                if j == ".":
                    continue
                if j in hash_set_c:
                    return False
                hash_set_c.add(j)
        
        for j in range(0,9,1):
            hash_set_r = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in hash_set_r:
                    return False
                hash_set_r.add(board[i][j])
        
        for k in range(0,9,3):
            for l in range(0,9,3):
                hash_set_s = set()
                for m in range(3):
                    for n in range(3):
                        if board[k+m][l+n] == ".":
                            continue
                        if board[k+m][l+n] in hash_set_s:
                            return False
                        hash_set_s.add(board[k+m][l+n])

        return True