# Author    : yofo
# Datetime  : 2019/11/4 7:11 下午
# File      : resp.py
# IDE       : PyCharm
from django.http import JsonResponse

CODE_OK = 0
CODE_AUTHENTICATION_FAILED = 201

CodeMsg = {
    CODE_OK: "success",

    CODE_AUTHENTICATION_FAILED: "wrong user name or password",
}


def resp_ok(data=None):
    """请求正常处理"""
    if data is None:
        data = dict()
    return JsonResponse({"code": CODE_OK, "msg": CodeMsg[CODE_OK], "data": data})


def resp_err(code: int, data=None):
    if data is None:
        data = dict()
    return JsonResponse({"code": code, "msg": CodeMsg[code], "data": data})
