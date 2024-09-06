grades = [[5,3,3,5,4], [2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

count = [len(grades[0]), len(grades[1]), len(grades[2]), len(grades[3]), len(grades[4])]

average_value = [
    sum(grades[0]) / count[0],
    sum(grades[1]) / count[1],
    sum(grades[2]) / count[2],
    sum(grades[3]) / count[3],
    sum(grades[4]) / count[4]
]

dict_st_gr = {key: value for key, value in zip(sorted(students), average_value)}
print(dict_st_gr)