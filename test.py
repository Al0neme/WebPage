import ast
with open("category_dict.txt","r",encoding="utf-8") as fr:
    r = fr.readlines()
# r = str(r)[1:-1]
# print(r[0])
# print(type(r))
r2 = ast.literal_eval(r[0])
print(r2)
print(type(r2))

# user ="{'aa':'bb','cc':'dd'}"
# print(type(ast.literal_eval(user)))