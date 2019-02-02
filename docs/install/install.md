# Product Service


## Add products to the database

Run the following against the product container
```
$ docker exec -i <CHANGE_TO_CONTAINER_NAME> python add_products.py
```

To find the container:
```
$ docker ps -a
CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS              PORTS                    NAMES
063bfdb6abf6        frontendgit_user       "python app.py"          About an hour ago   Up About an hour    0.0.0.0:8082->5000/tcp   frontendgit_user_1
6210faec3385        frontendgit_product    "python app.py"          About an hour ago   Up About an hour    0.0.0.0:8081->5000/tcp   frontendgit_product_1
9ac86d9588ad        frontendgit_order      "python app.py"          About an hour ago   Up About an hour    0.0.0.0:8083->5000/tcp   frontendgit_order_1
5ce04e5859d8        frontendgit_frontend   "/bin/sh -c 'python …"   About an hour ago   Up About an hour    0.0.0.0:80->5000/tcp     frontendgit_frontend_1
c451c131818b        mysql:5.7.22           "docker-entrypoint.s…"   About an hour ago   Up About an hour    3306/tcp                 frontendgit_user_db_1
a280b689942f        mysql:5.7.22           "docker-entrypoint.s…"   About an hour ago   Up About an hour    3306/tcp                 frontendgit_product_db_1
b86246a5b652        mysql:5.7.22           "docker-entrypoint.s…"   About an hour ago   Up About an hour    3306/tcp                 frontendgit_order_db_1

```

In this case the container name is ``frontendgit_product_1``