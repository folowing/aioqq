import asyncio
import json

from .exception import (
    AioQQTimeoutError,
    AioQQAuthError,
)


class AioQQAuth:

    async def get_user_info(self, access_token, open_id):
        params = {
            'access_token': access_token,
            'oauth_consumer_key': self.app_id,
            'openid': open_id,
        }

        user_info_url = 'https://graph.qq.com/user/get_user_info'

        try:
            async with self._session.get(user_info_url, params=params,
                                         timeout=self.timeout) as resp:
                resp_text = await resp.text()
                result = json.loads(resp_text)
                if result.get('ret') != 0:
                    raise AioQQAuthError(result)
                return result
        except asyncio.TimeoutError:
            raise AioQQTimeoutError()
