import allure
import pytest
import logging
from lib.readconfg import read_config
from lib.yamlContorl import YamlUsage
from lib.sendrequest import SendRequests


reqs = SendRequests()
yml = YamlUsage('./datebase/rqe.yaml')
yml_url = yml.get_yaml_url()
uml_data = yml.get_yaml_data()
host = read_config()


@allure.story("车管所查询")
@allure.title("用例标题  {data[detail]}")
@pytest.mark.parametrize('url_method', yml_url)
@pytest.mark.parametrize('data', uml_data)
def test_select(url_method, data):
    logging.info("*************** 开始执行用例 ({0}) ***************".format(data['detail']))
    url = host + url_method['url']
    re = reqs.sendRequests(url_method['method'], url, data['data'])
    result = re.json()
    logging.info("code ==>> 期望结果：{}， 实际结果：{}".format(data['resp']['code'], result['code']))
    assert data['resp']['code'] == result['code']
    assert data['resp']['message'] == result['message']
    logging.info("*************** 结束执行用例 ({0}) ***************".format(data['detail']))







