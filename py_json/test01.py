# -*- coding: utf-8 -*-

import json


def main():
    # 打开json文件
    file = open("./test.json", "r", encoding="utf-8")
    # 加载json文件
    info = json.load(file)
    print(type(info))
    # 获取json参数
    param_test = info["test"]
    print(type(param_test))
    print(param_test)
    info["test"] = 123456
    # 保存json文件
    with open("test_bak.json", "w") as fd:
        json.dump(info, fd)


if __name__ == "__main__":
    main()
