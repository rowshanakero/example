import redis, timeit
start_time = timeit.default_timer()
count = redis.Redis(host='127.0.0.1', port=6379, db=9)
keys = api_count.keys()

data = {}

for key in keys:
    value = count.get(key)
    if value:
        data[key.decode('utf-8')] = int(value.decode('utf-8'))

elapsed = timeit.default_timer() - start_time

print('Time to read {} records: '.format(len(keys)), elapsed)
