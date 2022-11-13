from com import functions

class SentimentQueueEntity:
    schema_name = None
    schema_fields = []

    id = None
    rrss_id = None
    insert_date = None
    update_date = None
    evaluation_text = None
    score = None
    status_id = None
    error_desc = None
    run_id = None

    def __init__(self):
        self.schema_name = "sentiment_queue"
        self.schema_fields.append("id_sentiment_queue")                     #0
        self.schema_fields.append("id_rrss")                                #1
        self.schema_fields.append("fecha_insert_sentiment_queue")           #2
        self.schema_fields.append("fecha_update_sentiment_queue")           #3
        self.schema_fields.append("texto_evaluacion_sentiment_queue")       #4
        self.schema_fields.append("puntaje_sentiment_queue")                #5
        self.schema_fields.append("estado_id_sentiment_queue")              #6
        self.schema_fields.append("descripcion_error_sentiment_queue")      #7
        self.schema_fields.append("run_id")                                 #8

    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_insert_date(self):
        return self.insert_date

    def set_insert_date(self, value):
        self.insert_date = value

    def get_update_date(self):
        return self.update_date

    def set_update_date(self, value):
        self.update_date = value

    def get_rrss_id(self):
        return self.rrss_id

    def set_rrss_id(self, value):
        self.rrss_id = value

    def get_evaluation_text(self):
        return self.evaluation_text

    def set_evaluation_text(self, value):
        self.evaluation_text = value

    def get_score(self):
        return self.score

    def set_score(self, value):
        self.score = value

    def get_status_id(self):
        return self.status_id

    def set_status_id(self, value):
        self.status_id = value

    def get_error_desc(self):
        return self.error_desc

    def set_error_desc(self, value):
        self.error_desc = value

    def get_run_id(self):
        return self.run_id

    def set_run_id(self, value):
        self.run_id = value

    def get_sentimetn_queue(self, **kwargs):
        log_output_mode = kwargs.get("debug_otuput")
        class_object = SentimentQueueEntity()
        data_base_object = kwargs.get("db_object")

        functions.verbose(outputMode=log_output_mode,  outputMessage="[" + self.__class__.__name__ + "] " + " get_sentimetns_queue() " + "Enter", logName="main")
        response_object = []

        query = "SELECT * FROM {} WHERE {} = {} ORDER BY {} ASC".format(class_object.schema_name, class_object.schema_fields[6], 1, class_object.schema_fields[0])
        query_response = data_base_object.execute_query(query=query, queryArgs={}, queryReference="[" + self.__class__.__name__ + "] " + " get_sentimetns_queue() " + "get_sentimetns_queue", logOutputMode=log_output_mode)

        functions.verbose(outputMode=log_output_mode, outputMessage="[" + self.__class__.__name__ + "] " + " get_sentimetns_queue() " + "Found {} rows".format(query_response[1]), logName="main")

        if (query_response[1] > 0):
            for x in range(query_response[1]):
                temp_class_object = SentimentQueueEntity()

                temp_class_object.set_id(query_response[0][x][0])
                temp_class_object.set_rrss_id(query_response[0][x][1])
                temp_class_object.set_insert_date(query_response[0][x][2])
                temp_class_object.set_update_date(query_response[0][x][3])
                temp_class_object.set_evaluation_text(query_response[0][x][4])
                temp_class_object.set_score(query_response[0][x][5])
                temp_class_object.set_status_id(query_response[0][x][6])
                temp_class_object.set_error_desc(query_response[0][x][7])
                temp_class_object.set_run_id(query_response[0][x][8])

                response_object.append(temp_class_object)

        functions.verbose(outputMode=log_output_mode, outputMessage="[" + self.__class__.__name__ + "] " + " get_sentimetns_queue() " + "Exit", logName="main")
        return response_object

    def flush(self, **kwargs):
        log_output_mode = kwargs.get("debug_otuput")
        class_object = SentimentQueueEntity()
        data_base_object = kwargs.get("db_object")

        functions.verbose(outputMode=log_output_mode, outputMessage="[" + self.__class__.__name__ + "] " + " flush() " + "Enter", logName="main")

        if self.get_rrss_id() is not None:
            query_args = [self.get_rrss_id(),self.get_id()]
            query = "UPDATE {} SET {} = ? WHERE {} = ?".format(class_object.schema_name, class_object.schema_fields[1], class_object.schema_fields[0])
            data_base_object.execute_query(query=query, queryArgs=query_args, queryReference="[" + self.__class__.__name__ + "] " + " flush() " + "flush", logOutputMode=log_output_mode)

        if self.get_insert_date() is not None:
            query_args = [self.get_insert_date(),self.get_id()]
            query = "UPDATE {} SET {} = ? WHERE {} = ?".format(class_object.schema_name, class_object.schema_fields[2], class_object.schema_fields[0])
            data_base_object.execute_query(query=query, queryArgs=query_args, queryReference="[" + self.__class__.__name__ + "] " + " flush() " + "flush", logOutputMode=log_output_mode)

        if self.get_update_date() is not None:
            query_args = [self.get_update_date(),self.get_id()]
            query = "UPDATE {} SET {} = ? WHERE {} = ?".format(class_object.schema_name, class_object.schema_fields[3], class_object.schema_fields[0])
            data_base_object.execute_query(query=query, queryArgs=query_args, queryReference="[" + self.__class__.__name__ + "] " + " flush() " + "flush", logOutputMode=log_output_mode)

        if self.get_evaluation_text() is not None:
            query_args = [self.get_evaluation_text(),self.get_id()]
            query = "UPDATE {} SET {} = ? WHERE {} = ?".format(class_object.schema_name, class_object.schema_fields[4], class_object.schema_fields[0])
            data_base_object.execute_query(query=query, queryArgs=query_args, queryReference="[" + self.__class__.__name__ + "] " + " flush() " + "flush", logOutputMode=log_output_mode)

        if self.get_score() is not None:
            query_args = [self.get_score(),self.get_id()]
            query = "UPDATE {} SET {} = ? WHERE {} = ?".format(class_object.schema_name, class_object.schema_fields[5], class_object.schema_fields[0])
            data_base_object.execute_query(query=query, queryArgs=query_args, queryReference="[" + self.__class__.__name__ + "] " + " flush() " + "flush", logOutputMode=log_output_mode)

        if self.get_status_id() is not None:
            query_args = [self.get_status_id(),self.get_id()]
            query = "UPDATE {} SET {} = ? WHERE {} = ?".format(class_object.schema_name, class_object.schema_fields[6], class_object.schema_fields[0])
            data_base_object.execute_query(query=query, queryArgs=query_args, queryReference="[" + self.__class__.__name__ + "] " + " flush() " + "flush", logOutputMode=log_output_mode)

        if self.get_error_desc() is not None:
            query_args = [self.get_status_id(),self.get_id()]
            query = "UPDATE {} SET {} = ? WHERE {} = ?".format(class_object.schema_name, class_object.schema_fields[7], class_object.schema_fields[0])
            data_base_object.execute_query(query=query, queryArgs=query_args, queryReference="[" + self.__class__.__name__ + "] " + " flush() " + "flush", logOutputMode=log_output_mode)

        if self.get_run_id() is not None:
            query_args = [self.get_status_id(),self.get_id()]
            query = "UPDATE {} SET {} = ? WHERE {} = ?".format(class_object.schema_name, class_object.schema_fields[8], class_object.schema_fields[0])
            data_base_object.execute_query(query=query, queryArgs=query_args, queryReference="[" + self.__class__.__name__ + "] " + " flush() " + "flush", logOutputMode=log_output_mode)

        functions.verbose(outputMode=log_output_mode, outputMessage="[" + self.__class__.__name__ + "] " + " flush() " + "Exit", logName="main")