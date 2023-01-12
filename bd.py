#Имитация Бд
server = {
    "Ru":{
    "status": "success",
    "result": {
        "server": "server_1",
        "bytes": 12345,
        "countries": ["RU", "TR"],
        "date_from": "2023-01-11 00:00:00",
        "date_to": "2023-01-11 23:59:59"
  }
},
    "En":{
    "status": "success",
    "result": {
        "server": "server_2",
        "bytes": 12345,
        "countries": ["En", "TR"],
        "date_from": "2023-01-11 00:00:00",
        "date_to": "2023-01-11 23:59:59"
  }
}
}

error = {
  "status": "error",
  "code": 500,
  "message": "Error description"
}

server_hour = {
    "Ru":{
        "status": "success",
        "result": {
            "server": "server_1",
            1: {
            "id": 123,
            "bytes": 12345,
            "countries": [
                "RU",
                "TR"
            ],
            "date_from": "2023-01-11 00:00:00",
            "date_to": "2023-01-11 23:59:59"
    },
            2: {
            "id": 321,
            "bytes": 65431,
            "countries": [
                "RU",
                "TR"
            ],
            "date_from": "2023-01-11 00:00:00",
            "date_to": "2023-01-11 23:59:59"
    }
  }
}
}