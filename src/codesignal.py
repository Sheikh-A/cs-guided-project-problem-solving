# def csWhereIsBob(names):
#     if "Bob" in names:
#         return names.index("Bob")
#     else:
#         return -1



# print(csWhereIsBob(["Jimmy", "Layla", "Bob"]))
# print(csWhereIsBob(["Jimmy", "Layla", "James"]))

# import re

# def csAlphanumericRestriction(input_str):
#     if re.match("^[A-Za-z]*$", input_str):
#         return True
#     elif re.match("^[0-9]*$", input_str):
#         return True
#     else:
#         return False



# print(csAlphanumericRestriction("123"))
# print(csAlphanumericRestriction("Hello"))
# print(csAlphanumericRestriction("Hello1"))

# def csOppositeReverse(txt):
#     reversed_txt = txt[::-1]
#     return reversed_txt.swapcase()

# print(csOppositeReverse("Hello World"))
# print(csOppositeReverse("Radar"))

# def csSquareAllDigits(n):
#     list_num = [int(i) for i in str(n)]
#     #print(list_num)

#     squared_num = [number ** 2 for number in list_num]

#     res = int("".join(map(str,squared_num)))

#     return res


# print(csSquareAllDigits(9119))


# import string


# def csSchoolYearsAndGroups(years, groups):
#     d = dict(enumerate(string.ascii_lowercase, 1))
#     #print(d[3]) # c


#     years_list = []
#     groups_list = []

#     main_str = ""

#     for x in range(years+1):
#         years_list.append(x)

#     years_list = years_list[1:years+1]

#     years_list = map(str, years_list)

#     for y in range(groups):
#         y += 1
#         y = d[y]
#         groups_list.append(y)

#     groups_list = groups_list[0:groups+1]

#     for a in years_list:
#         for b in groups_list:
#             if(a == "1" and b=="a"):
#                 main_str += a+b
#             else:
#                 main_str += ","+" "+a+b



#     return main_str

# print(csSchoolYearsAndGroups(7,2))



def csMakeItJazzy(chords):
    if len(chords) == 0:
        return chords

    chords_array = []

    for ele in chords:
        if "7" not in ele:
            new_ele = ele+"7"
            chords_array.append(new_ele)
        else:
            chords_array.append(ele)

    return chords_array


print(csMakeItJazzy(["G7", "F", "C"]))
print(csMakeItJazzy([]))
