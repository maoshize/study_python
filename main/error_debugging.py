# 错误、调试和测试


# 异常体系
import logging
logging.basicConfig(level=logging.INFO)

try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
    logging.info(u"hahahaha")
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

# logging模块
