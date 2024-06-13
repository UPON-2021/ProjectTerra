class checkerboard:
    """

    population（int） : 人口数量,降到0则游戏结束
    environment（int） : 环境值
    ecology（int） : 生态值
    """
    def __init__(self,population:int,environment:int,ecology:int) -> None:
        self.population = population
        self.environment = environment
        self.ecology = ecology
        pass

    def __str__(self) -> str:
        return (f"population:{self.population},environment:{self.environment},ecology:{self.ecology}")
    
    def change_population(self,operation:str,population:int) -> None:
        """更改人口数量，根据operation的不同，进行对应的操作

        Args:
            operation (str): 操作类型，"add"为增加，"sub"为减少 TODO:"???"更精细的自定义操作？
            population (int): 操作的数值
        """

        if operation == "add":
            self.population += population
        elif operation == "sub":
            self.population -= population
        else:
            raise ValueError(f"你他🐎的 -> {operation} <- 操作是什么玩意？ 我不认识!") 
        return
    
    def change_environment(self,operation:str,environment:int) -> None:
        """更改环境值，根据operation的不同，进行对应的操作

        Args:
            operation (str): 操作类型，"add"为增加，"sub"为减少 TODO:"???"更精细的自定义操作？
            environment (int): 操作的数值
        """

        if operation == "add":
            self.environment += environment
        elif operation == "sub":
            self.environment -= environment
        else:
            raise ValueError(f"你他🐎的 -> {operation} <- 操作是什么玩意？ 我不认识!") 
        return
    
    def change_ecology(self,operation:str,ecology:int) -> None:
        """更改生态值，根据operation的不同，进行对应的操作

        Args:
            operation (str): 操作类型，"add"为增加，"sub"为减少 TODO:"???"更精细的自定义操作？
            ecology (int): 操作的数值
        """

        if operation == "add":
            self.ecology += ecology
        elif operation == "sub":
            self.ecology -= ecology
        else:
            raise ValueError(f"你他🐎的 -> {operation} <- 操作是什么玩意？ 我不认识!") 
        return
    
