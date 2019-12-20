import re
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

    async def get_id_info(self, access_token):
        """
        :param access_token:
        :return: {'union_id': '', 'open_id': ''}
        """
        params = {
            'access_token': access_token,
            'unionid': 1,
        }

        unionid_url = 'https://graph.qq.com/oauth2.0/me'

        try:
            async with self._session.get(unionid_url, params=params,
                                         timeout=self.timeout) as resp:
                resp_text = await resp.text()
                json_text = re.sub(r'^callback\(', '', resp_text)
                json_text = re.sub(r'\);.*$', '', json_text).strip()
                result = json.loads(json_text)
                if result.get('error'):
                    raise AioQQAuthError(result)
                return {
                    'union_id': result.get('unionid'),
                    'open_id': result.get('openid'),
                }
        except asyncio.TimeoutError:
            raise AioQQTimeoutError()
