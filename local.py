import requests

# res = requests.get("http://127.0.0.1:3000/api/v1/server/rrrr")

res = requests.get("http://127.0.0.1:3000/api/v1/server/Ru/1")
# res2 = requests.get("http://127.0.0.1:3000/api/v1/server/Ru/")

# res = requests.put("http://127.0.0.1:3000/api/v1/server",json={"name":"Golang","videos":10})

print(res.json())