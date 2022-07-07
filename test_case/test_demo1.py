import logging
import allure


@allure.story("测试aaaa")
@allure.title("aaa测试用例")
def test_a():
    print("aaa")
    logging.error("tettete")


@allure.story("测试bbb")
@allure.title("bbb测试用例")
def test_b():
    print("bbb")
    logging.info("123123435")
    logging.warning("123124444")
    logging.debug("456")
    logging.error("ddddd")


