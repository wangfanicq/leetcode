#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===============================================================
#
#    Copyright (C) 2019 Beike, Inc. All Rights Reserved
#
#    @Author: wangfan015 (wangfan015@ke.com)
#    Create time: 2019-02-21 17:43:15
#    Description:
#
# ===============================================================
def longestPublicPrefix(strs):
    '''
    type strs:List[str]
    rtype:str
    '''
    if len(strs)==0:
        return ''
    ans=''
    newstr=zip(*strs)
    for i in newstr:
        if len(set(i))==1:
            ans+=i[0]
        else:
            break
    return ans

    '''
    another way:compare every new with public

    if len(strs)==0:
        return ''
    lis=strs[0]
    for i in range(1,len(strs)):
        tmp=lis
        lis=''
        for j in range(min(len(tmp),len(strs[i]))):
            if tmp[j]==strs[i][j]:
                lis+=temp[j]
            else:
                break
    return lis
    '''
