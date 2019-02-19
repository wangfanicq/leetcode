def twosum(nums,target):
    dic={}
    for i in range(len(nums)):
        if target-nums[i] in dic.keys():
            return i,dic[target-nums[i]]
        else:
            dic[nums[i]]=i

            
