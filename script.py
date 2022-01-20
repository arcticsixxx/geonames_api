import os
import sqlite3
import pendulum
from googletrans import Translator
from transliterate import translit
from flask import Flask, abort
from flask_restful import Api, Resource, request


app = Flask(__name__)
api = Api(app)


def searialize_to_dict(sql_row):
    '''Convert cursor object to dict'''
    for i in range(len(sql_row)):
        sql_row[i] = dict(zip(sql_row[i].keys(), list(sql_row[i])))
    return sql_row

class FileParser:
    '''Represents info for database from file RU.txt'''
    __parsed_info = []

    def __init__(self):
        self.dir = os.path.dirname(os.path.abspath(__file__))
        self.__parse_file()

    def __parse_file(self):
        with open(self.dir + "/RU.txt", encoding="utf-8") as file:
            for row in file:
                self.parsed_info.append(tuple(row.split('\t')))
        return self.parsed_info
    
    @property
    def parsed_info(self):
        return self.__parsed_info

class DataBase:
    '''Data Base'''
    def __init__(self):
        self.dir = os.path.dirname(os.path.abspath(__file__))
        self.connect_db()

    def connect_db(self):
        self.conn = sqlite3.connect(os.path.join(self.dir, 'geonames.db'), check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self. __check_db_existance()

    def disconnect_db(self):
        self.conn.close()

    def __check_db_existance(self):
        self.cursor.execute("SELECT name FROM sqlite_master "
                            "WHERE type='table' AND name='geonames'")
        table_exists = self.cursor.fetchall()
        if table_exists:
            return
        self.__init_db()

    def __insert(self, table: str, values: list):
        columns = "geonameid, name, asciiname, alternatenames, latitude, \
                    longitude, feature_class, feature_code, country_code, cc2, \
                    admin1_code, admin2_code, admin3_code, admin4_code, \
                    population, elevation, dem, timezone, modification_date"
        placeholders = ','.join("?" * len(values[0]))
        self.cursor.executemany(
            "INSERT INTO " + table +
            "(" + columns + ")" +
            "VALUES (" + placeholders + ")",
            values)
        self.conn.commit()

    def __init_db(self):
        self.cursor.executescript("""create table geonames(
                                id integer primary key,
                                geonameid integer,
                                name text,
                                asciiname text,
                                alternatenames text,
                                latitude real,
                                longitude real,
                                feature_class text,
                                feature_code text,
                                country_code text,
                                cc2 text,
                                admin1_code text,
                                admin2_code text,
                                admin3_code text,
                                admin4_code text,
                                population integer,
                                elevation integer,
                                dem integer,
                                timezone text,
                                modification_date text);""")
        self.__insert("geonames", FileParser().parsed_info)
        self.conn.commit()

    def get_max_id(self):
        '''Returns total amount of ids'''
        self.cursor.execute("SELECT MAX(id) FROM geonames")
        return geobase.cursor.fetchall()[0][0]

    def getby_geonameid(self, geonameid: str) -> list:
        '''Returns an info about location'''
        self.cursor.execute(
            "SELECT * FROM geonames WHERE geonameid = ?" , (geonameid, ))
        response = searialize_to_dict(geobase.cursor.fetchall())
        return response

    def show_obj_on_page(self, first_element: str, last_element: str) -> list:
        '''Returns a list of elements 
            located on one page'''
        self.cursor.execute(
            "SELECT * FROM geonames WHERE id >= ? AND id <= ? ", (str(first_element), str(last_element), ))
        response = searialize_to_dict(geobase.cursor.fetchall())
        return response
        
    def city_compare(self, city1_eng: str, city2_eng: str) -> list:
        '''This method finds two cities'''
        self.cursor.execute(
            "SELECT *, MAX(population) FROM geonames WHERE name = ?", (city1_eng,))
        cities1 = searialize_to_dict(geobase.cursor.fetchall())
        cities1[0].pop('MAX(population)')
        self.cursor.execute(
            "SELECT *, MAX(population) FROM geonames WHERE name = ?", (city2_eng,))
        cities2 = searialize_to_dict(geobase.cursor.fetchall())
        cities2[0].pop('MAX(population)')
        return cities1, cities2

    def find_matches(self, substring: str) -> list:
        '''This method finds all matches 
            with substr in name column'''
        self.cursor.execute(
            "SELECT * FROM geonames WHERE instr(name, ?)", (substring, ))
        all_matches = searialize_to_dict(geobase.cursor.fetchall())
        return all_matches

class GeoInfo(Resource):
    '''Returns JSON about geoname'''
    def get(self, geonameid):
        response = geobase.getby_geonameid(geonameid)
        if response:
            return dict(*response)
        abort(404, "This geoname id is not valid")

class Pages(Resource):
    '''This API-method gets number of page and amount of cities and returns 
        the page with info about these cities'''
    def get(self):
        page = request.args.get('page')
        cities_amount = request.args.get('amount')
        '''Max id in a table'''
        max_id = geobase.get_max_id()
        '''The way to define the first id that will be the first element
            on the page'''
        first_element = 1 + (int(page) - 1) * int(cities_amount) 
        '''The way to define the last id'''
        last_element = first_element + int(cities_amount) - 1 
        if last_element > max_id:
            last_element = max_id
        response = geobase.show_obj_on_page(first_element, last_element)
        if response:
            return {"results": response}
        abort(404, "Invalid page")

class CityCompare(Resource):
    '''Method gets names of two cities(on Russian) and gets info about it,
        and in additional returns info about timezone and latitude'''
    def get(self):
        city1 = request.args.get('city1')
        city2 = request.args.get('city2')
        translator = Translator()
        '''Translates from rus into eng'''
        city1_eng = translator.translate(city1, src="ru", dest="en").text 
        city2_eng = translator.translate(city2, src="ru", dest="en").text 
        cities1, cities2 = geobase.city_compare(city1_eng, city2_eng)
        if cities1[0]['name'] and cities2[0]['name']:
            northeren_ch = city1 if (
                cities1[0]['latitude'] > cities2[0]['latitude']) else city2
            timezone_ch = True if (
                cities1[0]['timezone'] == cities2[0]['timezone']) else False
            '''By using lib pendulum we can get the timedelta between two cities'''
            city1_time = pendulum.now(cities1[0].get('timezone'))
            city2_time = city1_time.in_timezone(cities2[0].get('timezone'))
            time_difference = abs(city1_time.hour - city2_time.hour)
            return {
                "city1": dict(*cities1),
                "city2": dict(*cities2),
                "northeren": northeren_ch,
                "timezone": timezone_ch,
                "time_difference": time_difference
                }
        abort(404, "Invalid request")

class Matches(Resource):
    '''This API method returns all variants 
        for continuing the name'''
    def get(self):
        substring = request.args.get('city')
        '''Here we used module translit because we need 
            to transliterate param, not to translate'''
        substring_en = translit(substring, language_code='ru', reversed=True)
        all_matches = geobase.find_matches(substring_en)
        response = dict()
        for i in range(len(all_matches)):
            response[i] = all_matches[i]['name'] 
        if response:
            return response
        abort(404, 'Invalid request')

geobase = DataBase()
api.add_resource(GeoInfo, "/api/geoinfo/<string:geonameid>")
api.add_resource(Pages, "/api/get_page")
api.add_resource(CityCompare, "/api/city_compare")
api.add_resource(Matches, "/api/get_matches")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)

    