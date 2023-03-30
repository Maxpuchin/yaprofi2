import requests

# res = requests.post(
#     "http://localhost:8080/group",
#     json={"name": "1234", "description": "123123"}
# )
# print(res.json())

# res = requests.get(
#     "http://localhost:8080/group",
# )
# print(res.json())

# res = requests.get(
#     "http://localhost:8080/group/1",
# )
# print(res.json())

# res = requests.put(
#     "http://localhost:8080/group/1",
#     json={"name": "123", "description": "123123"}
# )
# print(res.json())

# res = requests.get(
#     "http://localhost:8080/group",
# )
# print(res.json())

# res = requests.post(
#     "http://localhost:8080/group/1/participant",
#     json={"name": "1223", "wish": "123123"}
# )
# print(res.json())

# res = requests.post(
#     "http://localhost:8080/group/1/participant",
#     json={"name": "1233", "wish": "123123"}
# )
# print(res.json())

# res = requests.get(
#     "http://localhost:8080/group/1",
# )
# print(res.json())

# res = requests.post(
#     "http://localhost:8080/group/1/participant",
#     json={"name": "12323", "wish": "123123"}
# )
# print(res.json())

# res = requests.post(
#     "http://localhost:8080/group/1/toss",
# )
# print(res.json())

# res = requests.get(
#     "http://localhost:8080/group/1",
# )
# print(res.json())

res = requests.get(
    "http://localhost:8080/group/1/participant/3/recipient",
)
print(res.json())