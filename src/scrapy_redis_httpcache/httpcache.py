import pickle

import redis
from scrapy import Request, Spider
from scrapy.http import Headers, Response
from scrapy.responsetypes import responsetypes
from scrapy.settings import Settings


class RedisCacheStorage:
    """A scrapy response storage that caches responses in Redis."""

    def __init__(self, settings: Settings) -> None:
        """Construct an instance of the InfluxDBStatsCollector class.

        :param settings: The Scrapy settings.
        :type settings: Settings
        """
        self._expiration_secs = settings.getint("HTTPCACHE_EXPIRATION_SECS", 3600)
        self._redis = redis.Redis(
            host=settings.get("HTTPCACHE_REDIS_HOST", "localhost"),
            port=settings.getint("HTTPCACHE_REDIS_PORT", 6379),
            db=settings.getint("HTTPCACHE_REDIS_DB", 0),
            password=settings.get("HTTPCACHE_REDIS_PASSWORD", None),
            username=settings.get("HTTPCACHE_REDIS_USERNAME", None),
        )

    def close_spider(self, spider: Spider) -> None:
        """Close the spider.

        :param spider: The spider instance to close.
        :type spider: Spider
        """

    def open_spider(self, spider: Spider) -> None:
        """Open the spider.

        :param spider: The spider instance to open.
        :type spider: Spider
        """

    def retrieve_response(self, spider: Spider, request: Request) -> Response | None:
        """Retrieve a response from the cache.

        :param spider: The spider instance to retrieve the response for.
        :type spider: Spider
        :param request: The request to retrieve the response for.
        :type request: Request
        :return: The response from the cache, or None if not found.
        :rtype: Response | None
        """
        key = spider.crawler.request_fingerprinter.fingerprint(request).hex()
        _data = self._redis.get(key)

        if _data is None:
            return None

        data = pickle.loads(_data)  # noqa: S301
        url = data["url"]
        headers = Headers(data["headers"])
        status = data["status"]
        body = data["body"]
        respcls = responsetypes.from_args(headers=headers, url=url, body=body)
        return respcls(url=url, headers=headers, status=status, body=body)

    def store_response(
        self, spider: Spider, request: Request, response: Response
    ) -> None:
        """Store a response in the cache.

        :param spider: The spider instance to store the response for.
        :type spider: Spider
        :param request: The request to store the response for.
        :type request: Request
        :param response: The response to store.
        :type response: Response
        """
        key = spider.crawler.request_fingerprinter.fingerprint(request).hex()
        data = pickle.dumps(
            {
                "url": response.url,
                "headers": dict(response.headers),
                "status": response.status,
                "body": response.body,
            },
            protocol=pickle.HIGHEST_PROTOCOL,
        )
        self._redis.set(key, data, ex=self._expiration_secs)
