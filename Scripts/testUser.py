import logging

import pytest

import app
import utils
from Api.apiFactory import ApiFactory

@pytest.mark.run(order=0)
class TestUserApi:

    def test_get_token(self):
        """获取Token"""
        # 请求响应对象
        res = ApiFactory.get_user_api().get_token_api()
        # 打印请求地址,请求参数,请求响应数据
        logging.info(f"请求地址:{res.url}")
        logging.info(f"请求地址:{res.json()}")
        # 断言状态码
        utils.common_assert_code(res)
        # 断言token存在
        assert len(res.json().get("token")) > 0
        # 保存token
        app.headers["token"]=res.json().get("token")
        print(f"app.headers:{app.headers}")

    def test_verify_token(self):
        """验证token"""
        # 请求响应对象
        res = ApiFactory.get_user_api().verify_token_api()
        # 打印请求地址,请求参数,请求响应数据
        logging.info(f"请求地址:{res.url}")
        logging.info(f"请求地址:{res.json()}")
        # 断言状态码
        utils.common_assert_code(res)

        # 断言有效
        assert res.json().get("isValid") is True

    def test_user_address(self):
        """用户地址信息"""
        res =ApiFactory.get_user_api().user_address_api()
        # 打印请求地址,请求参数,请求响应数据
        logging.info(f"请求地址:{res.url}")
        logging.info(f"请求地址:{res.json()}")
        # 断言状态码
        utils.common_assert_code(res)

        # 断言信息
        assert False not in [i in res.text for i in ['大王', '13788888888', '北京市', '朝阳区', '002号']]
