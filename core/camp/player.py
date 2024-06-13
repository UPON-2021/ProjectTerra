class player:
    """作为human和earth的父类，包含基本属性和函数：
    
    Args:
        name(str):玩家名称
        priority(int):优先级,用于决定玩家的行动顺序        
    """

    def __init__(self,username) -> None:
        self.name = username
        self.priority = 0
        pass

    def __str__(self) -> str:
        return self.name
    
    def change_priority(self,priority):
        self.priority = priority
        return
    
    def get_priority(self):
        return self.priority
