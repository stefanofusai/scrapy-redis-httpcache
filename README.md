# scrapy-redis-httpcache

A simple package to cache Scrapy responses in Redis.

## Installation

```bash
pip install scrapy-redis-httpcache
```

## Usage

Add the following settings to your Scrapy project settings file:

```python
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = ... # optional, defaults to 3600
HTTPCACHE_REDIS_DB = ... # optional, defaults to 0
HTTPCACHE_REDIS_HOST = ... # optional, defaults to "localhost"
HTTPCACHE_REDIS_PASSWORD = ... # optional, defaults to None
HTTPCACHE_REDIS_PORT = ... # optional, defaults to 6379
HTTPCACHE_STORAGE = "scrapy_redis_httpcache.httpcache.RedisCacheStorage"
```

## Contributing

Contributions are welcome! To get started, please refer to our [contribution guidelines](https://github.com/stefanofusai/scrapy-influxdb-exporter/blob/main/CONTRIBUTING.md).

## Issues

If you encounter any problems while using this package, please open a new issue [here](https://github.com/stefanofusai/scrapy-influxdb-exporter/issues).
