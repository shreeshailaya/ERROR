/home/shree/PycharmProjects/StockDataColl/DataColl/Data/views.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

/home/shree/PycharmProjects/StockDataColl/venv/lib/python3.6/site-packages/pandas_datareader/compat/__init__.py:7: FutureWarning: pandas.util.testing is deprecated. Use the functions in the public API at pandas.testing instead.
  from pandas.util.testing import assert_frame_equal
System check identified no issues (0 silenced).
March 31, 2020 - 19:15:06
Django version 3.0.3, using settings 'DataColl.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[31/Mar/2020 19:15:07] "GET / HTTP/1.1" 200 3529
STNAME: <WSGIRequest: GET '/showplt/'>.NS
<class 'str'>
<class 'str'>
<class 'str'>
Not Found: /searchicon.png
[31/Mar/2020 19:15:07] "GET /searchicon.png HTTP/1.1" 404 2814
Internal Server Error: /showplt/
Traceback (most recent call last):
  File "/home/shree/PycharmProjects/StockDataColl/venv/lib/python3.6/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/shree/PycharmProjects/StockDataColl/venv/lib/python3.6/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/shree/PycharmProjects/StockDataColl/venv/lib/python3.6/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/shree/PycharmProjects/StockDataColl/DataColl/Data/views.py", line 86, in graph_data
    df = web.DataReader(st_name, data_source='yahoo', start='2019-01-01', end='2020-03-16')
  File "/home/shree/PycharmProjects/StockDataColl/venv/lib/python3.6/site-packages/pandas/util/_decorators.py", line 214, in wrapper
    return func(*args, **kwargs)
  File "/home/shree/PycharmProjects/StockDataColl/venv/lib/python3.6/site-packages/pandas_datareader/data.py", line 387, in DataReader
    session=session,
  File "/home/shree/PycharmProjects/StockDataColl/venv/lib/python3.6/site-packages/pandas_datareader/base.py", line 251, in read
    df = self._read_one_data(self.url, params=self._get_params(self.symbols))
  File "/home/shree/PycharmProjects/StockDataColl/venv/lib/python3.6/site-packages/pandas_datareader/yahoo/daily.py", line 153, in _read_one_data
    resp = self._get_response(url, params=params)
  File "/home/shree/PycharmProjects/StockDataColl/venv/lib/python3.6/site-packages/pandas_datareader/base.py", line 179, in _get_response
    raise RemoteDataError(msg)
pandas_datareader._utils.RemoteDataError: Unable to read URL: https://finance.yahoo.com/quote/<WSGIRequest: GET '/showplt/'>.NS/history?period1=1546315200&period2=1584417599&interval=1d&frequency=1d&filter=history
Response Text:
b'<html>\n<meta charset=\'utf-8\'>\n<script>\nvar u=\'https://www.yahoo.com/?err=404&err_url=https%3a%2f%2ffinance.yahoo.com%2fquote%2f%253CWSGIRequest%3a%2520GET%2520%27%2fshowplt%2f%27%253E.NS%2fhistory%3fperiod1%3d1546315200%26period2%3d1584417599%26interval%3d1d%26frequency%3d1d%26filter%3dhistory\';\nif(window!=window.top){\n  document.write(\'<p>Content is currently unavailable.</p><img src="//geo.yahoo.com/p?s=1197757039&t=\'+new Date().getTime()+\'&_R=\'+encodeURIComponent(document.referrer)+\'&err=404&err_url=\'+u+\'" width="0px" height="0px"/>\');\n}else{\n  window.location.replace(u);\n}\n</script>\n<noscript><META http-equiv="refresh" content="0;URL=\'https://www.yahoo.com/?err=404&err_url=https%3a%2f%2ffinance.yahoo.com%2fquote%2f%253CWSGIRequest%3a%2520GET%2520%27%2fshowplt%2f%27%253E.NS%2fhistory%3fperiod1%3d1546315200%26period2%3d1584417599%26interval%3d1d%26frequency%3d1d%26filter%3dhistory\'"></noscript>\n</html>\n'
[31/Mar/2020 19:15:12] "GET /showplt/ HTTP/1.1" 500 103901
STNAME: vbl.NS
<class 'str'>
<class 'str'>
<class 'str'>
                  High         Low        Open       Close    Volume   Adj Close
Date                                                                            
2019-01-01  552.666992  512.500000  526.666992  543.500000  106183.0  541.378418
2019-01-02  545.299988  526.833008  536.700012  530.367004   50379.0  528.296692
2019-01-03  539.367004  530.267029  530.666992  533.700012   26665.0  531.616699
2019-01-04  543.099976  532.299988  533.333008  538.232971   93513.0  536.131958
2019-01-07  550.000000  537.666992  540.900024  541.132996  463504.0  539.020691
...                ...         ...         ...         ...       ...         ...
2020-03-11  796.650024  726.099976  743.750000  782.700012  417185.0  782.700012
2020-03-12  770.799988  706.049988  770.799988  755.700012  305404.0  755.700012
2020-03-13  780.000000  605.099976  701.099976  775.349976  129043.0  775.349976
2020-03-16  747.950012  695.549988  745.000000  704.400024  148210.0  704.400024
2020-03-17  743.950012  686.549988  703.000000  709.049988  231000.0  709.049988

[295 rows x 6 columns]
[31/Mar/2020 19:15:16] "POST / HTTP/1.1" 200 3590
STNAME: <WSGIRequest: GET '/showplt/'>.NS
<class 'str'>
<class 'str'>
<class 'str'>
Not Found: /searchicon.png
[31/Mar/2020 19:15:16] "GET /searchicon.png HTTP/1.1" 404 2814
Internal Server Error: /showplt/
Traceback (most recent call last):
  File "/home/shree/PycharmProjects/StockDataColl/venv/lib/python3.6/site-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/home/shree/PycharmProjects/StockDataColl/venv/lib/python3.6/site-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/home/shree/PycharmProjects/StockDataColl/venv/lib/python3.6/site-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/shree/PycharmProjects/StockDataColl/DataColl/Data/views.py", line 86, in graph_data
    df = web.DataReader(st_name, data_source='yahoo', start='2019-01-01', end='2020-03-16')
  File "/home/shree/PycharmProjects/StockDataColl/venv/lib/python3.6/site-packages/pandas/util/_decorators.py", line 214, in wrapper
    return func(*args, **kwargs)
  File "/home/shree/PycharmProjects/StockDataColl/venv/lib/python3.6/site-packages/pandas_datareader/data.py", line 387, in DataReader
    session=session,
  File "/home/shree/PycharmProjects/StockDataColl/venv/lib/python3.6/site-packages/pandas_datareader/base.py", line 251, in read
    df = self._read_one_data(self.url, params=self._get_params(self.symbols))
  File "/home/shree/PycharmProjects/StockDataColl/venv/lib/python3.6/site-packages/pandas_datareader/yahoo/daily.py", line 153, in _read_one_data
    resp = self._get_response(url, params=params)
  File "/home/shree/PycharmProjects/StockDataColl/venv/lib/python3.6/site-packages/pandas_datareader/base.py", line 179, in _get_response
    raise RemoteDataError(msg)
pandas_datareader._utils.RemoteDataError: Unable to read URL: https://finance.yahoo.com/quote/<WSGIRequest: GET '/showplt/'>.NS/history?period1=1546315200&period2=1584417599&interval=1d&frequency=1d&filter=history
Response Text:
b'<html>\n<meta charset=\'utf-8\'>\n<script>\nvar u=\'https://www.yahoo.com/?err=404&err_url=https%3a%2f%2ffinance.yahoo.com%2fquote%2f%253CWSGIRequest%3a%2520GET%2520%27%2fshowplt%2f%27%253E.NS%2fhistory%3fperiod1%3d1546315200%26period2%3d1584417599%26interval%3d1d%26frequency%3d1d%26filter%3dhistory\';\nif(window!=window.top){\n  document.write(\'<p>Content is currently unavailable.</p><img src="//geo.yahoo.com/p?s=1197757039&t=\'+new Date().getTime()+\'&_R=\'+encodeURIComponent(document.referrer)+\'&err=404&err_url=\'+u+\'" width="0px" height="0px"/>\');\n}else{\n  window.location.replace(u);\n}\n</script>\n<noscript><META http-equiv="refresh" content="0;URL=\'https://www.yahoo.com/?err=404&err_url=https%3a%2f%2ffinance.yahoo.com%2fquote%2f%253CWSGIRequest%3a%2520GET%2520%27%2fshowplt%2f%27%253E.NS%2fhistory%3fperiod1%3d1546315200%26period2%3d1584417599%26interval%3d1d%26frequency%3d1d%26filter%3dhistory\'"></noscript>\n</html>\n'
[31/Mar/2020 19:15:19] "GET /showplt/ HTTP/1.1" 500 103901
