import logging

import requests
import app


class OrderApi:
    """订单API接口方法"""

    def __init__(self):
        # 用户订单列表
        self.order_list_url = app.base_url + "/order/by_user"
        # 创建订单
        self.create_order_url = app.base_url + "/order"
        # 查看订单
        self.query_order_url = app.base_url + "/order/{}"

    def order_list_api(self, page=1):
        """
        用户订单列表
        :param page:订单页数
        :return:
        """
        logging.info("订单-用户订单列表")

        # 请求数据
        data = {"page": page}
        # 请求
        return requests.get(self.order_list_url, params=data, headers=app.headers)

    def create_order_api(self, product_id, count):
        """创建订单"""
        logging.info("订单-创建订单")

        # 请求数据
        data = {"products": [{"product_id": product_id, "count": count}]}
        # 请求
        return requests.post(self.create_order_url, json=data, headers=app.headers)

    def query_order_api(self, order_id):
        """查看订单"""
        logging.info("订单-查看订单")

        return requests.get(self.query_order_url.format(order_id), headers=app.headers)
