from com import functions
from persistance.schemas import enumerations

class SentimentQueueStatusEnum:
    schema_name = None
    schema_fields = []

    id = None
    insert_date = None
    update_date = None
    name = None
    value = None

    def __init__(self):
        self.schema_name = "sentiment_queue_status_enum"
        self.schema_fields.append("id_sentiment_queue_status_enum")             #0
        self.schema_fields.append("fecha_insert_queue_status_enum")             #1
        self.schema_fields.append("fecha_update_queue_status_enum")             #2
        self.schema_fields.append("nombre_sentiment_queue_status_enum")         #3
        self.schema_fields.append("valor_sentiment_queue_status_enum")          #4

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

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_ready_status(self, **kwargs):
        log_output_mode = kwargs.get("debug_otuput")
        class_object = SentimentQueueStatusEnum()
        data_base_object = kwargs.get("db_object")

        functions.verbose(outputMode=log_output_mode, outputMessage="[" + self.__class__.__name__ + "] " + " get_ready_status() " + "Enter", logName="main")
        response_object = None

        query_args = [enumerations.READY,]
        query = "SELECT * FROM {} WHERE {} = ? ORDER BY {} ASC".format(class_object.schema_name, class_object.schema_fields[3], class_object.schema_fields[0])
        query_response = data_base_object.execute_query(query=query, queryArgs=query_args, queryReference="[" + self.__class__.__name__ + "] " + " get_ready_status() " + "get_ready_status", logOutputMode=log_output_mode)


        if (query_response[1] > 0):
            temp_class_object = SentimentQueueStatusEnum()

            temp_class_object.set_id(query_response[0][0][0])
            temp_class_object.set_insert_date(query_response[0][0][1])
            temp_class_object.set_update_date(query_response[0][0][2])
            temp_class_object.set_name(query_response[0][0][3])
            temp_class_object.set_value(query_response[0][0][4])

            response_object = temp_class_object

        functions.verbose(outputMode=log_output_mode,  outputMessage="[" + self.__class__.__name__ + "] " + " get_ready_status() " + "Exit", logName="main")
        return response_object

    def get_complete_status(self, **kwargs):
        log_output_mode = kwargs.get("debug_otuput")
        class_object = SentimentQueueStatusEnum()
        data_base_object = kwargs.get("db_object")

        functions.verbose(outputMode=log_output_mode, outputMessage="[" + self.__class__.__name__ + "] " + " get_complete_status() " + "Enter", logName="main")
        response_object = None

        query_args = [enumerations.COMPLETE,]
        query = "SELECT * FROM {} WHERE {} = ? ORDER BY {} ASC".format(class_object.schema_name, class_object.schema_fields[3], class_object.schema_fields[0])
        query_response = data_base_object.execute_query(query=query, queryArgs=query_args, queryReference="[" + self.__class__.__name__ + "] " + " get_complete_status() " + "get_complete_status", logOutputMode=log_output_mode)


        if (query_response[1] > 0):
            temp_class_object = SentimentQueueStatusEnum()

            temp_class_object.set_id(query_response[0][0][0])
            temp_class_object.set_insert_date(query_response[0][0][1])
            temp_class_object.set_update_date(query_response[0][0][2])
            temp_class_object.set_name(query_response[0][0][3])
            temp_class_object.set_value(query_response[0][0][4])

            response_object = temp_class_object

        functions.verbose(outputMode=log_output_mode,  outputMessage="[" + self.__class__.__name__ + "] " + " get_complete_status() " + "Exit", logName="main")
        return response_object

    def get_cancelled_status(self, **kwargs):
        log_output_mode = kwargs.get("debug_otuput")
        class_object = SentimentQueueStatusEnum()
        data_base_object = kwargs.get("db_object")

        functions.verbose(outputMode=log_output_mode, outputMessage="[" + self.__class__.__name__ + "] " + " get_cancelled_status() " + "Enter", logName="main")
        response_object = None

        query_args = [enumerations.CANCELLED,]
        query = "SELECT * FROM {} WHERE {} = ? ORDER BY {} ASC".format(class_object.schema_name, class_object.schema_fields[3], class_object.schema_fields[0])
        query_response = data_base_object.execute_query(query=query, queryArgs=query_args, queryReference="[" + self.__class__.__name__ + "] " + " get_cancelled_status() " + "get_cancelled_status", logOutputMode=log_output_mode)


        if (query_response[1] > 0):
            temp_class_object = SentimentQueueStatusEnum()

            temp_class_object.set_id(query_response[0][0][0])
            temp_class_object.set_insert_date(query_response[0][0][1])
            temp_class_object.set_update_date(query_response[0][0][2])
            temp_class_object.set_name(query_response[0][0][3])
            temp_class_object.set_value(query_response[0][0][4])

            response_object = temp_class_object

        functions.verbose(outputMode=log_output_mode,  outputMessage="[" + self.__class__.__name__ + "] " + " get_cancelled_status() " + "Exit", logName="main")
        return response_object