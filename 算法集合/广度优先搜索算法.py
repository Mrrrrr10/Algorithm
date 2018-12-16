__author__ = 'Mrrrrr10'
__date__ = '2018/12/16 1:20'
__github__ = 'https://github.com/Mrrrrr10'


from collections import deque


def person_is_seller(name):
    """判断是否为芒果供应商"""
    return name[-1] == 'm'


def search(name):
    """广度优先搜索算法"""
    graph = {}
    graph['you'] = ["alice", "bob", "claire"]
    graph['alice'] = ["Peggy"]
    graph['bob'] = ["Peggy", "Anuj"]
    graph['claire'] = ["Jonny", "Thom"]
    graph['Peggy'] = []
    graph['Anuj'] = []
    graph['Jonny'] = []
    graph['Thom'] = []

    search_queue = deque()                              # 创建双端队列
    search_queue += graph[name]
    searched = []                                       # 这个数组用于记录检查过的人
    while search_queue:                                 # 只要队列不为空
        person = search_queue.popleft()                 # 就取出其中的第一个人
        if person not in searched:                      # 仅当这个人没检查过时才检查
            if person_is_seller(person):                # 检查这个人是否是芒果销售商
                print(person + " is a mango seller!")   # 是芒果销售商
                return True
            else:
                search_queue += graph[person]           # 不是芒果销售商。将这个人的朋友都加入搜索队列
                searched.append(person)                 # 将这个人标记为检查过
    return False                                        # 如果到达了这里，就说明队列中没人是芒果销售商


search("you")



