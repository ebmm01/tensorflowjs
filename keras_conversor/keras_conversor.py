import tensorflowjs as tfjs
import keras
import tensorflow as tf

tf.compat.v1.disable_eager_execution()


#vgg16 = keras.applications.vgg16.VGG16()
#tfjs.converters.save_keras_model(vgg16, './VGG16')

mobilenet = keras.applications.mobilenet_v2.MobileNetV2()
tfjs.converters.save_keras_model(mobilenet, './mobilenet')
