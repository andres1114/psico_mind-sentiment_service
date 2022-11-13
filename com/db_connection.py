#=============================================================

#This script is in charge of creating a connection to a postgres database server
#and dealing with the possible errors during query runtime

#=============================================================
from com import functions
import sys


class DataBaseConnection:
    db_connection = None

    def __init__(self, db_host, db_user, db_pass, db_name, db_type):
        self.db_connection = self.create_db_connection(db_host=db_host, db_user=db_user, db_pass=db_pass, db_name=db_name, db_type=db_type)

    def create_db_connection(self, **kwargs):
        functions.verbose(outputMode=kwargs.get('logOutputMode'), outputMessage="[" + self.__class__.__name__ + "] " + " create_db_connection() " + " Enter", logName="main")

        db_host = kwargs.get('db_host')
        db_user = kwargs.get('db_user')
        db_pass = kwargs.get('db_pass')
        db_name = kwargs.get('db_name')
        db_type = kwargs.get('db_type')

        if db_type == 'mysql':
            try:
                import MySQLdb
                db_connection = MySQLdb.connect(host=db_host, user=db_user, password=db_pass, dbname=db_name)
                db_connection.set_client_encoding("utf8")
            except Exception as e:

                error_message = "ERR_CANT_CREATE_DB_CONNECTION "+str(e)
                functions.verbose(outputMode=kwargs.get('logOutputMode'), outputMessage="[" + self.__class__.__name__ + "] " + " create_db_connection() " + error_message, logName="main")
                sys.exit(error_message)

        elif db_type == 'postgres':
            try:
                import psycopg2
                db_connection = psycopg2.connect(host=db_host, user=db_user, password=db_pass, dbname=db_name)
                db_connection.set_client_encoding("utf8")
            except Exception as e:

                error_message = "ERR_CANT_CREATE_DB_CONNECTION "+str(e)
                functions.verbose(outputMode=kwargs.get('logOutputMode'), outputMessage="[" + self.__class__.__name__ + "] " + " create_db_connection() " + error_message, logName="main")
                sys.exit(error_message)
        elif db_type == 'sqlite':
            try:
                import sqlite3
                db_connection = sqlite3.connect(db_host)
            except Exception as e:

                error_message = "ERR_CANT_CREATE_DB_CONNECTION "+str(e)
                functions.verbose(outputMode=kwargs.get('logOutputMode'), outputMessage="[" + self.__class__.__name__ + "] " + " create_db_connection() " + error_message, logName="main")
                sys.exit(error_message)

        functions.verbose(outputMode=kwargs.get('logOutputMode'), outputMessage="[" + self.__class__.__name__ + "] " + " create_db_connection() " + "Exit", logName="main")
        return db_connection


    def execute_query(self, **kwargs):
        functions.verbose(outputMode=kwargs.get('logOutputMode'), outputMessage="[" + self.__class__.__name__ + "] " + " execute_query() " + "Enter", logName="main")
        try:
            cursor = self.db_connection.cursor()
        except Exception as e:

            error_message = "ERR_CANT_CREATE_DB_CONNECTION Caught exception '" + str(e) + "', on query reference '" + kwargs.get('queryReference') + "_CREATE_CURSOR'"
            functions.verbose(outputMode=kwargs.get('logOutputMode'), outputMessage="[" + self.__class__.__name__ + "] " + " execute_query() " + error_message, logName="main")
            sys.exit(error_message)

        try:
            if len(kwargs.get('queryArgs')) == 0:
                cursor.execute(kwargs.get('query'))
            else:
                cursor.execute(kwargs.get('query'), kwargs.get('queryArgs'))
        except Exception as e:

            error_message = "ERR_CANT_EXECUTE_CURSOR Caught exception '" + str(e) + "', on query reference '" + kwargs.get('queryReference') + "_EXECUTE_CURSOR'"
            functions.verbose(outputMode=kwargs.get('logOutputMode'), outputMessage="[" + self.__class__.__name__ + "] " + " execute_query() " + error_message, logName="main")
            self.db_connection.rollback()
            sys.exit(error_message)

        try:
            self.db_connection.commit()
        except Exception as e:

            error_message = "ERR_CANT_COMMIT_CURSOR Caught exception '" + str(e) + "', on query reference '" + kwargs.get('queryReference') + "_COMMIT_CURSOR'"
            functions.verbose(outputMode=kwargs.get('logOutputMode'), outputMessage="[" + self.__class__.__name__ + "] " + " execute_query() " + error_message, logName="main")
            self.db_connection.rollback()
            sys.exit(error_message)

        if cursor.description is None:
            fetchedResults = {}
            returnArray = [fetchedResults, 0, kwargs.get('query'), None]
        else:
            fetchedResults = cursor.fetchall()
            returnArray = [fetchedResults, len(fetchedResults), kwargs.get('query'), cursor.lastrowid]

        cursor.close()
        functions.verbose(outputMode=kwargs.get('logOutputMode'),  outputMessage="[" + self.__class__.__name__ + "] " + " execute_query() " + "Exit", logName="main")
        return returnArray



