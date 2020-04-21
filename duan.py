1. config.py 是用来被 app.py 来 import 的
2. 运行app出错的原因是没有开启mongo数据库软件
    windows 上已用mongod和robomongo打开了
    linux上海没有安装
3. 部署wsgi文件在 /var/www/bbs/bbs.conf，链接到/etc/supervisor/conf.d/bbs.conf
4. bbs.ngix 文件也一样，部署在/var/, 链接到/etc/
    为啥要用反向代理?
    要监听默认的80端口，转到2000或2001
5. 其他配置conf文件：
    mongod.conf
    redis-server.conf
6. 从web14到web20，添加了数据库，添加了redis，添加了ngix，保留了wsgi，
    服务器部署从windows上的能跑通变为了
    迁移在Linux上进行测试。
    