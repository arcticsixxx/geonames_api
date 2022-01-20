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

* <code>"northeren"</code> - Возвращает город, расположенный севернее
* <code>"timezone"</code> - Возвращает True, если временная зона городов совпадает, иначе False
* <code>"time_difference"</code> - Возвращает абсолютную разность во времени между двумя городами

### Пример запроса
<code>GET api/city_compare?city1=Явидово&city2=Житниково</code>

### Ответ
Успешный ответ приходит с кодом <code>200 OK</code> и содержит тело:
```json
{
  "city1": {
      "id": 64198,
      "geonameid": 524901,
      "name": "Moscow",
      "asciiname": "Moscow",
      "alternatenames": "MOW,Maeskuy,Maskav,Maskava,Maskva,Mat-xco-va,Matxcova,Matxcơva,Mosca,Moscfa,Moscha,Mosco,Moscou,Moscova,Moscovo,Moscow,Moscoƿ,Moscu,Moscua,Moscòu,Moscó,Moscù,Moscú,Moskva,Moska,Moskau,Mosko,Moskokh,Moskou,Moskov,Moskova,Moskovu,Moskow,Moskowa,Mosku,Moskuas,Moskva,Moskvo,Moskwa,Moszkva,Muskav,Musko,Mát-xcơ-va,Mòskwa,Məskeu,Məskəү,masko,maskw,mo si ke,moseukeuba,mosko,mosukuwa,mskw,mwskva,mwskw,mwsqbh,mx s ko,Μόσχα,Мæскуы,Маскав,Масква,Москва,Москова,Москох,Москъва,Мускав,Муско,Мәскеу,Мәскәү,Մոսկվա,מאָסקװע,מאסקווע,מוסקבה,ماسکو,مسکو,موسكو,موسكۋا,ܡܘܣܩܒܐ,मास्को,मॉस्को,মস্কো,மாஸ்கோ,มอสโก,མོ་སི་ཁོ།,მოსკოვი,ሞስኮ,モスクワ,莫斯科,모스크바",
      "latitude": 55.75222,
      "longitude": 37.61556,
      "feature_class": "P",
      "feature_code": "PPLC",
      "country_code": "RU",
      "cc2": "",
      "admin1_code": "48",
      "admin2_code": "",
      "admin3_code": "",
      "admin4_code": "",
      "population": 10381222,
      "elevation": "",
      "dem": 144,
      "timezone": "Europe/Moscow",
      "modification_date": "2020-03-31\n"
  },
  "city2": {
      "id": 164479,
      "geonameid": 1489425,
      "name": "Tomsk",
      "asciiname": "Tomsk",
      "alternatenames": "TOF,Tom'sku,Tomck,Tomium,Toms'k,Tomsk,Tomska,Tomskaj,Tomskas,Tomszk,Tomçk,tomseukeu,tomska,tomusuku,tuo mu si ke,twmsk,twmsq,Τομσκ,Томск,Томскай,Томськ,Томьскъ,Տոմսկ,טומסק,تومسك,تومسک,ٹومسک,तोम्स्क,トムスク,托木斯克,톰스크",
      "latitude": 56.49771,
      "longitude": 84.97437,
      "feature_class": "P",
      "feature_code": "PPLA",
      "country_code": "RU",
      "cc2": "",
      "admin1_code": "75",
      "admin2_code": "1489419",
      "admin3_code": "",
      "admin4_code": "",
      "population": 485519,
      "elevation": "",
      "dem": 117,
      "timezone": "Asia/Tomsk",
      "modification_date": "2019-09-05\n"
  },
    "northeren": "Томск",
    "timezone": false,
    "time_difference": 4
}
```

##	Метод принимает часть названия населенного пункта и возвращает подсказку с возможными вариантами продолжения.
<code>GET api/get_matches</code> - вернет список с подсказками

Параметры <code>?city</code> - Строчка, содержащая часть названия населенного пункта

### Пример запроса
<code>GET api/get_matches?city=Томс</code>

### Ответ
Успешный ответ приходит с кодом <code>200 OK</code> и содержит тело:
```json
{
  "0": "Tomsino",
  "1": "Tomsharovo",
  "2": "Stantsiya Tomsk Vtoroy",
  "3": "Stantsiya Tomsk Pervyy",
  "4": "Tomskoye",
  "5": "Tomskiy Rayon",
  "6": "Tomskiy Khutor",
  "7": "Tomsk Oblast",
  "8": "Tomskaya",
  "9": "Tomskaya",
  "10": "Tomskaya",
  "11": "Tomsk",
  "12": "Ozero Bol’shoye Tomskoye",
  "13": "Ozero Maloye Tomskoye",
  "14": "Tomskiy",
  "15": "Tomskoye",
  "16": "Tomskoye",
  "17": "Tomsyu",
  "18": "Ostrov Tomskiy",
  "19": "Tomsha",
  "20": "Tomsko-Obskaya Lesnaya Dacha",
  "21": "Ozero Tomskoye",
  "22": "Urochishche Tomshina",
  "23": "Tomsino",
  "24": "Ozero Tomsino",
  "25": "Tomsha",
  "26": "Tomskiy",
  "27": "Tomsk Bogashevo Airport",
  "28": "Gora Tomskaya",
  "29": "Stantsiya Tomsk-Severnyy",
  "30": "Meriya Goroda Tomska",
  "31": "Duma Goroda Tomska",
  "32": "Tomskaya Tamozhnya",
  "33": "Tomskiy Oblastnoy Sud",
  "34": "Tomsk"
}
```

