from django.http import HttpResponse
from django.shortcuts import render
import requests
from djangoProject.qqRobotApi import sendMes
import os
print(os.getcwd())
# 后端如何匹配前端传参数的地址，以及如何拿到参数

def index(request):
    # 获取好友列表
    getFriendsList = requests.post('http://127.0.0.1:5700/get_friend_list').json()
    # 获取群列表
    getGroupList = requests.post('http://127.0.0.1:5700/get_group_list').json()
    return render(request, 'index.html',{"friendList": getFriendsList,"getGroupList":getGroupList})

def sendMessage(request):
    # 拿到id
    id = request.GET.get("id")
    # 拿到type
    type = request.GET.get("type")
    # 给用户发
    if type == 'user':
        resp_dict = {'msg_type': 'private', 'number': id, 'msg': '大家好'}
    #  给群组发
    elif type == 'group':
        resp_dict = ({'msg_type': 'group', 'number': id, 'msg': '大家好'})
    print(id)
    print(resp_dict)
    sendMes.send_msg(resp_dict)
    return HttpResponse("<p>查找成功！</p>")
