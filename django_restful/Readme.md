# Overview

### Docker Containers
Use docker compose host the db, the file in the Root path.
```shell
docker-compose -f docker-compose-db.yml up -d 
```

+ Check the containers
```shell
 Name                Command               State                          Ports
------------------------------------------------------------------------------------------------------
mysql57   docker-entrypoint.sh mysqld      Up      0.0.0.0:3306->3306/tcp,:::3306->3306/tcp, 33060/tcp
redisdb   docker-entrypoint.sh redis ...   Up      0.0.0.0:6379->6379/tcp,:::6379->6379/tcp
```
+ Source the migration script
Execute the container.
```shell
docker exec -it 29a8f4f4f9c3 bash
```
Login mysql instance
```shell
root@29a8f4f4f9c3:/# mysql -u root -p
Enter password:
```
Show tables
```shell
mysql> show tables;
Empty set (0.00 sec)
```
After run the migration script
```shell
mysql> show tables;
+-----------------------+
| Tables_in_django_demo |
+-----------------------+
| classes               |
| courses               |
| stu_courses           |
| students              |
| teachers              |
| users                 |
+-----------------------+
6 rows in set (0.00 sec)
```

### Run application on laptop
+ Run the Api Service
```shell
python -m manage runserver 127.0.0.1:8000 --settings django2.api.settings
```

+ Run the JWT Backends Service
```shell
python -m manage runserver 127.0.0.1:8001 --settings django2.jwtd.settings
```

### API Example
+ UserLogin 
  
Request Example
```shell
$ curl -d "name=tonystark&password=12345678" -X POST http://127.0.0.1:8000/v1/api/login
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   610  100   578  100    32   7316    405 --:--:-- --:--:-- --:--:--  7820
```
Response Example
```json
{
    "id": "SeweQ67TDtJEPCb9yFoteL",
    "name": "tonystark",
    "password": "12345678",
    "jwt": {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NTM3MDMyNSwianRpIjoiNDQzNDRiNjZkNmQ4NDg5N2E0N2I5YmU1OWRjODZiYjIiLCJ1c2VyX2lkIjoiU2V3ZVE2N1REdEpFUENiOXlGb3RlTCJ9.Q3_cfTw3kkaCNVndhD-vJHT4y0EX4EHIwu78MURBSN4",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY1MzA1NTI1LCJqdGkiOiI0Nzk0Y2Y1ZDk2MjY0NGZhOWQ2ZmRjOGJkYmU0NzllMSIsInVzZXJfaWQiOiJTZXdlUTY3VER0SkVQQ2I5eUZvdGVMIn0.iSXYMsy5yDUWsE99G--9tHSYdRelNI84DOhNpOA74Ho"
    }
}
```
+ Create Teachers

Request Example
```shell
$ curl -X POST \
>    -H "Accept: application/json" \
>    -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY1MzA1ODU3LCJqdGkiOiIyNDhiMzAyMmE5Nzg0NDI4YTEzZTNmZTUzYWY5MjRhZCIsInVzZXJfaWQiOiJTZXdlUTY3VER0SkVQQ2I5eUZvdGVMIn0.Lhx_HrgYTSOC2Z3_1BU6i4U_rrPO_gfKcNRMIt4PhlE" \
>    -d "name=Teacher James" \
>    http://127.0.0.1:8000/v1/api/teachers
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   117  100    99  100    18      8      1  0:00:18  0:00:11  0:00:07    28
```
Response Example
```json
{
  "id":"EDDxfZ2kQ74gsAyGTr4ZRr",
  "name":"['Teacher James']",
  "created_at":"2020-4-19 15:19:38+00:00"
}
```
+ Create Class

Request Example
```shell
$ curl -X POST \
>    -H "Accept: application/json" \
>    -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY1MzA1ODU3LCJqdGkiOiIyNDhiMzAyMmE5Nzg0NDI4YTEzZTNmZTUzYWY5MjRhZCIsInVzZXJfaWQiOiJTZXdlUTY3VER0SkVQQ2I5eUZvdGVMIn0.Lhx_HrgYTSOC2Z3_1BU6i4U_rrPO_gfKcNRMIt4PhlE" \
>    -d "name=Class 1" \
>    http://127.0.0.1:8000/v1/api/classes
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   105  100    93  100    12   1609    207 --:--:-- --:--:-- --:--:--  1842
```
Response Exmaple
```json

{
  "id":"AicoCb2CFZVP3XrsRsKemZ",
  "name":"['Class 1']",
  "created_at":"2020-4-19 15:22:58+00:00"
}
```

+ Create Course
  
Request Example
```shell
$ curl -X POST \
>    -H "Accept: application/json" \
>    -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY1MzA1ODU3LCJqdGkiOiIyNDhiMzAyMmE5Nzg0NDI4YTEzZTNmZTUzYWY5MjRhZCIsInVzZXJfaWQiOiJTZXdlUTY3VER0SkVQQ2I5eUZvdGVMIn0.Lhx_HrgYTSOC2Z3_1BU6i4U_rrPO_gfKcNRMIt4PhlE" \
>    -d "name=Philosophy" \
>    http://127.0.0.1:8000/v1/api/courses
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   111  100    96  100    15   1713    267 --:--:-- --:--:-- --:--:--  2018

```
Response Example
```json
{
  "id":"GEHv98eNY5fLnvdRdhaoAq",
  "name":"['Philosophy']",
  "created_at":"2020-04-19 15:25:11+00:00"
}
```
+ Create Students

Request Example
```shell
$ curl -X POST \
>    -H "Content-Type: application/json" \
>    -H "Accept: application/json" \
>    -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY1MzA1ODU3LCJqdGkiOiIyNDhiMzAyMmE5Nzg0NDI4YTEzZTNmZTUzYWY5MjRhZCIsInVzZXJfaWQiOiJTZXdlUTY3VER0SkVQQ2I5eUZvdGVMIn0.Lhx_HrgYTSOC2Z3_1BU6i4U_rrPO_gfKcNRMIt4PhlE" \
>    -d '{"name":"Frank","phone":"123456789","teacher_id":"EDDxfZ2kQ74gsAyGTr4ZRr","class_id":"AicoCb2CFZVP3XrsRsKemZ"}' \
>    http://127.0.0.1:8000/v1/api/students
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   442  100   332  100   110    110     36  0:00:03  0:00:03 --:--:--   146
```
Response Example
```json
{
    "id":"Ypn8iVQz85ykN3enjeiJ3E",
    "name":"Frank",
    "phone":"123456789",
    "created_at":"2020-4-19 15:37:26+00:00",
    "teacher":{
          "id":"EDDxfZ2kQ74gsAyGTr4ZRr",
          "name":"['Teacher James']",
          "created_at":"2020-4-19 15:19:39+00:00"
    },
    "class_":{
        "id":"AicoCb2CFZVP3XrsRsKemZ",
        "name":"['Class 1']",
        "created_at":"2020-4-19 15:22:58+00:00"
    },
    "scores":[]
}
```

+ Create Score

Request Example
```shell
$  curl -X POST \
>    -H "Content-Type: application/json" \
>    -H "Accept: application/json" \
>    -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY1MzA1ODU3LCJqdGkiOiIyNDhiMzAyMmE5Nzg0NDI4YTEzZTNmZTUzYWY5MjRhZCIsInVzZXJfaWQiOiJTZXdlUTY3VER0SkVQQ2I5eUZvdGVMIn0.Lhx_HrgYTSOC2Z3_1BU6i4U_rrPO_gfKcNRMIt4PhlE" \
>    -d '{"score":99,"student_id":"Ypn8iVQz85ykN3enjeiJ3E","course_id":"GEHv98eNY5fLnvdRdhaoAq"}' \
>    http://127.0.0.1:8000/v1/api/scores
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   578  100   491  100    87   7245   1283 --:--:-- --:--:-- --:--:--  8626
```
Response Example
```json

{
    "id":"csaQ3M5uqBZozRKnr8XV4F",
    "score":99,
    "student":{
        "id":"Ypn8iVQz85ykN3enjeiJ3E",
        "name":"Frank",
        "phone":"123456789",
        "created_at":"2020-4-19 15:37:27+00:00",
        "teacher":{
            "id":"EDDxfZ2kQ74gsAyGTr4ZRr",
            "name":"['Teacher James']",
            "created_at":"2020-4-19 15:19:39+00:00"
        },
        "class_":{
            "id":"AicoCb2CFZVP3XrsRsKemZ",
            "name":"['Class 1']",
            "created_at":"2020-4-19 15:22:58+00:00"
        },
        "scores":[]
    },
    "course":{
        "id":"GEHv98eNY5fLnvdRdhaoAq",
        "name":"['Philosophy']",
        "created_at":"2020-4-19 15:25:11+00:00"
    }
}
```

### Deploy Service

Deploy on Docker and the demo code in the folder of `deploy`






