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
        
        # For n >= 5, there's a pattern
        # n * (n-1) / (n-2) gives us n+1 for most n >= 5
        # Then we add (n-3) and subtract (n-4)*(n-5)/(n-6) + ...
        
        ops = ['*', '/', '+', '-']
        
        # Use a stack to handle precedence
        stack = [n]
        op_idx = 0
        
        for i in range(n - 1, 0, -1):
            op = ops[op_idx % 4]
            
            if op == '*':
                stack[-1] *= i
            elif op == '/':
                stack[-1] = int(stack[-1] / i)  # truncate towards zero
            elif op == '+':
                stack.append(i)
            else:  # '-'
                stack.append(-i)
            
            op_idx += 1
        
        return sum(stack)