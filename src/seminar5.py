"""Seminar 5. Convolutional Networks"""
import tensorflow as tf
from test_utils import get_preprocessed_data

def build_conv_layer() -> tf.keras.layers.Conv2D:
    """
    Build Conv2D layer with some filters, kernel size and striding step
    Find necessary params, that match conditions
    Input image shape -> Output shape
    filters
    :param
    :return: keras convolutional layer
    """
    # TODO Create layer with necessary filters, kernel size and striding step:
    my_layer = tf.keras.layers.Conv2D(kernel_size=(5, 5), strides=5, filters=2)
    return my_layer


def build_padded_conv_layer(kernel_size) -> tf.keras.layers.Conv2D:
    """
    Build Conv2D layer with some filters and paddings
    Find necessary params, that match conditions
    Input image shape -> Output shape
    (10, 10, 3) -> (10, 10, 2)
    (20, 20, 3) -> (20, 20, 2)
    :param: kernel_size may vary
    :return: keras convolutional layer
    """

    # TODO Create layer with necessary filters and padding. Kernel size is builder parameter:
    padding = 'same' # to maintain the original image size
    my_layer = tf.keras.layers.Conv2D(filters=2, kernel_size=kernel_size, strides=1, padding=padding)
    return my_layer


def build_depth_wise_conv_layer() -> tf.keras.layers.DepthwiseConv2D:
    """Build DepthWise Convolution layer """

    # TODO Create layer with necessary kernel size and depth multiplier:
    my_layer = tf.keras.layers.DepthwiseConv2D(kernel_size=(3, 3), depth_multiplier=2)
    return my_layer


def build_pooling_layer() -> tf.keras.layers.MaxPooling2D:
    """Build MaxPooling layer with fixed pool and strides"""

    # TODO Create layer with necessary kernel size and strides:
    my_layer = tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2))
    return my_layer


def build_up_conv_layer() -> tf.keras.layers.Conv2DTranspose:
    """Build Transpose Convolution layer"""

    # TODO Create layer with necessary filters, kernel size and strides:
    my_layer = tf.keras.layers.Conv2DTranspose(filters=4, kernel_size=(3, 3), strides=(2, 2))
    return my_layer
