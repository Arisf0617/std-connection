# std-connection
石铁大校园网自动登录，使用python+selenium

1.安装驱动文件，获取对应Edge版本的msedgedriver驱动
驱动下载：https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
此文件夹内的驱动适配Edge 100.0.1185.50版本，其他版本未测试
建议将驱动和connect.exe文件放在同一目录下
注：Edge浏览器版本可在设置->关于中查看

2.编辑STD.ini文件
driver=驱动文件地址，如果将驱动和connect.exe文件放在同一目录下，只需要写成msedgedriver.exe即可
name=学号/账号
password=密码

3.运行connect.exe文件

4.如需设置连接wifi后自动运行程序，请查看此教程：https://www.cnblogs.com/Arisf/p/16186145.html
