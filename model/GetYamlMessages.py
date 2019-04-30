import re

from model.Yaml import MyConfig, MyProject


class GetConfigMessage(object):
    """用例读取common.yaml文件中的内容"""
    def __init__(self, module="about", class_name="TestAboutUs", case_name="test_profile"):
        """
        初始化，读取common中的数据，self.data_messages为对应数据
        :param module: 模块：如 staff_manage
        :param class_name: 类：如：'className': 'TestLogin'
        :param case_name: 用例名称：如：test_accountError
        """
        global url, value
        self.module = module
        self.class_name = class_name
        self.case_name = case_name
        self.url = MyConfig('url').base_url
        self.all_parm = MyProject('').parameter_ui
        data_messages = {}
        for a in self.all_parm[module]:
            if a["className"] == class_name:
                if a['url'] is None:
                    url = self.url
                else:
                    url = self.url + a['url']
                for b in a["funName"]:
                    try:
                        value = b[case_name]
                        if value["url"] is not None:
                            url = self.url + value["url"]
                        data_messages["url"] = url
                        data_messages["author"] = value["author"]
                        data_messages["level"] = value["level"]
                        data_messages["asserts"] = value["asserts"]
                        data_messages["scene"] = value["scene"]
                    except Exception as exc:
                        reason = "{}.{}.{}.common.yaml中的caseName与测试类caseName不存在，该条用例已终止测试...原因:{}异常".\
                            format(self.module, self.class_name, self.case_name, exc)
                        raise ValueError(reason)
        if data_messages:
            self.data_messages = data_messages
        else:
            reason_one = "{}.{}.{}.data_messages无数据，请检查对应参数是否正确，该条用例已终止测试...".\
                          format(self.module, self.class_name, self.case_name)
            raise ValueError(reason_one)


    def re(self):
        """返回数据"""
        return self.data_messages

    def param_extract(self, value: str):
        """
        处理场景中存在的{XX}数据，进行转换处理
        :param value: 场景的所有数据
        :return: 返回{}里面的数据
        """
        data = re.findall("{(.*?)}", value)
        if not data:
            raise ValueError("{}.{}.{}，场景中scene存在空数据，此项不能存在为空，否则会影响测试用例的正常执行情况，需修正...".
                             format(self.module, self.class_name, self.case_name, ))
        else:
            return data

