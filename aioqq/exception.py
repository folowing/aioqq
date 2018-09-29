
class AioQQError(Exception):
    pass


class AioQQTimeoutError(AioQQError):
    pass


class AioQQAuthError(AioQQError):
    pass
