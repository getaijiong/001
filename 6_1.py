lst_score=[9,10,8,9,10,7,6,8,7,8]
lst_score.sort()
print(sorted(lst_score))
lst_score.pop()
lst_score.pop(0)
count=len(lst_score)
print("该参赛选手的最终得分：",sum(lst_score)/count)
