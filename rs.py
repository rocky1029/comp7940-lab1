"""Basic connection example.
"""

import redis

r = redis.Redis(
    host='redis-18957.c325.us-east-1-4.ec2.redns.redis-cloud.com',
    port=18957,
    decode_responses=True,
    username="default",
    password="wHWcBkCSLdvfdP8vBZr0VayFIQALDoVs",
)

success = r.set('foo', 'bar')
# True

result = r.get('foo')
print(result)
# >>> bar

