import redis

r = redis.Redis(host='localhost', port=6379, db=0)
p = r.pipeline()
for key in keys:
    p.hgetall(key)

for h in p.execute():
    print h
