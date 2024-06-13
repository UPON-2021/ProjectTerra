from .player import player

class earth(player):
    """地球阵营类
    继承player类，包含地球阵营特有的属性和函数：

    Args:
        power (int):地球阵营的力量，地球的可行动点数
    
    Functions:
        change_power(operation:str,power:int):更改地球的power值，根据operation的不同，进行对应的操作
    """

    def __init__(self,username:str,power:int) -> None:
        """初始化地球阵营对象

        Args:
            username (str): 用户名
            power (int): 力量
        """
        super().__init__(username)
        super().change_priority(0) # 地球阵营的优先级设置为0，优先级最高
        self.power = power

    def __str__(self) -> str:
        return (f"username:{self.name},power:{self.power}")
    
    def __lt__(self, other) -> bool:
        """重载小于运算符，用于排序
        """
        return self.priority < other.priority
    
    def change_power(self,operation:str,power:int) -> None:
        """更改地球的power值，根据operation的不同，进行对应的操作

        Args:
            operation (str): 操作类型，"add"为增加，"sub"为减少 TODO:"???"更精细的自定义操作？
            power (int): 操作的数值
        """

        if operation == "add":
            self.power += power
        elif operation == "sub":
            self.power -= power
        else:
            raise ValueError(f"你他🐎的 -> {operation} <- 操作是什么玩意？ 我不认识!") 
        return


