#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===============================================================
#
#    Copyright (C) 2019 Beike, Inc. All Rights Reserved
#
#    @Author: wangfan015 (wangfan015@ke.com)
#    Create time: 2019-02-21 21:53:33
#    Description:
#
# ===============================================================
def validBracket(sstr):
    '''
    type sstr:str
    rtype:boolean
    '''
    dic={')':'(',']':'[','}':'{'}
    if len(sstr)==0:
        return ''
    res=[]
    for i in range(len(sstr)):
        if sstr[i] in dic.keys():
            left=res.pop() if res else '#'
            if dic[sstr[i]]!=left:
                return False
        else:
            res.append(sstr[i])
    if len(res)==0:
        return True
    else:
        return False

