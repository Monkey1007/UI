import inspect

def _get_function_name(path):
    """获取方法名称"""
    return path + '\\' + inspect.stack()[1][3]

def _Exception():
    return Exception

FUN_NAME = _get_function_name
_EXCEPTION = _Exception()

class RequestsError(_EXCEPTION):
    """
        当接口发生错误时，调用该方法，即可返回错误信息到控制台!
    """
    def __init__(self, interface_name, back_message):
        self.interface_name = interface_name
        self.back_message = back_message

    def __str__(self):
        return "接口{!r}-请求失败，失败原因:{!r}".format(self.interface_name, self.back_message)


class AssertParams(_EXCEPTION):
    """
        当断言参数发生错误时，调用该方法，即可返回错误信息到控制台!
    """
    def __init__(self, module_name, assert_first, assert_second, error):
        self.assert_first = assert_first
        self.assert_second = assert_second
        self.module_name = module_name
        self.error = error

    def __str__(self):
        return "模块:{!r},断言:{!r}不存在或者断言:{!r}不存在,或者{!r}存在".\
            format(self.module_name, self.assert_first, self.assert_second, self.error)


class WaitTypeError(_EXCEPTION):
    """
        当浏览器等待参数发生错误时，调用该方法，即可返回错误信息到控制台!
    """
    def __init__(self, module_name):
        self.module_name = module_name

    def __str__(self):
        return "模块:{!r},等待时间格式错误,格式应该为int类型".format(self.module_name)


class SQLDataError(_EXCEPTION):
    """
        当SQL数据为空时时，调用该方法，即可返回错误信息到控制台!
    """
    def __init__(self, module_name):
        self.module_name = module_name

    def __str__(self):
        return "模块:{!r},SQL数据库为空数据,未能生成Excel测试报告".format(self.module_name)


class TypeErrors(_EXCEPTION):
    """
        类型有误时，调用该方法，即可返回错误的信息到控制台!
    """
    def __init__(self, module_name):
        self.module_name = module_name

    def __str__(self):
        return "模块:{!r},类型错误,请更正".format(self.module_name)

class LogErrors(_EXCEPTION):
    """
        记录错误日志到日志中!
    """
    def __init__(self, module_name, current_time, reason):
        self.module_name = module_name
        self.reason = reason
        self.time = current_time

    def __str__(self):
        return "执行时间:{},错误路径:{!r},错误原因:{}".format(self.time, self.module_name, self.reason)


class CreateFileError(_EXCEPTION):
    """
        生成模板出现问题时，调用该异常!
    """

    def __init__(self, module_name, current_time, reason):
        self.module_name = module_name
        self.reason = reason
        self.time = current_time

    def __str__(self):
        return "执行时间:{},模块:{!r},错误原因:{}".format(self.time, self.module_name, self.reason)

class LoginError(_EXCEPTION):
    """
        登录出现异常
    """
    def __init__(self, class_name, reason):
        self.class_name = class_name
        self.reason = reason

    def __str__(self):
        return "执行:{}时，在登录过程中遇到异常，测试被终止；异常原因:{}".format(self.class_name, self.reason)


class LoginSelectError(_EXCEPTION):
    """
        登录出现公司异常
    """

    def __init__(self, class_name):
        self.class_name = class_name

    def __str__(self):
        return "执行:{}时，当in_login为True时，account或者password不能为None"


class SceneError(_EXCEPTION):
    """
        场景错误
    """
    def __str__(self):
        return "common中scene参数为空，此参数不能为空，请增加"