def twosum(nums,target):
    
    '''
    type nums : list[int]
    type target : int
    type return : list
    '''
    
    dic={}
    for i in range(len(nums)):
        if target-nums[i] in dic.keys():
            return [i,dic[target-nums[i]]]
        else:
            dic[nums[i]]=i
   
    '''
    复杂度O(n^2)
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i]+nums[j]=target:
                return i,j
   '''
