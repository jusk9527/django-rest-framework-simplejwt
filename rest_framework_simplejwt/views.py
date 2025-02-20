from rest_framework import generics, status
from rest_framework.response import Response

from . import serializers
from .authentication import AUTH_HEADER_TYPES
from .exceptions import InvalidToken, TokenError
from rest_framework.views import APIView
import time
import random
import hashlib
import base64
from django.core.cache import cache
import string
from captcha.image import ImageCaptcha
from io import BytesIO

class TokenViewBase(generics.GenericAPIView):
    permission_classes = ()
    authentication_classes = ()

    serializer_class = None

    www_authenticate_realm = 'api'

    def get_authenticate_header(self, request):
        return '{0} realm="{1}"'.format(
            AUTH_HEADER_TYPES[0],
            self.www_authenticate_realm,
        )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class TokenObtainPairView(TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    serializer_class = serializers.TokenObtainPairSerializer


token_obtain_pair = TokenObtainPairView.as_view()


class TokenRefreshView(TokenViewBase):
    """
    Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.
    """
    serializer_class = serializers.TokenRefreshSerializer


token_refresh = TokenRefreshView.as_view()


class TokenObtainSlidingView(TokenViewBase):
    """
    Takes a set of user credentials and returns a sliding JSON web token to
    prove the authentication of those credentials.
    """
    serializer_class = serializers.TokenObtainSlidingSerializer


token_obtain_sliding = TokenObtainSlidingView.as_view()


class TokenRefreshSlidingView(TokenViewBase):
    """
    Takes a sliding JSON web token and returns a new, refreshed version if the
    token's refresh period has not expired.
    """
    serializer_class = serializers.TokenRefreshSlidingSerializer


token_refresh_sliding = TokenRefreshSlidingView.as_view()


class TokenVerifyView(TokenViewBase):
    """
    Takes a token and indicates if it is valid.  This view provides no
    information about a token's fitness for a particular use.
    """
    serializer_class = serializers.TokenVerifySerializer


class ImageInfo(APIView):
    def image_uuid(self):
        result = random.sample(string.ascii_letters, 4)
        captcha = "".join(result)

        # 根据生成验证码生成唯一id
        str = captcha+"helloword"
        h = hashlib.md5()

        h.update(str.encode('utf-8'))

        uuid = h.hexdigest()
        # 60 秒过期
        cache.set(uuid, captcha, 120)

        image = ImageCaptcha().generate_image(captcha)
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img = b"data:image/png;base64," + base64.b64encode(buffered.getvalue())
        data = {
            "uuid":uuid,
            "img":img,
        }
        return data

    def get(self,requests):
        data = self.image_uuid()

        return Response(data)


token_verify = TokenVerifyView.as_view()
