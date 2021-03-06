import os
import shutil
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text
#from official.nlp import optimization  # to create AdamW optimizer
tf.get_logger().setLevel('ERROR')
tf.compat.v1.reset_default_graph()



    
def predict(text):
    saved_model_path='./saved_model'
    reloaded_model = tf.saved_model.load(saved_model_path)
    pred=tf.sigmoid(reloaded_model(tf.constant([str(text)])))
    
    return pred

