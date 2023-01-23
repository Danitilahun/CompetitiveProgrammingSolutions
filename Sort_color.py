class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=len(nums)-1
        while left<right:
            while left<=right and nums[left]!=2:
                left+=1
            while right>=left and nums[right]==2:
                right-=1
            if left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
                while right>=left and nums[right]==2:
                    right-=1
        start=0
        end=right
        while start<end:
            while start<end and nums[start]==0:
                start+=1
            while start<end and nums[end]==1:
                end-=1
            if start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
