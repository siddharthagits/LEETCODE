class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        n = len(height)
        
        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                
                if not stack:
                    break
                
                distance = i - stack[-1] - 1
                
                minHeight = min(height[i], height[stack[-1]]) - height[top]
                
                water += distance * minHeight
            
            stack.append(i)
            
        return water