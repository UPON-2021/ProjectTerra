from camp.earth import earth
from camp.human import human

import json

# 模拟游戏开始，玩家选择角色，不同的角色拥有不同的 priority

earth = earth("earth",10)
human1 = human("human1",priority=5,score=100,influence=1)
human2 = human("human2",priority=4,score=100,influence=1)
human3 = human("human3",priority=3,score=100,influence=1)
human4 = human("human4",priority=2,score=100,influence=1)
human5 = human("human5",priority=1,score=100,influence=1)

seq = [human1,human5,human3,human2,human4,earth]

# 将所有玩家按照优先级排序，并按此 顺序执行游戏
seq.sort()
print("排序后：")
for i in seq:
    print(i)


test_event_data = """
{
    "earth_event_union_key1":{
        "piroity":0,
        "//":"此处使用piroity表示特定优先级的玩家才能触发此事件，此处0代表地球玩家",
        "eventinfo":"这是一个事件的信息",
        "choices":[
            {
                "choiceinfo":"这是这个选项的信息",
                "requirement":[
                    {
                        "target":0,
                        "require":{
                            "property":"power",
                            "operator":"SUB",
                            "value":"10"
                        }
                    }
                ],
                "result":[
                    {   
                        "piroity":1,
                        "property":"score",
                        "operator":"ADD",
                        "value":"10"
                    },
                    {
                        "piroity":2,
                        "property":"score",
                        "operator":"SUB",
                        "value":"10"
                    },
                    {
                        "piroity":3,
                        "property":"power",
                        "operator":"ADD",
                        "value":"10"
                    },
                    {
                        "piroity":4,
                        "property":"power",
                        "operator":"SUB",
                        "value":"10"
                    },
                    {
                        "piroity":5,
                        "property":"money",
                        "operator":"ADD",
                        "value":"10"
                    }
                ]
            }
        ],
        "next_event":["earth_event_union_key5","earth_event_union_key6"]
    },

    "earth_event_union_key5":{
        "piroity":0,
        "//":"此处使用piroity表示特定优先级的玩家才能触发此事件，此处0代表地球玩家",
        "eventinfo":"这是第二轮的分支1事件",
        "next_event":["end1","end2"]
    },

    "earth_event_union_key6":{
        "piroity":0,
        "//":"此处使用piroity表示特定优先级的玩家才能触发此事件，此处0代表地球玩家",
        "eventinfo":"这是第二轮的分支2事件",
        "next_event":["end5","end6"]
    }
}
"""

event = json.loads(test_event_data)
print(event)

# 第一回合开始，假设地球玩家选了了  `earth_event_union_key1` 这个事件

round_one = event["earth_event_union_key1"]
print(round_one["eventinfo"])

# 选项，这里先偷懒不写判断条件了，直接选第一个选项
choices = round_one["choices"]
print(choices)

# TODO: check requirement and result

# 选项的结果
result = choices[0]["result"]
print(result)

# 地球执行event了
for i in result:
    seqnum = i["piroity"]
    seq[seqnum].change_score(i["operator"],int(i["value"]))
    print(seq[seqnum])


# 略过这玩家的事件,玩家的事件选项与地球事件的选项处理方式一致，这里主要展示事件树的想法


# 第二回合开始前

print(round_one["next_event"])

# 假设选取有两个事件分支 `earth_event_union_key5` 和 `earth_event_union_key6`，这里偷懒不写判断条件了，假设地球直接选第一个分支

round_two = event["earth_event_union_key5"]

# 仍旧是和第一个分支一样的处理方式，这里不赘述

...

# 以此类推，直到游戏结束即某个事件的 next_event 为end
# 事件树的优势在于，可以将游戏的事件分支化，每个事件都是一个独立的对象，可以根据玩家的选择进行不同的处理，从树的根出发，根据玩家的选择和 game state 进行不同的处理，直到游戏结束