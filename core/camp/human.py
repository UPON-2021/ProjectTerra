from .player import player

class human(player):
    """人类阵营类
    继承player类，包含人类阵营特有的属性和函数：

    Args:
        score (int):人类阵营的分数，按照此分数来计算胜负
        influence (float):人类阵营的影响力，此参数给分数提供加成
        cooperation (int):合作次数
        betrayal (int):背叛次数
    Functions:
    """

    def __init__(self,username:str,priority:int,score:int,influence:float,cooperation:int=2,betrayal:int=2) -> None:
        """初始化人类阵营对象

        Args:
            username (str): 用户名
            priority (int): 优先级
            score (int): 分数
            influence (float): 影响力
            cooperation (int, optional): 合作次数. 默认是 2.
            betrayal (int, optional): 拒绝合作次数. 默认是 2.
        """
        super().__init__(username)
        super().change_priority(priority)
        self.score = score
        self.influence = influence
        self.cooperation = cooperation
        self.betrayal = betrayal
        pass

    def __str__(self) -> str:
        return (f"username:{self.name},score:{self.score},influence:{self.influence},cooperation:{self.cooperation},betrayal:{self.betrayal}")
        # return super().__str__() + f",score:{self.score},influence:{self.influence}"

    def __lt__(self, other) -> bool:
        """重载小于运算符，用于排序
        """
        return self.priority < other.priority

    def change_score(self,operation:str,score:int) -> None:
        """更改人类的score值，根据operation的不同，进行对应的操作,

        Args:
            operation (str): 操作类型 REP为直接修改数值，ADD为增加，SUB为减少,MUL为乘法,DIV为除法 TODO:更多操作？
            score (int): 操作的数值
        """
        if operation == "REP":
            self.score = score
        elif operation == "ADD":
            self.score = int(self.score + score)
        elif operation == "SUB":
            self.score = int(self.score - score)
        elif operation == "MUL":
            self.score = int(self.score * score)
        elif operation == "DIV":
            self.score = int(self.score / score)
        else:
            raise ValueError(f"你他🐎的 -> {operation} <- 操作是什么玩意？ 我不认识!")
        return
    
    def change_influence(self,influence:float) -> None:
        """更改人类的influence值
        Args:
            influence (float): 影响力值
        """
        self.influence = influence
        return
    
    def change_score_with_influence(self,operation:str="MUL") -> None:
        """更改人类的score值，根据operation的不同，进行对应的操作,并根据influence的值进行加成，默认为乘法

        Args:
            operation (str): 操作类型 MUL 为core*influence,DIV为除法 TODO:更多操作？
        """
        if operation == "MUL":
            self.score = int(self.score * self.influence)
        elif operation == "DIV":
            self.score = int(self.score / self.influence)
        else:
            raise ValueError(f"你他🐎的 -> {operation} <- 操作是什么玩意？ 我不认识!")
        return
    
    def do_cooperation(self) -> None:
        """合作一次,扣除合作次数"""
        assert self.cooperation >= 0
        self.cooperation -= 1
        return
    
    def do_betrayal(self) -> None:
        """背叛一次，扣除背叛次数"""
        assert self.betrayal >= 0
        self.betrayal -= 1
        return
    
    def get_cooperation(self) -> None:
        """获得一个合作次数"""
        self.cooperation += 1
        return
    
    def get_betrayal(self) -> None:
        """获得一个背叛次数"""
        self.betrayal += 1
        return
