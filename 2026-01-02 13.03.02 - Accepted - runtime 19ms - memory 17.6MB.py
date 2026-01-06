class Solution:
    def clumsy(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 6
        if n == 4:
            return 7
        
        # For n >= 5, pattern emerges
        # n * (n-1) // (n-2) + (n-3) - ...
        # After first group, pattern stabilizes
        
        stack = []
        ops = ['*', '//', '+', '-']
        op_idx = 0
        
        stack.append(n)
        for i in range(n-1, 0, -1):
            if ops[op_idx] == '*':
                stack[-1] *= i
            elif ops[op_idx] == '//':
                stack[-1] = int(stack[-1] / i) if stack[-1] >= 0 else -(-stack[-1] // i)
            elif ops[op_idx] == '+':
                stack.append(i)
            else:  # '-'
                stack.append(-i)
            op_idx = (op_idx + 1) % 4
        
        return sum(stack)