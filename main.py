from com import functions
from com.db_connection import DataBaseConnection
from persistance.schemas.sentiment_queue_entity import SentimentQueueEntity
from persistance.schemas.sentiment_queue_status_enum_entity import SentimentQueueStatusEnum
from persistance.schemas.run_entity import RunEntity
import os.path
import sys
import time
from textblob import TextBlob
import goslate

# Get the output argument
if len(sys.argv) > 1:
    log_output_arg = sys.argv[1]
else:
    log_output_arg = "no_logs"

if log_output_arg == "save_logs":
    log_output_mode = 1
elif log_output_arg == "no_logs":
    log_output_mode = 0
else:
    log_output_arg = "no_logs"
    log_output_mode = 0

#Define the constants
current_dir_path = os.path.dirname(os.path.abspath(__file__))
db_dir_path = "db"
sqlite_database_filename = "sentiments.sqlite3"
gs = goslate.Goslate()
sentiment_queue_object = SentimentQueueEntity()
sentiment_queue_status_enum = SentimentQueueStatusEnum()
run_object = RunEntity()

functions.verbose(outputMode=log_output_mode, outputMessage="[main] " + "SentimentService() " + "Enter", logName="main")
sqlite_db_connection = DataBaseConnection(db_type='sqlite', db_host=current_dir_path + "\\..\\" + db_dir_path + "\\" + sqlite_database_filename, db_user='', db_pass='', db_name='')

sentiment_queue_list = sentiment_queue_object.get_sentimetn_queue(db_object=sqlite_db_connection, debug_otuput=log_output_mode)
sentiment_queue_ready_list = []

ready_status_enum_id = sentiment_queue_status_enum.get_ready_status(db_object=sqlite_db_connection, debug_otuput=log_output_mode).get_id()
for x in range(len(sentiment_queue_list)):
    functions.verbose(outputMode=log_output_mode, outputMessage="[main] " + "SentimentService() " + "item_status_id [{}], ready_status_id [{}]".format(sentiment_queue_list[x].get_status_id(), ready_status_enum_id),logName="main")
    if int(sentiment_queue_list[x].get_status_id()) == int(ready_status_enum_id):
        temp_object = SentimentQueueEntity()
        temp_object.set_id(sentiment_queue_list[x].get_id())
        temp_object.set_evaluation_text(sentiment_queue_list[x].get_evaluation_text())

        sentiment_queue_ready_list.append(temp_object)
    else:
        functions.verbose(outputMode=log_output_mode, outputMessage="[main] " + "SentimentService() " + "id mismatch, skipping",logName="main")

functions.verbose(outputMode=log_output_mode, outputMessage="[main] " + "SentimentService() " + "Found {} elements to process".format(len(sentiment_queue_ready_list)), logName="main")

for x in range(len(sentiment_queue_ready_list)):
    try:
        raw_text = sentiment_queue_ready_list[x].get_evaluation_text()

        sentence_process_object = TextBlob(raw_text)
        translated_text = sentence_process_object.translate(from_lang='es', to='en')

        sentiment_queue_ready_list[x].set_score(float(sentence_process_object.sentiment.polarity))
        sentiment_queue_ready_list[x].set_update_date(time.strftime('%Y-%m-%d %H:%M:%S'))
        sentiment_queue_ready_list[x].set_status_id(sentiment_queue_status_enum.get_complete_status(db_object=sqlite_db_connection, debug_otuput=log_output_mode).get_id())
        sentiment_queue_ready_list[x].flush(db_object=sqlite_db_connection, debug_otuput=log_output_mode)

        #functions.verbose(outputMode=log_output_mode, outputMessage="[main] " + "SentimentService() " + "Processed element: raw_text: '{}', translated_text: '{}', sentiment: {}".format(raw_text, translated_text, sentence_process_object.sentiment), logName="main")
        functions.verbose(outputMode=log_output_mode,outputMessage="[main] " + "SentimentService() " + "Processed element: sentiment: {}".format(sentence_process_object.sentiment), logName="main")
    except:
        sentiment_queue_ready_list[x].set_update_date(time.strftime('%Y-%m-%d %H:%M:%S'))
        sentiment_queue_ready_list[x].set_status_id(sentiment_queue_status_enum.get_cancelled_status(db_object=sqlite_db_connection, debug_otuput=log_output_mode).get_id())
        functions.verbose(outputMode=log_output_mode, outputMessage="[main] " + "SentimentService() " + "Failed element [{}]".fomat(sentiment_queue_ready_list[x].get_id()), logName="main")
        sentiment_queue_ready_list[x].flush(db_object=sqlite_db_connection, debug_otuput=log_output_mode)


functions.verbose(outputMode=log_output_mode, outputMessage="[main] " + "SentimentService() " + "Exit", logName="main")
