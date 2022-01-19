## Тестовое задание для стажера на позицию «Программист на языке Python»
Реализовать HTTP-сервер для предоставления информации по географическим объектам.
Данные взять из географической базы данных GeoNames, по [ссылке](http://download.geonames.org/export/dump/RU.zip)

# Краткий обзор методов
| Метод HTTP | Действие | Пример |
|:----------------:|:---------:|:----------------:|
| GET | Метод принимает идентификатор geonameid и возвращает информацию о городе. | http://[hostname]/api/geoinfo/[geonameid] |
| GET | Метод принимает страницу и количество отображаемых на странице городов и возвращает список городов с их информацией.  | http://[hostname]/api/get_page?[page]&[amount] |
| GET | Метод принимает названия двух городов (на русском языке) и получает информацию о найденных городах, а также дополнительно: какой из них расположен севернее и одинаковая ли у них временная зона  | http://[hostname]/api/city_compare?[city1]&[city2] |
| GET | Метод принимает часть названия города и возвращает подсказку с возможными вариантами продолжения. | http://[hostname]/api/get_matches?[city] |

##	Метод принимает идентификатор geonameid и возвращает информацию о городе.
<code>GET api/geoinfo</code> - вернет полную информацию о населенном пункте

### Пример запроса
<code>GET api/geoinfo/451797</code>

### Ответ
Успешный ответ приходит с кодом <code>200 OK</code> и содержит тело:
```json
{
  "id": 51, 
  "geonameid": 451797,
  "name": "Vechernyaya Zarya",
  "asciiname": "Vechernyaya Zarya",
  "alternatenames": "",
  "latitude": 56.93608,
  "longitude": 34.42266,
  "feature_class": "P",
  "feature_code": "PPL",
  "country_code": "RU",
  "cc2": "",
  "admin1_code": "77",
  "admin2_code": "",
  "admin3_code": "",
  "admin4_code": "",
  "population": 0,
  "elevation": "",
  "dem": 223,
  "timezone": "Europe/Moscow",
  "modification_date": "2011-07-09\n"
}
```

##	Метод принимает страницу и количество отображаемых на странице городов и возвращает список городов с их информацией. 
<code>GET api/get_page</code> - вернет список населенных пунктов с полной информацией о них

### Пример запроса
<code>GET api/get_page?page=20&amount=5</code>

### Ответ
Успешный ответ приходит с кодом <code>200 OK</code> и содержит тело:
```json
{
    "results": [
        {
            "id": 58,
            "geonameid": 451804,
            "name": "Turlayevo",
            "asciiname": "Turlayevo",
            "alternatenames": "",
            "latitude": 57.23878,
            "longitude": 34.34752,
            "feature_class": "P",
            "feature_code": "PPL",
            "country_code": "RU",
            "cc2": "",
            "admin1_code": "77",
            "admin2_code": "",
            "admin3_code": "",
            "admin4_code": "",
            "population": 0,
            "elevation": "",
            "dem": 244,
            "timezone": "Europe/Moscow",
            "modification_date": "2011-07-09\n"
        },
        {
            "id": 59,
            "geonameid": 451805,
            "name": "Turkovo",
            "asciiname": "Turkovo",
            "alternatenames": "",
            "latitude": 56.74924,
            "longitude": 34.15238,
            "feature_class": "P",
            "feature_code": "PPL",
            "country_code": "RU",
            "cc2": "",
            "admin1_code": "77",
            "admin2_code": "",
            "admin3_code": "",
            "admin4_code": "",
            "population": 0,
            "elevation": "",
            "dem": 226,
            "timezone": "Europe/Moscow",
            "modification_date": "2011-07-09\n"
        },
        {
            "id": 60,
            "geonameid": 451806,
            "name": "Tsapushevo",
            "asciiname": "Tsapushevo",
            "alternatenames": "",
            "latitude": 56.80251,
            "longitude": 34.68958,
            "feature_class": "P",
            "feature_code": "PPL",
            "country_code": "RU",
            "cc2": "",
            "admin1_code": "77",
            "admin2_code": "",
            "admin3_code": "",
            "admin4_code": "",
            "population": 0,
            "elevation": "",
            "dem": 203,
            "timezone": "Europe/Moscow",
            "modification_date": "2011-07-09\n"
        }
    ]
}
```

## Метод принимает названия двух городов (на русском языке) и получает информацию о найденных городах, а также дополнительно: какой из них расположен севернее и одинаковая ли у них временная зона.
<code>GET api/city_compare</code> - вернет полную информацию о сравниваемых населенных пунктах, а также информацию о временной зоне, и о том какой населенный пункт севернее

Парметры <code>?city1</code> - первый населенный пункт и <code>?city2</code> - второй населенный пункт
<code>"northeren"</code> - Возвращает город, расположенный севернее
<code>"timezone"</code> - Возвращает True, если временная зона городов совпадает, иначе False

### Пример запроса
<code>GET api/city_compare?city1=Явидово&city2=Житниково</code>

### Ответ
Успешный ответ приходит с кодом <code>200 OK</code> и содержит тело:
```json
{
    "city1": {
        "id": 23,
        "geonameid": 451769,
        "name": "Yavidovo",
        "asciiname": "Yavidovo",
        "alternatenames": "Javidovo,Yavidovo,\u042f\u0432\u0438\u0434\u043e\u0432\u043e",
        "latitude": 56.87068,
        "longitude": 34.51994,
        "feature_class": "P",
        "feature_code": "PPL",
        "country_code": "RU",
        "cc2": "",
        "admin1_code": "77",
        "admin2_code": "",
        "admin3_code": "",
        "admin4_code": "",
        "population": 0,
        "elevation": "",
        "dem": 217,
        "timezone": "Europe/Moscow",
        "modification_date": "2012-01-16\n"
    },
    "city2": {
        "id": 5,
        "geonameid": 451751,
        "name": "Zhitnikovo",
        "asciiname": "Zhitnikovo",
        "alternatenames": "",
        "latitude": 57.20064,
        "longitude": 34.57831,
        "feature_class": "P",
        "feature_code": "PPL",
        "country_code": "RU",
        "cc2": "",
        "admin1_code": "77",
        "admin2_code": "",
        "admin3_code": "",
        "admin4_code": "",
        "population": 0,
        "elevation": "",
        "dem": 198,
        "timezone": "Europe/Moscow",
        "modification_date": "2011-07-09\n"
    },
    "northeren": "\u0416\u0438\u0442\u043d\u0438\u043a\u043e\u0432\u043e",
    "timezone": true
}
```

##	Метод принимает часть названия населенного пункта и возвращает подсказку с возможными вариантами продолжения.
<code>GET api/get_matches</code> - вернет список с подсказками

Параметры <code>?city</code> - Строчка, содержащая часть названия населенного пункта

### Пример запроса
<code>GET api/get_matches?city=Tom</code>

### Ответ
Успешный ответ приходит с кодом <code>200 OK</code> и содержит тело:
```json
{
    "0": "Vasil’-Tomashëvka",
    "1": "Tomzhen’ga",
    "2": "Tomyz’",
    "3": "Tomyz’",
    "4": "Tomyshevka",
    "5": "Stantsiya Tomylovo",
    "6": "Tomylovo",
    "7": "Bol’shoye Tomylovo",
    "8": "Tomuzlovskoye",
    "9": "Tomuzlovskoye",
    "10": "Tomuzlovka",
    "11": "Ozero Tomut",
    "12": "Tomsino",
    "13": "Tomlenaya",
    "14": "Stantsiya Tomitsy",
    "15": "Tominga",
    "16": "Tomilino",
    "17": "Tomilino",
    "18": "Tomba",
    "19": "Tomazy",
    "20": "Tomazov",
    "21": "Tomashi",
    "22": "Stantsiya Tomashëvo",
    "23": "Tomasha",
    "24": "Tomasha",
    "25": "Tomasha",
    "26": "Mys Tomasa",
    "27": "Tomorovo",
    "28": "Tomarovo",
    "29": "Tomarovo",
    "30": "Tomarovo",
    "31": "Tomarovka",
    "32": "Ostrov Toma",
    "33": "Toma",
    "34": "Tom",
    "35": "Tomilin Kolodez’",
    ...
}
```

