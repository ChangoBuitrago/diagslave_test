1 ) Run `diagslave` in bg

```
docker build -t diagslave .
docker run -d -p 502:502 diagslave
```

2 ) Run `test.py`

```
pipenv install
pipenv shell
```

```
(modbus_master) > python3 test.py
```


