# scrapy-redis-httpcache

Cache Scrapy responses with Redis.

This package uses [uv](https://docs.astral.sh/uv/) for project management. To get started, ensure that **uv** is installed on your machine and updated to the `0.5.6` version. Detailed installation instructions for **uv** can be found [here](https://docs.astral.sh/uv/getting-started/installation/).

## Installation

```bash
uv add scrapy-redis-httpcache
```

## Usage

Add the following settings to your Scrapy project settings file:

```python
DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware": 100,
    ...
}
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = ... # optional, defaults to 3600
HTTPCACHE_REDIS_DB = ... # optional, defaults to 0
HTTPCACHE_REDIS_HOST = ... # optional, defaults to "localhost"
HTTPCACHE_REDIS_PASSWORD = ... # optional, defaults to None
HTTPCACHE_REDIS_PORT = ... # optional, defaults to 6379
HTTPCACHE_REDIS_USERNAME = ... # optional, defaults to None
HTTPCACHE_STORAGE = "scrapy_redis_httpcache.RedisCacheStorage"
```

## Development

```bash
uv sync --frozen --group=development
uv run --frozen pre-commit install --install-hooks
uv run --frozen pre-commit install --hook-type=commit-msg
```

## Contributing

Contributions are welcome! To get started, please refer to our [contribution guidelines](https://github.com/stefanofusai/scrapy-influxdb-exporter/blob/main/CONTRIBUTING.md).

## Issues

If you encounter any problems while using this package, please open a new issue [here](https://github.com/stefanofusai/scrapy-influxdb-exporter/issues).
