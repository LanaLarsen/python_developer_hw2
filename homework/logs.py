import logging

logger = logging.getLogger("inf")
logger.setLevel(logging.INFO)
handler_inf = logging.FileHandler('inf.log', 'w', 'utf-8')
formatter = logging.Formatter("%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s")
handler_inf.setFormatter(formatter)
logger.addHandler(handler_inf)

err = logging.getLogger("err")
err.setLevel(logging.ERROR)
handler_err = logging.FileHandler('err.log', 'w', 'utf-8')
handler_err.setFormatter(formatter)
err.addHandler(handler_err)