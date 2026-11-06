import json
# >>>>>>>>>>>>>>>>>>>>>>>>>-1-<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# with open("users.json") as ptr:
#     data=json.load(ptr)
#     for x in data["branches"]:
#         print(x["name"])
# >>>>>>>>>>>>>>>>>>>>>>>>>-2-<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# with open("users.json") as ptr:
#     data=json.load(ptr)
#     for x in data["branches"]:
#         for i in x["teachers"]:
#             if "Python" in i["subject"]:
#                 print(i)
# >>>>>>>>>>>>>>>>>>>>>>>>>-3-<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# with open("users.json") as ptr:
#     data=json.load(ptr)
#     count=0
#     for x in data["branches"]:
#         for i in x["students"]:
#             count+=1
#     print(count)
# >>>>>>>>>>>>>>>>>>>>>>>>>-4-<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# with open("users.json") as ptr:
#     data=json.load(ptr)
#     dct={}
#     for x in data["branches"]:
#         for i in x["students"]:
#             dct[i["name"]]=[i["payment"]]

# print(max(dct, key=dct.get))
# >>>>>>>>>>>>>>>>>>>>>>>>>-5-<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# with open("users.json") as ptr:
#     data=json.load(ptr)
#     lst=[]
#     for x in data["branches"]:
#         for i in x["students"]:
#             lst.append(int(i["payment"]))
# print(sum(lst))
# >>>>>>>>>>>>>>>>>>>>>>>>>-6-<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# with open("users.json") as ptr:
#     data=json.load(ptr)
#     for x in data["branches"]:
#         for i in x["teachers"]:
#             if i["experience"] <5:
#                 print(i)
# >>>>>>>>>>>>>>>>>>>>>>>>>-7-<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# with open("users.json") as ptr:
#     data=json.load(ptr)
#     for x in data["branches"]:
#         for i in x["students"]:
#             if "Python" in i["course"]:
#                 print(i)