class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        temp = []
        for i in range(len(position)):
            time =( target - position[i])/speed[i]
            temp.append([position[i], time])
            
        temp.sort(reverse = True)
        stack = [temp[0][1]]
        for i in range(1,len(temp)):
            if stack[-1] < temp[i][1]:
                stack.append(temp[i][1])
        return len(stack)
