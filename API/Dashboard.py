#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/7/19 上午1:24
# @Author  : tudouya (568865013@qq.com)
# @Version : 1.0.0

from .Base import Base
import requests


class Dashboard(Base):
    def __init__(self, api_base_url, api_key):
        super().__init__(api_base_url, api_key)

        self.logger = self.get_logger

    def stats(self):
        dashboard_stats_api = f'{self.api_base_url}/api/v1/me/stats'
        print(dashboard_stats_api)
        try:
            response = requests.get(dashboard_stats_api, headers=self.auth_headers, verify=False)
            print(response.text)
        except Exception:
            self.logger.error('Get Dashboard Stats Failed......', exc_info=True)
