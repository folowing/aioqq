import aiohttp

from .auth import AioQQAuth


class AioQQ(AioQQAuth):

    def __init__(self, app_id, app_key, redirect_uri=None, timeout=5):
        """
        :param app_id:
        :param app_key:
        :param redirect_uri: get_access_token required
        :param timeout: request timeout
        """
        conn = aiohttp.TCPConnector(limit=1024)
        self._session = aiohttp.ClientSession(
            connector=conn,
            skip_auto_headers={'Content-Type'},
        )
        self.app_id = app_id
        self.app_key = app_key
        self.redirect_uri = redirect_uri
        self.timeout = timeout

    def __del__(self):
        if not self._session.closed:
            if self._session._connector is not None \
                    and self._session._connector_owner:
                self._session._connector.close()
            self._session._connector = None
