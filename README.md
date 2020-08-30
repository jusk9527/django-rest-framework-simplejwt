# Simple JWT

![License](https://img.shields.io/badge/license-Apache%202-blue)


## Abstract


Simple JWT is a JSON Web Token authentication plugin for the Django REST

Framework ![http://www.django-rest-framework.org/]()

For full documentation, visit django-rest-framework-simplejwt.readthedocs.io
![https://django-rest-framework-simplejwt.readthedocs.io/en/latest/]()


二次开发的Simple JWT
## Installation

You can use this command to install this package:


```markdown
pip install djangorestframework-simplejwt-captcha==1.1.6
```



## Usage


```markdown
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,ImageInfo

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/images_captcha/',ImageInfo.as_view(), name='images_captcha'),

]
```

- api/images_captcha 是获取图片base64和uuid
- api/token/是登录获取jwt

```markdown
传入4个参数
- username
- password
- uuid          # 获取上一个api 的uuid
- captcha       # 图片验证码
```

- api/token/refresh     刷新token




## For more information, see here
### 验证码有效期是120秒

![https://github.com/SimpleJWT/django-rest-framework-simplejwt/issues/207]()



