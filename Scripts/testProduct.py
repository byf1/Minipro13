import logging

import utils
from Api.apiFactory import ApiFactory


class TestProductApi:

    def test_product_classify_api(self):
        """商品分类"""
        # 请求响应对象
        res = ApiFactory.get_product_api().product_classify_api()
        # 打印请求地址,请求参数,请求响应数据
        logging.info(f"请求地址:{res.url}")
        logging.info(f"请求地址:{res.json()}")
        # 断言状态码
        utils.common_assert_code(res)

        # 断言关键字段name,description,topic_img,head_img
        assert False not in [i in res.text for i in ['name', 'id', 'topic_img_id', 'description']]
        # 断言长度大于0
        assert len(res.json()) > 0

    def test_classify_product_api(self):
        """分类下的商品"""
        # 请求返回数据
        res = ApiFactory.get_product_api().classify_product_api()
        # 打印请求地址,请求参数,请求响应数据
        logging.info(f"请求地址:{res.url}")
        logging.info(f"请求地址:{res.json()}")
        # 断言状态码
        utils.common_assert_code(res)

        # 断言关键字段name,description,topic_img,head_img
        assert False not in [i in res.text for i in ['name', 'id', 'price', 'stock','main_img_url','img_id']]
        # 断言长度大于0
        assert len(res.json()) > 0

    def test_product_detail_api(self):
        """商品信息"""
        # 请求返回数据
        res = ApiFactory.get_product_api().product_detail_api()
        # 打印请求地址,请求参数,请求响应数据
        logging.info(f"请求地址:{res.url}")
        logging.info(f"请求地址:{res.json()}")
        # 断言状态码
        utils.common_assert_code(res)

        # 断言id,name,price
        assert res.json().get("id") == 2 and res.json().get("name") == "梨花带雨 3个" and res.json().get("price") == "0.01"

