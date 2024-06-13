from core.checkerboard.checkerboard import checkerboard

if __name__ == "__main__":
    # 初始化一个棋盘
    cb = checkerboard(100,100,100)
    print(cb)
    # 更改人口数量
    cb.change_population("add",100)
    print(cb)
    # 更改环境值
    cb.change_environment("sub",50)
    print(cb)
    # 更改生态值
    cb.change_ecology("add",50)
    print(cb)
    pass