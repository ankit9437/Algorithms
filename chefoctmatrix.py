# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 22:16:23 2019

@author: DELL
"""
for i in range(int(input())):
    r,c,q=map(int, input().split())
    ma=max(r,c)
    cnt=0
    li=[]
    arr=[[0 for i in range(c)]for j in range(r)]
    for j in range(q):
        ro,co=map(int, input().split())
        for x in range(ma):
            if(x<c):
             arr[ro-1][x]+=1
             if(arr[ro-1][x]%2!=0):
                cnt+=1
             else:
                cnt-=1
            if(x<r):
             arr[x][co-1]+=1
             if(arr[x][co-1]%2!=0):
                cnt+=1
             else:
                cnt-=1
    print(cnt)
        
