import tensorflowjs as tfjs
import keras

vgg16 = keras.applications.vgg16.VGG16()
tfjs.converters.save_keras_model(vgg16, './VGG16')
